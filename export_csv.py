import sqlite3,pandas as pd
con=sqlite3.connect("scraped_data.db")
df=pd.read_sql_query("SELECT * FROM headlines",con)
df.to_csv("data/exported_data.csv",index=False)
print("CSV exported")
