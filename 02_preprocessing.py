from core.conn import mongodb_connection
import pandas as pd

collection = mongodb_connection(db_host="mongodb://root:example@mongo:27017/")
df = pd.DataFrame(list(collection.find()))

# Timestamp to Datetime -------------------------------------
df['Datetime'] = pd.to_datetime(df['Time'], unit='s')

# Text to Sentiment -----------------------------------------
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
def to_sentiment(x):
    senti_dict = sia.polarity_scores(x)
    return senti_dict

df['Sentiment'] = df['Text'].apply(to_sentiment)

# Update Database -------------------------------------------
for index, row in df.iterrows():
    query = {"_id": row["_id"]}
    new_values = {"$set": {"Datetime": row["Datetime"], "Sentiment": row['Sentiment']}}
    collection.update_many(query, new_values)


