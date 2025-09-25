# calculator.py
import json
import math
import pandas as pd # Add pandas for dataframe conversion

class ResourceCalculator:
    """
    Calculates resource consumption for a trailer based on trip configuration.
    
    This class uses pre-defined lookup data to estimate energy (Wh) and 
    water (gallons) usage for various activities like living, cooking, showering, etc.
    
    Refactored to separate base consumption rates from multipliers.
    """

    WH_TO_KWH = 1000
    SECONDS_PER_HOUR = 3600

    def __init__(self, lookup_data, **kwargs):
        """
        Initializes the calculator with trip parameters.

        Args:
            lookup_data (dict): The main data structure containing all lookup values.
            **kwargs: User-defined trip parameters. Expected keys are:
                - user_type (str): 'Glamper', 'Typical', or 'Expert'.
                - num_people (int): Number of occupants.
                - trip_duration_days (int): Duration of the trip.
                - hvac_runtime_hrs (int): Hours per day HVAC is active.
                - relocation_count (int): Number of campsite moves.
                - temperature (str): 'Hot', 'Temperate', 'Cold'.
                - humidity (str): 'Humid', 'Comfortable', 'Dry'.
                - sunlight (str): 'Hi- Sunny', 'Mid- Cloudy', 'Lo- Shady'.
        """
        self.config = kwargs
        self.data = lookup_data
        
        # Easy access to nested data
        self.profiles = self.data["lookups"]["user_profiles"]["profiles"]
        self.specs = self.data["trailer_specs"]["specs"]
        
        # Create a mapping of component names to their specs for easy lookup
        self.component_map = self._create_component_map()
        
        # Store base consumption rates and cycle counts
        self.consumption_rates = {}
        self.cycle_counts = {}
        self.results = {}

    def _calculate_energy_from_components_per_unit(self, components):
        """
        Calculates energy consumption for components per unit (hour, cycle, etc.).

        Args:
            components (dict): A dictionary where keys are component names and
                               values are their runtime in hours per unit.

        Returns:
            float: The energy consumed in Watt-hours per unit.
        """
        total_wh_per_unit = 0
        for name, runtime_hrs_per_unit in components.items():
            total_wh_per_unit += self._get_component_power_wh_per_hour(name) * runtime_hrs_per_unit
        return total_wh_per_unit

    def _create_component_map(self):
        """Creates a single dictionary mapping component names to their data lists."""
        component_map = {}
        comp_data = self.data["lookups"]["components"]
        schema = comp_data["schema"]
        
        for category in comp_data:
            if category in ["schema", "unit"]:
                continue
            for item_list in comp_data[category]:
                # Use a dictionary for easier access by schema name
                item_dict = dict(zip(schema, item_list))
                component_map[item_dict['name']] = item_dict
        return component_map

    def _get_component_power_wh_per_hour(self, name):
        """Calculates energy consumption for a component per hour of operation."""
        comp = self.component_map.get(name)
        if not comp:
            return 0
        return comp['voltage_v'] * comp['avg_amps']

    def _get_component_idle_power_wh_per_hour(self, name):
        """Calculates idle energy consumption for a component per hour."""
        comp = self.component_map.get(name)
        if not comp:
            return 0
        return comp['voltage_v'] * comp['idle_amps']

    def calculate_base_rates(self):
        """
        Calculates all base consumption rates and cycle counts.
        
        Returns:
            dict: Dictionary containing consumption rates and cycle counts for each category.
        """
        # Reset for re-calculation
        self.consumption_rates = {}
        self.cycle_counts = {}

        # Calculate base rates for each category
        self._calculate_living_base()
        self._calculate_cooking_base()
        self._calculate_shower_base()
        self._calculate_toilet_base()
        self._calculate_laundry_base()
        self._calculate_hvac_base()
        self._calculate_solar_base()
        self._calculate_actuation_base()
        self._calculate_dumping_base()

        return {
            "consumption_rates": self.consumption_rates,
            "cycle_counts": self.cycle_counts
        }

    def apply_multipliers(self):
        """
        Applies multipliers to base consumption rates to get total consumption.
        
        Returns:
            dict: Results with total consumption for each category.
        """
        self.results = {}
        
        for category in self.consumption_rates:
            energy_per_unit = self.consumption_rates[category]['energy_wh_per_unit']
            water_per_unit = self.consumption_rates[category]['water_gal_per_unit']
            unit_count = self.cycle_counts[category]['units']
            
            total_energy = energy_per_unit * unit_count
            total_water = water_per_unit * unit_count
            
            self.results[category] = {
                'energy_wh': total_energy,
                'water_gal': total_water
            }
            
        return self.results

    def calculate(self):
        """
        Performs all resource calculations and returns a summary.
        
        Returns:
            dict: A dictionary containing base rates, cycle counts, and final summary.
        """
        # Calculate base rates first
        base_data = self.calculate_base_rates()
        
        # Apply multipliers to get totals
        totals = self.apply_multipliers()
        
        # Calculate dump trips needed based on waste water produced
        dump_trip_counts = self._calculate_dump_trips()
        
        # Update actuation and dumping with dump trip counts
        self._update_actuation_cycles(dump_trip_counts['total'])
        self._update_dumping_cycles(dump_trip_counts['total'])
        
        # Recalculate totals with updated cycles
        totals = self.apply_multipliers()
        
        return self._summarize_results(dump_trip_counts, base_data)

    def _get_profile_value(self, category, subcategory, key):
        """Helper method to get values from the categorized profile data."""
        profile = self.profiles[self.config['user_type']]
        return profile[category][subcategory][key]

    def _calculate_living_base(self):
        """Calculate base living consumption per day."""
        # Assuming a 5-second runtime for each smart key cycle
        SMART_KEY_CYCLE_SECONDS = 5
        smart_key_cycles_per_day = self._get_profile_value('count_based', 'cycles_per_day', 'living_smart_key')
        
        # Define components and their daily runtime in hours
        component_runtimes_hrs_per_day = {
            'Audio Amplifier': self._get_profile_value('time_based', 'mins_per_day', 'living_audio') / 60,
            'Television': self._get_profile_value('time_based', 'mins_per_day', 'living_tv') / 60,
            'Lighting': self._get_profile_value('time_based', 'mins_per_day', 'living_lighting') / 60,
            'Smart Glass Display': self._get_profile_value('time_based', 'hrs_per_day', 'living_smart_glass'),
            'Consumer Electronics': self._get_profile_value('time_based', 'hrs_per_day', 'living_electronics'),
            'Party Lighting': self._get_profile_value('time_based', 'hrs_per_day', 'living_party_lighting'),
            'Tire Pressure Sensors': self._get_profile_value('time_based', 'hrs_per_day', 'living_tire_sensors'),
            'Misc. Sensors & Controllers': self._get_profile_value('time_based', 'hrs_per_day', 'living_sensors_controllers'),
            'Security Cameras': self._get_profile_value('time_based', 'hrs_per_day', 'living_security_cameras'),
            'Exterior Camp Lights': self._get_profile_value('time_based', 'hrs_per_day', 'living_ext_camp_lights'),
            'Exterior Porch Lighting': self._get_profile_value('time_based', 'hrs_per_day', 'living_ext_porch_lights'),
            'SmartTint DC PSU': self._get_profile_value('time_based', 'hrs_per_day', 'living_smart_tint'),
            'Smart Key Lighting': (smart_key_cycles_per_day * SMART_KEY_CYCLE_SECONDS) / self.SECONDS_PER_HOUR,
            'Refrigerator': 24, # Always on
            'Satellite Internet PSU': 24, # Always on
            'AI Compute': 24, # Always on
        }
        
        energy_wh_per_day = self._calculate_energy_from_components_per_unit(component_runtimes_hrs_per_day)

        # Water consumption per person per day
        water_sources_gal_per_person_per_day = {
            'cleaning': self._get_profile_value('volume_based', 'gal_per_day', 'living_cleaning'),
            'drinking': self._get_profile_value('volume_based', 'gal_per_day', 'living_drinking_water'),
            'ice_maker': self._get_profile_value('volume_based', 'gal_per_day', 'living_ice_maker_water'),
        }
        water_gal_per_day = sum(water_sources_gal_per_person_per_day.values()) * self.config['num_people']

        self.consumption_rates['living'] = {
            'energy_wh_per_unit': energy_wh_per_day,
            'water_gal_per_unit': water_gal_per_day,
            'unit_type': 'day'
        }
        self.cycle_counts['living'] = {
            'units': self.config['trip_duration_days'],
            'unit_type': 'days'
        }

    def _calculate_cooking_base(self):
        """Calculate base cooking consumption per meal."""
        # Base energy per meal (before stove multiplier)
        component_runtime_hrs_per_meal = {
            'Microwave': self._get_profile_value('time_based', 'mins_per_meal', 'cooking_microwave') / 60,
            'Dishwasher': 80/60 * self._get_profile_value('count_based', 'cycles_per_meal', 'cooking_dishwasher'),
            'Tankless Water Heater': self._get_profile_value('time_based', 'mins_per_meal', 'cooking_water_heater') / 60,
            'Garbage Disposal': self._get_profile_value('time_based', 'mins_per_meal', 'cooking_garbage_disposal') / 60,
            'Consumer Electronics': self._get_profile_value('time_based', 'mins_per_meal', 'cooking_consumer_electronics') / 60,
            'Water Pump': self._get_profile_value('time_based', 'mins_per_meal', 'cooking_pump') / 60,
            'Range Hood': self._get_profile_value('time_based', 'mins_per_meal', 'cooking_range_hood') / 60
        }
        
        base_energy_wh_per_meal = self._calculate_energy_from_components_per_unit(component_runtime_hrs_per_meal)
        
        # Add stove energy (with burner multiplier)
        stove_runtime_hrs_per_meal = self._get_profile_value('time_based', 'mins_per_meal', 'cooking_stove') / 60
        stove_burners_per_meal = self._get_profile_value('count_based', 'burners_per_meal', 'cooking_stove')
        stove_energy_wh_per_meal = self._get_component_power_wh_per_hour('Stove') * stove_runtime_hrs_per_meal * stove_burners_per_meal
        
        total_energy_wh_per_meal = base_energy_wh_per_meal + stove_energy_wh_per_meal

        # Water per meal
        water_gal_per_meal = (
            self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_dishwasher_water') * 
            self._get_profile_value('count_based', 'cycles_per_meal', 'cooking_dishwasher') +
            self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet')
        )

        self.consumption_rates['cooking'] = {
            'energy_wh_per_unit': total_energy_wh_per_meal,
            'water_gal_per_unit': water_gal_per_meal,
            'unit_type': 'meal'
        }
        
        total_meals = self._get_profile_value('count_based', 'meals_per_day', 'cooking') * self.config['trip_duration_days']
        self.cycle_counts['cooking'] = {
            'units': total_meals,
            'unit_type': 'meals'
        }

    def _calculate_shower_base(self):
        """Calculate base shower consumption per cycle."""
        component_runtime_hrs_per_cycle = {
            'Electric Shower': self._get_profile_value('time_based', 'mins_per_cycle', 'shower_duration') / 60,
            'Bathroom Vent Fan': self._get_profile_value('time_based', 'mins_per_cycle', 'shower_vent_fan') / 60,
            'Consumer Electronics': self._get_profile_value('time_based', 'mins_per_cycle', 'shower_electronics') / 60,
            'Water Pump': self._get_profile_value('time_based', 'mins_per_cycle', 'shower_water_pump') / 60
        }

        energy_wh_per_cycle = self._calculate_energy_from_components_per_unit(component_runtime_hrs_per_cycle)
        water_gal_per_cycle = self._get_profile_value('volume_based', 'gal_per_cycle', 'shower_water')

        self.consumption_rates['shower'] = {
            'energy_wh_per_unit': energy_wh_per_cycle,
            'water_gal_per_unit': water_gal_per_cycle,
            'unit_type': 'cycle'
        }
        
        total_cycles = (self._get_profile_value('count_based', 'cycles_per_day_per_person', 'shower') * 
                       self.config['num_people'] * self.config['trip_duration_days'])
        self.cycle_counts['shower'] = {
            'units': total_cycles,
            'unit_type': 'cycles'
        }

    def _calculate_toilet_base(self):
        """Calculate base toilet consumption per cycle."""
        component_runtime_hrs_per_cycle = {
            'Water Pump': self._get_profile_value('time_based', 'mins_per_cycle', 'toilet_pump') / 60,
            'Bathroom Vent Fan': self._get_profile_value('time_based', 'mins_per_cycle', 'toilet_vent_fan') / 60,
            'Tankless Water Heater': self._get_profile_value('time_based', 'mins_per_cycle', 'toilet_water_heater') / 60
        }
        
        energy_wh_per_cycle = self._calculate_energy_from_components_per_unit(component_runtime_hrs_per_cycle)
        
        water_gal_per_cycle = (
            self._get_profile_value('volume_based', 'gal_per_cycle', 'toilet_sink_water') +
            self._get_profile_value('volume_based', 'gal_per_cycle', 'toilet_gravity_flush')
        )

        self.consumption_rates['toilet'] = {
            'energy_wh_per_unit': energy_wh_per_cycle,
            'water_gal_per_unit': water_gal_per_cycle,
            'unit_type': 'cycle'
        }
        
        total_cycles = (self._get_profile_value('count_based', 'cycles_per_day_per_person', 'toilet') * 
                       self.config['num_people'] * self.config['trip_duration_days'])
        self.cycle_counts['toilet'] = {
            'units': total_cycles,
            'unit_type': 'cycles'
        }

    def _calculate_laundry_base(self):
        """Calculate base laundry consumption per cycle."""
        component_runtime_hrs_per_cycle = {
            'Washer/Dryer Combo': 80/60,  # 80 min/cycle
            'Tankless Water Heater': self._get_profile_value('time_based', 'mins_per_cycle', 'laundry_water_heater') / 60,
            'Water Pump': self._get_profile_value('time_based', 'mins_per_cycle', 'laundry_water_pump') / 60
        }
        
        energy_wh_per_cycle = self._calculate_energy_from_components_per_unit(component_runtime_hrs_per_cycle)
        water_gal_per_cycle = self.component_map['Washer/Dryer Combo']['water_gal_per_cycle']

        self.consumption_rates['laundry'] = {
            'energy_wh_per_unit': energy_wh_per_cycle,
            'water_gal_per_unit': water_gal_per_cycle,
            'unit_type': 'cycle'
        }
        
        total_cycles = (self._get_profile_value('count_based', 'cycles_per_day_per_person', 'laundry') * 
                       self.config['num_people'] * self.config['trip_duration_days'])
        self.cycle_counts['laundry'] = {
            'units': total_cycles,
            'unit_type': 'cycles'
        }

    def _calculate_hvac_base(self):
        """Calculate base HVAC consumption per day."""
        lookups = self.data["lookups"]
        cfg = self.config

        # Energy per day at full runtime (24 hrs)
        daily_energy_wh_24hr = lookups["hvac_energy_wh_day"][cfg['temperature']]
        # Scale to actual runtime hours
        energy_wh_per_day = daily_energy_wh_24hr * (cfg['hvac_runtime_hrs'] / 24)

        # Water Generation per day
        day_hrs = min(cfg['hvac_runtime_hrs'], 12)
        night_hrs = max(0, cfg['hvac_runtime_hrs'] - 12)

        gen_rate_day = lookups["hvac_water_gen_gph"]["day"][cfg['temperature']][cfg['humidity']]
        gen_rate_night = lookups["hvac_water_gen_gph"]["night"][cfg['temperature']][cfg['humidity']]

        water_generated_gal_per_day = (gen_rate_day * day_hrs) + (gen_rate_night * night_hrs)

        self.consumption_rates['hvac'] = {
            'energy_wh_per_unit': energy_wh_per_day,
            'water_gal_per_unit': -water_generated_gal_per_day,  # Negative for generation
            'unit_type': 'day'
        }
        self.cycle_counts['hvac'] = {
            'units': cfg['trip_duration_days'],
            'unit_type': 'days'
        }

    def _calculate_solar_base(self):
        """Calculate base solar production per day."""
        lookups = self.data["lookups"]
        cfg = self.config

        insolation = lookups["solar"]["insolation_wh_m2_day"][cfg['temperature']][cfg['humidity']]
        sunlight_factor = lookups["solar"]["sunlight_factor"][cfg['sunlight']]
        tilt_factor = lookups["solar"]["tilt_factor"][cfg['temperature']]
        loss_factor = lookups["solar"]["system_loss_factor"]
        
        effective_sun_hours = (insolation / self.WH_TO_KWH) * sunlight_factor * tilt_factor * loss_factor
        daily_prod_kwh = self.specs['solar_capacity_kw']['value'] * effective_sun_hours
        daily_prod_wh = daily_prod_kwh * self.WH_TO_KWH

        self.consumption_rates['solar'] = {
            'energy_wh_per_unit': -daily_prod_wh,  # Negative for production
            'water_gal_per_unit': 0,
            'unit_type': 'day'
        }
        self.cycle_counts['solar'] = {
            'units': cfg['trip_duration_days'],
            'unit_type': 'days'
        }

    def _calculate_actuation_base(self):
        """Calculate base actuation consumption per cycle."""
        # Runtime per cycle: 30 seconds
        RUNTIME_PER_CYCLE_HRS = 30 / self.SECONDS_PER_HOUR
        
        components_to_actuate = [
            'Side Room Floor', 'Side Room Wall', 'Front Room',
            'Rear Room', 'Room Support Jacks', 'Gearage'
        ]
        
        energy_wh_per_cycle = sum(
            self._get_component_power_wh_per_hour(name) * RUNTIME_PER_CYCLE_HRS 
            for name in components_to_actuate
        )

        self.consumption_rates['actuation'] = {
            'energy_wh_per_unit': energy_wh_per_cycle,
            'water_gal_per_unit': 0,
            'unit_type': 'cycle'
        }
        
        # Initial cycle count (will be updated after dump trip calculation)
        base_cycles = 2 + (self.config['relocation_count'] * 2)  # Deploy/retract for trip + relocations
        self.cycle_counts['actuation'] = {
            'units': base_cycles,
            'unit_type': 'cycles'
        }

    def _calculate_dumping_base(self):
        """Calculate base dumping consumption per dump trip."""
        # 1 dump = 4 activations of 1.5s each = 6s total
        RUNTIME_PER_DUMP_HRS = 6 / 3600
        energy_wh_per_dump = self._get_component_power_wh_per_hour('Electric Waste Valves') * RUNTIME_PER_DUMP_HRS

        self.consumption_rates['dumping'] = {
            'energy_wh_per_unit': energy_wh_per_dump,
            'water_gal_per_unit': 0,
            'unit_type': 'dump_trip'
        }
        
        # Initial count (will be updated after waste calculation)
        self.cycle_counts['dumping'] = {
            'units': 0,  # Will be calculated based on waste production
            'unit_type': 'dump_trips'
        }

    def _update_actuation_cycles(self, num_dump_trips):
        """Update actuation cycles to include dump trips."""
        base_cycles = 2 + (self.config['relocation_count'] * 2)
        total_cycles = base_cycles + (num_dump_trips * 2)
        self.cycle_counts['actuation']['units'] = total_cycles

    def _update_dumping_cycles(self, num_dump_trips):
        """Update dumping cycles based on waste production."""
        self.cycle_counts['dumping']['units'] = num_dump_trips

    def _calculate_waste_production(self):
        """Calculate total waste production based on current consumption rates and cycles."""
        if not self.results:
            # If results not calculated yet, calculate them temporarily
            temp_results = {}
            for category in self.consumption_rates:
                energy_per_unit = self.consumption_rates[category]['energy_wh_per_unit']
                water_per_unit = self.consumption_rates[category]['water_gal_per_unit']
                unit_count = self.cycle_counts[category]['units']
                
                temp_results[category] = {
                    'energy_wh': energy_per_unit * unit_count,
                    'water_gal': water_per_unit * unit_count
                }
        else:
            temp_results = self.results

        waste_lookup = self.data["lookups"]["waste_production"]
        
        # Get key consumption values
        total_meals = self.cycle_counts['cooking']['units']
        total_toilet_cycles = self.cycle_counts['toilet']['units']
        kitchen_faucet_water = (self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet') * 
                               total_meals)
        
        # Calculate Black Water Production
        cooking_black_water = kitchen_faucet_water * (waste_lookup['cooking_sink']['black'] / 
                            self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet')) \
                            if self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet') > 0 else 0
        toilet_flush_black_water = waste_lookup['toilet_flush']['black'] * total_toilet_cycles
        total_black_produced = cooking_black_water + toilet_flush_black_water

        # Calculate Grey Water Production
        total_fresh_consumed = sum(v['water_gal'] for v in temp_results.values() if v.get('water_gal', 0) > 0)
        total_grey_produced = total_fresh_consumed - total_black_produced
        
        return {
            "grey_produced_gal": total_grey_produced,
            "black_produced_gal": total_black_produced
        }

    def _calculate_dump_trips(self):
        """Calculate required dump trips based on waste water generation."""
        waste_totals = self._calculate_waste_production()
        grey_produced = waste_totals["grey_produced_gal"]
        black_produced = waste_totals["black_produced_gal"]

        grey_capacity = self.specs['greywater_capacity_gal']['value']
        black_capacity = self.specs['blackwater_capacity_gal']['value']
        
        if grey_capacity == 0 or black_capacity == 0:
            return {"grey": 0, "black": 0, "total": 0}

        grey_dumps = math.floor(grey_produced / grey_capacity) if grey_capacity > 0 else 0
        black_dumps = math.floor(black_produced / black_capacity) if black_capacity > 0 else 0
        total_trips = max(grey_dumps, black_dumps)
        
        return {"grey": grey_dumps, "black": black_dumps, "total": total_trips}

    def _summarize_results(self, dump_trip_counts, base_data):
        """Assemble the final summary with base rates, cycles, and totals."""
        # Create enhanced base consumption rates that include cycle counts
        enhanced_base_rates = {}
        for category in self.consumption_rates:
            enhanced_base_rates[category] = {
                **self.consumption_rates[category],
                'cycle_count': self.cycle_counts[category]['units'],
                'unit_type': self.consumption_rates[category]['unit_type']
            }
        
        summary = {
            "inputs": self.config,
            "base_consumption_rates": enhanced_base_rates,
            "breakdown": self.results
        }
        
        total_energy_consumption_wh = sum(v['energy_wh'] for k, v in self.results.items() 
                                        if k not in ['solar', 'hvac'] and v.get('energy_wh', 0) > 0)
        total_water_consumption_gal = sum(v['water_gal'] for v in self.results.values() 
                                        if v.get('water_gal', 0) > 0)
        net_energy_wh = sum(v['energy_wh'] for v in self.results.values())
        
        waste_totals = self._calculate_waste_production()
        grey_produced = waste_totals["grey_produced_gal"]
        black_produced = waste_totals["black_produced_gal"]

        grey_capacity = self.specs['greywater_capacity_gal']['value']
        black_capacity = self.specs['blackwater_capacity_gal']['value']

        grey_dumps_needed = dump_trip_counts['grey']
        black_dumps_needed = dump_trip_counts['black']
        
        final_grey_level = grey_produced - (grey_dumps_needed * grey_capacity)
        final_black_level = black_produced - (black_dumps_needed * black_capacity)
        final_fresh_level = (self.specs['freshwater_capacity_gal']['value'] - 
                           total_water_consumption_gal - self.results['hvac']['water_gal'])
        final_battery_level_kwh = (self.specs['battery_capacity_kwh']['value'] - 
                                 (net_energy_wh / self.WH_TO_KWH))
        
        summary['summary'] = {
            "total_consumption": {
                "energy_kwh": total_energy_consumption_wh / self.WH_TO_KWH,
                "water_gal": total_water_consumption_gal
            },
            "total_production": {
                "solar_energy_kwh": -self.results['solar']['energy_wh'] / self.WH_TO_KWH,
                "generated_water_gal": -self.results['hvac']['water_gal']
            },
            "net_consumption": {
                "energy_kwh": net_energy_wh / self.WH_TO_KWH,
            },
            "waste_summary": {
                "grey_water_produced_gal": grey_produced,
                "black_water_produced_gal": black_produced,
                "required_dump_trips": dump_trip_counts['total'],
                "grey_water_dump_trips": grey_dumps_needed,
                "black_water_dump_trips": black_dumps_needed,
            },
            "final_tank_levels": {
                "battery_kwh": final_battery_level_kwh,
                "battery_percent": (final_battery_level_kwh / self.specs['battery_capacity_kwh']['value']) * 100,
                "fresh_water_gal": final_fresh_level,
                "fresh_water_percent": (final_fresh_level / self.specs['freshwater_capacity_gal']['value']) * 100,
                "grey_water_gal": final_grey_level,
                "grey_water_percent": (final_grey_level / grey_capacity) * 100 if grey_capacity > 0 else 0,
                "black_water_gal": final_black_level,
                "black_water_percent": (final_black_level / black_capacity) * 100 if black_capacity > 0 else 0
            }
        }
        
        return summary