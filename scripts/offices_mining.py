from dotenv import load_dotenv
import requests
import os
from pymongo import MongoClient
import pandas as pd

import sys
sys.path.append("../")
from src.insertInfoGoogle import *
from src.queries_google import *

#Load apiKey Google Places
load_dotenv()
apiKey=os.getenv("key")

#Load dataframe companies_processed from MongoDB
client = MongoClient(f"mongodb://localhost/companies")
db = client.get_database()
data=list(db.companies_processed.find({}))
df = pd.DataFrame(data)

#Select games_video companies with existing offices 
df=df[df['category_code']=='games_video']
df=df[df['clean_state']=='success']
df.reset_index(drop=True, inplace=True)

#Obtain Queries 
queryParams_s, queryParams_p, queryParams_d, queryParams_a = queries_google(df,apiKey)

#Call GooglePlaces API
df = insert_info_google(df, queryParams_s, col='Starbucks')
df = insert_info_google(df, queryParams_p, col='Preschool')
df = insert_info_google(df, queryParams_d, col='Disco')
df = insert_info_google(df, queryParams_a, col='Airport')

#Save df
df=df.drop('_id', axis=1)
df.to_json("../output/companies_mining.json",orient="records")

#mongoimport --db companies --collection companies_mining --file companies_mining.json --jsonArray