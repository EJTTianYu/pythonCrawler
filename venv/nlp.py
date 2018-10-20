# coding=utf-8
import os
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'D:\stanford-corenlp-full-2018-10-05\stanford-corenlp-full-2018-10-05', lang='zh')

file=open(r'D:\pythonCrawler\scrapXML\news.xml','r',encoding='utf-8')

for line in open(r'D:\pythonCrawler\scrapXML\test.xml','r',encoding='utf-8'):
    print(nlp.ner(line))

nlp.close()
