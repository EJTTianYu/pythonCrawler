#coding=utf-8

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'D:\stanford-corenlp-full-2018-10-05\stanford-corenlp-full-2018-10-05', lang='zh')

sentence=''
print(nlp.word_tokenize(sentence))
print(nlp.dependency_parse(sentence))
print(nlp.parse(sentence))

nlp.close()