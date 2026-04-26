from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (username, password, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the MongoDB collection"""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create failed:", e)
                return False
        else:
            return False

    def read(self, query):
        """Query documents from the MongoDB collection"""
        if query is not None:
            try:
                data = self.collection.find(query)
                return list(data)
            except Exception as e:
                print("Read failed:", e)
                return []
        else:
            return []

    def update(self, query, new_values):
        """Update document(s) in the MongoDB collection"""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Update failed:", e)
                return 0
        else:
            return 0

    def delete(self, query):
        """Delete document(s) from the MongoDB collection"""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete failed:", e)
                return 0
        else:
            return 0