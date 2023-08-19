"""
    1. create account on mongodb atlas
    2.netword access = 0.0.0.0/0
    3.create database user and password
    4.navigate to browse

"""

import pymongo
import certifi  #pip install certifi | if SSL ERROR

ca = certifi.where()

uri = "mongodb+srv://D_SHARMA2401:D_SHARMA2401@cluster0.lnoagiu.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
client = pymongo.MongoClient(uri, tlsCAFile=ca) #if SSL ERROR

db = client['dsharma24']
collections = db.list_collection_names()

for collection in collections:
    print(collection)

documents = db['customer'].find()
for document in documents:
    print(document)