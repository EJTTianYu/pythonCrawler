import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url=['http://mil.news.sina.com.cn/roll/index.d.html?cid=57918',]
count=0#用于统计总共爬取新闻数量
html = urlopen(url[0]).read().decode('utf-8')
res=re.findall(r'<a href="(.*?)" target="_blank">(.+?)</a>',html)#用于爬取超链接和新闻标题

for i in res:
    try:
        urli=i[0]
        htmli=urlopen(urli).read().decode('utf-8')
        time=re.findall(r'<span class="date">(.*?)</span>',htmli)
        resp=re.findall(r'<p>(.*?)</p>',htmli)
        print(i)
        print(time)
        print(resp)
        count+=1
    except:
        print(count)
        break
#print(html)
#bsObj = BeautifulSoup(spData, 'html.parser')
#bsObj.encode("GBK")
#t1=bsObj.select("ul.linkNews")
#print(t1)
