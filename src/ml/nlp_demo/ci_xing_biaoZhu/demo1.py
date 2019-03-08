
import nltk

data = "and I love you"
data = "make love with us"
text = nltk.word_tokenize(data)
print(text)
print(nltk.pos_tag(text))

data2 = "They refuse to permit us to obtain the refuse permit"
text2 = nltk.word_tokenize(data2)
print(text2)
print(nltk.pos_tag(text))