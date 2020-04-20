import pandas as pd

import sys
sys.path.append("../")
from src.googlePoint import GooglePoint

def insert_info_google(df, queryParams, col):

    points=[]
    for e in queryParams:
        points.append(GooglePoint(e))
    aux=pd.Series(points)
    aux_df=pd.DataFrame(aux.tolist(), columns=[f'{col}',f'{col}_state'])
    df_new = pd.concat([df, aux_df], axis=1)

    return df_new