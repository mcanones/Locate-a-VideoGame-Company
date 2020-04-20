from src.geocode import geocode

def getOfficeNear(address, maxDist=1000):
    point = geocode(address)
    return {
       "office": {
         "$near": {
           "$geometry": point,
           "$maxDistance": maxDist,
         }
       }
    }