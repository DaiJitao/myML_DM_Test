#coding:utf-8
import numpy as np
from nltk.corpus import brown
from data_mining_demo.python_jiqixuexijingdianshili.chapter6.chunking import splitter

text = "Are you curious about tokenization? Let's see how it works! We need to analyze " \
       "a couple of sentences with punctuations to see it in action."

if __name__=='__main__':
    data = " ".join(brown.words()[:10000])
    num_words = 2000
    chunks = []
    counter = 0
    text_chunks = splitter(data, num_words)
    for text in text_chunks:
        chunk = {'index':counter, 'text':text}
        chunks.append(chunk)
        counter+=1
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(min_df=5, max_df=.95)
    doc_term_matrix = vectorizer.fit_transform([chunk['text'] for chunk in chunks])
    vocab = np.array(vectorizer.get_feature_names())
    print('===>Vocabulary')
    print(vocab)
    print(len(vocab))
    print()
    print("\nDocument term matrix:")
    chunk_names = ['Chunk-0', 'Chunk-1', 'Chunk-2', 'Chunk-3', 'Chunk-4']
    formatted_row = '{:>12}' * (len(chunk_names) + 1)
    print("\n", formatted_row.format('Word', *chunk_names), '\n')
    for word, item in zip(vocab, doc_term_matrix):
        output = [ x for x in item.data]
        print(word)
        print(output)
        print(formatted_row(word, *output))