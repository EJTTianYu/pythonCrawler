import requests
from bs4 import BeautifulSoup#用于解析网页

url=
html = urlopen('https://news.baidu.com/mil')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find_all('a')
for t2 in t1:
    t3 = t2.get('href')
    print(t3)