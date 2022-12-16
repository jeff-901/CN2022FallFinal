from pymongo import MongoClient
import os, math
from dotenv import load_dotenv
import json
from bson.raw_bson import RawBSONDocument
from bson.objectid import ObjectId

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
message_collection = dbname["messages"]
file_collection = dbname["file"]
file_chunk_collection = dbname["chunk"]
CHUNKSIZE = 16000000
# item_1 = {
#     "username": "john",
#     "password": "1234",
#     "friends": []
# }

# item_2 = {
#     "username": "amy",
#     "password": "1234",
#     "friends": []
# }
# user_collection.insert_many([item_1,item_2])

# message = {
#    "senders": "amy,john",
#    "msg": "hi",
#    "timestamp": 1670483779
# }


def get_user(username):
    users = list(user_collection.find({"username": username}))
    print(f"find users with username {username}: {users}")
    return users


def create_user(user):
    print(f"create users with {json.dumps(user)}")
    return user_collection.insert_one(user)


def update_user(user):
    print(f"update user with {json.dumps(user)}")
    myquery = {"username": {"$regex": user["username"]}}
    newvalues = {"$set": {"friends": user["friends"]}}
    x = user_collection.update_many(myquery, newvalues)
    assert x.modified_count == 1
    return True


def create_message(message):
    print(f"create message with {json.dumps(message)}")
    return message_collection.insert_one(message)


def get_messages(user1, user2):
    print(f"get message between {user1} and {user2}")
    myquery = {"senders": {"$regex": f"({user1},{user2}|{user2},{user1})"}}
    # print(myquery)
    return list(message_collection.find(myquery))


def create_file(file, data):
    print(f"create file with {file}")
    data += b"\0"
    insert_file = {"name": file, "chunks": []}
    chunk_num = math.ceil(len(data) / CHUNKSIZE)
    chunk_id = []
    for i in range(chunk_num):
        chunk = file_chunk_collection.insert_one(
            {"data": data[i * CHUNKSIZE : (i + 1) * CHUNKSIZE]}
        )
        chunk_id.append(str(chunk.inserted_id))
    insert_file["chunks"] = chunk_id
    file_meta = file_collection.insert_one(insert_file)
    return str(file_meta.inserted_id)


def get_file(file_id):
    print(f"get file: {file_id}")
    myquery = {"_id": ObjectId(file_id)}
    files = list(file_collection.find(myquery))
    if len(files) == 0:
        return None
    file = files[0]
    data = b""
    for chunk in file["chunks"]:
        chunk_data = file_chunk_collection.find_one({"_id": ObjectId(chunk)})
        # print(type(chunk_data["data"]))
        data += chunk_data["data"]
    # print(data)
    return data[:-1]
