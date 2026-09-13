"""
Basic usage example for metrics_mexico
Run:
    python basic_usage.py
"""
import metrics_mexico as mmx
print("=== metrics_mexico: Basic Usage Example ===\n")

# Load a dataset

print("Loading 'mexico_budget' dataset...")
budget = mmx.load_dataset("mexico_budget")

# Show basic information

print("\nFirst 5 rows:")
print(budget.head())
print("\nDataset shape:")
print(budget.shape)
print("\nColumn names:")
print(list(budget.columns))

# Load another dataset

print("\nLoading 'mexico_salaries' dataset...")
salaries = mmx.load_dataset("mexico_salaries")
print("\nFirst 5 rows:")
print(salaries.head())
print("\nDone.")
