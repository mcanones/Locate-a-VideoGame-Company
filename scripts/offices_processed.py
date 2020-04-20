from pymongo import MongoClient
import pandas as pd

import sys
sys.path.append("../")
from src.officeToGeoPoint import officeToGeoPoint_function
from src.easylatlng import easyLatLng_offices

#Import database from MongoDB 

client = MongoClient(f"mongodb://localhost/companies")
db = client.get_database()
data=list(db.companies.find({},{"offices":1,"name":1,"category_code":1}))
df = pd.DataFrame(data)

#Explode and clean column <offices>

df = df.explode("offices")
cleaned_offices = df.apply(officeToGeoPoint_function, axis=1, result_type="expand")
cleaned_offices.columns=["office","clean_state"]

#Concat original df + cleaned_offices df

company_processed = pd.concat([df,cleaned_offices], axis=1)
company_processed = company_processed[['name','category_code','office','clean_state']]

#Concat columns latitude and longitude to company_processed

df = pd.concat([company_processed, company_processed.apply(easyLatLng_offices, axis=1, result_type="expand")], axis=1)

#Save the resulting df as .json in output 

df.to_json("../output/company_processed.json",orient="records")

#Instruction to import the json to MongoDB from terminal 

#mongoimport --db companies --collection companies_processed --file companies_processed.json --jsonArray
