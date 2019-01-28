
import nltk

data = "and I love you"
data = "make love with us"
text = nltk.word_tokenize(data)
print(text)
print(nltk.pos_tag(text))