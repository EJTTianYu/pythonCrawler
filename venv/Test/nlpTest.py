# coding=utf-8
import os
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'D:\stanford-corenlp-full-2018-10-05\stanford-corenlp-full-2018-10-05', lang='zh')

for line in open(r'D:\pythonCrawler\dataProcess\newsPT.xml','r',encoding='utf-8'):
    res=nlp.ner(line)
    person = ["PERSON:"]
    location=['LOCATION:']
    organization=['ORGNIZATION']
    gpe=['GRE']
    for i in range(len(res)):
        if res[i][1]=='PERSON':
            person.append(res[i][0])
    for i in range(len(res)):
        if res[i][1]=='LOCATION':
            location.append(res[i][0])
    for i in range(len(res)):
        if res[i][1]=='ORGANIZATION':
            organization.append(res[i][0])
    for i in range(len(res)):
        if res[i][1]=='GPE':
            gpe.append(res[i][0])
    print(person)
    print(location)
    print(organization)
    print(gpe)


nlp.close()
