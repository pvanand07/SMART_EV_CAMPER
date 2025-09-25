#!/usr/bin/env python3
"""
Fixed Modular Resource Calculator with correct lookup paths.
Each function returns detailed daily/cycle values with multipliers for later calculation.
"""

import json
import math

class ModularResourceCalculator:
    """Calculator that returns consumption rates and multipliers for modular calculation."""
    
    def __init__(self, lookup_data):
        """Initialize with optimized lookup data structure."""
        self.data = lookup_data
        self.constants = self.data["metadata"]["constants"]
        self.components = self.data["components"]["library"]
        
    def get_living_consumption_rates(self, user_type):
        """
        Returns living activity consumption rates with multipliers.
        
        Returns:
            dict: Complete living activity rates and multipliers
        """
        profile = self.data["user_profiles"][user_type]
        living_activities = self.data["components"]["living_activities"]
        
        result = {
            "description": "Living activity consumption rates and multipliers",
            "scale": "household_energy + per_person_water",
            
            "time_based_components": {
                "description": "Components with variable daily runtime",
                "unit": "wh_per_day_base",
                "scale": "household",
                "components": {}
            },
            
            "always_on_components": {
                "description": "Components running 24/7", 
                "unit": "wh_per_day_fixed",
                "scale": "household", 
                "components": {}
            },
            
            "cycle_based_components": {
                "description": "Components with cycle-based usage",
                "unit": "wh_per_cycle_base",
                "scale": "household",
                "components": {}
            },
            
            "water_consumption": {
                "description": "Daily water consumption per person",
                "unit": "gal_per_day_base", 
                "scale": "per_person",
                "sources": {}
            }
        }
        
        # Time-based components (variable daily usage)
        time_based = living_activities["time_based_daily"]["components"]
        daily_usage = profile["daily_patterns"]["living_usage"]
        
        for comp_name, usage_info in time_based.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                
                # Parse usage info: "living_audio|mins_per_day"
                parts = usage_info.split("|")
                usage_key = parts[0]
                unit = parts[1] if len(parts) > 1 else "mins_per_day"
                
                # Get runtime from profile based on component
                runtime_value = 0
                if comp_name == "Audio Amplifier":
                    runtime_value = daily_usage["audio_mins"]
                    unit = "mins_per_day"
                elif comp_name == "Television":
                    runtime_value = daily_usage["tv_mins"]
                    unit = "mins_per_day"
                elif comp_name == "Lighting":
                    runtime_value = daily_usage["lighting_mins"]
                    unit = "mins_per_day"
                elif comp_name == "Smart Glass Display":
                    runtime_value = daily_usage["smart_glass_hrs"]
                    unit = "hrs_per_day"
                elif comp_name == "Party Lighting":
                    runtime_value = daily_usage["party_lighting_hrs"]
                    unit = "hrs_per_day"
                elif comp_name == "Exterior Camp Lights":
                    runtime_value = daily_usage["ext_camp_lights_hrs"]
                    unit = "hrs_per_day"
                elif comp_name == "Exterior Porch Lighting":
                    runtime_value = daily_usage["ext_porch_lights_hrs"]
                    unit = "hrs_per_day"
                elif comp_name == "SmartTint DC PSU":
                    runtime_value = daily_usage["smart_tint_hrs"]
                    unit = "hrs_per_day"
                
                # Calculate wh_per_day based on unit
                if unit == "mins_per_day":
                    wh_per_day = comp_data["electrical"]["active_power_w"] * (runtime_value / self.constants["MINUTES_PER_HOUR"])
                elif unit == "hrs_per_day":
                    wh_per_day = comp_data["electrical"]["active_power_w"] * runtime_value
                else:
                    wh_per_day = 0
                
                result["time_based_components"]["components"][comp_name] = {
                    "base_power_w": comp_data["electrical"]["active_power_w"],
                    "runtime_pattern": runtime_value,
                    "runtime_unit": unit,
                    "wh_per_day_base": wh_per_day,
                    "multipliers": {"duration_days": 1, "num_people": 0}
                }
        
        # Always-on components (24/7 operation)
        always_on = living_activities["always_on_24x7"]["components"]
        
        for comp_name, operation_type in always_on.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                
                if operation_type == "always_on":
                    wh_per_day = comp_data["electrical"]["active_power_w"] * self.constants["HOURS_PER_DAY"]
                elif operation_type == "idle_only":
                    wh_per_day = comp_data["electrical"]["idle_power_w"] * self.constants["HOURS_PER_DAY"]
                else:
                    wh_per_day = 0
                
                result["always_on_components"]["components"][comp_name] = {
                    "active_power_w": comp_data["electrical"]["active_power_w"],
                    "idle_power_w": comp_data["electrical"]["idle_power_w"],
                    "operation_type": operation_type,
                    "wh_per_day_base": wh_per_day,
                    "multipliers": {"duration_days": 1, "num_people": 0}
                }
        
        # Cycle-based components (Smart Key Lighting)
        cycle_based = living_activities["cycle_based_daily"]["components"]
        
        for comp_name, cycle_info in cycle_based.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                cycles_per_day = daily_usage["smart_key_cycles"]
                cycle_seconds = self.data["metadata"]["special_cycle_durations"]["smart_key_seconds"]
                
                wh_per_cycle = comp_data["electrical"]["active_power_w"] * (cycle_seconds / self.constants["SECONDS_PER_HOUR"])
                wh_per_day = wh_per_cycle * cycles_per_day
                
                result["cycle_based_components"]["components"][comp_name] = {
                    "power_w": comp_data["electrical"]["active_power_w"],
                    "cycle_duration_seconds": cycle_seconds,
                    "cycles_per_day": cycles_per_day,
                    "wh_per_cycle_base": wh_per_cycle,
                    "wh_per_day_base": wh_per_day,
                    "multipliers": {"duration_days": 1, "num_people": 0}
                }
        
        # Water consumption (per person)
        water_usage = profile["daily_patterns"]["water_consumption"]
        
        result["water_consumption"]["sources"] = {
            "drinking_water": {
                "gal_per_day_base": water_usage["drinking_gal"],
                "multipliers": {"duration_days": 1, "num_people": 1}
            },
            "cleaning_water": {
                "gal_per_day_base": water_usage["cleaning_gal"],
                "multipliers": {"duration_days": 1, "num_people": 1}
            },
            "ice_water": {
                "gal_per_day_base": water_usage["ice_gal"], 
                "multipliers": {"duration_days": 1, "num_people": 1}
            }
        }
        
        return result
    
    def get_cooking_consumption_rates(self, user_type):
        """
        Returns cooking activity consumption rates with multipliers.
        
        Returns:
            dict: Per-meal consumption rates and multipliers
        """
        profile = self.data["user_profiles"][user_type]
        cooking_activities = self.data["components"]["cooking_activities"]
        
        result = {
            "description": "Cooking activity consumption rates and multipliers",
            "scale": "household",
            "meals_per_day": profile["meal_patterns"]["meals_per_day"],
            
            "per_meal_components": {
                "description": "Components that run during meal preparation",
                "unit": "wh_per_meal_base",
                "scale": "household",
                "components": {}
            },
            
            "dishwasher_cycles": {
                "description": "Dishwasher with fixed cycle duration",
                "unit": "wh_per_cycle_base", 
                "scale": "household",
                "components": {}
            },
            
            "water_consumption": {
                "description": "Water used during cooking",
                "unit": "gal_per_meal_base",
                "scale": "household", 
                "sources": {}
            }
        }
        
        # Per-meal components
        per_meal = cooking_activities["per_meal_components"]["components"]
        cooking_usage = profile["meal_patterns"]["cooking_usage"]
        
        for comp_name, usage_pattern in per_meal.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                
                # Get runtime from profile based on component
                runtime_mins = 0
                burner_multiplier = 1
                
                if comp_name == "Stove":
                    runtime_mins = cooking_usage["stove_mins"]
                    burner_multiplier = cooking_usage["stove_burners"]
                elif comp_name == "Microwave":
                    runtime_mins = cooking_usage["microwave_mins"]
                elif comp_name == "Garbage Disposal":
                    runtime_mins = cooking_usage["disposal_mins"]
                elif comp_name == "Range Hood":
                    runtime_mins = cooking_usage["range_hood_mins"]
                elif comp_name == "Tankless Water Heater":
                    runtime_mins = cooking_usage["water_heater_mins"]
                elif comp_name == "Water Pump":
                    runtime_mins = cooking_usage["pump_mins"]
                
                wh_per_meal = comp_data["electrical"]["active_power_w"] * (runtime_mins / self.constants["MINUTES_PER_HOUR"]) * burner_multiplier
                
                component_info = {
                    "power_w": comp_data["electrical"]["active_power_w"],
                    "runtime_mins_per_meal": runtime_mins,
                    "wh_per_meal_base": wh_per_meal,
                    "multipliers": {"meals_per_day": 1, "duration_days": 1, "num_people": 0}
                }
                
                # Add burner multiplier for stove
                if comp_name == "Stove":
                    component_info["burner_multiplier"] = burner_multiplier
                
                result["per_meal_components"]["components"][comp_name] = component_info
        
        # Dishwasher cycles
        if "Dishwasher" in self.components:
            comp_data = self.components["Dishwasher"]
            cycle_time_mins = self.data["metadata"]["special_cycle_durations"]["dishwasher_cycle_minutes"]
            cycles_per_meal = cooking_usage["dishwasher_cycles"]
            
            wh_per_cycle = comp_data["electrical"]["active_power_w"] * (cycle_time_mins / self.constants["MINUTES_PER_HOUR"])
            
            result["dishwasher_cycles"]["components"]["Dishwasher"] = {
                "power_w": comp_data["electrical"]["active_power_w"],
                "cycle_time_minutes": cycle_time_mins,
                "cycles_per_meal": cycles_per_meal,
                "wh_per_cycle_base": wh_per_cycle,
                "water_gal_per_cycle": comp_data["water"]["consumption_gal_per_cycle"],
                "multipliers": {"meals_per_day": 1, "duration_days": 1, "num_people": 0}
            }
        
        # Water consumption
        water_usage = profile["meal_patterns"]["water_consumption"]
        
        result["water_consumption"]["sources"] = {
            "kitchen_faucet": {
                "gal_per_meal_base": water_usage["kitchen_faucet_gal"],
                "multipliers": {"meals_per_day": 1, "duration_days": 1, "num_people": 0}
            },
            "dishwasher_water": {
                "gal_per_meal_base": water_usage["dishwasher_gal"] * cooking_usage["dishwasher_cycles"],
                "multipliers": {"meals_per_day": 1, "duration_days": 1, "num_people": 0}
            }
        }
        
        return result
    
    def get_personal_care_consumption_rates(self, user_type):
        """
        Returns personal care consumption rates with multipliers.
        
        Returns:
            dict: Per-cycle per-person consumption rates
        """
        profile = self.data["user_profiles"][user_type]
        personal_care = self.data["components"]["personal_care_activities"]
        
        result = {
            "description": "Personal care consumption rates and multipliers",
            "scale": "per_person",
            
            "toilet_cycles": {
                "description": "Components per toilet cycle per person",
                "unit": "wh_per_cycle_base",
                "scale": "per_person",
                "cycles_per_day": profile["personal_care"]["toilet"]["cycles_per_day"],
                "components": {},
                "water_consumption": {}
            },
            
            "shower_cycles": {
                "description": "Components per shower cycle per person", 
                "unit": "wh_per_cycle_base",
                "scale": "per_person",
                "cycles_per_day": profile["personal_care"]["shower"]["cycles_per_day"],
                "components": {},
                "water_consumption": {}
            },
            
            "laundry_cycles": {
                "description": "Components per laundry cycle per person",
                "unit": "wh_per_cycle_base",
                "scale": "per_person", 
                "cycles_per_day": profile["personal_care"]["laundry"]["cycles_per_day"],
                "components": {},
                "water_consumption": {}
            }
        }
        
        # Toilet cycles
        toilet_components = personal_care["toilet_per_cycle"]["components"]
        toilet_profile = profile["personal_care"]["toilet"]
        
        for comp_name, usage_pattern in toilet_components.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                
                # Get runtime based on component
                runtime_mins = 0
                if comp_name == "Grey Water Pump" or comp_name == "Macerating Pump":
                    runtime_mins = toilet_profile["pump_mins"]
                elif comp_name == "Bathroom Vent Fan":
                    runtime_mins = toilet_profile["vent_fan_mins"]  
                elif comp_name == "Tankless Water Heater":
                    runtime_mins = toilet_profile["water_heater_mins"]
                
                wh_per_cycle = comp_data["electrical"]["active_power_w"] * (runtime_mins / self.constants["MINUTES_PER_HOUR"])
                
                result["toilet_cycles"]["components"][comp_name] = {
                    "power_w": comp_data["electrical"]["active_power_w"],
                    "runtime_mins_per_cycle": runtime_mins,
                    "wh_per_cycle_base": wh_per_cycle,
                    "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
                }
        
        result["toilet_cycles"]["water_consumption"] = {
            "sink_water": {
                "gal_per_cycle_base": toilet_profile["sink_water_gal"],
                "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
            },
            "flush_water": {
                "gal_per_cycle_base": toilet_profile["flush_water_gal"],
                "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
            }
        }
        
        # Shower cycles 
        shower_components = personal_care["shower_per_cycle"]["components"]
        shower_profile = profile["personal_care"]["shower"]
        
        for comp_name, usage_pattern in shower_components.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                
                # Get runtime based on component
                runtime_mins = 0
                if comp_name == "Electric Shower":
                    runtime_mins = shower_profile["duration_mins"]
                elif comp_name == "Bathroom Vent Fan":
                    runtime_mins = shower_profile["vent_fan_mins"]
                elif comp_name == "Water Pump":
                    runtime_mins = shower_profile["water_pump_mins"]
                
                wh_per_cycle = comp_data["electrical"]["active_power_w"] * (runtime_mins / self.constants["MINUTES_PER_HOUR"])
                
                result["shower_cycles"]["components"][comp_name] = {
                    "power_w": comp_data["electrical"]["active_power_w"],
                    "runtime_mins_per_cycle": runtime_mins,
                    "wh_per_cycle_base": wh_per_cycle,
                    "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
                }
        
        result["shower_cycles"]["water_consumption"] = {
            "shower_water": {
                "gal_per_cycle_base": shower_profile["water_gal"],
                "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
            }
        }
        
        # Laundry cycles
        laundry_components = personal_care["laundry_per_cycle"]["components"]
        laundry_profile = profile["personal_care"]["laundry"]
        
        for comp_name, usage_pattern in laundry_components.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                
                if comp_name == "Washer/Dryer Combo":
                    cycle_time_mins = self.data["metadata"]["special_cycle_durations"]["laundry_cycle_minutes"]
                    wh_per_cycle = comp_data["electrical"]["active_power_w"] * (cycle_time_mins / self.constants["MINUTES_PER_HOUR"])
                    
                    result["laundry_cycles"]["components"][comp_name] = {
                        "power_w": comp_data["electrical"]["active_power_w"],
                        "cycle_time_minutes": cycle_time_mins,
                        "wh_per_cycle_base": wh_per_cycle,
                        "water_gal_per_cycle": comp_data["water"]["consumption_gal_per_cycle"],
                        "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
                    }
                else:
                    # Water heater and pump
                    runtime_mins = 0
                    if comp_name == "Tankless Water Heater":
                        runtime_mins = laundry_profile["water_heater_mins"]
                    elif comp_name == "Water Pump":
                        runtime_mins = laundry_profile["water_pump_mins"]
                    
                    wh_per_cycle = comp_data["electrical"]["active_power_w"] * (runtime_mins / self.constants["MINUTES_PER_HOUR"])
                    
                    result["laundry_cycles"]["components"][comp_name] = {
                        "power_w": comp_data["electrical"]["active_power_w"],
                        "runtime_mins_per_cycle": runtime_mins,
                        "wh_per_cycle_base": wh_per_cycle,
                        "multipliers": {"cycles_per_day": 1, "duration_days": 1, "num_people": 1}
                    }
        
        return result
    
    def get_hvac_consumption_rates(self, temperature, humidity):
        """
        Returns HVAC consumption and water generation rates.
        
        Returns:
            dict: HVAC energy consumption and water generation rates
        """
        hvac_data = self.data["environmental_conditions"]["hvac_conditions"]
        
        result = {
            "description": "HVAC energy consumption and water generation rates",
            "scale": "household",
            "conditions": {"temperature": temperature, "humidity": humidity},
            
            "energy_consumption": {
                "description": "HVAC energy consumption based on temperature",
                "unit": "wh_per_day_base",
                "wh_per_day_base": hvac_data["energy_consumption_wh_per_day"][temperature],
                "multipliers": {"runtime_factor": 1, "duration_days": 1, "num_people": 0},
                "calculation": "base_wh_per_day * (runtime_hrs / 24) * duration_days"
            },
            
            "water_generation": {
                "description": "Water generation from HVAC condensation",
                "unit": "gal_per_hour_rates",
                "day_rate_gph": hvac_data["water_generation"]["day_rates"][temperature][humidity],
                "night_rate_gph": hvac_data["water_generation"]["night_rates"][temperature][humidity],
                "multipliers": {"runtime_factor": 1, "duration_days": 1, "num_people": 0},
                "calculation": hvac_data["water_generation"]["calculation_logic"]
            }
        }
        
        return result
    
    def get_solar_generation_rates(self, temperature, humidity, sunlight):
        """
        Returns solar generation rates with environmental multipliers.
        
        Returns:
            dict: Solar generation rates and environmental factors
        """
        solar_data = self.data["environmental_conditions"]["solar_conditions"]
        specs = self.data["system_specifications"]["capacities"]
        
        # Calculate base generation
        base_insolation = solar_data["base_insolation_wh_per_m2_per_day"][temperature][humidity]
        sunlight_factor = solar_data["multipliers"]["sunlight_factor"][sunlight]
        tilt_factor = solar_data["multipliers"]["tilt_factor"][temperature]
        system_efficiency = solar_data["multipliers"]["system_efficiency"]
        solar_capacity_kw = specs["solar_kw"]
        
        daily_generation_kwh = solar_capacity_kw * (base_insolation / self.constants["WH_TO_KWH"]) * sunlight_factor * tilt_factor * system_efficiency
        
        result = {
            "description": "Solar energy generation rates with environmental factors",
            "scale": "household",
            "conditions": {"temperature": temperature, "humidity": humidity, "sunlight": sunlight},
            
            "generation": {
                "description": "Daily solar energy generation",
                "unit": "kwh_per_day_base",
                "solar_capacity_kw": solar_capacity_kw,
                "base_insolation_wh_per_m2": base_insolation,
                "environmental_factors": {
                    "sunlight_factor": sunlight_factor,
                    "tilt_factor": tilt_factor,
                    "system_efficiency": system_efficiency
                },
                "kwh_per_day_base": daily_generation_kwh,
                "multipliers": {"duration_days": 1, "num_people": 0},
                "calculation": solar_data["calculation_formula"]
            }
        }
        
        return result
    
    def get_waste_production_rates(self):
        """
        Returns waste water production rates and dump trip calculation logic.
        
        Returns:
            dict: Waste production allocation and dump trip logic
        """
        waste_data = self.data["waste_and_operations"]["waste_production"]
        specs = self.data["system_specifications"]["capacities"]
        
        result = {
            "description": "Waste water production rates and dump trip calculation",
            "scale": "calculated_from_water_consumption",
            
            "allocation_rules": {
                "description": "How consumed water becomes waste water",
                "lookup_table": waste_data["lookup_table"],
                "black_water_sources": waste_data["calculation_logic"]["black_water_sources"],
                "grey_water_calculation": waste_data["calculation_logic"]["grey_water_calculation"]
            },
            
            "tank_capacities": {
                "greywater_gal": specs["greywater_gal"],
                "blackwater_gal": specs["blackwater_gal"]
            },
            
            "dump_trip_logic": {
                "description": "Calculate required dump trips from waste production",
                "formula": waste_data["calculation_logic"]["dump_trip_requirement"],
                "calculation": "max(grey_water_produced / grey_capacity, black_water_produced / black_capacity)"
            }
        }
        
        return result
    
    def get_operational_consumption_rates(self):
        """
        Returns operational energy consumption rates (actuation and dumping).
        
        Returns:
            dict: Actuation and dumping energy consumption rates
        """
        operational_data = self.data["waste_and_operations"]["operational_energy"]
        actuation_components = self.data["components"]["operational_activities"]["actuation_cycles"]["components"]
        dumping_components = self.data["components"]["operational_activities"]["dumping_operations"]["components"]
        
        result = {
            "description": "Operational energy consumption rates", 
            "scale": "per_cycle_and_per_trip",
            "dependency": "calculated_from_relocations_and_dump_trips",
            
            "actuation_cycles": {
                "description": "Energy for setup/teardown operations",
                "unit": "wh_per_cycle_base",
                "base_cycles": operational_data["actuation"]["base_cycles"],
                "additional_cycles_formula": operational_data["actuation"]["additional_cycles_formula"],
                "cycle_duration_seconds": self.data["metadata"]["special_cycle_durations"]["actuation_cycle_seconds"],
                "components": {},
                "total_energy_per_cycle": 0
            },
            
            "dumping_operations": {
                "description": "Energy for waste dumping operations",
                "unit": "wh_per_trip_base", 
                "cycle_duration_seconds": self.data["metadata"]["special_cycle_durations"]["dumping_cycle_seconds"],
                "components": {},
                "total_energy_per_trip": 0
            }
        }
        
        # Calculate actuation energy per cycle
        total_actuation_energy = 0
        for comp_name, cycle_info in actuation_components.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                cycle_time_seconds = self.data["metadata"]["special_cycle_durations"]["actuation_cycle_seconds"]
                wh_per_cycle = comp_data["electrical"]["active_power_w"] * (cycle_time_seconds / self.constants["SECONDS_PER_HOUR"])
                total_actuation_energy += wh_per_cycle
                
                result["actuation_cycles"]["components"][comp_name] = {
                    "power_w": comp_data["electrical"]["active_power_w"],
                    "cycle_time_seconds": cycle_time_seconds,
                    "wh_per_cycle_base": wh_per_cycle
                }
        
        result["actuation_cycles"]["total_energy_per_cycle"] = total_actuation_energy
        result["actuation_cycles"]["multipliers"] = {"total_cycles": 1, "num_people": 0}
        
        # Calculate dumping energy per trip
        total_dumping_energy = 0
        for comp_name, cycle_info in dumping_components.items():
            if comp_name in self.components:
                comp_data = self.components[comp_name]
                cycle_time_seconds = self.data["metadata"]["special_cycle_durations"]["dumping_cycle_seconds"]
                wh_per_trip = comp_data["electrical"]["active_power_w"] * (cycle_time_seconds / self.constants["SECONDS_PER_HOUR"])
                total_dumping_energy += wh_per_trip
                
                result["dumping_operations"]["components"][comp_name] = {
                    "power_w": comp_data["electrical"]["active_power_w"],
                    "cycle_time_seconds": cycle_time_seconds,
                    "wh_per_trip_base": wh_per_trip
                }
        
        result["dumping_operations"]["total_energy_per_trip"] = total_dumping_energy
        result["dumping_operations"]["multipliers"] = {"dump_trips": 1, "num_people": 0}
        
        return result
    
    def get_all_consumption_rates(self, user_type, temperature, humidity, sunlight):
        """
        Returns all consumption rates and multipliers in one call.
        
        Returns:
            dict: Complete consumption rates for all calculation steps
        """
        return {
            "description": "Complete consumption rates and multipliers for all activities",
            "calculation_sequence": self.data["calculation_sequence"],
            
            "step_1_living": self.get_living_consumption_rates(user_type),
            "step_2_cooking": self.get_cooking_consumption_rates(user_type), 
            "step_3_personal_care": self.get_personal_care_consumption_rates(user_type),
            "step_4_hvac": self.get_hvac_consumption_rates(temperature, humidity),
            "step_5_solar": self.get_solar_generation_rates(temperature, humidity, sunlight),
            "step_6_waste": self.get_waste_production_rates(),
            "step_7_operational": self.get_operational_consumption_rates()
        }


# Example usage and testing
def example_usage():
    """Demonstrate how to use the modular calculator."""
    # Load the optimized lookup data
    try:
        with open('optimized_lookup_data.json', 'r') as f:
            lookup_data = json.load(f)
    except FileNotFoundError:
        print("Error: optimized_lookup_data.json not found. Run the converter first.")
        return
    
    calc = ModularResourceCalculator(lookup_data)
    
    print("=== MODULAR CALCULATOR DEMO ===")
    
    # Test each function
    print("\n1. Living consumption rates...")
    living_rates = calc.get_living_consumption_rates('Typical')
    print(f"Time-based components: {len(living_rates['time_based_components']['components'])}")
    print(f"Always-on components: {len(living_rates['always_on_components']['components'])}")
    print(f"Water sources: {len(living_rates['water_consumption']['sources'])}")
    
    print("\n2. Cooking consumption rates...")
    cooking_rates = calc.get_cooking_consumption_rates('Typical')
    print(f"Per-meal components: {len(cooking_rates['per_meal_components']['components'])}")
    print(f"Dishwasher cycles: {len(cooking_rates['dishwasher_cycles']['components'])}")
    
    print("\n3. Personal care rates...")
    personal_rates = calc.get_personal_care_consumption_rates('Typical')
    print(f"Toilet components: {len(personal_rates['toilet_cycles']['components'])}")
    print(f"Shower components: {len(personal_rates['shower_cycles']['components'])}")
    print(f"Laundry components: {len(personal_rates['laundry_cycles']['components'])}")
    
    print("\n4. HVAC rates...")
    hvac_rates = calc.get_hvac_consumption_rates('Hot', 'Comfortable')
    print(f"Energy base rate: {hvac_rates['energy_consumption']['wh_per_day_base']} Wh/day")
    
    print("\n5. Solar generation...")
    solar_rates = calc.get_solar_generation_rates('Hot', 'Comfortable', 'Hi- Sunny')
    print(f"Generation base rate: {solar_rates['generation']['kwh_per_day_base']:.2f} kWh/day")
    
    print("\n6. Waste production...")
    waste_rates = calc.get_waste_production_rates()
    print(f"Tank capacities: {waste_rates['tank_capacities']}")
    
    print("\n7. Operational rates...")
    operational_rates = calc.get_operational_consumption_rates()
    print(f"Actuation energy per cycle: {operational_rates['actuation_cycles']['total_energy_per_cycle']:.2f} Wh")
    print(f"Dumping energy per trip: {operational_rates['dumping_operations']['total_energy_per_trip']:.2f} Wh")
    
    print("\n✅ All lookup keys working correctly!")
    
    # Example of getting all rates at once
    print("\n=== ALL RATES SUMMARY ===")
    all_rates = calc.get_all_consumption_rates('Typical', 'Hot', 'Comfortable', 'Hi- Sunny')
    
    for step_key, step_data in all_rates.items():
        if step_key.startswith("step_"):
            print(f"{step_key}: {step_data.get('description', 'No description')}")
    with open('all_rates.json', 'w') as f:
        json.dump(all_rates, f, indent=4)

if __name__ == "__main__":
    example_usage()