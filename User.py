from Database import client
def User():
        db = client()
        user = db["users"]
        return user

def drop_collection():
    user = User()

    user.drop()