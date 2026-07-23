__version__ = "0.1.0"

from .core import load_dataset, list_datasets
from .datasets import DATASETS

__all__ = [
    "load_dataset",
    "list_datasets",
    "DATASETS",
    "__version__",
]