import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import xml.dom.minidom

doc=xml.dom.minidom.Document()
root=doc.createElement('AllNews')
doc.appendChild(root)
#用于爬取新浪教育的网页
urls2=['http://roll.edu.sina.com.cn/lm/ky3/kyzx/kaoshi/index.shtml','http://roll.edu.sina.com.cn/lm/ky3/kyzx/kaoshi/index_2.shtml','http://roll.edu.sina.com.cn/lm/ky3/kyzx/kaoshi/index_3.shtml','http://roll.edu.sina.com.cn/lm/ky3/kyzx/kaoshi/index_4.shtml','http://roll.edu.sina.com.cn/lm/ky3/kyzx/kaoshi/index_5.shtml']


def scrap():
    for url in urls2:
        count = 0  # 用于统计总共爬取新闻数量
        html = urlopen(url).read().decode('gbk')
        #print(html)
        res=re.findall(r'<a href="(.*?)" target="_blank">(.+?)</a><span>',html)#用于爬取超链接和新闻标题

        for i in res:
            try:
                urli=i[0]
                htmli=urlopen(urli).read().decode('utf-8')
                time=re.findall(r'<span class="date" data-sudaclick="content_time_p">(.+?)</span>',htmli)
                resp=re.findall(r'<p>(.*?)</p>',htmli)
                #subHtml=re.findall('',htmli)
                nodeNews=doc.createElement('News')
                nodeTopic=doc.createElement('Topic')
                nodeTopic.appendChild(doc.createTextNode('education'))
                nodeLink=doc.createElement('Link')
                nodeLink.appendChild(doc.createTextNode(str(i[0])))
                nodeTitle=doc.createElement('Title')
                nodeTitle.appendChild(doc.createTextNode(str(i[1])))
                nodeTime=doc.createElement('Time')
                nodeTime.appendChild(doc.createTextNode(str(time)))
                nodeText=doc.createElement('Text')
                nodeText.appendChild(doc.createTextNode(str(resp)))
                nodeNews.appendChild(nodeTopic)
                nodeNews.appendChild(nodeLink)
                nodeNews.appendChild(nodeTitle)
                nodeNews.appendChild(nodeTime)
                nodeNews.appendChild(nodeText)
                root.appendChild(nodeNews)
                print(i)
                print(time)
                print(resp)
                count+=1
            except:
                print(count)
                break
scrap()
fp=open('/Users/tianyu/news3.xml','w')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")
#print(html)
#bsObj = BeautifulSoup(spData, 'html.parser')
#bsObj.encode("GBK")
#t1=bsObj.select("ul.linkNews")
#print(t1)
