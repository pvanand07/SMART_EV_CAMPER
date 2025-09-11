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
        num_dump_trips = self._calculate_dump_trips()

        # These calculations depend on the number of dump trips
        self._calculate_actuation(num_dump_trips)
        self._calculate_dumping(num_dump_trips)
        
        # Calculate energy production
        self._calculate_solar()
        
        return self._summarize_results(num_dump_trips)

    def _calculate_living(self):
        profile = self.profiles[self.config['user_type']]
        duration_days = self.config['trip_duration_days']
        
        runtime_hrs = {
            'Audio Amplifier': profile['living_audio_mins_day'] * duration_days / 60,
            'Television': profile['living_tv_mins_day'] * duration_days / 60,
            'Smart Glass Display': profile['living_smart_glass_hrs_day'] * duration_days,
            'Refrigerator': 24 * duration_days, # Always on
            'Satellite Internet PSU': 24 * duration_days,
            'Lighting': profile['living_lighting_mins_day'] * duration_days / 60,
            'Consumer Electronics': profile['living_electronics_hrs_day'] * duration_days,
            'AI Compute': 24 * duration_days # Assumed always on like in sheet
        }
        
        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())
        total_water_gal = (profile['living_cleaning_gal_day'] + profile['living_drinking_water_gal_day']) * self.config['num_people'] * duration_days

        self.results['living'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_cooking(self):
        profile = self.profiles[self.config['user_type']]
        # Cooking does not scale with number of people in the model
        total_meals = profile['cooking_meals_day'] * self.config['trip_duration_days']

        runtime_hrs = {
            'Stove': (profile['cooking_stove_mins_meal'] / 60) * total_meals,
            'Microwave': (profile['cooking_microwave_mins_meal'] / 60) * total_meals,
            'Dishwasher': 80/60 * profile['cooking_dishwasher_cycles_meal'] * total_meals, # From sheet, 80 min/cycle
            'Tankless Water Heater': (profile['cooking_water_heater_mins_meal'] / 60) * total_meals
        }
        
        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())

        water_gal = {
            'dishwasher': profile['cooking_dishwasher_water_gal_meal'] * profile['cooking_dishwasher_cycles_meal'] * total_meals,
            'kitchen_faucet': profile['cooking_kitchen_faucet_gal_meal'] * total_meals
        }
        
        self.results['cooking'] = {'energy_wh': total_energy_wh, 'water_gal': sum(water_gal.values())}

    def _calculate_shower(self):
        profile = self.profiles[self.config['user_type']]
        total_showers = profile['shower_cycles_day_person'] * self.config['num_people'] * self.config['trip_duration_days']
        
        runtime_hrs = {
            'Electric Shower': (profile['shower_duration_min_cycle'] / 60) * total_showers,
            'Bathroom Vent Fan': (profile['shower_vent_fan_min_cycle'] / 60) * total_showers
        }

        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())
        total_water_gal = profile['shower_water_gal_cycle'] * total_showers
        
        self.results['shower'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_toilet(self):
        profile = self.profiles[self.config['user_type']]
        total_cycles = profile['toilet_cycles_day_person'] * self.config['num_people'] * self.config['trip_duration_days']
        
        runtime_hrs = {
            'Grey Water Pump': (profile['toilet_pump_min_cycle'] / 60) * total_cycles,
            'Bathroom Vent Fan': (profile['toilet_vent_fan_min_cycle'] / 60) * total_cycles,
            'Tankless Water Heater': (profile['toilet_water_heater_min_cycle'] / 60) * total_cycles
        }
        
        total_energy_wh = sum(self._get_component_power_wh(name, hrs) for name, hrs in runtime_hrs.items())
        total_water_gal = profile['toilet_sink_water_gal_cycle'] * total_cycles # Fresh water for sink

        self.results['toilet'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_laundry(self):
        profile = self.profiles[self.config['user_type']]
        total_cycles = profile['laundry_cycles_day_person'] * self.config['num_people'] * self.config['trip_duration_days']
        
        # Energy is a fixed value per cycle from the sheet, not calculated from volts/amps
        ENERGY_PER_CYCLE_WH = 346.15
        total_energy_wh = ENERGY_PER_CYCLE_WH * total_cycles
        total_water_gal = self.component_map['Washer/Dryer Combo']['water_gal_per_cycle'] * total_cycles

        self.results['laundry'] = {'energy_wh': total_energy_wh, 'water_gal': total_water_gal}

    def _calculate_actuation(self, num_dump_trips):
        # 1 cycle = deploy, 1 cycle = retract.
        # Base is 2 (one deploy/retract per trip). Add 2 for each relocation and dump trip.
        total_cycles = 2 + (self.config['relocation_count'] * 2) + (num_dump_trips * 2)
        
        # Runtimes are fixed per cycle from Actuation sheet (e.g., 30s = 0.008333 hrs)
        RUNTIME_PER_CYCLE_HRS = 30 / 3600
        
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
        """Calculates required dump trips based on waste water generation."""
        waste_lookup = self.data["lookups"]["waste_production"]
        profile = self.profiles[self.config['user_type']]
        cfg = self.config
        
        total_meals = profile['cooking_meals_day'] * cfg['trip_duration_days']
        total_showers = profile['shower_cycles_day_person'] * cfg['num_people'] * cfg['trip_duration_days']
        total_toilet_cycles = profile['toilet_cycles_day_person'] * cfg['num_people'] * cfg['trip_duration_days']
        total_laundry_cycles = profile['laundry_cycles_day_person'] * cfg['num_people'] * cfg['trip_duration_days']

        grey_sources = {
            'living': self.results.get('living', {}).get('water_gal', 0),
            'cooking': self.results.get('cooking', {}).get('water_gal', 0),
            'shower': self.results.get('shower', {}).get('water_gal', 0),
            'laundry': self.results.get('laundry', {}).get('water_gal', 0),
            'toilet': self.results.get('toilet', {}).get('water_gal', 0)
        }
        
        black_sources = {
            'cooking': (waste_lookup['cooking_sink']['black'] / profile['cooking_kitchen_faucet_gal_meal']) * self.results['cooking']['water_gal'] if profile['cooking_kitchen_faucet_gal_meal'] > 0 else 0,
            'toilet_flush': waste_lookup['toilet_flush']['black'] * total_toilet_cycles
        }

        grey_produced = sum(grey_sources.values())
        black_produced = sum(black_sources.values())
        
        grey_capacity = self.specs['greywater_capacity_gal']['value']
        black_capacity = self.specs['blackwater_capacity_gal']['value']
        
        if grey_capacity == 0 or black_capacity == 0: return 0

        num_trips = math.floor(max(grey_produced / grey_capacity, black_produced / black_capacity))
        
        return num_trips

    def _summarize_results(self, num_dump_trips):
        """Assembles the final summary dictionary with corrected tank logic."""
        summary = {
            "inputs": self.config,
            "breakdown": self.results
        }
        
        # --- Pre-calculation from the original method ---
        total_energy_consumption_wh = sum(v['energy_wh'] for k, v in self.results.items() if k != 'solar' and v['energy_wh'] > 0)
        total_water_consumption_gal = sum(v['water_gal'] for v in self.results.values() if v['water_gal'] > 0)
        net_energy_wh = sum(v['energy_wh'] for v in self.results.values())
        
        waste_lookup = self.data["lookups"]["waste_production"]
        profile = self.profiles[self.config['user_type']]
        cfg = self.config
        
        total_toilet_cycles = profile['toilet_cycles_day_person'] * cfg['num_people'] * cfg['trip_duration_days']
        grey_flush_usage = abs(waste_lookup['toilet_flush']['grey'] * total_toilet_cycles)

        grey_produced = total_water_consumption_gal # Simplified: all consumed fresh water becomes grey water
        black_produced = (waste_lookup['toilet_flush']['black'] * total_toilet_cycles)

        # --- CORRECTED LOGIC STARTS HERE ---

        grey_capacity = self.specs['greywater_capacity_gal']['value']
        black_capacity = self.specs['blackwater_capacity_gal']['value']

        # Calculate dumps needed for each tank INDEPENDENTLY for final level calc
        grey_dumps_needed = math.floor(grey_produced / grey_capacity) if grey_capacity > 0 else 0
        black_dumps_needed = math.floor(black_produced / black_capacity) if black_capacity > 0 else 0

        # The *reported* required trips is the max of the two
        reported_required_trips = max(grey_dumps_needed, black_dumps_needed)

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