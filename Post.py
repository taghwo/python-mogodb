from Database import client

def Post():
    db = client()
    post = db['posts']
    return post