# coding;utf-8

text = "Are you curious about tokenization? Let's see how it works! We need to analyze " \
       "a couple of sentences with punctuations to see it in action."

from nltk.tokenize import sent_tokenize

sent_tokenize_list = sent_tokenize(text)
print(sent_tokenize_list)