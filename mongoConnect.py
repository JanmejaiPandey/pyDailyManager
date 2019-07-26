from pymongo import MongoClient
import os
import time

client = MongoClient('mongodb+srv://try:pass@clusterdailymanager-f440g.mongodb.net/test?retryWrites=true&w=majority')


class usersDB:
    db = client.dailyManagerDB
    col = db.users

    @staticmethod
    def addUser(email, p):
        rec = {
            "email": email,
            "password": p
        }
        usersDB.col.insert_one(rec)
        print("user added Succesfully!!")


class tasksDB:
    db = client.dailyManagerDB
    col = db.tasks

    @staticmethod
    def addTask(task):
        rec = {
            "task": task
        }
        tasksDB.col.insert_one(rec)
        print("Task added Succesfully!!")

    @staticmethod
    def showTask():
        i = 1
        for t in tasksDB.col.find():
            print(str(i)+". " + t.get('task'))
            i = i+1


id = None
password = None


class names:

    @staticmethod
    def colNames():
        name = usersDB.db.list_collection_names()
        return name

    @staticmethod
    def dbNames():
        name = client.list_database_names()
        return name


class verify:

    @staticmethod
    def checkUser(email):
        if(usersDB.col.find_one({"email": email})):
            global id
            global password
            res = usersDB.col.find_one({"email": email})
            id = res.get("_id")
            password = res.get("password")

            return True
        else:
            return False

    @staticmethod
    def checkPass(p):
        global password
        if(password == p):
            return True
        else:
            return False
