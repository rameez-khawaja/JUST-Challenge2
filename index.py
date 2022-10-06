from bs4 import BeautifulSoup
import requests
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("DELETE FROM articles;")
# cur.execute("DROP TABLE IF EXISTS articles")
# cur.execute("CREATE TABLE articles(title, text, date, source)")

url = "http://feeds.bbci.co.uk/news/rss.xml"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="xml")
articles = soup.find_all("item")

for i in articles:
    title = i.title.text
    text = i.description.text
    date = i.pubDate.text
    source = i.guid.text
    cur.execute("INSERT INTO articles VALUES (?, ?, ?, ?)", (title, text, date, source))
    con.commit()

for row in cur.execute("SELECT * FROM articles"):
    print(row)
    print("\n")
