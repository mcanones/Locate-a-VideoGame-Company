import pandas as pd 
from geopy import distance

def calcDist(df,lat_col, lng_col):
    offices   = pd.Series(zip(df['latitude'], df['longitude']))
    starbucks = pd.Series(zip(df[lat_col], df[lng_col]))
    off_star =[]
    for i in range(df.shape[0]):
        off_star.append(distance.distance(offices[i], starbucks[i]).km)
    return pd.Series(off_star)

