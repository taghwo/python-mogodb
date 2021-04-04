from pymongo import MongoClient

def client():
        client =  MongoClient('localhost', 27017)

        db = client['mongo_client']

        # print(client.list_database_names())

        # print(db.list_collection_names())

        return db
