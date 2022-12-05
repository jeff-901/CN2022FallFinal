from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json
load_dotenv()

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.environ["MONGO_URL"]

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["cnfinal"]


dbname = get_database()
user_collection = dbname["users"]
item_1 = {
    "username": "john",
    "password": "1234",
    "friends": []
}

item_2 = {
    "username": "amy",
    "password": "1234",
    "friends": []
}
user_collection.insert_many([item_1,item_2])


def get_user(username):
    users = list(user_collection.find({"username": username}))
    print(f"find users with username {username}: {users}")
    return users


def create_user(user):
    print(f"create users with {json.dumps(user)}")
    return user_collection.insert_one(user)

def update_user(user):
    print(f"update user with {json.dumps(user)}")
    myquery = { "username": { "$regex": user["username"] } }
    newvalues = { "$set": { "friends": user["friends"] } }
    x = user_collection.update_many(myquery, newvalues)
    assert x.modified_count == 1
    return True


# for x in get_user("john"):
#     print(x)
