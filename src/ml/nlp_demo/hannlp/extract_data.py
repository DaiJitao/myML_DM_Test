#-*- coding=utf8 -*-
import jieba
import re
from src.ml.nlp_demo.hannlp.tokenizer import seg_sentences
#jieba.load_userdict("dict.txt")

#jieba.add_word(row[0].strip(),tag=row[1].strip())
#jieba.suggest_freq(segment)
fp=open("../data/text.txt",'r',encoding='utf8')
fout=open("../out.txt",'w',encoding='utf8')
for line in fp:
    line=line.strip()
    if len(line)>0:
        fout.write(' '.join(seg_sentences(line))+"\n")
fout.close()
if __name__=="__main__":
    pass
    
  
