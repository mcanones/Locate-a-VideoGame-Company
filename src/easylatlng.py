import pandas as pd

def easyLatLng_offices(row):
    if row.clean_state=='success':
        of = row.office 
        return {
            "latitude":of["coordinates"][1],
            "longitude":of["coordinates"][0]
        }

def easyLatLng_filtering(row):
        of = row
        return {
            "latitude":of["coordinates"][1],
            "longitude":of["coordinates"][0]
        }

