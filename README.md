# **NTUST-ML**

## 專案架構
```yaml
│  cloud.jpg # 繪製文字雲的底圖
│  ML_refactor.ipynb # 目前進度都在這裡
│  README.md 
│  requirements.txt # 需要下載的套件
│  Reviews_withURL.csv # 這邊要自己放入 csv 檔案，github 上沒有放
│  stopwords.txt # 一些客製化的停斷詞，但是沒有用到
│
└─core
    │  conn.py # 連接 MongoDB
    │  my_wordcloud.py # 可以快速建立文字雲的模組
    └─ __init__.py
```