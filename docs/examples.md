# metrics_mexico – Examples

This page provides practical examples of using `metrics_mexico` for data analysis and exploration.

## Basic Examples

### Example 1: Loading and Exploring a Dataset

Learn how to load a dataset and perform basic exploration.

```python
import metrics_mexico as mmx

# Load the Mexico Budget dataset
budget = mmx.load_dataset("mexico_budget")

# Display first few rows
print(budget.head())

# Check dataset shape
print(f"\nDataset shape: {budget.shape}")

# View column names
print(f"\nColumns: {list(budget.columns)}")

# Get summary statistics
print("\nSummary statistics:")
print(budget.describe())

# Check for missing values
print("\nMissing values:")
print(budget.isnull().sum())
```

### Example 2: Salary Levels Analysis

Explore salary data across sectors and regions in Mexico.

```python
import metrics_mexico as mmx

# Load Mexico Salaries data
salaries = mmx.load_dataset("mexico_salaries")

# Display first few rows
print(salaries.head())

# Check dataset shape
print(f"\nDataset shape: {salaries.shape}")

# View column names
print(f"\nColumns: {list(salaries.columns)}")

# Filter data for a specific sector
sector_salaries = salaries[salaries['Sector'] == 'Manufactura']
print("\nManufactura - Salaries:")
print(sector_salaries[['Occupation', 'State', 'Salary']].head(10))
```
