import Server
HOST = '0.0.0.0'
PORT = 5000

if __name__ == '__main__':
    server = Server()
    server.run(HOST, PORT)