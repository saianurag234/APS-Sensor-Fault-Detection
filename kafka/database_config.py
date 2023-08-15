import pymongo


class MongoDBOperation:

    client = None
    MongoDB_URL = "mongodb://localhost:27017"

    def __init__(self, Database_name: str, Collection_name: str):

        database_name = Database_name
        collection_name = Collection_name

        MongoDBOperation.client = pymongo.MongoClient(
            MongoDBOperation.MongoDB_URL)

        self.client = MongoDBOperation.client

        self.database = self.client[database_name]

        self.collection = self.database[collection_name]
