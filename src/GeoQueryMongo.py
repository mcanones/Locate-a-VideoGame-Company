from src.getOfficeNear import getOfficeNear
from pymongo import MongoClient
import pandas as pd 

def GeoQueryMongo(address):
    try:
        
        query = getOfficeNear(address, maxDist=2000)

        client = MongoClient(f"mongodb://localhost/companies")
        db = client.get_database()
        cur = db.companies_selected.find(query, {"_id":0})
        result = list(cur)
        df = pd.json_normalize(result)
        df=df[['name','category_code','latitude','longitude']]
        df.drop_duplicates(inplace=True)
        #display(df)
        df.to_json(f"./output/query_{address}.json",orient="records")

        return df

    except Exception as err:
        print(err, type(err))