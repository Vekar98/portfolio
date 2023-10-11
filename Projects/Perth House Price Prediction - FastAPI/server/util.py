import json
import pickle
import numpy as np
import warnings
from typing import List

warnings.filterwarnings("ignore", category=UserWarning)

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("loading saved artifacts.....start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[6:]

    global __model
    with open("./artifacts/Perth House Price Prediction.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts.....done")

# Dodaj wywołanie load_saved_artifacts() tutaj
load_saved_artifacts()

def get_estimated_price(location: str, bedrooms: int, bathrooms: int, garage: int, land_area: int, floor_area: int, build_year: int) -> float:
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = garage
    x[3] = land_area
    x[4] = floor_area
    x[5] = build_year
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names() -> List[str]:
    return __locations

def get_data_columns() -> List[str]:
    return __data_columns

if __name__ == '__main__':
    print(get_location_names())
    print(get_estimated_price('alexander heights', 2, 1, 1, 150, 300, 1990))
