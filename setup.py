from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="metrics_mexico",
    version="0.1.0",
    author="Karina Fernanda Pérez Domínguez",
    author_email="karinaf1427@gmail.com",
    description=(
        "A curated collection of Mexico-related datasets for data analysis, "
    "economic research, and education. Includes population statistics, "
    "salary levels, international rankings, government budgets, trade data, "
    "stock market data, airport traffic, earthquakes, and environmental indicators "
    "from Kaggle sources."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karinaf1427/metrics_mexico",
    project_urls={
        "Bug Tracker": "https://github.com/karinaf1427/metrics_mexico/issues",
        "Documentation": "https://github.com/karinaf1427/metrics_mexico",
        "Source Code": "https://github.com/karinaf1427/metrics_mexico",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "metrics_mexico": [
            "data/*.csv",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        
        # Topics
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
        
        # Versiones de Python
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        
        # Sistema Operativo
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords=(
        "datasets, mexico, mexican data, population, demographics, salaries, "
    "minimum wage, economics, government budget, trade, tariffs, "
    "stock market, financial data, international rankings, airports, "
    "earthquakes, environmental data, data analysis, data science, "
    "research, education, kaggle"
    ),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    license="MIT",
    zip_safe=False,
)