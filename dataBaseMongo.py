import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://Ortiz:team09@cluster0-mvofe.mongodb.net/test?retryWrites=true&w=majority")
db = cluster.test

collection = db["test"]

post = {"name": "tim", "score": 5}
project = {"title": "BEAT", "name":"Gustavo"}

collection.insert_many([post, project])


