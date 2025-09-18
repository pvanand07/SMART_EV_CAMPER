# calculator.py
import json
import math
import pandas as pd # Add pandas for dataframe conversion

class ResourceCalculator:
    """
    Calculates resource consumption for a trailer based on trip configuration.
    
    This class uses pre-defined lookup data to estimate energy (Wh) and 
    water (gallons) usage for various activities like living, cooking, showering, etc.
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
        
        self.results = {}

    def _calculate_energy_from_components(self, components, scale_factor=1):
        """
        Calculates total energy consumption for a list of components.

        Args:
            components (dict): A dictionary where keys are component names and
                               values are their calculated runtime in hours.
            scale_factor (float): A factor to scale the final energy result (e.g., for per-meal calculations).

        Returns:
            float: The total energy consumed in Watt-hours.
        """
        total_wh = 0
        for name, runtime_hrs in components.items():
            total_wh += self._get_component_power_wh(name, runtime_hrs * scale_factor)
        return total_wh

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

    def _get_component_power_wh(self, name, runtime_hrs):
        """Calculates energy consumption for a component."""
        comp = self.component_map.get(name)
        if not comp:
            return 0
        power = comp['voltage_v'] * comp['avg_amps'] * runtime_hrs
        idle_power = comp['voltage_v'] * comp['idle_amps'] * (self.config['trip_duration_days'] * 24 - runtime_hrs)
        return power + idle_power

    def calculate(self):
        """
        Performs all resource calculations and returns a summary.

        Returns:
            dict: A dictionary containing the breakdown of consumption by category
                  and a final summary of net resources and tank levels.
        """
        # Reset results for re-calculation
        self.results = {}

        # These calculations must run first as they determine water waste
        self._calculate_living()
        self._calculate_cooking()
        self._calculate_shower()
        self._calculate_toilet()
        self._calculate_laundry()
        self._calculate_hvac_and_water_gen()

        # Calculate dump trips needed based on waste water produced
        dump_trip_counts = self._calculate_dump_trips()

        # These calculations depend on the number of dump trips
        self._calculate_actuation(dump_trip_counts['total'])
        self._calculate_dumping(dump_trip_counts['total'])
        
        # Calculate energy production
        self._calculate_solar()
        
        return self._summarize_results(dump_trip_counts)

    def _calculate_waste_production(self):
        """
        Calculates the total grey and black water produced during the trip.
        This method acts as the single source of truth for waste calculations.
        """
        waste_lookup = self.data["lookups"]["waste_production"]
        cfg = self.config

        # --- Recalculate component water usage for accurate waste allocation ---
        total_meals = self._get_profile_value('count_based', 'meals_per_day', 'cooking') * cfg['trip_duration_days']
        total_toilet_cycles = self._get_profile_value('count_based', 'cycles_per_day_per_person', 'toilet') * cfg['num_people'] * cfg['trip_duration_days']

        kitchen_faucet_water = self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet') * total_meals
        
        # --- Calculate Black Water Production ---
        # Black water comes from the kitchen sink (food scraps) and toilet flushes.
        cooking_black_water = kitchen_faucet_water * (waste_lookup['cooking_sink']['black'] / self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet')) if self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet') > 0 else 0
        toilet_flush_black_water = waste_lookup['toilet_flush']['black'] * total_toilet_cycles
        
        total_black_produced = cooking_black_water + toilet_flush_black_water

        # --- Calculate Grey Water Production ---
        # Grey water is all consumed fresh water minus what becomes black water.
        total_fresh_consumed = sum(v['water_gal'] for v in self.results.values() if v.get('water_gal', 0) > 0)
        
        # The toilet flush uses grey water, so it's a net neutral for the grey tank (in/out)
        # but we must account for the fresh water that becomes black water.
        total_grey_produced = total_fresh_consumed - total_black_produced
        
        return {
            "grey_produced_gal": total_grey_produced,
            "black_produced_gal": total_black_produced
        }

    def _get_profile_value(self, category, subcategory, key):
        """Helper method to get values from the categorized profile data."""
        profile = self.profiles[self.config['user_type']]
        return profile[category][subcategory][key]

    def _calculate_living(self):
        duration_days = self.config['trip_duration_days']
        
        # Assuming a 5-second runtime for each smart key cycle
        SMART_KEY_CYCLE_SECONDS = 5
        smart_key_total_cycles = self._get_profile_value('count_based', 'cycles_per_day', 'living_smart_key') * duration_days
        
        # Define components and their runtime calculations
        component_runtimes_hrs = {
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
            'Smart Key Lighting': (smart_key_total_cycles * SMART_KEY_CYCLE_SECONDS) / self.SECONDS_PER_HOUR,
            'Refrigerator': 24, # Always on
            'Satellite Internet PSU': 24, # Always on
            'AI Compute': 24, # Always on
        }
        
        total_energy_wh = self._calculate_energy_from_components(component_runtimes_hrs, duration_days)

        # Define water consumption sources
        water_sources_gal_per_day = {
            'cleaning': self._get_profile_value('volume_based', 'gal_per_day', 'living_cleaning'),
            'drinking': self._get_profile_value('volume_based', 'gal_per_day', 'living_drinking_water'),
            'ice_maker': self._get_profile_value('volume_based', 'gal_per_day', 'living_ice_maker_water'),
        }
        total_water_gal = sum(water_sources_gal_per_day.values()) * self.config['num_people'] * duration_days

        self.results['living'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_cooking(self):
        # Cooking does not scale with number of people in the model
        total_meals = self._get_profile_value('count_based', 'meals_per_day', 'cooking') * self.config['trip_duration_days']

        runtime_hrs = {
            'Stove': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_stove') / 60) * total_meals,
            'Microwave': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_microwave') / 60) * total_meals,
            'Dishwasher': 80/60 * self._get_profile_value('count_based', 'cycles_per_meal', 'cooking_dishwasher') * total_meals, # From sheet, 80 min/cycle
            'Tankless Water Heater': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_water_heater') / 60) * total_meals,
            'Garbage Disposal': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_garbage_disposal') / 60) * total_meals,
            'Consumer Electronics': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_consumer_electronics') / 60) * total_meals,
            'Water Pump': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_pump') / 60) * total_meals,
            'Range Hood': (self._get_profile_value('time_based', 'mins_per_meal', 'cooking_range_hood') / 60) * total_meals
        }
        
        # Calculate base energy, then add stove energy multiplied by burner count
        base_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items() if name != 'Stove')
        stove_energy_wh = self._get_component_power_wh('Stove', runtime_hrs['Stove']) * self._get_profile_value('count_based', 'burners_per_meal', 'cooking_stove')
        total_energy_wh = base_energy_wh + stove_energy_wh

        water_gal = {
            'dishwasher': self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_dishwasher_water') * self._get_profile_value('count_based', 'cycles_per_meal', 'cooking_dishwasher') * total_meals,
            'kitchen_faucet': self._get_profile_value('volume_based', 'gal_per_meal', 'cooking_kitchen_faucet') * total_meals
        }
        
        self.results['cooking'] = {'energy_wh': total_energy_wh, 'water_gal': sum(water_gal.values())}

    def _calculate_shower(self):
        total_showers = self._get_profile_value('count_based', 'cycles_per_day_per_person', 'shower') * self.config['num_people'] * self.config['trip_duration_days']
        
        runtime_hrs = {
            'Electric Shower': (self._get_profile_value('time_based', 'mins_per_cycle', 'shower_duration') / 60) * total_showers,
            'Bathroom Vent Fan': (self._get_profile_value('time_based', 'mins_per_cycle', 'shower_vent_fan') / 60) * total_showers,
            'Consumer Electronics': (self._get_profile_value('time_based', 'mins_per_cycle', 'shower_electronics') / 60) * total_showers,
            'Water Pump': (self._get_profile_value('time_based', 'mins_per_cycle', 'shower_water_pump') / 60) * total_showers
        }

        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())
        total_water_gal = self._get_profile_value('volume_based', 'gal_per_cycle', 'shower_water') * total_showers
        
        self.results['shower'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_toilet(self):
        total_cycles = self._get_profile_value('count_based', 'cycles_per_day_per_person', 'toilet') * self.config['num_people'] * self.config['trip_duration_days']
        
        runtime_hrs = {
            'Water Pump': (self._get_profile_value('time_based', 'mins_per_cycle', 'toilet_pump') / 60) * total_cycles,
            'Bathroom Vent Fan': (self._get_profile_value('time_based', 'mins_per_cycle', 'toilet_vent_fan') / 60) * total_cycles,
            'Tankless Water Heater': (self._get_profile_value('time_based', 'mins_per_cycle', 'toilet_water_heater') / 60) * total_cycles
        }
        
        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())
        
        sink_water_gal = self._get_profile_value('volume_based', 'gal_per_cycle', 'toilet_sink_water') * total_cycles # Fresh water for sink
        flush_water_gal = self._get_profile_value('volume_based', 'gal_per_cycle', 'toilet_gravity_flush') * total_cycles
        total_water_gal = sink_water_gal + flush_water_gal

        self.results['toilet'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_laundry(self):
        total_cycles = self._get_profile_value('count_based', 'cycles_per_day_per_person', 'laundry') * self.config['num_people'] * self.config['trip_duration_days']
        
        runtime_hrs = {
            'Washer/Dryer Combo': (80/60) * total_cycles, # From sheet, 80 min/cycle approx
            'Tankless Water Heater': (self._get_profile_value('time_based', 'mins_per_cycle', 'laundry_water_heater') / 60) * total_cycles,
            'Water Pump': (self._get_profile_value('time_based', 'mins_per_cycle', 'laundry_water_pump') / 60) * total_cycles
        }
        
        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())
        total_water_gal = self.component_map['Washer/Dryer Combo']['water_gal_per_cycle'] * total_cycles

        self.results['laundry'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_actuation(self, num_dump_trips):
        # 1 cycle = deploy, 1 cycle = retract.
        # Base is 2 (one deploy/retract per trip). Add 2 for each relocation and dump trip.
        total_cycles = 2 + (self.config['relocation_count'] * 2) + (num_dump_trips * 2)
        
        # Runtimes are fixed per cycle from Actuation sheet (e.g., 30s = 0.008333 hrs)
        RUNTIME_PER_CYCLE_HRS = 30 / self.SECONDS_PER_HOUR
        
        components_to_actuate = [
            'Side Room Floor', 'Side Room Wall', 'Front Room',
            'Rear Room', 'Room Support Jacks', 'Gearage'
        ]
        
        total_energy_wh = sum(self._get_component_power_wh(name, RUNTIME_PER_CYCLE_HRS * total_cycles) for name in components_to_actuate)
        
        self.results['actuation'] = {'energy_wh': total_energy_wh, 'water_gal': 0}

    def _calculate_dumping(self, num_dump_trips):
        if num_dump_trips == 0:
            self.results['dumping'] = {'energy_wh': 0, 'water_gal': 0}
            return
            
        # From Dumping sheet: 1 cycle = 4 activations of 1.5s each = 6s total
        RUNTIME_PER_DUMP_HRS = 6 / 3600
        total_runtime_hrs = RUNTIME_PER_DUMP_HRS * num_dump_trips
        total_energy_wh = self._get_component_power_wh('Electric Waste Valves', total_runtime_hrs)
        
        self.results['dumping'] = {'energy_wh': total_energy_wh, 'water_gal': 0}

    def _calculate_hvac_and_water_gen(self):
        lookups = self.data["lookups"]
        cfg = self.config

        # Energy calculation
        daily_energy_wh = lookups["hvac_energy_wh_day"][cfg['temperature']]
        total_energy_wh = daily_energy_wh * (cfg['hvac_runtime_hrs'] / 24) * cfg['trip_duration_days']

        # Water Generation Calculation
        day_hrs = min(cfg['hvac_runtime_hrs'], 12)
        night_hrs = max(0, cfg['hvac_runtime_hrs'] - 12)

        gen_rate_day = lookups["hvac_water_gen_gph"]["day"][cfg['temperature']][cfg['humidity']]
        gen_rate_night = lookups["hvac_water_gen_gph"]["night"][cfg['temperature']][cfg['humidity']]

        water_generated_gal = ((gen_rate_day * day_hrs) + (gen_rate_night * night_hrs)) * cfg['trip_duration_days']
        
        # Water generated is negative consumption
        self.results['hvac'] = {'energy_wh': total_energy_wh, 'water_gal': -water_generated_gal}

    def _calculate_solar(self):
        lookups = self.data["lookups"]
        cfg = self.config

        insolation = lookups["solar"]["insolation_wh_m2_day"][cfg['temperature']][cfg['humidity']]
        sunlight_factor = lookups["solar"]["sunlight_factor"][cfg['sunlight']]
        tilt_factor = lookups["solar"]["tilt_factor"][cfg['temperature']]
        loss_factor = lookups["solar"]["system_loss_factor"]
        
        # Simplified formula: Daily_Prod = Solar_Capacity_kW * Insolation_kWh_m2 * Factors
        effective_sun_hours = (insolation / self.WH_TO_KWH) * sunlight_factor * tilt_factor * loss_factor
        
        daily_prod_kwh = self.specs['solar_capacity_kw']['value'] * effective_sun_hours
        total_prod_wh = daily_prod_kwh * self.WH_TO_KWH * cfg['trip_duration_days']
        
        self.results['solar'] = {'energy_wh': -total_prod_wh, 'water_gal': 0}
        
    def _calculate_dump_trips(self):
        """
        Calculates required dump trips based on waste water generation.
        Returns a dictionary with individual and total trip counts.
        """
        waste_totals = self._calculate_waste_production()
        grey_produced = waste_totals["grey_produced_gal"]
        black_produced = waste_totals["black_produced_gal"]

        grey_capacity = self.specs['greywater_capacity_gal']['value']
        black_capacity = self.specs['blackwater_capacity_gal']['value']
        
        if grey_capacity == 0 or black_capacity == 0:
            return {"grey": 0, "black": 0, "total": 0}

        # Calculate dumps needed for each tank
        grey_dumps = math.floor(grey_produced / grey_capacity) if grey_capacity > 0 else 0
        black_dumps = math.floor(black_produced / black_capacity) if black_capacity > 0 else 0

        # The required number of trips is the maximum needed for either tank
        total_trips = max(grey_dumps, black_dumps)
        
        return {"grey": grey_dumps, "black": black_dumps, "total": total_trips}

    def _summarize_results(self, dump_trip_counts):
        """Assembles the final summary dictionary with corrected tank logic."""
        summary = {
            "inputs": self.config,
            "breakdown": self.results
        }
        
        total_energy_consumption_wh = sum(v['energy_wh'] for k, v in self.results.items() if k != 'solar' and v.get('energy_wh', 0) > 0)
        total_water_consumption_gal = sum(v['water_gal'] for v in self.results.values() if v.get('water_gal', 0) > 0)
        net_energy_wh = sum(v['energy_wh'] for v in self.results.values())
        
        # Get consistent waste calculations
        waste_totals = self._calculate_waste_production()
        grey_produced = waste_totals["grey_produced_gal"]
        black_produced = waste_totals["black_produced_gal"]

        # --- CORRECTED LOGIC STARTS HERE ---

        grey_capacity = self.specs['greywater_capacity_gal']['value']
        black_capacity = self.specs['blackwater_capacity_gal']['value']

        # Get dump counts from the pre-calculated dictionary
        grey_dumps_needed = dump_trip_counts['grey']
        black_dumps_needed = dump_trip_counts['black']
        reported_required_trips = dump_trip_counts['total']

        # Calculate final levels based on their own dump count
        final_grey_level = grey_produced - (grey_dumps_needed * grey_capacity)
        final_black_level = black_produced - (black_dumps_needed * black_capacity)
        
        # --- End of corrected logic ---

        final_fresh_level = self.specs['freshwater_capacity_gal']['value'] - total_water_consumption_gal - self.results['hvac']['water_gal']
        final_battery_level_kwh = self.specs['battery_capacity_kwh']['value'] - (net_energy_wh / self.WH_TO_KWH)
        
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
                "required_dump_trips": reported_required_trips, # Use the overall max here for the user
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