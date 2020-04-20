import sys
sys.path.append("../")
from src.getFromGoogle import getFromGooglePlacesNear

def GooglePoint(e):
    pos=getFromGooglePlacesNear(e)
    if pos['status']=='OK':
        return ({
            "type":"Point",
            "coordinates": [pos['results'][0]['geometry']['location']['lng'], pos['results'][0]['geometry']['location']['lat']]
        }, 'success')
    else: 
        return (None, 'Not found')