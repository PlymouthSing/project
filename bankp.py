#!/usr/bin/python3

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

rule = open("pass.txt")

lst = rule.read().splitlines()

rule.close()

print(lst[0])


tokenized_word=word_tokenize(lst[0])
new = [i for i in tokenized_word if i.isalnum()]
#print(new)

stop_words=set(stopwords.words("english"))
filtered_sent=[]
for w in new:
    if w not in stop_words:
        filtered_sent.append(w)
print(new)
print(filtered_sent)

fdist = FreqDist(new)
fdist2 = FreqDist(filtered_sent)
print(fdist)
print(fdist2)

print("\n")

tfidfvectorizer = TfidfVectorizer(analyzer="word", stop_words="english")
tfidfvectorizer.fit(lst)
tfidf_train = tfidfvectorizer.transform(lst)
tokens = tfidfvectorizer.get_feature_names()

df_tfidfvect = pd.DataFrame(data = tfidf_train.toarray(), columns = tokens)

print(df_tfidfvect)
#print(tfidf_train.todense())
#print(tfidfvectorizer.get_feature_names())

df_tfidfvect.to_csv("test.txt", index = False, sep = "\t")

