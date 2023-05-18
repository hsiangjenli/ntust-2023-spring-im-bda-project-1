# **NTUST - BDA**

## **Flow Chart**

### CSV to MongoDB
```mermaid
graph LR
A[Read local CSV file] --> B[Convert CSV file to MongoDB format]
B --> C[Save to MongoDB database]
```

### Preprocssing & Analysis

```mermaid
graph TB
MongoDB[(Amazon<br>Reviews)] --> Preprocessing[Preprocessing<br><div align='left'>1. Add new field Timestamp to Datetime<br>2. Add new field reviewers sentiment</div>]
Preprocessing -- update --> MongoDB

MongoDB --> Visualization[Visualization<div align='left'>1. Wordcloud<br>&nbsp;&nbsp;&nbsp;&nbsp;- All reviews<br>&nbsp;&nbsp;&nbsp;&nbsp;- Postive/Negeative reviews</div>]

```

### Helpfulness predict
```mermaid
graph TB
MongoDB[(Amazon<br>Reviews)] --> Filter[Filter<br>]
```






✅ TODO
- [ ] Wordcloud
   - [ ] Different sentiment

```yaml
.
├── 01_load_data_into_mongodb.py
├── 02_query_mongo_create_fields.py
├── Dockerfile # for docker
├── Makefile
├── README.md
├── Reviews_withURL.csv
├── compose-dev.yaml # for docker
└── requirements.txt # for python
```