from pymongo import MongoClient
import pandas as pd

# Load data
df = pd.read_csv("Reviews_withURL.csv")
df.drop(columns=['Unnamed: 0', 'Id'], inplace=True)

# MongoDB connection
client = MongoClient("mongodb://root:example@mongo:27017/")

# Create database and collection
db = client["bigdata"]
collection = db["amazon"]

# Insert many data
collection.insert_many(df.to_dict('records'))

# Close client
client.close()