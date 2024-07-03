from physcard_backend.mongo import MongoInit
from bson.objectid import ObjectId

class CardService:
    def __init__(self):
        self.mongo = MongoInit()
        self.collection = self.mongo.get_collection("cards")

    def get_all_cards(self):
        return list(self.collection.find())

    def get_card_by_id(self, id):
        return self.collection.find_one({"_id": id})

    def create_card(self, card):
        card["_id"] = str(ObjectId())
        insert_result=self.collection.insert_one(card)
        return insert_result.inserted_id
    
    def update_card(self, id, card):
        self.collection.update_one({"_id": id}, {"$set": card})

    def delete_card(self, id):
        self.collection.delete_one({"_id": id})