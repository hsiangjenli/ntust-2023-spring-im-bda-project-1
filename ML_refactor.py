# %% 載入套件
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer as SIA
import re


# %% 載入資料
df = pd.read_csv(r"Reviews_withURL.csv")
df.drop(['Unnamed: 0'], axis=1, inplace=True)


# %% 新增 helpfulness_ratio 欄位
df = df[df["HelpfulnessNumerator"] < df["HelpfulnessDenominator"]]
df["HelpfulnessRatio"] = df["HelpfulnessNumerator"] / df["HelpfulnessDenominator"]


# %% 新增 Sentiment 欄位
sia = SIA()
df["Sentiment"] = df["Text"].apply(lambda x: 1 if sia.polarity_scores(x)["compound"] > 0 else -1)

def to_helpfulness_class(row):
    if row["HelpfulnessRatio"] > 0.5 and row["Sentiment"] == 1:
        return "HelpfulPos"
    elif row["HelpfulnessRatio"] > 0.5 and row["Sentiment"] == -1:
        return "HelpfulNeg"
    elif row["HelpfulnessRatio"] <= 0.5 and row["Sentiment"] == 1:
        return "UnhelpfulPos"
    elif row["HelpfulnessRatio"] <= 0.5 and row["Sentiment"] == -1:
        return "UnhelpfulNeg"
    

# %% 新增 helpfulness_class 欄位
df['HelpfulnessClass'] = df.apply(to_helpfulness_class, axis=1)


# %% 使用正則表達式移除不必要的字元
def remove_special_characters(text):
    text = re.sub("[^a-zA-Z]|<br>", " ", text)
    return text

df['Text'] = df.Text.apply(remove_special_characters)

# %% 詞性標註
def segment_pos_tagging(text):
    
    text = re.sub("[0-9]|br|<|>|com", "", text, 0, re.MULTILINE)
    words = text.split()
    
    return nltk.tag.pos_tag(words)

df['TextSegment'] = df.Text.apply(segment_pos_tagging)

# %% 只保留正向/負向形容詞
def reconnect(text_segment):

    pos_tags = ['JJ', 'JJR', 'JJS']
    reconnect_adj = []
    
    for i in range(len(text_segment)):
        if text_segment[i][1] in pos_tags:
            
            adj = text_segment[i][0]
            adj = adj.replace(' ', '').replace(',','').replace(' ','').replace('/', '').replace('br', '')

            if len(adj) >= 4:

                if text_segment[i-1][0] == 'not':
                    reconnect_adj.append(f'not_{adj}')
                
                else:
                    reconnect_adj.append(adj)
            
            else:
                pass
    
    return " ".join(text for text in reconnect_adj)

df['TextAdj'] = df.TextSegment.apply(reconnect)

# %% 切分成訓練集與測試集
from sklearn.model_selection import train_test_split as TTS

X = df.TextAdj
y = df.HelpfulnessClass

X_train, X_test, y_train, y_test = TTS(X, y, test_size=0.2, random_state=42)

# %% 計算 TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# %% 訓練模型
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)

# %% 預測
y_pred = rfc.predict(X_test)

# %% 評估模型
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
print("Classification Report: \n", classification_report(y_test, y_pred))