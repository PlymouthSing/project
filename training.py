#!/usr/bin/python3

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords, wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from pickle import dump, load

class customTokenizer:
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    
    def __call__(self, d):
        tokenized_word = [t for t in word_tokenize(d) if t.isalnum()]
        
        stop_words = set(stopwords.words("english"))
        filtered = []
        for w in tokenized_word:
            if w not in stop_words:
                filtered.append(w)
        
        #tag = pos_tag([f])[0][1][0].upper()
        tag_dict = {
                "J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV
        }
        
        return [self.wnl.lemmatize(f,\
                tag_dict.get(pos_tag([f])[0][1][0].upper(), wordnet.NOUN))\
                for f in filtered]


txt = open("password.txt")
line = txt.read().splitlines()
txt.close()
password_rule = [x for x in line if x]
for i, x in enumerate(password_rule):
    if x[len(x) - 1] != ".":
        password_rule[i] += "."

txt = open("wifi.txt")
line = txt.read().splitlines()
txt.close()
wifi_rule = [x for x in line if x]
for i, x in enumerate(wifi_rule):
    if x[len(x) - 1] != ".":
        wifi_rule[i] += "."

vectorizer = TfidfVectorizer(tokenizer = customTokenizer(), norm = None)

vectorizer.fit_transform(password_rule)
dump(vectorizer, open("password.pkl", "wb"))

vectorizer.fit_transform(wifi_rule)
dump(vectorizer, open("wifi.pkl", "wb"))


#password_pkl = load(open("password.pkl", "rb"))
#wifi_pkl = load(open("wifi.pkl", "rb"))

#v = wifi_pkl.transform(wifi_rule)

#print(wifi_rule)
#print()

#print(wifi_pkl.vocabulary_)
#print()

#print(wifi_pkl.get_feature_names())
#print()

#print(v.toarray())
#print()


#for i in v.toarray():
#    for key, value in wifi_pkl.vocabulary_.items():
#        print(key, i[value])

#score = []
#for i, j in enumerate(v.toarray()):
#    s = 0
#    for k, l in enumerate(wifi_pkl.get_feature_names()):
#        if l == "wifi":
#            j[k] *= 10
#        if l == "company":
#            j[k] *= 2
#        s += j[k]
#    score += ((wifi_rule[i], s),)
#score.sort(key = lambda v: v[1], reverse = True)

#print(score[0][1])
#result = None
#for m in score:
#    if m[1] > 20:
#        result += m[0]
#print(result)

#print(wifi_rule)

#txt = open("policy_bank.txt")
#rule = txt.read().splitlines()
#txt.close()
#rule2 = [x for x in rule if x]

#for i, x in enumerate(rule2):
#    if x[len(x) - 1] != ".":
#        rule2[i] += "."
#print(rule2)
print("Done!")
