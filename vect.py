#!/usr/bin/python3

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from pickle import dump, load

class customTokenizer:
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def __call__(self, doc):
        tokenized_word = [t for t in word_tokenize(doc) if t.isalnum()]
        
        stop_words = set(stopwords.words("english"))
        filtered = []
        for w in tokenized_word:
            if w not in stop_words:
                filtered.append(w)
        
        return [self.wnl.lemmatize(f) for f in filtered]

sentences1 = ["This is the first documents.", "This document is the second document."]
sentences2 = ["The sky is blue document.", "The sun is bright."]

rule = open("bank.txt")

sentence = rule.read().splitlines()

rule.close()

vectorizer = TfidfVectorizer(tokenizer = customTokenizer(), norm = None)

vectorizer.fit_transform(sentence)

dump(vectorizer, open("vectorizer.pkl", "wb"))
m = load(open("vectorizer.pkl", "rb"))

a = m.transform(sentence)

print(m.vocabulary_)
print()

print(m.get_feature_names())
print()

print(a.toarray())

print(sentence)
