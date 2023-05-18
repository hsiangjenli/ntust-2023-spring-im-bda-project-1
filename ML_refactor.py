# %% 載入套件
import pandas as pd
import nltk
import re


# %% 載入資料
df = pd.read_csv(r"Reviews_withURL.csv")
df.drop(['Unnamed: 0'], axis=1, inplace=True)


# %% 新增 helpfulness_ratio 欄位
df = df[df["HelpfulnessNumerator"] < df["HelpfulnessDenominator"]]
df["HelpfulnessRatio"] = df["HelpfulnessNumerator"] / df["HelpfulnessDenominator"]


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
# TODO