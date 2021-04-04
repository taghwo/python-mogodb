from Post import Post
from User import User
from bson.objectid import ObjectId

def create_user():
        user = User()

        mydict = { "name": "John", "address": "Highway 37" }

        new_user = user.insert_one(mydict)


        users = [
                    { "name": "Amy", "address": "Apple st 652"},
                    { "name": "Hannah", "address": "Mountain 21"},
                    { "name": "Michael", "address": "Valley 345"},
                    { "name": "Sandy", "address": "Ocean blvd 2"},
                    { "name": "Betty", "address": "Green Grass 1"},
                    { "name": "Richard", "address": "Sky st 331"},
                    { "name": "Susan", "address": "One way 98"},
                    { "name": "Vicky", "address": "Yellow Garden 2"},
                    { "name": "Ben", "address": "Park Lane 38"},
                    { "name": "William", "address": "Central st 954"},
                    { "name": "Chuck", "address": "Main Road 989"},
                    { "name": "Viola", "address": "Sideway 1633"}
                 ]
        new_users = user.insert_many(users)

        print(new_user.inserted_id)

def create_post():
    data = { "title": "go duck and go duck", "description": "Lorep ipsum dorem ipsolet" }

    post = Post()

    new_post = post.insert_one(data)

    print(new_post.inserted_id)

def fetch_user():
    user = User()

    single_user = user.find_one()

    print(single_user)

def fetch_by_id():
    user = User()

    user_by_id = user.find_one(ObjectId("6069e079bf37a0b16186dc8e"))

    print(user_by_id)

def fetch_many():
    user = User()

    users = user.find()

    for user in users:
      print(user['name'])

def fetch_with_select():
    user = User()

    users = user.find({},{'_id':0,'name':1})

    for user in users:
      print(user)


def fetch_with_query():
    user = User()

    query = {"name": {"$gt":"W"}}
    user_query = user.find(query)

    for user in user_query:
      print(user)

def fetch_with_sort():
    user = User()

    users = user.find().sort('name')
    # users = user.find().sort('name':-1)

    for user in users:
      print(user)

def delete_document():
    user = User()

    deleted_user = user.delete_one({"name":"Amy"})

    # user.delete_many({})

    users = user.find().sort('name')

    print(deleted_user)

    for user in users:
      print(user)

def update_document():
    user = User()

    myquery = { "_id": ObjectId("6069e079bf37a0b16186dc8e") }

    new_values = { "$set": { "address": "Canyon 123","name":"Taghwo" } }

    user.update_one(myquery, new_values)

    print(user.find_one({'_id':ObjectId("6069e079bf37a0b16186dc8e")}))

def fetch_with_limit():
    user = User()
    users = user.find()

    for user in users:
      print(user)

def count_document():
    user = User()

    print(user.count_documents({}))


    #conditionals
    # { status: { $in: [ "A", "D" ] } }
    # {"name": {"$gt":"W"}}
    # { status: "A", qty: { $lt: 30 } }
    # { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] }
    # { status: "A", $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ] }
    # { "size.uom": "in" }
    # { "size.h": { $lt: 15 } }
    # { "size.h": { $lt: 15 }, "size.uom": "in", status: "D" }
    # users.find( { tags: ["red", "blank"] } )
    # user.find( { tags: { $all: ["red", "blank"] } } )
    # user.find( { "tags": { $size: 3 } } )
    # user.find( { "instock": { warehouse: "A", qty: 5 } } )

    # indexing
    # user.createIndex( { name: "text", address: "text" } )

    #exact phrase
    # user.find( { $text: { $search: "\"coffee shop\"" } } )

    # sort and skip
    # user.find(query, { sort: { rating: -1}, skip: 2});
    # user.find(query).sort({rating: -1}).skip(2);

    #aggregate with searching
    #     user.aggregate(
    # [
    #     { $match: { $text: { $search: "cake" } } },
    #     { $group: { _id: null, views: { $sum: "$views" } } }
    # ]
    # )


    # Find all documents where field "a" is less than "b" plus "c".
    # for doc in db.test.find().where('this.a < (this.b + this.c)'):
    # print(doc)

    # text search
    # user.find( { $text: { $search: "java coffee shop" } } )

    # user.aggregate([
    # { $match: { name: "Mills" } },
    # { $group: { _id: "$cust_id", total: { $sum: "$amount" } } }
    # ])

    # user.aggregate([
        # {
        #     $lookup:
        #     {
        #         from: "user",
        #         localField: "item",
        #         foreignField: "sku",
        #         as: "inventory_docs"
        #     }
        # }
        # ])
# create_user()
# create_post()

# fetch_user()
# fetch_many()
# fetch_with_select()
# fetch_with_query()
# fetch_with_sort()
# delete_document()
# update_document()
# fetch_with_limit()

count_document()