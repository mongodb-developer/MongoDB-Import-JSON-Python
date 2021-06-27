import json
from pymongo import MongoClient


# Making Connection
myclient = MongoClient(
    "<mongo-uri>")


db = myclient["<DATABASE>"]


Collection = db["<COLLECTION>"]

# Loading or Opening the json file
with open("<FILE PATH>") as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    Collection.insert_many(file_data)
    print("inserted")
else:
    Collection.insert_one(file_data)
    print("inserted")
