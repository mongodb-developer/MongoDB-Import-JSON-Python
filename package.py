import json
from pymongo import MongoClient


# Making Connection
myclient = MongoClient(
    "mongodb+srv://bipin:mynameis@sandbox.jadwj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = myclient["test"]


Collection = db["jsonImport"]

# Loading or Opening the json file
with open("C:\\Users\\Bipin\\Downloads\\Data.json") as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    Collection.insert_many(file_data)
    print("inserted")
else:
    Collection.insert_one(file_data)
    print("inserted")
