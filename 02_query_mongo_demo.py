from pymongo import MongoClient
import pandas as pd
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://root:example@mongo:27017/")

# Create database and collection
db = client["bigdata"]
collection = db["amazon"]

# Query datetime in range
def query_datetime_in_range(start_year: int, end_year: int) -> pd.DataFrame:
    # gte: greater than and equal to
    # lte: less than and equal to
    start = datetime(year=start_year, month=1, day=1)
    end = datetime(year=end_year, month=12, day=31)
    datetime_range = {"$gte": start, "$lte": end}
    return pd.DataFrame(
        list(collection.find({"Datetime": datetime_range}))
    )

print(
    query_datetime_in_range(start_year=2011, end_year=2012)
)