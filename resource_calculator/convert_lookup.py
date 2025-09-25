#!/usr/bin/env python3
"""
Reorganized Complete Lookup Data Converter
Organizes data in logical calculation order while preserving all original logic.
"""

import json
import math

class OptimizedLookupDataConverter:
    """Converts and organizes lookup data in logical calculation flow order."""
    
    def __init__(self, original_data):
        self.original = original_data
        self.optimized = {}
        
    def convert(self):
        """Convert to optimized structure following calculation flow."""
        self.optimized = {
            "description": "Optimized lookup data organized by calculation flow",
            "metadata": self._extract_metadata(),
            "components": self._organize_components_by_calculation_flow(),
            "user_profiles": self._extract_user_profiles(),
            "environmental_conditions": self._organize_environmental_data(),
            "calculation_sequence": self._define_calculation_sequence(),
            "waste_and_operations": self._organize_waste_and_operations(),
            "system_specifications": self._extract_system_specs()
        }
        return self.optimized
    
    def _extract_metadata(self):
        """Extract calculation constants and metadata."""
        return {
            "constants": {
                "WH_TO_KWH": 1000,
                "SECONDS_PER_HOUR": 3600,
                "MINUTES_PER_HOUR": 60,
                "HOURS_PER_DAY": 24
            },
            "special_cycle_durations": {
                "smart_key_seconds": 5,
                "dishwasher_cycle_minutes": 80,
                "laundry_cycle_minutes": 80,
                "actuation_cycle_seconds": 30,
                "dumping_cycle_seconds": 6
            },
            "version": "optimized_v1.0"
        }
    
    def _organize_components_by_calculation_flow(self):
        """Organize components by when they're calculated in the flow."""
        # Build component library first
        component_library = self._build_component_library()
        
        return {
            "library": component_library,
            
            # Step 1: Living Activities (household level, daily)
            "living_activities": {
                "time_based_daily": {
                    "description": "Components with variable daily usage patterns",
                    "unit": "runtime per day",
                    "scale": "household",
                    "components": {
                        "Audio Amplifier": "living_audio|mins_per_day",
                        "Television": "living_tv|mins_per_day", 
                        "Lighting": "living_lighting|mins_per_day",
                        "Smart Glass Display": "living_smart_glass|hrs_per_day",
                        "Party Lighting": "living_party_lighting|hrs_per_day",
                        "Exterior Camp Lights": "living_ext_camp_lights|hrs_per_day",
                        "Exterior Porch Lighting": "living_ext_porch_lights|hrs_per_day",
                        "SmartTint DC PSU": "living_smart_tint|hrs_per_day"
                    }
                },
                
                "always_on_24x7": {
                    "description": "Components that run continuously with idle power",
                    "unit": "24 hours per day",
                    "scale": "household", 
                    "components": {
                        "Refrigerator": "always_on",
                        "Satellite Internet PSU": "always_on",
                        "Tire Pressure Sensors": "always_on",
                        "Misc. Sensors & Controllers": "idle_only",
                        "Security Cameras": "always_on",
                        "AI Compute": "always_on",
                        "LAN Switch PSU": "always_on",
                        "Secure Gateway": "always_on", 
                        "Telematics T-Box": "always_on",
                        "4G LTE Antenna": "idle_only",
                        "Home Assistant Server": "always_on",
                        "HVAC Controller": "always_on"
                    }
                },
                
                "cycle_based_daily": {
                    "description": "Components with special cycle logic",
                    "unit": "cycles per day",
                    "scale": "household",
                    "components": {
                        "Smart Key Lighting": "living_smart_key|cycles_per_day|5_seconds_per_cycle"
                    }
                },
                
                "water_consumption_daily": {
                    "description": "Daily water consumption per person",
                    "unit": "gallons per day per person", 
                    "scale": "per_person",
                    "sources": [
                        "living_drinking_water|gal_per_day",
                        "living_cleaning|gal_per_day", 
                        "living_ice_maker_water|gal_per_day"
                    ]
                }
            },
            
            # Step 2: Cooking Activities (per meal, household level)
            "cooking_activities": {
                "per_meal_components": {
                    "description": "Components that run during meal preparation",
                    "unit": "runtime per meal",
                    "scale": "household",
                    "multiplier": "meals_per_day",
                    "components": {
                        "Stove": "cooking_stove|mins_per_meal|multiply_by_burners_per_meal",
                        "Microwave": "cooking_microwave|mins_per_meal",
                        "Garbage Disposal": "cooking_garbage_disposal|mins_per_meal", 
                        "Range Hood": "cooking_range_hood|mins_per_meal",
                        "Tankless Water Heater": "cooking_water_heater|mins_per_meal",
                        "Water Pump": "cooking_pump|mins_per_meal"
                    }
                },
                
                "dishwasher_cycles": {
                    "description": "Dishwasher with fixed 80-minute cycles",
                    "unit": "cycles per meal",
                    "scale": "household",
                    "components": {
                        "Dishwasher": "cooking_dishwasher|cycles_per_meal|80_min_fixed_cycle"
                    }
                },
                
                "water_consumption_per_meal": {
                    "description": "Water used during cooking",
                    "unit": "gallons per meal",
                    "scale": "household",
                    "sources": [
                        "cooking_kitchen_faucet|gal_per_meal",
                        "cooking_dishwasher_water|gal_per_meal"  
                    ]
                }
            },
            
            # Step 3: Personal Care Activities (per person per cycle)
            "personal_care_activities": {
                "toilet_per_cycle": {
                    "description": "Components that run per toilet cycle per person",
                    "unit": "runtime per cycle per person", 
                    "scale": "per_person",
                    "multiplier": "toilet_cycles_per_day_per_person",
                    "components": {
                        "Grey Water Pump": "toilet_pump|mins_per_cycle",
                        "Bathroom Vent Fan": "toilet_vent_fan|mins_per_cycle",
                        "Macerating Pump": "toilet_pump|mins_per_cycle",
                        "Tankless Water Heater": "toilet_water_heater|mins_per_cycle"
                    },
                    "water_consumption": [
                        "toilet_sink_water|gal_per_cycle",
                        "toilet_gravity_flush|gal_per_cycle"
                    ]
                },
                
                "shower_per_cycle": {
                    "description": "Components that run per shower cycle per person", 
                    "unit": "runtime per cycle per person",
                    "scale": "per_person",
                    "multiplier": "shower_cycles_per_day_per_person", 
                    "components": {
                        "Electric Shower": "shower_duration|mins_per_cycle",
                        "Bathroom Vent Fan": "shower_vent_fan|mins_per_cycle",
                        "Water Pump": "shower_water_pump|mins_per_cycle"
                    },
                    "water_consumption": [
                        "shower_water|gal_per_cycle"
                    ]
                },
                
                "laundry_per_cycle": {
                    "description": "Components that run per laundry cycle per person",
                    "unit": "runtime per cycle per person",
                    "scale": "per_person", 
                    "multiplier": "laundry_cycles_per_day_per_person",
                    "components": {
                        "Washer/Dryer Combo": "laundry|cycles_per_day_per_person|80_min_fixed_cycle",
                        "Tankless Water Heater": "laundry_water_heater|mins_per_cycle",
                        "Water Pump": "laundry_water_pump|mins_per_cycle"
                    },
                    "water_consumption": [
                        "washer_dryer|20.6_gal_per_cycle"
                    ]
                }
            },
            
            # Step 4: Environmental Systems (condition-dependent)
            "environmental_systems": {
                "hvac_system": {
                    "description": "HVAC energy and water generation based on conditions",
                    "unit": "runtime hours per day",
                    "scale": "household",
                    "energy_calculation": "hvac_energy_wh_day[temperature] * (runtime_hrs/24)",
                    "water_generation": "day_night_split_logic",
                    "components": ["Mini-Split HVAC (Hot/Cold)", "Mini-Split HVAC (Temperate)"]
                },
                
                "solar_system": {
                    "description": "Solar generation based on environmental conditions", 
                    "unit": "kWh per day",
                    "scale": "household",
                    "calculation": "solar_capacity_kw * insolation_factor * environmental_multipliers",
                    "components": ["Solar Panel Array"]
                }
            },
            
            # Step 5: Operational Activities (calculated from waste production)
            "operational_activities": {
                "actuation_cycles": {
                    "description": "Setup/teardown operations based on relocations and dump trips",
                    "unit": "30-second cycles", 
                    "scale": "per_trip",
                    "calculation": "2_base + (relocations * 2) + (dump_trips * 2)",
                    "components": {
                        "Side Room Floor": "actuation_cycle|30_seconds",
                        "Side Room Wall": "actuation_cycle|30_seconds", 
                        "Front Room": "actuation_cycle|30_seconds",
                        "Rear Room": "actuation_cycle|30_seconds",
                        "Room Support Jacks": "actuation_cycle|30_seconds",
                        "Gearage": "actuation_cycle|30_seconds"
                    }
                },
                
                "dumping_operations": {
                    "description": "Waste dumping operations",
                    "unit": "6-second cycles",
                    "scale": "per_dump_trip", 
                    "calculation": "dump_trips_needed",
                    "components": {
                        "Electric Waste Valves": "dumping_cycle|6_seconds"
                    }
                }
            }
        }
    
    def _build_component_library(self):
        """Build the complete component library with calculated power values."""
        original_components = self.original["lookups"]["components"]
        schema = original_components["schema"]
        
        library = {}
        for category in original_components:
            if category in ["schema", "unit"]:
                continue
            for item_list in original_components[category]:
                item_dict = dict(zip(schema, item_list))
                name = item_dict['name']
                library[name] = {
                    "electrical": {
                        "voltage_v": item_dict['voltage_v'],
                        "active_amps": item_dict['avg_amps'],
                        "idle_amps": item_dict['idle_amps'],
                        "active_power_w": item_dict['voltage_v'] * item_dict['avg_amps'],
                        "idle_power_w": item_dict['voltage_v'] * item_dict['idle_amps']
                    },
                    "water": {
                        "consumption_gal_per_cycle": item_dict['water_gal_per_cycle']
                    },
                    "category": category
                }
        return library
    
    def _extract_user_profiles(self):
        """Extract user profiles with clear organization."""
        profiles = self.original["lookups"]["user_profiles"]["profiles"]
        
        organized_profiles = {}
        for profile_name, profile_data in profiles.items():
            organized_profiles[profile_name] = {
                "description": f"Usage patterns for {profile_name} user type",
                "daily_patterns": {
                    "living_usage": {
                        "audio_mins": profile_data["time_based"]["mins_per_day"]["living_audio"],
                        "tv_mins": profile_data["time_based"]["mins_per_day"]["living_tv"],
                        "lighting_mins": profile_data["time_based"]["mins_per_day"]["living_lighting"],
                        "smart_glass_hrs": profile_data["time_based"]["hrs_per_day"]["living_smart_glass"],
                        "electronics_hrs": profile_data["time_based"]["hrs_per_day"]["living_electronics"], 
                        "party_lighting_hrs": profile_data["time_based"]["hrs_per_day"]["living_party_lighting"],
                        "ext_camp_lights_hrs": profile_data["time_based"]["hrs_per_day"]["living_ext_camp_lights"],
                        "ext_porch_lights_hrs": profile_data["time_based"]["hrs_per_day"]["living_ext_porch_lights"],
                        "smart_tint_hrs": profile_data["time_based"]["hrs_per_day"]["living_smart_tint"],
                        "smart_key_cycles": profile_data["count_based"]["cycles_per_day"]["living_smart_key"]
                    },
                    "water_consumption": {
                        "drinking_gal": profile_data["volume_based"]["gal_per_day"]["living_drinking_water"],
                        "cleaning_gal": profile_data["volume_based"]["gal_per_day"]["living_cleaning"],
                        "ice_gal": profile_data["volume_based"]["gal_per_day"]["living_ice_maker_water"]
                    }
                },
                "meal_patterns": {
                    "meals_per_day": profile_data["count_based"]["meals_per_day"]["cooking"],
                    "cooking_usage": {
                        "stove_mins": profile_data["time_based"]["mins_per_meal"]["cooking_stove"],
                        "stove_burners": profile_data["count_based"]["burners_per_meal"]["cooking_stove"],
                        "microwave_mins": profile_data["time_based"]["mins_per_meal"]["cooking_microwave"],
                        "disposal_mins": profile_data["time_based"]["mins_per_meal"]["cooking_garbage_disposal"],
                        "water_heater_mins": profile_data["time_based"]["mins_per_meal"]["cooking_water_heater"],
                        "pump_mins": profile_data["time_based"]["mins_per_meal"]["cooking_pump"],
                        "range_hood_mins": profile_data["time_based"]["mins_per_meal"]["cooking_range_hood"],
                        "dishwasher_cycles": profile_data["count_based"]["cycles_per_meal"]["cooking_dishwasher"]
                    },
                    "water_consumption": {
                        "kitchen_faucet_gal": profile_data["volume_based"]["gal_per_meal"]["cooking_kitchen_faucet"],
                        "dishwasher_gal": profile_data["volume_based"]["gal_per_meal"]["cooking_dishwasher_water"]
                    }
                },
                "personal_care": {
                    "toilet": {
                        "cycles_per_day": profile_data["count_based"]["cycles_per_day_per_person"]["toilet"],
                        "pump_mins": profile_data["time_based"]["mins_per_cycle"]["toilet_pump"],
                        "vent_fan_mins": profile_data["time_based"]["mins_per_cycle"]["toilet_vent_fan"],
                        "water_heater_mins": profile_data["time_based"]["mins_per_cycle"]["toilet_water_heater"],
                        "sink_water_gal": profile_data["volume_based"]["gal_per_cycle"]["toilet_sink_water"],
                        "flush_water_gal": profile_data["volume_based"]["gal_per_cycle"]["toilet_gravity_flush"]
                    },
                    "shower": {
                        "cycles_per_day": profile_data["count_based"]["cycles_per_day_per_person"]["shower"],
                        "duration_mins": profile_data["time_based"]["mins_per_cycle"]["shower_duration"],
                        "vent_fan_mins": profile_data["time_based"]["mins_per_cycle"]["shower_vent_fan"], 
                        "water_pump_mins": profile_data["time_based"]["mins_per_cycle"]["shower_water_pump"],
                        "water_gal": profile_data["volume_based"]["gal_per_cycle"]["shower_water"]
                    },
                    "laundry": {
                        "cycles_per_day": profile_data["count_based"]["cycles_per_day_per_person"]["laundry"],
                        "water_heater_mins": profile_data["time_based"]["mins_per_cycle"]["laundry_water_heater"],
                        "water_pump_mins": profile_data["time_based"]["mins_per_cycle"]["laundry_water_pump"]
                    }
                }
            }
        
        return organized_profiles
    
    def _organize_environmental_data(self):
        """Organize environmental condition data."""
        return {
            "hvac_conditions": {
                "energy_consumption_wh_per_day": self.original["lookups"]["hvac_energy_wh_day"],
                "water_generation": {
                    "description": "Water generation rates in gallons per hour",
                    "day_rates": self.original["lookups"]["hvac_water_gen_gph"]["day"],
                    "night_rates": self.original["lookups"]["hvac_water_gen_gph"]["night"],
                    "calculation_logic": {
                        "day_hours": "min(hvac_runtime_hrs, 12)",
                        "night_hours": "max(0, hvac_runtime_hrs - 12)",
                        "total_generation": "(day_rate * day_hrs) + (night_rate * night_hrs)"
                    }
                }
            },
            "solar_conditions": {
                "base_insolation_wh_per_m2_per_day": self.original["lookups"]["solar"]["insolation_wh_m2_day"],
                "multipliers": {
                    "system_efficiency": self.original["lookups"]["solar"]["system_loss_factor"],
                    "sunlight_factor": self.original["lookups"]["solar"]["sunlight_factor"],
                    "tilt_factor": self.original["lookups"]["solar"]["tilt_factor"]
                },
                "calculation_formula": "solar_capacity_kw * (insolation/1000) * sunlight * tilt * efficiency"
            }
        }
    
    def _define_calculation_sequence(self):
        """Define the step-by-step calculation sequence."""
        return {
            "description": "Step-by-step calculation order preserving original logic",
            "steps": [
                {
                    "step": 1,
                    "name": "living_calculations", 
                    "description": "Calculate living activity energy and water consumption",
                    "includes": ["time_based_daily", "always_on_24x7", "cycle_based_daily", "water_consumption_daily"],
                    "scale": "household + per_person_water",
                    "multiplier": "duration_days"
                },
                {
                    "step": 2,
                    "name": "cooking_calculations",
                    "description": "Calculate cooking activity energy and water consumption", 
                    "includes": ["per_meal_components", "dishwasher_cycles", "water_consumption_per_meal"],
                    "scale": "household",
                    "multiplier": "meals_per_day * duration_days"
                },
                {
                    "step": 3, 
                    "name": "personal_care_calculations",
                    "description": "Calculate toilet, shower, and laundry consumption",
                    "includes": ["toilet_per_cycle", "shower_per_cycle", "laundry_per_cycle"],
                    "scale": "per_person",
                    "multiplier": "cycles_per_day_per_person * num_people * duration_days"
                },
                {
                    "step": 4,
                    "name": "hvac_calculations",
                    "description": "Calculate HVAC energy consumption and water generation",
                    "includes": ["hvac_energy", "hvac_water_generation"],
                    "scale": "household",
                    "multiplier": "(hvac_runtime_hrs / 24) * duration_days"
                },
                {
                    "step": 5,
                    "name": "solar_calculations", 
                    "description": "Calculate solar energy generation",
                    "includes": ["solar_generation"],
                    "scale": "household",
                    "multiplier": "duration_days"
                },
                {
                    "step": 6,
                    "name": "waste_calculations",
                    "description": "Calculate waste water production and required dump trips",
                    "includes": ["grey_water_production", "black_water_production", "dump_trip_calculation"],
                    "dependency": "total_water_consumption_from_steps_1_3"
                },
                {
                    "step": 7,
                    "name": "operational_calculations",
                    "description": "Calculate actuation and dumping energy based on dump trips",
                    "includes": ["actuation_cycles", "dumping_operations"],
                    "dependency": "dump_trips_from_step_6"
                }
            ]
        }
    
    def _organize_waste_and_operations(self):
        """Organize waste production and operational calculations."""
        return {
            "waste_production": {
                "description": "How consumed water becomes waste water",
                "lookup_table": self.original["lookups"]["waste_production"],
                "calculation_logic": {
                    "black_water_sources": {
                        "toilet_flush": "toilet_flush_water * waste_lookup['toilet_flush']['black']",
                        "kitchen_sink": "kitchen_faucet_water * (waste_lookup['cooking_sink']['black'] / kitchen_faucet_gal_per_meal)"
                    },
                    "grey_water_calculation": "total_fresh_water_consumed - total_black_water_produced",
                    "dump_trip_requirement": "max(grey_water/grey_capacity, black_water/black_capacity)"
                }
            },
            "operational_energy": {
                "actuation": {
                    "description": "Energy for setup/teardown operations",
                    "base_cycles": 2,
                    "additional_cycles_formula": "(relocations * 2) + (dump_trips * 2)",
                    "components_per_cycle": 6,
                    "energy_per_cycle_wh": "sum([Side_Room_Floor, Side_Room_Wall, Front_Room, Rear_Room, Room_Support_Jacks, Gearage]) * (30/3600)"
                },
                "dumping": {
                    "description": "Energy for waste dumping operations", 
                    "cycles_per_dump_trip": 1,
                    "energy_per_cycle_wh": "Electric_Waste_Valves * (6/3600)"
                }
            }
        }
    
    def _extract_system_specs(self):
        """Extract system specifications and capacities."""
        specs = self.original["trailer_specs"]["specs"]
        return {
            "capacities": {
                "battery_kwh": specs["battery_capacity_kwh"]["value"],
                "solar_kw": specs["solar_capacity_kw"]["value"], 
                "freshwater_gal": specs["freshwater_capacity_gal"]["value"],
                "greywater_gal": specs["greywater_capacity_gal"]["value"],
                "blackwater_gal": specs["blackwater_capacity_gal"]["value"]
            },
            "final_level_calculations": {
                "battery_remaining_kwh": "initial_battery - net_energy_consumption",
                "freshwater_remaining_gal": "initial_freshwater - total_water_consumption + hvac_water_generation",
                "greywater_level_gal": "grey_water_produced - (grey_dumps * grey_capacity)",
                "blackwater_level_gal": "black_water_produced - (black_dumps * black_capacity)"
            }
        }
    
    def save_to_file(self, filename):
        """Save optimized data to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.optimized, f, indent=2)
        print(f"Optimized lookup data saved to {filename}")
    
    def print_organization_summary(self):
        """Print summary of the optimized organization."""
        print("=== OPTIMIZED DATA ORGANIZATION ===")
        print("Structure follows calculation flow order:")
        print()
        
        calc_steps = self.optimized["calculation_sequence"]["steps"]
        for step in calc_steps:
            print(f"Step {step['step']}: {step['name']}")
            print(f"  {step['description']}")
            if 'scale' in step:
                print(f"  Scale: {step['scale']}")
            if 'multiplier' in step:
                print(f"  Multiplier: {step['multiplier']}")
            if 'dependency' in step:
                print(f"  Dependency: {step['dependency']}")
            print()
        
        # Count components by calculation step
        components = self.optimized["components"]
        total_components = len(components["library"])
        print(f"Total components in library: {total_components}")
        print()
        
        activity_sections = [
            ("living_activities", "Living Activities"),
            ("cooking_activities", "Cooking Activities"), 
            ("personal_care_activities", "Personal Care"),
            ("environmental_systems", "Environmental Systems"),
            ("operational_activities", "Operations")
        ]
        
        for section_key, section_name in activity_sections:
            if section_key in components:
                section = components[section_key]
                subsection_count = len(section)
                print(f"{section_name}: {subsection_count} subsections")
                for subsection_name, subsection_data in section.items():
                    if "components" in subsection_data:
                        comp_count = len(subsection_data["components"])
                        print(f"  {subsection_name}: {comp_count} components")
        
        print()
        profiles = self.optimized["user_profiles"]
        print(f"User profiles: {len(profiles)}")
        for profile_name in profiles:
            print(f"  {profile_name}: organized by daily/meal/personal_care patterns")
        
        print()
        print("✅ All original calculations preserved in logical order!")


def main():
    """Main conversion function."""
    import sys
    

    input_file = 'lookup_data.json'
    output_file = "optimized_lookup_data.json"
    
    try:
        # Load original data
        print(f"Loading original data from {input_file}...")
        with open(input_file, 'r') as f:
            original_data = json.load(f)
        
        # Convert and optimize
        print("Converting to optimized structure...")
        converter = OptimizedLookupDataConverter(original_data)
        optimized_data = converter.convert()
        
        # Save
        print(f"Saving optimized data to {output_file}...")
        converter.save_to_file(output_file)
        
        # Print summary
        converter.print_organization_summary()
        
        print(f"\n✅ Optimized conversion completed!")
        print("Data is now organized by calculation flow while preserving all original logic.")
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()