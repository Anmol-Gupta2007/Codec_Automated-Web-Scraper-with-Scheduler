import sqlite3
con=sqlite3.connect("scraped_data.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS headlines(id INTEGER PRIMARY KEY,title TEXT)")
con.commit();con.close()
print("Database ready")
