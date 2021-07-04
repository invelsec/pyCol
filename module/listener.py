import socket

class Listener():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 0
    SERVER_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def __init__(self,SERVER_PORT):
        self.SERVER_PORT = SERVER_PORT
        self.startServer()
        while True:
            try:
                self.serverListener()
            except KeyboardInterrupt:
                print("\nKeyboard Interrupt.. Closing!")
                self.stopServer()
                exit()

    def startServer(self):
        self.SERVER_SOCK.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.SERVER_SOCK.bind((self.SERVER_HOST,int(self.SERVER_PORT)))
        self.SERVER_SOCK.listen(1)
        print(f"Server Started On -> {self.SERVER_HOST}:{self.SERVER_PORT}")

    def serverListener(self):
        client_connection, client_address = self.SERVER_SOCK.accept()
        try:
            incoming_req = client_connection.recv(1024).decode()
        except UnicodeDecodeError:
            print("Connection Decode Error!")
        print(f"\nClientAddr -> {client_address}\nRequest -> {incoming_req}")

    def stopServer(self):
        self.SERVER_SOCK.close()

