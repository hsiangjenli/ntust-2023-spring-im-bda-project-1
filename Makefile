load_csv_without_admin:
	mongoimport --db bigdata --collection amazon --type csv --file Reviews_withURL.csv --headerline

load_csv_with_admin:
	mongoimport --host localhost --port 27017 --username root --password example --authenticationDatabase admin --db bigdata --collection amazon --type csv --headerline --file Reviews_withURL.csv