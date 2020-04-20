from pymongo import MongoClient
import pandas as pd

import sys
sys.path.append("../")
from src.easylatlng import easyLatLng_offices
from src.separateLatLngCols import separateLatLngCols

client = MongoClient(f"mongodb://localhost/companies")
db = client.get_database()
data=list(db.companies_mining.find({}))
df = pd.DataFrame(data)

df=df[df['Starbucks_state']=='success']
df=df[df['Preschool_state']=='success']
df=df[df['Disco_state']=='success']
df=df[df['Airport_state']=='success']
df.reset_index(drop=True, inplace=True)

latlng_starbucks = separateLatLngCols(df, col='Starbucks',sub_col='s')
latlng_preschool = separateLatLngCols(df, col='Preschool',sub_col='p')
latlng_disco = separateLatLngCols(df, col='Disco',sub_col='d')
latlng_airport = separateLatLngCols(df, col='Airport',sub_col='a')

df_full = pd.concat ([df,
                     latlng_starbucks,
                     latlng_preschool,
                     latlng_disco,
                     latlng_airport], axis=1)

order_cols = ['name', 'category_code', 'office', 'clean_state', 'latitude', 'longitude', 'Starbucks', 'Starbucks_state', 'lat_s', 'lng_s', 'Preschool', 'Preschool_state', 'lat_p', 'lng_p', 'Disco', 'Disco_state', 'lat_d', 'lng_d', 'Airport', 'Airport_state', 'lat_a', 'lng_a']

df_full=df_full[order_cols]

df_full.to_json("../output/companies_selected.json",orient="records")

#mongoimport --db companies --collection companies_selected --file companies_selected.json --jsonArray
