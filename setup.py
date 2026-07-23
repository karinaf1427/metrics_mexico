from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="metrics_mexico",
    version="0.1.0",
    author="karinaf1427",
    author_email="karinaf1427@gmail.com",
    description=(
        "A Curated Dataset of Mexicos Economic Indicators"
        "for data analysis, education, and research"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/karinaf1427/metrics_mexico",
    project_urls={
        "Bug Tracker": "https://github.com/karinaf1427/metrics_mexico",
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
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords=(
        "datasets, mexico, mx, data, statistics, ",
        "economy, salary levels, housing prices",
         "Natural Language :: English",
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