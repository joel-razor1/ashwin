import sys
import pymongo
import pandas as pd
import numpy as np
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test.closing
test1 = db.find()

fields = {}
for doc in test1:
    for key, val in doc.items():
        try: 
            fields[key] = np.append(fields[key], val)
        except:
            fields[key] = np.array([val])
print(fields)

series_list = []
for key, val in fields.items():
    
    if key != "_id":
        fields[key] = pd.Series(fields[key])
        fields[key].index = fields["_id"]

        print ("\n\n-----------------------------")
        print (key)
        print (fields[key])
        print (fields[key].index)

        put the series with index into a list
        series_list += [fields[key]]

df_series = {}
for num, series in enumerate(series_list):
    same as: df_series["data 1"] = series
    df_series['data ' + str(num)] = series

# create a DataFrame object from Series dictionary
mongo_df = pd.DataFrame(df_series)
# print ("\nmongo_df:", type(mongo_df))

for series in mongo_df.itertuples():
    print (series)
    print ("\n")