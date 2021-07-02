import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.d1apg.mongodb.net/myData?retryWrites=true&w=majority")
db = client.mydata
collection = db.mytable
requesting = []

with open("C:\\Users\\bishwanath.parajuli\\Desktop\\2.json") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()
