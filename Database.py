import pymongo as pm
# DBHOST = "122.202.43.154" # 희수 1
DBHOST = "121.183.10.54" # 희수 2
# DBHOST = "118.45.99.84" # 재웅
# DBHOST = 'localhost'
DBPORT = 27017

class Database:
    __instance = None

    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance != None:
            raise Exception("Already exists.")
        else:
            Database.__instance = pm.MongoClient(DBHOST, DBPORT)