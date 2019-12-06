import pymongo
from pymongo import MongoClient
class DBController(object):

    def __init__(self):
        cluster = MongoClient("mongodb://localhost:27017")
        db = cluster.test
        self.collection = db["beat"]

    def insertProject(self, insert):
        self.collection.insert_many([insert])

    def insertPlugin(self, insert):
        self.collection.insert_many([insert])

    def findPlugins(self, plugins):
        for document in self.collection.find():
            plugins.pluginManagementList.addItem(document.get("Plugin Name"))

    def findProjects(self, projects):
        for document in self.collection.find():
            projects.projectList.addItem(document.get("Project Name"))

    def findProject(self, name, list):
        return self.collection.find_one({name: list})

    def deleteProject(self, project):
        self.collection.delete_one(project)

    def findPlugin(self, name, list):
        return self.collection.find_one({name: list})

    def deletePlugin(self, plugin):
        self.collection.delete_one(plugin)

    def findDocument(self, name, list):
        return self.collection.find_one({name: list})

    def insertDocument(self, document):
        self.collection.insert_one(document)

    def countDocuments(self, name, list):
        return self.collection.count_documents({name: list})

    def replaceDocument(self, name, list, text_file_doc):
        self.collection.replace_one({name: list}, text_file_doc)

    def insertDocument(self, name, list, text_file_doc):
        self.collection.insert_one({name: list}, text_file_doc)