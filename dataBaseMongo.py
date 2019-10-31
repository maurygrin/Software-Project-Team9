import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://Ortiz:team09@cluster0-mvofe.mongodb.net/test?retryWrites=true&w=majority")
db = cluster.test

collection = db["test"]


project = {"title": "BEAT",
           "Project Description":"Description",
           "Binary File Path": "PATH"}

collection.insert_many([project])


