import requests,sqlite3
from bs4 import BeautifulSoup
url="https://news.ycombinator.com/"
html=requests.get(url).text
soup=BeautifulSoup(html,"html.parser")
con=sqlite3.connect("scraped_data.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS headlines(id INTEGER PRIMARY KEY,title TEXT)")
for a in soup.select(".titleline a")[:10]:
    cur.execute("INSERT INTO headlines(title) VALUES(?)",(a.text,))
con.commit();con.close()
print("Done")
