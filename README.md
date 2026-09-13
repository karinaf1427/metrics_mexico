# metrics_mexico

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

The `metrics_mexico` package provides a curated collection of Mexico-related datasets, designed for data analysis, economic research, and education in Python.

It includes extensive data on **population statistics, salary levels, international rankings, government budgets, trade data, stock market data, airport traffic, earthquakes, and environmental indicators**, sourced from Kaggle.

## Installation
You can install the `metrics_mexico` package from PyPI:
```bash
pip install metrics_mexico
```

## Usage
```python

import metrics_mexico as mmx

# List all available datasets

datasets = mmx.list_datasets()
print(datasets)

# Load a specific dataset

df = mmx.load_dataset('mexico_budget')
print(df.head())

```

## 📊 Some Available Datasets

### Mexico-Related Datasets

| Dataset | Description | 
|---------|-------------|
| `mexico_budget` | Government budget data for Mexico, including allocations and spending across sectors and fiscal years |
| `mexico_salaries` | Salary level data across different sectors, professions, and regions in Mexico |
| `minimum_wage_history` | Historical record of minimum wage values in Mexico over time |

The `metrics_mexico` library is released under the **MIT License**, allowing free use for both commercial and non-commercial purposes.
