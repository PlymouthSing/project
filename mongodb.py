#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())
