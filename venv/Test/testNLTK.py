#coding=utf-8
import re
import nltk
from nltk.corpus import sinica_treebank
# 命名实体的关系是 X in Y
# 命名实体的关系是 X in Y
re_in = re.compile(r'.*\bin\b(?!\b.+ing)')

# ieer 是一个命名实体语料库
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    # 我们抽取组织和位置之间的关系
    for rel in nltk.sem.extract_rels('ORGANIZATION', 'LOCATION', doc, corpus='ieer', pattern=re_in):
        print(rel['subjtext'], 'IN', rel['objtext'])