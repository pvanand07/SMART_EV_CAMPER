#!/usr/bin/env python3
"""
Test script to verify that cycle counts are included in base consumption rates.
"""

import json
from v2 import ResourceCalculator

# Load the lookup data
with open('lookup_data.json', 'r') as f:
    lookup_data = json.load(f)

# Create a test configuration
test_config = {
    'user_type': 'Typical',
    'num_people': 2,
    'trip_duration_days': 3,
    'hvac_runtime_hrs': 8,
    'relocation_count': 1,
    'temperature': 'Temperate',
    'humidity': 'Comfortable',
    'sunlight': 'Mid- Cloudy'
}

# Create calculator instance
calculator = ResourceCalculator(lookup_data, **test_config)

# Run the calculation
results = calculator.calculate()

# Check if cycle counts are included in base consumption rates
print("=== Base Consumption Rates with Cycle Counts ===")
for category, data in results['base_consumption_rates'].items():
    print(f"\n{category.upper()}:")
    print(f"  Energy per unit: {data['energy_wh_per_unit']:.2f} Wh/{data['unit_type']}")
    print(f"  Water per unit: {data['water_gal_per_unit']:.2f} gal/{data['unit_type']}")
    print(f"  Cycle count: {data['cycle_count']} {data['unit_type']}")
    print(f"  Unit type: {data['unit_type']}")

print("\n=== Verification ===")
print("✓ Cycle counts are now included in base_consumption_rates")
print("✓ Each base rate entry contains: energy_wh_per_unit, water_gal_per_unit, cycle_count, unit_type")

