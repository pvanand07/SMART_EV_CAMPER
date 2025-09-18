# simple_calculator.py

class SimpleResourceCalculator:
    """
    Ultra-simplified resource calculator that returns daily/cycle values with multipliers.
    Final calculation is just: base_value * usage_pattern * multipliers
    """
    
    def __init__(self, lookup_data):
        self.data = lookup_data
    
    def get_daily_consumption_rates(self, user_type, temperature, humidity, sunlight):
        """
        Returns a simple dict of daily consumption rates and multipliers.
        Each item has: base_rate, daily_usage, and scale_factors
        """
        profile = self.data['user_profiles'][user_type]
        components = self.data['components']
        
        return {
            # === ENERGY CONSUMPTION (Wh per day base) ===
            "energy": {
                # Living - household level (doesn't scale with people)
                "living_audio": {
                    "wh_per_day": (components['living']['Audio Amplifier']['power_w'] * profile['daily_usage']['audio_mins']) / 60,
                    "scale_with_people": False
                },
                "living_tv": {
                    "wh_per_day": (components['living']['Television']['power_w'] * profile['daily_usage']['tv_mins']) / 60,
                    "scale_with_people": False
                },
                "living_lighting": {
                    "wh_per_day": (components['living']['Lighting']['power_w'] * profile['daily_usage']['lighting_mins']) / 60,
                    "scale_with_people": False
                },
                "living_refrigerator": {
                    "wh_per_day": components['living']['Refrigerator']['power_w'] * 24,  # Always on
                    "scale_with_people": False
                },
                
                # Cooking - household level 
                "cooking_stove": {
                    "wh_per_day": (components['cooking']['Stove']['power_w'] * profile['meal_patterns']['stove_mins_per_meal'] * profile['meal_patterns']['meals_per_day'] * profile['meal_patterns']['stove_burners_per_meal']) / 60,
                    "scale_with_people": False
                },
                "cooking_microwave": {
                    "wh_per_day": (components['cooking']['Microwave']['power_w'] * profile['meal_patterns']['microwave_mins_per_meal'] * profile['meal_patterns']['meals_per_day']) / 60,
                    "scale_with_people": False
                },
                "cooking_dishwasher": {
                    "wh_per_day": (components['cooking']['Dishwasher']['power_w'] * components['cooking']['Dishwasher']['cycle_time_min'] * profile['meal_patterns']['dishwasher_cycles_per_meal'] * profile['meal_patterns']['meals_per_day']) / 60,
                    "scale_with_people": False
                },
                
                # Personal care - scales with people
                "shower_heater": {
                    "wh_per_day": (components['bathroom']['Electric Shower']['power_w'] * profile['personal_care']['shower_duration_mins'] * profile['personal_care']['shower_cycles_per_day']) / 60,
                    "scale_with_people": True
                },
                "shower_pump": {
                    "wh_per_day": (components['bathroom']['Water Pump']['power_w'] * profile['personal_care']['shower_duration_mins'] * profile['personal_care']['shower_cycles_per_day']) / 60,
                    "scale_with_people": True
                },
                "laundry": {
                    "wh_per_day": (components['laundry']['Washer Dryer']['power_w'] * components['laundry']['Washer Dryer']['cycle_time_min'] * profile['personal_care']['laundry_cycles_per_day']) / 60,
                    "scale_with_people": True
                }
            },
            
            # === WATER CONSUMPTION (gallons per day base) ===
            "water": {
                # Personal consumption - scales with people
                "drinking": {
                    "gal_per_day": profile['daily_usage']['drinking_water_gal'],
                    "scale_with_people": True
                },
                "cleaning": {
                    "gal_per_day": profile['daily_usage']['cleaning_water_gal'],
                    "scale_with_people": True
                },
                "ice": {
                    "gal_per_day": profile['daily_usage']['ice_water_gal'],
                    "scale_with_people": True
                },
                "shower": {
                    "gal_per_day": profile['personal_care']['shower_water_gal_per_cycle'] * profile['personal_care']['shower_cycles_per_day'],
                    "scale_with_people": True
                },
                "toilet_sink": {
                    "gal_per_day": profile['personal_care']['toilet_sink_water_gal_per_cycle'] * profile['personal_care']['toilet_cycles_per_day'],
                    "scale_with_people": True
                },
                "toilet_flush": {
                    "gal_per_day": profile['personal_care']['toilet_flush_water_gal_per_cycle'] * profile['personal_care']['toilet_cycles_per_day'],
                    "scale_with_people": True
                },
                "laundry": {
                    "gal_per_day": components['laundry']['Washer Dryer']['water_gal_per_cycle'] * profile['personal_care']['laundry_cycles_per_day'],
                    "scale_with_people": True
                },
                
                # Household consumption - doesn't scale with people
                "cooking": {
                    "gal_per_day": profile['meal_patterns']['kitchen_water_gal_per_meal'] * profile['meal_patterns']['meals_per_day'],
                    "scale_with_people": False
                },
                "dishwasher": {
                    "gal_per_day": components['cooking']['Dishwasher']['water_gal_per_cycle'] * profile['meal_patterns']['dishwasher_cycles_per_meal'] * profile['meal_patterns']['meals_per_day'],
                    "scale_with_people": False
                }
            },
            
            # === ENVIRONMENTAL SYSTEMS ===
            "hvac": {
                "energy_wh_per_day": self.data['environmental_systems']['hvac']['energy_consumption_wh_per_day'][temperature],
                "water_generation_gal_per_day": -self.data['environmental_systems']['hvac']['water_generation_gph'][temperature][humidity] * 24,  # Negative = generation
                "runtime_multiplier": True  # Gets multiplied by (actual_hours / 24)
            },
            
            "solar": {
                "energy_kwh_per_day": -self._calculate_solar_generation_per_day(temperature, humidity, sunlight),  # Negative = generation
                "environmental_dependent": True
            }
        }
    
    def _calculate_solar_generation_per_day(self, temperature, humidity, sunlight):
        """Calculate daily solar generation in kWh."""
        solar_data = self.data['environmental_systems']['solar']
        
        base_insolation = solar_data['base_insolation_wh_per_m2_per_day'][temperature][humidity]
        sunlight_factor = solar_data['sunlight_multiplier'][sunlight]
        tilt_factor = solar_data['tilt_multiplier'][temperature]
        efficiency = solar_data['system_efficiency']
        solar_capacity = self.data['trailer_specs']['solar_capacity_kw']
        
        return solar_capacity * (base_insolation / 1000) * sunlight_factor * tilt_factor * efficiency
    
    def calculate_trip_totals(self, rates, num_people, duration_days, hvac_runtime_hrs=12, relocation_count=0):
        """
        Apply multipliers to get final trip totals.
        This is where the magic happens - everything else is just lookup!
        """
        results = {
            "daily_breakdown": {},
            "trip_totals": {
                "energy_consumption_kwh": 0,
                "energy_generation_kwh": 0,
                "water_consumption_gal": 0,
                "water_generation_gal": 0
            }
        }
        
        # === ENERGY CALCULATIONS ===
        for item, data in rates['energy'].items():
            daily_wh = data['wh_per_day']
            if data['scale_with_people']:
                daily_wh *= num_people
            
            trip_total_kwh = (daily_wh * duration_days) / 1000
            results['daily_breakdown'][f"{item}_energy"] = {
                "daily_kwh": daily_wh / 1000,
                "trip_total_kwh": trip_total_kwh
            }
            results['trip_totals']['energy_consumption_kwh'] += trip_total_kwh
        
        # === WATER CALCULATIONS ===  
        for item, data in rates['water'].items():
            daily_gal = data['gal_per_day']
            if data['scale_with_people']:
                daily_gal *= num_people
                
            trip_total_gal = daily_gal * duration_days
            results['daily_breakdown'][f"{item}_water"] = {
                "daily_gal": daily_gal,
                "trip_total_gal": trip_total_gal
            }
            results['trip_totals']['water_consumption_gal'] += trip_total_gal
        
        # === HVAC (with runtime factor) ===
        hvac_energy_kwh = (rates['hvac']['energy_wh_per_day'] * (hvac_runtime_hrs / 24) * duration_days) / 1000
        hvac_water_gal = rates['hvac']['water_generation_gal_per_day'] * (hvac_runtime_hrs / 24) * duration_days
        
        results['daily_breakdown']['hvac'] = {
            "daily_energy_kwh": hvac_energy_kwh / duration_days,
            "daily_water_gal": hvac_water_gal / duration_days,
            "trip_energy_kwh": hvac_energy_kwh,
            "trip_water_gal": hvac_water_gal
        }
        results['trip_totals']['energy_consumption_kwh'] += hvac_energy_kwh
        results['trip_totals']['water_generation_gal'] += abs(hvac_water_gal)  # Make positive for display
        
        # === SOLAR ===
        solar_energy_kwh = rates['solar']['energy_kwh_per_day'] * duration_days  # Already negative
        results['daily_breakdown']['solar'] = {
            "daily_energy_kwh": rates['solar']['energy_kwh_per_day'],
            "trip_energy_kwh": solar_energy_kwh
        }
        results['trip_totals']['energy_generation_kwh'] += abs(solar_energy_kwh)  # Make positive for display
        
        # === OPERATIONAL (relocations + dump trips) ===
        # Simplified: assume 1 dump trip for now (could be calculated from waste)
        dump_trips = 1  # This would be calculated from waste production vs tank capacity
        
        actuation_energy_kwh = self._calculate_actuation_energy(duration_days, relocation_count, dump_trips) / 1000
        dumping_energy_kwh = self._calculate_dumping_energy(dump_trips) / 1000
        
        results['daily_breakdown']['operations'] = {
            "actuation_kwh": actuation_energy_kwh,
            "dumping_kwh": dumping_energy_kwh,
            "total_kwh": actuation_energy_kwh + dumping_energy_kwh
        }
        results['trip_totals']['energy_consumption_kwh'] += actuation_energy_kwh + dumping_energy_kwh
        
        # === NET CONSUMPTION ===
        results['net_consumption'] = {
            "energy_kwh": results['trip_totals']['energy_consumption_kwh'] - results['trip_totals']['energy_generation_kwh'],
            "water_gal": results['trip_totals']['water_consumption_gal'] - results['trip_totals']['water_generation_gal']
        }
        
        return results
    
    def _calculate_actuation_energy(self, duration_days, relocations, dump_trips):
        """Calculate actuation energy in Wh."""
        # Base: 2 cycles per trip (deploy + retract)
        # Additional: 2 cycles per relocation, 2 cycles per dump trip
        total_cycles = 2 + (relocations * 2) + (dump_trips * 2)
        return self.data['components']['operational']['Room Actuators']['power_w'] * (30 / 3600) * total_cycles
    
    def _calculate_dumping_energy(self, dump_trips):
        """Calculate dumping energy in Wh."""
        return self.data['components']['operational']['Dump Valves']['power_w'] * (6 / 3600) * dump_trips


# === EXAMPLE USAGE ===
def demo():
    import json
    
    # This would load from your JSON file
    with open('simplified_lookup_data.json', 'r') as f:
        lookup_data = json.load(f)
    
    calc = SimpleResourceCalculator(lookup_data)
    
    # Get base daily rates
    rates = calc.get_daily_consumption_rates(
        user_type='Typical',
        temperature='Hot', 
        humidity='Comfortable',
        sunlight='Hi- Sunny'
    )
    
    # Apply trip parameters to get final totals
    results = calc.calculate_trip_totals(
        rates=rates,
        num_people=1,
        duration_days=3,
        hvac_runtime_hrs=12,
        relocation_count=1
    )
    
    # Print clean summary
    print("=== TRIP RESOURCE SUMMARY ===")
    print(f"Energy Consumption: {results['trip_totals']['energy_consumption_kwh']:.1f} kWh")
    print(f"Energy Generation:  {results['trip_totals']['energy_generation_kwh']:.1f} kWh") 
    print(f"Net Energy:         {results['net_consumption']['energy_kwh']:.1f} kWh")
    print()
    print(f"Water Consumption:  {results['trip_totals']['water_consumption_gal']:.1f} gal")
    print(f"Water Generation:   {results['trip_totals']['water_generation_gal']:.1f} gal")
    print(f"Net Water:          {results['net_consumption']['water_gal']:.1f} gal")
    print(json.dumps(results, indent=4))
    return results

if __name__ == "__main__":
    demo()