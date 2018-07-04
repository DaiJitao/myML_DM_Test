import random
from nltk.corpus import names
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as ntlk_accuracy

def gender_features(word, num_letters = 2):
    return {'feature':word[-num_letters:].lower()}

if __name__=="__main__":
    labeld_names = ([ (name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words("female.txt")])
    print("labled_names:", labeld_names)
    random.seed(7)
    random.shuffle(labeld_names)
    print("\nlabled_names:", labeld_names)

    input_names = ['Leonardo', 'Amy', 'Sam']
