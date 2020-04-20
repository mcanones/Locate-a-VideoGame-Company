import requests
import pandas as pd

def getFromGooglePlacesNear(queryParams=dict()): 
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    res = requests.get(url, params=queryParams)
    print(res.status_code, res.url)
    return res.json()