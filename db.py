from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.environ["MONGO_URL"]

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["cnfinal"]


dbname = get_database()
collection_name = dbname["users"]
# item_1 = {
#     "username": "john",
#     "password": "1234"
# }

# item_2 = {
#     "username": "amy",
#     "password": "1234"
# }
# collection_name.insert_many([item_1,item_2])


def get_user(username):
    return list(collection_name.find({"username": username}))


def create_user(user):
    return collection_name.insert_one(user)


# for x in get_user("john"):
#     print(x)
