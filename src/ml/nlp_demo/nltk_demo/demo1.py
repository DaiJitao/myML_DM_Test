import os,sys
import nltk
from nltk.corpus import treebank
from nltk.tree import Tree

sentree = "(IP (NP (NR 张三)) (VP (VV 参加) (AS 了) (NP (NN 会议))))"

tree = Tree.fromstring(sentree)
tree.draw()