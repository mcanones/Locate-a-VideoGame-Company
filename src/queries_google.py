import pandas as pd

def queries_google(df,apiKey):

    loc=df[['latitude','longitude']]
    loc.reset_index(drop=True)

    queryParams_s=[]
    for index, row in loc.iterrows():
        sub_query={
            'keyword':'Starbucks',
            'location':str(row[0])+','+str(row[1]),
            'radius':500,
            'type':'cafe',
            "key":apiKey
        }
        queryParams_s.append(sub_query)

    queryParams_p=[]
    for index, row in loc.iterrows():
        sub_query={
        'keyword':'Pre-school',
        'location':str(row[0])+','+str(row[1]),
        'radius':500,
        "key":apiKey
        }
        queryParams_p.append(sub_query)

    queryParams_d=[]
    for index, row in loc.iterrows():
        sub_query={
        'location':str(row[0])+','+str(row[1]),
        'radius':500,
        'type':'night_club',
        "key":apiKey
        }
        queryParams_d.append(sub_query)

    queryParams_a=[]
    for index, row in loc.iterrows():
        sub_query={
        'location':str(row[0])+','+str(row[1]),
        'radius':20000,
        'type':'airport',
        "key":apiKey
        }
        queryParams_a.append(sub_query)

    return queryParams_s, queryParams_p, queryParams_d, queryParams_a 