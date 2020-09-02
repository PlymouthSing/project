#!/usr/bin/python3

import cgi
import cgitb
import datetime
import hashlib
import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords, wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from pickle import dump, load
from bson.objectid import ObjectId

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

class Block:
    def __init__(self, index, data, timestamp, p_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.p_hash = p_hash
        self.hash = self.hashing()
    
    def hashing(self):
        h = hashlib.sha256()
        h.update(str(self.index).encode("UTF-8"))
        h.update(str(self.data).encode("UTF-8"))
        h.update(str(self.timestamp).encode("UTF-8"))
        h.update(str(self.p_hash).encode("UTF-8"))
        return h.hexdigest()

class Chain:
    def __init__(self):
        self.blocks = [self.initial_block()]
    
    def chain_size(self):
        return len(self.blocks) - 1
    
    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks),
            data,
            datetime.datetime.utcnow(),
            self.blocks[len(self.blocks) - 1].hash))
    
    def initial_block(self):
        return Block(0, "Blockchain starts here!",
            datetime.datetime.utcnow(), "Hash Code!")

class vChain(Chain):
    def __init__(self, ini_timestamp):
        self.blocks = [self.initial_block(ini_timestamp)]
    
    def add_block(self, data, timestamp):
        self.blocks.append(Block(len(self.blocks),
            data,
            timestamp,
            self.blocks[len(self.blocks) - 1].hash))
    
    def initial_block(self, ini_timestamp):
        return Block(0, "Blockchain starts here!",
            ini_timestamp, "Hash Code!")

cgitb.enable()
form = cgi.FieldStorage()

companyname = None
businesstype = None
organizationsize = None
numberofworkstations = None
numberofservers = None
editor = None
typeofpolicy = None
result = None
gen = None
hashcode = None
find = None
filled = 0
count = 0

if form.getvalue("companyname"):
    companyname = form.getvalue("companyname")

if form.getvalue("businesstype"):
    businesstype = form.getvalue("businesstype")

if form.getvalue("organizationsize"):
    organizationsize = form.getvalue("organizationsize")

if form.getvalue("numberofworkstations"):
    numberofworkstations = form.getvalue("numberofworkstations")

if form.getvalue("numberofservers"):
    numberofservers = form.getvalue("numberofservers")

if form.getvalue("editor"):
    editor = form.getvalue("editor")

if form.getvalue("typeofpolicy"):
    typeofpolicy = form.getvalue("typeofpolicy")

if form.getvalue("gen"):
    gen = form.getvalue("gen")

if form.getvalue("hashcode"):
    hashcode = form.getvalue("hashcode")

if form.getvalue("find"):
    find = form.getvalue("find")

if companyname\
        and businesstype\
        and organizationsize\
        and numberofworkstations\
        and numberofservers\
        and editor\
        and typeofpolicy:
    filled = 1

if gen == "Generate" and filled == 1:
    result = ""
    txt = open("policy_bank.txt")
    line = txt.read().splitlines()
    txt.close()
    rule = [x for x in line if x]
    for i, x in enumerate(rule):
        if x[len(x) - 1] != ".":
            rule[i] += "."
    
    if typeofpolicy == "WiFi":
        pkl = load(open("wifi.pkl", "rb"))
        vectorize = pkl.transform(rule)
        
        score = []
        for i, j in enumerate(vectorize.toarray()):
            s = 0
            for k, l in enumerate(pkl.get_feature_names()):
                if l == "wifi" and j[k]:
                    j[k] += 100
                if businesstype == "Education":
                    if l == "School" and j[k]:
                        j[k] += 20
                    if l == "student" and j[k]:
                        j[k] += 20
                    if l == "company" and j[k]:
                        j[k] -= 20
                if businesstype == "IT Services":
                    if l == "School" and j[k]:
                        j[k] -= 20
                    if l == "student" and j[k]:
                        j[k] -= 20
                    if l == "company" and j[k]:
                        j[k] += 20
                s += j[k]
            score += ((rule[i], s),)
        score.sort(key = lambda v: v[1], reverse = True)
        
        for m in score:
            if m[1] > 100:
                result += m[0]
    elif typeofpolicy == "Password":
        pkl = load(open("password.pkl", "rb"))
        vectorize = pkl.transform(rule)
        
        score = []
        for i, j in enumerate(vectorize.toarray()):
            s = 0
            for k, l in enumerate(pkl.get_feature_names()):
                if l == "password" and j[k]:
                    j[k] += 100
                if businesstype == "Education":
                    if l == "School" and j[k]:
                        j[k] += 20
                    if l == "student" and j[k]:
                        j[k] += 20
                    if l == "company" and j[k]:
                        j[k] -= 20
                if businesstype == "IT Services":
                    if l == "School" and j[k]:
                        j[k] -= 20
                    if l == "student" and j[k]:
                        j[k] -= 20
                    if l == "company" and j[k]:
                        j[k] += 20
                s += j[k]
            score += ((rule[i], s),)
        score.sort(key = lambda v: v[1], reverse = True)
        
        for m in score:
            if m[1] > 100:
                result += m[0]
    
    document = Chain()
    document.add_block(companyname)
    document.add_block(businesstype)
    document.add_block(organizationsize)
    document.add_block(numberofworkstations)
    document.add_block(numberofservers)
    document.add_block(editor)
    document.add_block(typeofpolicy)
    document.add_block(result)
    document.add_block("Blockchain ends here!")
    
    hashcode = document.blocks[document.chain_size()].p_hash
    
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    database = client["database"]
    collection = database["collection"]
    
    for i in range(document.chain_size() + 1):
        info = {
            "index": str(document.blocks[i].index),
            "data": str(document.blocks[i].data),
            "timestamp": str(document.blocks[i].timestamp),
            "p_hash": str(document.blocks[i].p_hash)
            }
        collection.insert_one(info)
elif find == "Find" and hashcode != None:
    result = ""
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    database = client["database"]
    collection = database["collection"]
    
    query = {"p_hash": hashcode}
    target = collection.find_one(query)
    
    h = int(str(target["_id"]), 16) - 9
    query = {"_id": ObjectId(format(h, "x"))}
    target = collection.find_one(query)
    
    if target:
        vdoc = vChain(target["timestamp"])
    
    while target and vdoc.blocks[count].p_hash == target["p_hash"]:
        h += 1
        query = {"_id": ObjectId(format(h, "x"))}
        target = collection.find_one(query)
        if target:
            vdoc.add_block(target["data"], target["timestamp"])
            count += 1
    
    query = {"p_hash": hashcode}
    target = collection.find_one(query)
    if count == 9:
        companyname = vdoc.blocks[1].data
        businesstype = vdoc.blocks[2].data
        organizationsize = vdoc.blocks[3].data
        numberofworkstations = vdoc.blocks[4].data
        numberofservers = vdoc.blocks[5].data
        editor = vdoc.blocks[6].data
        typeofpolicy = vdoc.blocks[7].data
        result = vdoc.blocks[8].data
        hashcode = vdoc.blocks[9].p_hash



print("Content-type:text/html\r\n\r\n")

if gen == "Generate" and filled == 1:
    print(score)
elif find == "Find" and hashcode != None:
    print(count)

print("""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Security Regulation Generator</title>
<style type="text/css">
    #CompanyInformation {
        width: 800px;
        margin: 50px auto;
    }
    
    table, th, td {
        border: 1px solid white;
        border-collapse: collapse;
    }
    
    th, td {
        padding: 5px;
        text-align: left;
    }
</style>
</head>
""")

print("""
<body>
<div id="CompanyInformation">
    <form method="post">
    <fieldset>
    <legend>Enter company information</legend>
        <table style="width:100%;">
        <tr>
        <td colspan="2">
        <label for="companyname">Name of Company</label>
        <br />
""")

if companyname != None:
    print(f"""
        <input type="text" id="companyname" name="companyname" style="width:100%;" value="{companyname}" required />
    """)
else:
    print(f"""
        <input type="text" id="companyname" name="companyname" style="width:100%;" required />
    """)

print("""
        </td>
        </tr>
        <tr>
        <td style="width:50%;">
        <label for="businesstype">Type of Business</label>
        <br />
        <select id="businesstype" name="businesstype" style="width:150px;" required>
            <option value="">-</option>
""")

if businesstype == "Education":
    print("""<option selected value="Education">Education</option>""")
else:
    print("""<option value="Education">Education</option>""")

if businesstype == "IT Services":
    print("""<option selected value="IT Services">IT Services</option>""")
else:
    print("""<option value="IT Services">IT Services</option>""")

print("""
        </select>
        </td>
        <td style="width:50%;">
        <label for="organizationsize">Size of Organization</label>
        <br />
        <select id="organizationsize" name="organizationsize" style="width:150px;" required>
            <option value="">-</option>
""")

if organizationsize == "10":
    print("""<option selected value="10">< 10 employees</option>""")
else:
    print("""<option value="10">< 10 employees</option>""")

if organizationsize == "11~50":
    print("""<option selected value="11~50">11 ~ 50 employees</option>""")
else:
    print("""<option value="11~50">11 ~ 50 employees</option>""")

if organizationsize == "51~200":
    print("""<option selected value="51~200">51 ~ 200 employees</option>""")
else:
    print("""<option value="51~200">51 ~ 200 employees</option>""")

if organizationsize == "201":
    print("""<option selected value="201">> 201 employees</option>""")
else:
    print("""<option value="201">> 201 employees</option>""")

print("""
        </select>
        </td>
        </tr>
        <tr>
        <td>
        <label for="numberofworkstations">Number of Workstations</label>
        <br />
        <select id="numberofworkstations" name="numberofworkstations" style="width:150px;" required>
            <option value="">-</option>
""")

if numberofworkstations == "10":
    print("""<option selected value="10">< 10 workstations</option>""")
else:
    print("""<option value="10">< 10 workstations</option>""")

if numberofworkstations == "11~50":
    print("""<option selected value="11~50">11 ~ 50 workstations</option>""")
else:
    print("""<option value="11~50">11 ~ 50 workstations</option>""")

if numberofworkstations == "51~200":
    print("""<option selected value="51~200">51 ~ 200 workstations</option>""")
else:
    print("""<option value="51~200">51 ~ 200 workstations</option>""")

if numberofworkstations == "201":
    print("""<option selected value="201">> 201 workstations</option>""")
else:
    print("""<option value="201">> 201 workstations</option>""")

print("""
        </select>
        </td>
        <td>
        <label for="numberofservers">Number of Servers</label>
        <br />
        <select id="numberofservers" name="numberofservers" style="width:150px;" required>
            <option value="">-</option>
""")

if numberofservers == "0":
    print("""<option selected value="0">0 servers</option>""")
else:
    print("""<option value="0">0 servers</option>""")

if numberofservers == "1~5":
    print("""<option selected value="1~5">1 ~ 5 servers</option>""")
else:
    print("""<option value="1~5">1 ~ 5 servers</option>""")

if numberofservers == "6~15":
    print("""<option selected value="6~15">6 ~ 15 servers</option>""")
else:
    print("""<option value="6~15">6 ~ 15 servers</option>""")

if numberofservers == "15":
    print("""<option selected value="15">> 15 servers</option>""")
else:
    print("""<option value="15">> 15 servers</option>""")

print("""
        </select>
        </td>
        </tr>
        <tr>
        <td></td>
        </tr>
        <tr>
        <td>
        <label for="editor">Editor</label>
        <br />
""")

if editor != None:
    print(f"""
        <input type="text" id="editor" name="editor" style="width:150px;" value="{editor}" required />
    """)
else:
    print("""
        <input type="text" id="editor" name="editor" style="width:150px;" required />
    """)

print("""
        </td>
        </tr>
        <tr>
        <td colspan="2">
        <label for="typeofpolicy">Type of  policy to be generated: </label>
        <select id="typeofpolicy" name="typeofpolicy" style="width:150px;" required>
            <option value="">-</option>
""")

if typeofpolicy == "WiFi":
    print("""<option selected value="WiFi">WiFi Policy</option>""")
else:
    print("""<option value="WiFi">WiFi Policy</option>""")

if typeofpolicy == "Password":
    print("""<option selected value="Password">Password Policy</option>""")
else:
    print("""<option value="Password">Password Policy</option>""")

print("""
        </select>
        <input type="submit" id="gen" name="gen" value="Generate" required />
        </td>
        </tr>
    </table>
    </fieldset>
    </form>
</div>
<div id="CompanyInformation">
    <form method="post">
    <fieldset>
    <legend>Policy Hash Code</legend>
        <table style="width:100%;">
""")

if hashcode != None:
    print(f"""
        <input type="text" id="hashcode" name="hashcode" style="width:700px;" value="{hashcode}" required />
    """)
else:
    print(f"""
        <input type="text" id="hashcode" name="hashcode" style="width:700px;" required />
    """)

print("""
        <input type="submit" id="find" name="find" value="Find" required />
        </table>
    </fieldset>
    </form>
</div>
<div id="CompanyInformation">
    <fieldset>
    <legend>Policy</legend>
        <table style="width:100%;">
""")

if (gen == "Generate" and filled == 1)\
        or (find == "Find" and count == 9):
    print(f"""
        <tr>
        <td style="text-align: center; font-size: 50px">
        {typeofpolicy} Policy
        </td>
        </tr>
        <tr>
        <td>
    """)
    if result == "":
        print("No rules were generated.")
    else:
        for i, everyrule in enumerate(result.split(".")):
            if i < len(result.split(".")) - 1:
                print(str(i + 1) + ". " + everyrule + ".")
                print("<br />")
    
    print("""
        </td>
        </tr>
    """)
elif find == "Find" and count != 9:
    print("""
        <tr>
        <td style="text-align: center; color: red; font-size: 50px">
        Not exists
        </td>
        </tr>
    """)
else:
    print("""
        <tr>
        <td style="text-align: center; font-size: 50px">
        Waiting for generation
        </td>
        </tr>
    """)

print("""
        </table>
    </fieldset>
</div>
""")


if gen == "Generate" and filled == 1:
    print(document.chain_size())
    print("<br />")
    
    for i in range(document.chain_size() + 1):
        print(document.blocks[i].index)
        print("<br />")
        print(document.blocks[i].data)
        print("<br />")
        print(document.blocks[i].timestamp)
        print("<br />")
        print(document.blocks[i].p_hash)
        print("<br />")


client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
database = client["database"]
collection = database["collection"]
print(client.list_database_names())
print("<br />")
print(database.list_collection_names())
print("<br />")

for i in collection.find():
    print(i)
    print("<br />")

#collection.drop()


print("</body>")
print("</html>")

