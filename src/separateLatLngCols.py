import sys
sys.path.append("../")
from src.easylatlng import easyLatLng_filtering

import pandas as pd

def separateLatLngCols(df, col,sub_col):

    latlng_aux=pd.json_normalize(df[f'{col}'])
    latlng_aux=pd.DataFrame(latlng_aux.coordinates)
    latlng_aux=latlng_aux.apply(easyLatLng_filtering, axis=1, result_type="expand")
    latlng_aux.columns=[f'lat_{sub_col}',f'lng_{sub_col}']

    return latlng_aux