import pymongo as pm

class Database:
    __instance = None

    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self, host, port):
        if Database.__instance != None:
            raise Exception("Already exists.")
        else:
            Database.__instance = pm.MongoClient(host, port)