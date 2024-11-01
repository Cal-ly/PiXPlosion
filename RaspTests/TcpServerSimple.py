import socket
from socket import *
import threading

serverHost = "192.168.1.113"
serverPort = 13000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost,serverPort))
serverSocket.listen(1)

def ClientHandler(connectionSocket, addr):

    lastMessage = False

    while lastMessage == False:
        message = connectionSocket.recv(1024).decode()
        modifiedMessage = message.upper()
        connectionSocket.send(modifiedMessage.encode())
        if message.strip().upper() == "QUIT":
            lastMessage = True

    connectionSocket.close()


connectionSocket, addr = serverSocket.accept()
message = connectionSocket.recv(1024).decode()
modifiedMessage = message.upper()
print(modifiedMessage)
connectionSocket.close()
    
    #ClientHandler(connectionSocket, addr)
    #threading.Thread(target=ClientHandler, args=(connectionSocket, addr)).start()