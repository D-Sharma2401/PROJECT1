import pymongo
import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDBHelper:

    def __init__(self, collection='customer'):
        ca = certifi.where()
        uri = "mongodb+srv://D_SHARMA2401:D_SHARMA2401@cluster0.lnoagiu.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, tlsCAFile=ca)
        self.db = client['dsharma24']
        self.collection = self.db[collection]
        print("MongoDB Connected...")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted: ", result.inserted_id)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted:", result.deleted_count)

    def fetch(self, query=None):
        documents = self.collection.find(query) if query else self.collection.find()
        return list(documents)

    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print("Updated Document:", result.modified_count)


# Usage example
if __name__ == "__main__":
    MongoDBHelper()

