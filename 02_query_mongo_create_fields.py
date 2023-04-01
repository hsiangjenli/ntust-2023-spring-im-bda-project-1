from pymongo import MongoClient
import pandas as pd

# MongoDB connection
client = MongoClient("mongodb://root:example@mongo:27017/")

# Create database and collection
db = client["bigdata"]
collection = db["amazon"]

df = pd.DataFrame(
        list(collection.find())
    )

df['Datetime'] = pd.to_datetime(df['Time'], unit='s')

for index, row in df.iterrows():
    query = {"_id": row["_id"]}
    new_values = {"$set": {"Datetime": row["Datetime"]}}
    collection.update_many(query, new_values)