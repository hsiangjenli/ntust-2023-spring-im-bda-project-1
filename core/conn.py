from pymongo import MongoClient


def mongodb_connection(db_host: str="mongodb://localhost:27017"):

    # MongoDB connection
    client = MongoClient("mongodb://root:example@mongo:27017/")

    # Create database and collection
    db = client["bigdata"]
    collection = db["amazon"]

    return collection