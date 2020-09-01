#!/usr/bin/python3

import cgi
import cgitb
import datetime
import hashlib
import pymongo
from bson.objectid import ObjectId

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


client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
database = client["database"]
collection = database["collection"]
print(client.list_database_names())

print(database.list_collection_names())

hashcode = "36e348752de4a7d29e87eb052c8d3d5d7917f2e4f5274307fdd44c114fbab193"
query = {"p_hash": hashcode}
target = collection.find_one(query)

h = int(str(target["_id"]), 16) - 9
query = {"_id": ObjectId(format(h, "x"))}
target = collection.find_one(query)

#print(target)
if target:
    vdoc = vChain(target["timestamp"])

count = 0
while target and vdoc.blocks[count].p_hash == target["p_hash"]:
    h += 1
    query = {"_id": ObjectId(format(h, "x"))}
    target = collection.find_one(query)
    print(target)
    if target:
        vdoc.add_block(target["data"], target["timestamp"])
        count += 1
print(count)
#info = {
#    "index": "999",
#    "data": "",
#    "timestamp": "",
#    "p_hash": ""
#    }
#collection.insert_one(info)

#target = collection.find_one({"index": "999"})
#print(target["data"])

#print(vdoc.blocks[0].index)
#print(vdoc.blocks[0].data)
#print(vdoc.blocks[0].timestamp)
#print(vdoc.blocks[0].p_hash)
#print(vdoc.chain_size())
#print()

