from Server import Server
from Summarizer import Summarizer
from TaskManager import TaskManager
HOST = '0.0.0.0'
PORT = 5000

if __name__ == '__main__':
    summarizer = Summarizer()
    tm = TaskManager(summarizer)
    server = Server(tm)
    server.run(HOST, PORT)