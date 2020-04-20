from src.geocode import geocode

def getOfficeNear(address, maxDist=3500):
    point = geocode(address)
    return {
       "office": {
         "$near": {
           "$geometry": point,
           "$maxDistance": maxDist,
         }
       }
    }