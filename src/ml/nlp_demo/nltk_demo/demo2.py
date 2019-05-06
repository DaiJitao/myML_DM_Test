from nltk.corpus import stopwords
from wordcloud import WordCloud
import gensim
from  gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

stop = stopwords.words('english')
w = WordCloud()
w.generate("python and wordcloud")
w.to_file("F:/test.jpg")


def word2vector():
    sentences = [['I', 'love', 'nlp'],
                 ['I', 'will', 'learn', 'nlp', 'in', '2', 'months'],
                 ['nlp', 'is', 'future'],
                 ['nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of', 'industry', 'problems'],
                 ['nlp', 'uses', 'machine', 'learning']]
    skipgram = Word2Vec(sentences=sentences, size=50, window=3, min_count=1, sg=1)
    print(skipgram)
    print(skipgram['nlp'])
    print(len(skipgram['nlp']))
    skipgram.save("./skipgram.bin")


def show_word2vector():
    # word2vector()
    skipgram = Word2Vec.load("skipgram.bin")
    X = skipgram[skipgram.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    pyplot.scatter(result[:, 0], result[:, 1])
    words = list(skipgram.wv.vocab)
    for i, word in enumerate(words):
        pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
    pyplot.show()


# show_word2vector()


def CBOW():
    ''' cbow模型使用方法 '''
    sentences = [['I', 'love', 'nlp'],
                 ['I', 'will', 'learn', 'nlp', 'in', '2', 'months'],
                 ['nlp', 'is', 'future'],
                 ['nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of', 'industry', 'problems'],
                 ['nlp', 'uses', 'machine', 'learning']]
    cbow = Word2Vec(sentences=sentences, size=50, window=3, min_count=1, sg=0)
    print(cbow)
    cbow.save("./cbow.bin")


def show_CBOW():
    cbow = Word2Vec.load("./cbow.bin")
    X = cbow[cbow.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    # create a scatter plot of the projection
    pyplot.scatter(result[:, 0], result[:, 1])
    words = list(cbow.wv.vocab)
    for i, word in enumerate(words):
        pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
    pyplot.show()
