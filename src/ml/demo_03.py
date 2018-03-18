# coding;utf-8

from sklearn.feature_extraction.text import CountVectorizer

corpus = ['The dog ate a sandwich, the wizard transfigured a sandwich, and I ate a sandwich']
vectorizer = CountVectorizer(stop_words='english')
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)

from sklearn.feature_extraction.text import TfidfVectorizer
corpus_2 = [
    'The dog ate a sandwich and I ate a sandwich',
    'The wizard transfigured a sandwich'
    ]
vectorizer_2 = TfidfVectorizer(stop_words='english')
print(vectorizer_2.fit_transform(corpus_2).todense())
print(vectorizer_2.vocabulary_)