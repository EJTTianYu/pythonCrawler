import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url='http://mil.news.sina.com.cn/roll/index.d.html?cid=57918'
html = urlopen(url).read().decode('utf-8')
res=re.findall(r'<a href="(.*?)" target="_blank">(.+?)</a>',html)
for i in res:
    print(i)
#print(html)
#bsObj = BeautifulSoup(spData, 'html.parser')
#bsObj.encode("GBK")
#t1=bsObj.select("ul.linkNews")
#print(t1)
