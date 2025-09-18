#!/usr/bin/env python3
"""
Converter to transform existing complex lookup data into simplified structure.
Takes the original nested lookup data and flattens it for the new calculator.
"""

import json

class LookupDataConverter:
    """Converts complex lookup data to simplified structure."""
    
    def __init__(self, original_data):
        self.original = original_data
        self.simplified = {}
        
    def convert(self):
        """Perform the full conversion."""
        self.simplified = {
            "description": "Simplified lookup data structure for modular resource calculations",
            "components": self._convert_components(),
            "user_profiles": self._convert_user_profiles(), 
            "environmental_systems": self._convert_environmental_systems(),
            "trailer_specs": self._convert_trailer_specs(),
            "waste_allocation": self._convert_waste_allocation()
        }
        return self.simplified
    
    def _convert_components(self):
        """Convert component data to simplified power/water structure."""
        original_components = self.original["lookups"]["components"]
        schema = original_components["schema"]
        
        # Build component lookup by name
        component_map = {}
        for category in original_components:
            if category in ["schema", "unit"]:
                continue
            for item_list in original_components[category]:
                item_dict = dict(zip(schema, item_list))
                name = item_dict['name']
                component_map[name] = {
                    "voltage_v": item_dict['voltage_v'],
                    "avg_amps": item_dict['avg_amps'],
                    "idle_amps": item_dict['idle_amps'],
                    "water_gal_per_cycle": item_dict['water_gal_per_cycle']
                }
        
        # Organize into simplified categories
        return {
            "living": {
                "Audio Amplifier": {
                    "power_w": component_map["Audio Amplifier"]["voltage_v"] * component_map["Audio Amplifier"]["avg_amps"],
                    "idle_w": component_map["Audio Amplifier"]["voltage_v"] * component_map["Audio Amplifier"]["idle_amps"]
                },
                "Television": {
                    "power_w": component_map["Television"]["voltage_v"] * component_map["Television"]["avg_amps"],
                    "idle_w": component_map["Television"]["voltage_v"] * component_map["Television"]["idle_amps"]
                },
                "Lighting": {
                    "power_w": component_map["Lighting"]["voltage_v"] * component_map["Lighting"]["avg_amps"],
                    "idle_w": component_map["Lighting"]["voltage_v"] * component_map["Lighting"]["idle_amps"]
                },
                "Refrigerator": {
                    "power_w": component_map["Refrigerator"]["voltage_v"] * component_map["Refrigerator"]["avg_amps"],
                    "idle_w": component_map["Refrigerator"]["voltage_v"] * component_map["Refrigerator"]["idle_amps"]
                },
                "Smart Glass": {
                    "power_w": component_map["Smart Glass Display"]["voltage_v"] * component_map["Smart Glass Display"]["avg_amps"],
                    "idle_w": component_map["Smart Glass Display"]["voltage_v"] * component_map["Smart Glass Display"]["idle_amps"]
                },
                "Electronics": {
                    "power_w": component_map["Consumer Electronics"]["voltage_v"] * component_map["Consumer Electronics"]["avg_amps"],
                    "idle_w": component_map["Consumer Electronics"]["voltage_v"] * component_map["Consumer Electronics"]["idle_amps"]
                },
                "Party Lighting": {
                    "power_w": component_map["Party Lighting"]["voltage_v"] * component_map["Party Lighting"]["avg_amps"],
                    "idle_w": component_map["Party Lighting"]["voltage_v"] * component_map["Party Lighting"]["idle_amps"]
                },
                "Cameras": {
                    "power_w": component_map["Security Cameras"]["voltage_v"] * component_map["Security Cameras"]["avg_amps"],
                    "idle_w": component_map["Security Cameras"]["voltage_v"] * component_map["Security Cameras"]["idle_amps"]
                }
            },
            "cooking": {
                "Stove": {
                    "power_w": component_map["Stove"]["voltage_v"] * component_map["Stove"]["avg_amps"],
                    "idle_w": component_map["Stove"]["voltage_v"] * component_map["Stove"]["idle_amps"],
                    "burner_multiplier": True
                },
                "Microwave": {
                    "power_w": component_map["Microwave"]["voltage_v"] * component_map["Microwave"]["avg_amps"],
                    "idle_w": component_map["Microwave"]["voltage_v"] * component_map["Microwave"]["idle_amps"]
                },
                "Dishwasher": {
                    "power_w": component_map["Dishwasher"]["voltage_v"] * component_map["Dishwasher"]["avg_amps"],
                    "idle_w": component_map["Dishwasher"]["voltage_v"] * component_map["Dishwasher"]["idle_amps"],
                    "cycle_time_min": 80,
                    "water_gal_per_cycle": component_map["Dishwasher"]["water_gal_per_cycle"]
                },
                "Water Heater": {
                    "power_w": component_map["Tankless Water Heater"]["voltage_v"] * component_map["Tankless Water Heater"]["avg_amps"],
                    "idle_w": component_map["Tankless Water Heater"]["voltage_v"] * component_map["Tankless Water Heater"]["idle_amps"]
                },
                "Range Hood": {
                    "power_w": component_map["Range Hood"]["voltage_v"] * component_map["Range Hood"]["avg_amps"],
                    "idle_w": component_map["Range Hood"]["voltage_v"] * component_map["Range Hood"]["idle_amps"]
                }
            },
            "bathroom": {
                "Electric Shower": {
                    "power_w": component_map["Electric Shower"]["voltage_v"] * component_map["Electric Shower"]["avg_amps"],
                    "idle_w": component_map["Electric Shower"]["voltage_v"] * component_map["Electric Shower"]["idle_amps"]
                },
                "Water Pump": {
                    "power_w": component_map["Water Pump"]["voltage_v"] * component_map["Water Pump"]["avg_amps"],
                    "idle_w": component_map["Water Pump"]["voltage_v"] * component_map["Water Pump"]["idle_amps"]
                },
                "Vent Fan": {
                    "power_w": component_map["Bathroom Vent Fan"]["voltage_v"] * component_map["Bathroom Vent Fan"]["avg_amps"],
                    "idle_w": component_map["Bathroom Vent Fan"]["voltage_v"] * component_map["Bathroom Vent Fan"]["idle_amps"]
                }
            },
            "laundry": {
                "Washer Dryer": {
                    "power_w": component_map["Washer/Dryer Combo"]["voltage_v"] * component_map["Washer/Dryer Combo"]["avg_amps"],
                    "idle_w": component_map["Washer/Dryer Combo"]["voltage_v"] * component_map["Washer/Dryer Combo"]["idle_amps"],
                    "cycle_time_min": 80,
                    "water_gal_per_cycle": component_map["Washer/Dryer Combo"]["water_gal_per_cycle"]
                }
            },
            "operational": {
                "Room Actuators": {
                    "power_w": self._calculate_total_actuation_power(component_map),
                    "idle_w": 0,
                    "cycle_time_sec": 30
                },
                "Dump Valves": {
                    "power_w": component_map["Electric Waste Valves"]["voltage_v"] * component_map["Electric Waste Valves"]["avg_amps"],
                    "idle_w": component_map["Electric Waste Valves"]["voltage_v"] * component_map["Electric Waste Valves"]["idle_amps"],
                    "cycle_time_sec": 6
                }
            }
        }
    
    def _calculate_total_actuation_power(self, component_map):
        """Calculate total power for all actuation components."""
        actuation_components = [
            'Side Room Floor', 'Side Room Wall', 'Front Room',
            'Rear Room', 'Room Support Jacks', 'Gearage'
        ]
        total_power = 0
        for comp_name in actuation_components:
            if comp_name in component_map:
                total_power += component_map[comp_name]["voltage_v"] * component_map[comp_name]["avg_amps"]
        return total_power
    
    def _convert_user_profiles(self):
        """Convert complex nested user profiles to flat daily usage patterns."""
        original_profiles = self.original["lookups"]["user_profiles"]["profiles"]
        
        converted_profiles = {}
        
        for profile_name, profile_data in original_profiles.items():
            converted_profiles[profile_name] = {
                "daily_usage": {
                    "audio_mins": profile_data["time_based"]["mins_per_day"]["living_audio"],
                    "tv_mins": profile_data["time_based"]["mins_per_day"]["living_tv"],
                    "lighting_mins": profile_data["time_based"]["mins_per_day"]["living_lighting"],
                    "smart_glass_hrs": profile_data["time_based"]["hrs_per_day"]["living_smart_glass"],
                    "electronics_hrs": profile_data["time_based"]["hrs_per_day"]["living_electronics"],
                    "party_lighting_hrs": profile_data["time_based"]["hrs_per_day"]["living_party_lighting"],
                    "drinking_water_gal": profile_data["volume_based"]["gal_per_day"]["living_drinking_water"],
                    "cleaning_water_gal": profile_data["volume_based"]["gal_per_day"]["living_cleaning"],
                    "ice_water_gal": profile_data["volume_based"]["gal_per_day"]["living_ice_maker_water"]
                },
                "meal_patterns": {
                    "meals_per_day": profile_data["count_based"]["meals_per_day"]["cooking"],
                    "stove_mins_per_meal": profile_data["time_based"]["mins_per_meal"]["cooking_stove"],
                    "stove_burners_per_meal": profile_data["count_based"]["burners_per_meal"]["cooking_stove"],
                    "microwave_mins_per_meal": profile_data["time_based"]["mins_per_meal"]["cooking_microwave"],
                    "dishwasher_cycles_per_meal": profile_data["count_based"]["cycles_per_meal"]["cooking_dishwasher"],
                    "water_heater_mins_per_meal": profile_data["time_based"]["mins_per_meal"]["cooking_water_heater"],
                    "kitchen_water_gal_per_meal": profile_data["volume_based"]["gal_per_meal"]["cooking_kitchen_faucet"]
                },
                "personal_care": {
                    "toilet_cycles_per_day": profile_data["count_based"]["cycles_per_day_per_person"]["toilet"],
                    "toilet_sink_water_gal_per_cycle": profile_data["volume_based"]["gal_per_cycle"]["toilet_sink_water"],
                    "toilet_flush_water_gal_per_cycle": profile_data["volume_based"]["gal_per_cycle"]["toilet_gravity_flush"],
                    "shower_cycles_per_day": profile_data["count_based"]["cycles_per_day_per_person"]["shower"],
                    "shower_duration_mins": profile_data["time_based"]["mins_per_cycle"]["shower_duration"],
                    "shower_water_gal_per_cycle": profile_data["volume_based"]["gal_per_cycle"]["shower_water"],
                    "laundry_cycles_per_day": profile_data["count_based"]["cycles_per_day_per_person"]["laundry"]
                }
            }
        
        return converted_profiles
    
    def _convert_environmental_systems(self):
        """Convert HVAC and solar data to simplified structure."""
        return {
            "hvac": {
                "description": "HVAC energy consumption and water generation by temperature",
                "energy_consumption_wh_per_day": self.original["lookups"]["hvac_energy_wh_day"],
                "water_generation_gph": self._convert_hvac_water_generation()
            },
            "solar": {
                "description": "Solar generation factors by environmental conditions",
                "system_efficiency": self.original["lookups"]["solar"]["system_loss_factor"],
                "base_insolation_wh_per_m2_per_day": self.original["lookups"]["solar"]["insolation_wh_m2_day"],
                "sunlight_multiplier": self.original["lookups"]["solar"]["sunlight_factor"],
                "tilt_multiplier": self.original["lookups"]["solar"]["tilt_factor"]
            }
        }
    
    def _convert_hvac_water_generation(self):
        """Convert HVAC water generation data to simplified average values."""
        original_hvac = self.original["lookups"]["hvac_water_gen_gph"]
        
        # Average day and night rates for simplicity
        simplified = {}
        for temp in original_hvac["day"]:
            simplified[temp] = {}
            for humidity in original_hvac["day"][temp]:
                day_rate = original_hvac["day"][temp][humidity]
                night_rate = original_hvac["night"][temp][humidity]
                # Average of day and night rates
                simplified[temp][humidity] = (day_rate + night_rate) / 2
        
        return simplified
    
    def _convert_trailer_specs(self):
        """Extract trailer specifications."""
        specs = self.original["trailer_specs"]["specs"]
        return {
            "description": "Physical capacities and limits",
            "battery_capacity_kwh": specs["battery_capacity_kwh"]["value"],
            "solar_capacity_kw": specs["solar_capacity_kw"]["value"],
            "freshwater_capacity_gal": specs["freshwater_capacity_gal"]["value"],
            "greywater_capacity_gal": specs["greywater_capacity_gal"]["value"],
            "blackwater_capacity_gal": specs["blackwater_capacity_gal"]["value"]
        }
    
    def _convert_waste_allocation(self):
        """Create waste allocation mapping from original data."""
        # This is derived from the waste_production lookup in original data
        return {
            "description": "How consumed water becomes waste water",
            "greywater_sources": {
                "shower": 1.0,           # All shower water becomes grey
                "laundry": 0.2,          # 4.12 grey / 20.6 total ≈ 0.2
                "dishwasher": 1.0,       # All dishwasher water becomes grey  
                "cleaning": 1.0,         # All cleaning water becomes grey
                "toilet_sink": 1.0       # All sink water becomes grey
            },
            "blackwater_sources": {
                "toilet_flush": 1.0,     # All flush water becomes black
                "kitchen_sink": 0.75     # Portion of kitchen water becomes black (food scraps)
            }
        }
    
    def save_to_file(self, filename):
        """Save converted data to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.simplified, f, indent=2)
        print(f"Simplified lookup data saved to {filename}")
    
    def print_conversion_summary(self):
        """Print a summary of the conversion."""
        print("=== CONVERSION SUMMARY ===")
        print(f"Original user profiles: {len(self.original['lookups']['user_profiles']['profiles'])}")
        print(f"Converted user profiles: {len(self.simplified['user_profiles'])}")
        print()
        
        # Count original components
        original_comp_count = 0
        for category in self.original["lookups"]["components"]:
            if category not in ["schema", "unit"]:
                original_comp_count += len(self.original["lookups"]["components"][category])
        
        # Count simplified components  
        simplified_comp_count = 0
        for category in self.simplified["components"]:
            simplified_comp_count += len(self.simplified["components"][category])
        
        print(f"Original components: {original_comp_count}")
        print(f"Simplified components: {simplified_comp_count}")
        print()
        print("Converted categories:")
        for category in self.simplified["components"]:
            count = len(self.simplified["components"][category])
            print(f"  {category}: {count} components")


def main():
    """Main conversion function."""

    try:
        # Load original data

        with open('lookup_data.json', 'r') as f:
            original_data = json.load(f)
        output_file = 'simplified_lookup_data.json'
        # Convert
        print("Converting data structure...")
        converter = LookupDataConverter(original_data)
        simplified_data = converter.convert()
        
        # Save
        print(f"Saving simplified data to {output_file}...")
        converter.save_to_file(output_file)
        
        # Print summary
        converter.print_conversion_summary()
        
        print("\n✅ Conversion completed successfully!")
        print(f"You can now use {output_file} with the SimpleResourceCalculator")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find input file '{input_file}'")




if __name__ == "__main__":
    main()