#!/usr/bin/env python3
"""
Final Calculator Summary Script
Takes all_rates.json from modular calculator and performs final calculations.
Applies all multipliers and produces trip totals and system status.
"""

import json
import math
import sys
from typing import Dict, Any

class FinalCalculationSummary:
    """Performs final calculations from modular calculator rates and multipliers."""
    
    def __init__(self, all_rates_data, trip_config):
        """
        Initialize with rates data and trip configuration.
        
        Args:
            all_rates_data (dict): Output from modular calculator
            trip_config (dict): Trip parameters (people, duration, hvac_hrs, relocations)
        """
        self.rates = all_rates_data
        self.config = trip_config
        self.results = {}
        
        # Extract trip parameters
        self.num_people = trip_config['num_people']
        self.duration_days = trip_config['duration_days']
        self.hvac_runtime_hrs = trip_config.get('hvac_runtime_hrs', 12)
        self.relocation_count = trip_config.get('relocation_count', 0)
        
        # Constants
        self.WH_TO_KWH = 1000
        
    def calculate_all(self):
        """Perform all final calculations in sequence."""
        print("Performing final calculations...")
        
        # Step 1-5: Calculate consumption and generation
        self._calculate_living_totals()
        self._calculate_cooking_totals() 
        self._calculate_personal_care_totals()
        self._calculate_hvac_totals()
        self._calculate_solar_totals()
        
        # Step 6: Calculate waste production and dump trips
        self._calculate_waste_and_dump_trips()
        
        # Step 7: Calculate operational energy (depends on dump trips)
        self._calculate_operational_totals()
        
        # Final summaries
        self._calculate_trip_totals()
        self._calculate_final_system_status()
        
        return self.results
    
    def _apply_multipliers(self, base_value, multipliers):
        """Apply multiplier factors to a base value."""
        result = base_value
        
        if 'duration_days' in multipliers and multipliers['duration_days']:
            result *= self.duration_days
            
        if 'num_people' in multipliers and multipliers['num_people']:
            result *= self.num_people
            
        if 'runtime_factor' in multipliers and multipliers['runtime_factor']:
            # HVAC runtime factor: actual_hours / 24
            result *= (self.hvac_runtime_hrs / 24)
            
        return result
    
    def _calculate_living_totals(self):
        """Calculate final living activity consumption."""
        living_data = self.rates['step_1_living']
        
        living_totals = {
            'energy_kwh': 0,
            'water_gal': 0,
            'breakdown': {
                'time_based_kwh': 0,
                'always_on_kwh': 0, 
                'cycle_based_kwh': 0,
                'water_sources_gal': 0
            }
        }
        
        # Time-based components
        for comp_name, comp_data in living_data['time_based_components']['components'].items():
            final_wh = self._apply_multipliers(comp_data['wh_per_day_base'], comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            living_totals['energy_kwh'] += final_kwh
            living_totals['breakdown']['time_based_kwh'] += final_kwh
        
        # Always-on components  
        for comp_name, comp_data in living_data['always_on_components']['components'].items():
            final_wh = self._apply_multipliers(comp_data['wh_per_day_base'], comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            living_totals['energy_kwh'] += final_kwh
            living_totals['breakdown']['always_on_kwh'] += final_kwh
        
        # Cycle-based components
        for comp_name, comp_data in living_data['cycle_based_components']['components'].items():
            final_wh = self._apply_multipliers(comp_data['wh_per_day_base'], comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            living_totals['energy_kwh'] += final_kwh
            living_totals['breakdown']['cycle_based_kwh'] += final_kwh
        
        # Water consumption
        for source_name, source_data in living_data['water_consumption']['sources'].items():
            final_gal = self._apply_multipliers(source_data['gal_per_day_base'], source_data['multipliers'])
            living_totals['water_gal'] += final_gal
            living_totals['breakdown']['water_sources_gal'] += final_gal
        
        self.results['living'] = living_totals
    
    def _calculate_cooking_totals(self):
        """Calculate final cooking activity consumption."""
        cooking_data = self.rates['step_2_cooking']
        meals_per_day = cooking_data['meals_per_day']
        
        cooking_totals = {
            'energy_kwh': 0,
            'water_gal': 0,
            'breakdown': {
                'per_meal_kwh': 0,
                'dishwasher_kwh': 0,
                'water_sources_gal': 0
            }
        }
        
        # Per-meal components
        for comp_name, comp_data in cooking_data['per_meal_components']['components'].items():
            # Apply meals_per_day multiplier first, then duration
            base_wh = comp_data['wh_per_meal_base'] * meals_per_day
            final_wh = self._apply_multipliers(base_wh, comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            cooking_totals['energy_kwh'] += final_kwh
            cooking_totals['breakdown']['per_meal_kwh'] += final_kwh
        
        # Dishwasher cycles
        for comp_name, comp_data in cooking_data['dishwasher_cycles']['components'].items():
            cycles_per_day = comp_data['cycles_per_meal'] * meals_per_day
            base_wh = comp_data['wh_per_cycle_base'] * cycles_per_day
            final_wh = self._apply_multipliers(base_wh, comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            cooking_totals['energy_kwh'] += final_kwh
            cooking_totals['breakdown']['dishwasher_kwh'] += final_kwh
        
        # Water consumption
        for source_name, source_data in cooking_data['water_consumption']['sources'].items():
            base_gal = source_data['gal_per_meal_base'] * meals_per_day
            final_gal = self._apply_multipliers(base_gal, source_data['multipliers'])
            cooking_totals['water_gal'] += final_gal
            cooking_totals['breakdown']['water_sources_gal'] += final_gal
        
        self.results['cooking'] = cooking_totals
    
    def _calculate_personal_care_totals(self):
        """Calculate final personal care consumption."""
        personal_data = self.rates['step_3_personal_care']
        
        personal_totals = {
            'energy_kwh': 0,
            'water_gal': 0,
            'breakdown': {
                'toilet_kwh': 0,
                'shower_kwh': 0,
                'laundry_kwh': 0,
                'toilet_water_gal': 0,
                'shower_water_gal': 0,
                'laundry_water_gal': 0
            }
        }
        
        # Toilet cycles
        toilet_cycles_per_day = personal_data['toilet_cycles']['cycles_per_day']
        for comp_name, comp_data in personal_data['toilet_cycles']['components'].items():
            base_wh = comp_data['wh_per_cycle_base'] * toilet_cycles_per_day
            final_wh = self._apply_multipliers(base_wh, comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            personal_totals['energy_kwh'] += final_kwh
            personal_totals['breakdown']['toilet_kwh'] += final_kwh
        
        for water_name, water_data in personal_data['toilet_cycles']['water_consumption'].items():
            base_gal = water_data['gal_per_cycle_base'] * toilet_cycles_per_day
            final_gal = self._apply_multipliers(base_gal, water_data['multipliers'])
            personal_totals['water_gal'] += final_gal
            personal_totals['breakdown']['toilet_water_gal'] += final_gal
        
        # Shower cycles
        shower_cycles_per_day = personal_data['shower_cycles']['cycles_per_day']
        for comp_name, comp_data in personal_data['shower_cycles']['components'].items():
            base_wh = comp_data['wh_per_cycle_base'] * shower_cycles_per_day
            final_wh = self._apply_multipliers(base_wh, comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            personal_totals['energy_kwh'] += final_kwh
            personal_totals['breakdown']['shower_kwh'] += final_kwh
        
        for water_name, water_data in personal_data['shower_cycles']['water_consumption'].items():
            base_gal = water_data['gal_per_cycle_base'] * shower_cycles_per_day
            final_gal = self._apply_multipliers(base_gal, water_data['multipliers'])
            personal_totals['water_gal'] += final_gal
            personal_totals['breakdown']['shower_water_gal'] += final_gal
        
        # Laundry cycles
        laundry_cycles_per_day = personal_data['laundry_cycles']['cycles_per_day']
        for comp_name, comp_data in personal_data['laundry_cycles']['components'].items():
            if comp_name == "Washer/Dryer Combo":
                # Use water from component data
                base_gal = comp_data['water_gal_per_cycle'] * laundry_cycles_per_day
                final_gal = self._apply_multipliers(base_gal, comp_data['multipliers'])
                personal_totals['water_gal'] += final_gal
                personal_totals['breakdown']['laundry_water_gal'] += final_gal
            
            base_wh = comp_data['wh_per_cycle_base'] * laundry_cycles_per_day
            final_wh = self._apply_multipliers(base_wh, comp_data['multipliers'])
            final_kwh = final_wh / self.WH_TO_KWH
            personal_totals['energy_kwh'] += final_kwh
            personal_totals['breakdown']['laundry_kwh'] += final_kwh
        
        self.results['personal_care'] = personal_totals
    
    def _calculate_hvac_totals(self):
        """Calculate final HVAC consumption and water generation."""
        hvac_data = self.rates['step_4_hvac']
        
        # Energy consumption (with runtime factor)
        base_wh_per_day = hvac_data['energy_consumption']['wh_per_day_base']
        runtime_factor = self.hvac_runtime_hrs / 24
        final_energy_wh = base_wh_per_day * runtime_factor * self.duration_days
        
        # Water generation (day/night split)
        day_rate = hvac_data['water_generation']['day_rate_gph']
        night_rate = hvac_data['water_generation']['night_rate_gph']
        
        day_hours = min(self.hvac_runtime_hrs, 12)
        night_hours = max(0, self.hvac_runtime_hrs - 12)
        
        daily_water_generation = (day_rate * day_hours) + (night_rate * night_hours)
        total_water_generation = daily_water_generation * self.duration_days
        
        hvac_totals = {
            'energy_kwh': final_energy_wh / self.WH_TO_KWH,
            'water_generation_gal': total_water_generation,  # Positive value (generated)
            'breakdown': {
                'runtime_factor': runtime_factor,
                'day_hours': day_hours,
                'night_hours': night_hours,
                'daily_generation_gal': daily_water_generation
            }
        }
        
        self.results['hvac'] = hvac_totals
    
    def _calculate_solar_totals(self):
        """Calculate final solar generation."""
        solar_data = self.rates['step_5_solar']
        
        base_kwh_per_day = solar_data['generation']['kwh_per_day_base']
        final_generation_kwh = base_kwh_per_day * self.duration_days
        
        solar_totals = {
            'generation_kwh': final_generation_kwh,  # Positive value (generated)
            'breakdown': {
                'daily_generation_kwh': base_kwh_per_day,
                'environmental_factors': solar_data['generation']['environmental_factors']
            }
        }
        
        self.results['solar'] = solar_totals
    
    def _calculate_waste_and_dump_trips(self):
        """Calculate waste water production and required dump trips."""
        waste_data = self.rates['step_6_waste']
        
        # Get total water consumption from previous steps
        total_fresh_consumed = (
            self.results['living']['water_gal'] +
            self.results['cooking']['water_gal'] + 
            self.results['personal_care']['water_gal']
        )
        
        # Calculate black water production
        # Based on original logic: toilet flush and kitchen sink waste
        toilet_water = self.results['personal_care']['breakdown']['toilet_water_gal']
        kitchen_water = self.results['cooking']['breakdown']['water_sources_gal'] / 2  # Approximate kitchen faucet portion
        
        # Use waste allocation from lookup
        lookup_table = waste_data['allocation_rules']['lookup_table']
        
        # Black water: toilet flush + portion of kitchen water
        toilet_flush_portion = toilet_water * 0.4  # Based on toilet_flush waste ratio
        kitchen_black_portion = kitchen_water * 0.75  # Based on cooking_sink waste ratio  
        total_black_water = toilet_flush_portion + kitchen_black_portion
        
        # Grey water: remaining fresh water consumption
        total_grey_water = total_fresh_consumed - total_black_water
        
        # Calculate required dump trips
        tank_capacities = waste_data['tank_capacities']
        grey_capacity = tank_capacities['greywater_gal']
        black_capacity = tank_capacities['blackwater_gal']
        
        grey_dumps_needed = math.floor(total_grey_water / grey_capacity) if grey_capacity > 0 else 0
        black_dumps_needed = math.floor(total_black_water / black_capacity) if black_capacity > 0 else 0
        total_dump_trips = max(grey_dumps_needed, black_dumps_needed)
        
        waste_totals = {
            'total_fresh_consumed_gal': total_fresh_consumed,
            'grey_water_produced_gal': total_grey_water,
            'black_water_produced_gal': total_black_water,
            'dump_trips_needed': total_dump_trips,
            'breakdown': {
                'grey_dumps_needed': grey_dumps_needed,
                'black_dumps_needed': black_dumps_needed,
                'grey_capacity_gal': grey_capacity,
                'black_capacity_gal': black_capacity
            }
        }
        
        self.results['waste'] = waste_totals
    
    def _calculate_operational_totals(self):
        """Calculate operational energy based on relocations and dump trips."""
        operational_data = self.rates['step_7_operational']
        dump_trips = self.results['waste']['dump_trips_needed']
        
        # Actuation cycles: base 2 + relocations*2 + dump_trips*2
        base_cycles = operational_data['actuation_cycles']['base_cycles']
        total_actuation_cycles = base_cycles + (self.relocation_count * 2) + (dump_trips * 2)
        
        actuation_energy_per_cycle = operational_data['actuation_cycles']['total_energy_per_cycle']
        total_actuation_energy_wh = actuation_energy_per_cycle * total_actuation_cycles
        
        # Dumping energy: per dump trip
        dumping_energy_per_trip = operational_data['dumping_operations']['total_energy_per_trip']
        total_dumping_energy_wh = dumping_energy_per_trip * dump_trips
        
        operational_totals = {
            'energy_kwh': (total_actuation_energy_wh + total_dumping_energy_wh) / self.WH_TO_KWH,
            'breakdown': {
                'actuation_cycles': total_actuation_cycles,
                'actuation_kwh': total_actuation_energy_wh / self.WH_TO_KWH,
                'dumping_trips': dump_trips,
                'dumping_kwh': total_dumping_energy_wh / self.WH_TO_KWH
            }
        }
        
        self.results['operational'] = operational_totals
    
    def _calculate_trip_totals(self):
        """Calculate overall trip totals."""
        total_energy_consumption = (
            self.results['living']['energy_kwh'] +
            self.results['cooking']['energy_kwh'] + 
            self.results['personal_care']['energy_kwh'] +
            self.results['hvac']['energy_kwh'] +
            self.results['operational']['energy_kwh']
        )
        
        total_energy_generation = self.results['solar']['generation_kwh']
        net_energy_consumption = total_energy_consumption - total_energy_generation
        
        total_water_consumption = (
            self.results['living']['water_gal'] +
            self.results['cooking']['water_gal'] +
            self.results['personal_care']['water_gal']
        )
        
        total_water_generation = self.results['hvac']['water_generation_gal']
        net_water_consumption = total_water_consumption - total_water_generation
        
        trip_totals = {
            'energy': {
                'total_consumption_kwh': total_energy_consumption,
                'total_generation_kwh': total_energy_generation,
                'net_consumption_kwh': net_energy_consumption
            },
            'water': {
                'total_consumption_gal': total_water_consumption,
                'total_generation_gal': total_water_generation,
                'net_consumption_gal': net_water_consumption
            },
            'waste': {
                'grey_water_gal': self.results['waste']['grey_water_produced_gal'],
                'black_water_gal': self.results['waste']['black_water_produced_gal'],
                'dump_trips_needed': self.results['waste']['dump_trips_needed']
            }
        }
        
        self.results['trip_totals'] = trip_totals
    
    def _calculate_final_system_status(self):
        """Calculate final battery and tank levels."""
        # Assume system starts at full capacity (these would be parameters in real use)
        initial_battery_kwh = 100  # From system specs
        initial_freshwater_gal = 100
        grey_capacity = 50
        black_capacity = 45
        
        # Final levels
        final_battery_kwh = initial_battery_kwh - self.results['trip_totals']['energy']['net_consumption_kwh']
        final_freshwater_gal = initial_freshwater_gal - self.results['trip_totals']['water']['net_consumption_gal']
        
        # Tank levels after dumps
        grey_produced = self.results['waste']['grey_water_produced_gal']
        black_produced = self.results['waste']['black_water_produced_gal']
        grey_dumps = self.results['waste']['breakdown']['grey_dumps_needed']
        black_dumps = self.results['waste']['breakdown']['black_dumps_needed']
        
        final_grey_level = grey_produced - (grey_dumps * grey_capacity)
        final_black_level = black_produced - (black_dumps * black_capacity)
        
        system_status = {
            'battery': {
                'final_level_kwh': final_battery_kwh,
                'final_percentage': (final_battery_kwh / initial_battery_kwh) * 100,
                'initial_kwh': initial_battery_kwh
            },
            'freshwater': {
                'final_level_gal': final_freshwater_gal,
                'final_percentage': (final_freshwater_gal / initial_freshwater_gal) * 100,
                'initial_gal': initial_freshwater_gal
            },
            'greywater': {
                'final_level_gal': final_grey_level,
                'final_percentage': (final_grey_level / grey_capacity) * 100 if grey_capacity > 0 else 0,
                'capacity_gal': grey_capacity
            },
            'blackwater': {
                'final_level_gal': final_black_level,
                'final_percentage': (final_black_level / black_capacity) * 100 if black_capacity > 0 else 0,
                'capacity_gal': black_capacity
            }
        }
        
        self.results['final_system_status'] = system_status
    
    def print_summary(self):
        """Print a comprehensive summary of all calculations."""
        print("="*60)
        print("TRIP RESOURCE CONSUMPTION SUMMARY")
        print("="*60)
        
        print(f"Trip Configuration:")
        print(f"  People: {self.num_people}")
        print(f"  Duration: {self.duration_days} days") 
        print(f"  HVAC Runtime: {self.hvac_runtime_hrs} hrs/day")
        print(f"  Relocations: {self.relocation_count}")
        print()
        
        # Energy Summary
        print("ENERGY CONSUMPTION:")
        energy_totals = self.results['trip_totals']['energy']
        print(f"  Total Consumption: {energy_totals['total_consumption_kwh']:.2f} kWh")
        print(f"  Solar Generation:  {energy_totals['total_generation_kwh']:.2f} kWh")
        print(f"  Net Consumption:   {energy_totals['net_consumption_kwh']:.2f} kWh")
        print()
        
        print("  Breakdown by Activity:")
        for activity in ['living', 'cooking', 'personal_care', 'hvac', 'operational']:
            if activity in self.results:
                kwh = self.results[activity]['energy_kwh']
                print(f"    {activity.title()}: {kwh:.2f} kWh")
        print()
        
        # Water Summary
        print("WATER CONSUMPTION:")
        water_totals = self.results['trip_totals']['water']
        print(f"  Total Consumption: {water_totals['total_consumption_gal']:.2f} gal")
        print(f"  HVAC Generation:   {water_totals['total_generation_gal']:.2f} gal")
        print(f"  Net Consumption:   {water_totals['net_consumption_gal']:.2f} gal")
        print()
        
        print("  Breakdown by Activity:")
        for activity in ['living', 'cooking', 'personal_care']:
            if activity in self.results:
                gal = self.results[activity]['water_gal']
                print(f"    {activity.title()}: {gal:.2f} gal")
        print()
        
        # Waste Summary
        print("WASTE PRODUCTION:")
        waste = self.results['waste']
        print(f"  Grey Water:  {waste['grey_water_produced_gal']:.2f} gal")
        print(f"  Black Water: {waste['black_water_produced_gal']:.2f} gal")
        print(f"  Dump Trips Needed: {waste['dump_trips_needed']}")
        print()
        
        # Final System Status
        print("FINAL SYSTEM STATUS:")
        status = self.results['final_system_status']
        
        print(f"  Battery:    {status['battery']['final_level_kwh']:.1f} kWh ({status['battery']['final_percentage']:.1f}%)")
        print(f"  Freshwater: {status['freshwater']['final_level_gal']:.1f} gal ({status['freshwater']['final_percentage']:.1f}%)")
        print(f"  Greywater:  {status['greywater']['final_level_gal']:.1f} gal ({status['greywater']['final_percentage']:.1f}%)")
        print(f"  Blackwater: {status['blackwater']['final_level_gal']:.1f} gal ({status['blackwater']['final_percentage']:.1f}%)")
        print()
        
        # Warnings
        self._print_warnings()
    
    def _print_warnings(self):
        """Print any warnings about system status."""
        status = self.results['final_system_status']
        warnings = []
        
        if status['battery']['final_percentage'] < 10:
            warnings.append(f"⚠️  LOW BATTERY: {status['battery']['final_percentage']:.1f}% remaining")
        
        if status['freshwater']['final_percentage'] < 10:
            warnings.append(f"⚠️  LOW FRESHWATER: {status['freshwater']['final_percentage']:.1f}% remaining")
            
        if status['greywater']['final_percentage'] > 90:
            warnings.append(f"⚠️  GREYWATER FULL: {status['greywater']['final_percentage']:.1f}% full")
            
        if status['blackwater']['final_percentage'] > 90:
            warnings.append(f"⚠️  BLACKWATER FULL: {status['blackwater']['final_percentage']:.1f}% full")
        
        if warnings:
            print("WARNINGS:")
            for warning in warnings:
                print(f"  {warning}")
            print()
        else:
            print("✅ All systems within normal operating range")
            print()


def main():
    """Main execution function."""

    rates_file = "all_rates.json"

    try:
        # Load rates data
        print(f"Loading rates data from {rates_file}...")
        with open(rates_file, 'r') as f:
            all_rates_data = json.load(f)
        


            # Default configuration
        trip_config = {
            'num_people': 1,
            'duration_days': 1,
            'hvac_runtime_hrs': 12,
            'relocation_count': 1
        }
        print("Using default trip configuration:")
        print(json.dumps(trip_config, indent=2))
        
        # Perform calculations
        calculator = FinalCalculationSummary(all_rates_data, trip_config)
        results = calculator.calculate_all()
        
        # Print summary
        calculator.print_summary()
        
        # Save detailed results
        output_file = "calculation_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Detailed results saved to {output_file}")
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error during calculation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()