# metrics_mexico Documentation

## Welcome

The `metrics_mexico` package provides a comprehensive collection of Mexico-related datasets for data analysis, economic research, and education. It includes extensive data on topics such as **population statistics, salary levels, international rankings, government budgets, trade data, stock market data, airport traffic, earthquakes, and environmental indicators**.

The package contains detailed population records, salary and wage histories, government budget figures, trade and tariff data, stock market data, and environmental indicators, sourced from curated Kaggle datasets focused on Mexico.

### Philosophy

The author's vision is to create **specialized dataset packages** focused on specific themes and topics. Instead of searching through multiple generic data packages to find relevant datasets, users can go directly to a thematic package where all datasets are carefully curated around a particular subject.

In the case of `metrics_mexico`, every dataset is **exclusively focused on Mexico-related data**, making it the go-to resource for researchers, data scientists, economists, policy analysts, and students working in economics, demographics, and related fields.

## Getting Started

### Installation

#### From PyPI (Recommended)

The easiest way to install `metrics_mexico` is directly from PyPI:

```bash
pip install metrics_mexico
```

#### From GitHub (Latest Development Version)

To get the latest development version with the newest features and bug fixes:

```bash
pip install git+https://github.com/karinaf1427/metrics_mexico
```

### Quick Start Tutorial

#### 1. Import the Package

```python
import metrics_mexico as mmx
```

#### 2. List Available Datasets

See all datasets included in the package:

```python
# Get list of all datasets
datasets = mmx.list_datasets()
print(datasets)
```

#### 3. Load a Dataset

Load any dataset as a pandas DataFrame:

```python
# Load mexico_budget
df = mmx.load_dataset('mexico_budget')

# Display first rows
print(df.head())

# Check dataset dimensions
print(f"Shape: {df.shape}")
```

### Basic Concepts

#### Dataset Naming Convention

All dataset names in `metrics_mexico` follow a consistent naming pattern:

- Lowercase with underscores: `mexico_budget`
- Descriptive names that reflect content
- Some include year or period references: `busiest_airports_2022`

#### Some Datasets available at `metrics_mexico`

Every dataset is **exclusively focused on Mexico-related data**:

- **mexico_budget**: Curated dataset of the Mexican government budget.
- **mexico_salaries**: Curated data of salary levels in Mexico.
- **minimum_wage_history**: Historical record of minimum wage values in Mexico.

#### Data Licenses

All datasets maintain their original open-source licenses:

- Most datasets use **CC0: Public Domain** (free for any use)
- The `metrics_mexico` package itself is licensed under **MIT**
