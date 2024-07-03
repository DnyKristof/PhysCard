import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient



class MongoDB:
    _initiated = None
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.database = self.client.physcard_database
    def get_collection(self,collection):
        return self.database[collection]


def MongoInit():
    if MongoDB._initiated is None:
        MongoDB._initiated = MongoDB()
    return MongoDB._initiated