"""
Datasets registry for Mexico's Ecomnomic Indicators.
"""

DATASETS = {
    "casa_toluca": {
        "filename": "Casa_toluca.csv",
        "source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/jeanpierrebetancourt/houses-price-web-scraping-mexico", 
        "license": "CC0: Public Domain",
        "description": "Curated Data of House Prices in Mexico"
    },

    "data_2021": {
        "filename": "Data population 2010 - 2021.csv",
        "source": "Kaggle",
        "url": "hhttps://www.kaggle.com/datasets/dextercastillo/data-population-in-mexico-2000-2021", 
        "license": "CC0: Public Domain",
        "description": "Curated Data of Population in Mexico from 2000 to 2021"
    },


}

__all__ = ["DATASETS"]