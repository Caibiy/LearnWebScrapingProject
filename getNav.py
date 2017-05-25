from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors
import datetime
import random
#连接数据库
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='scraping',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
# 保存到数据库
def store(name,url):
    cur.execute("INSERT INTO NAV (name, url) VALUES (%s,%s)",(name,url))
    conn.commit()
html = urlopen("http://www.ivsky.com/")
bsObj = BeautifulSoup(html)
navList = bsObj.find("ul",{"id":"menu"}).find_all('li')

for nav in navList:
   print(nav.a.get_text())
    

