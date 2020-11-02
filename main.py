from Server import Server
from Database import Database
from Summarizer import Summarizer
from TaskManager import TaskManager
HOST = '0.0.0.0'
PORT = 5000
# DBHOST = "122.202.43.154" # 희수 1
DBHOST = "121.183.10.54" # 희수 2
# DBHOST = "118.45.99.84" # 재웅
# DBHOST = 'localhost'
DBPORT = 27017

if __name__ == '__main__':
    summarizer = Summarizer()
    tm = TaskManager(summarizer)
    Database(DBHOST, DBPORT)
    server = Server(tm)
    server.run(HOST, PORT)