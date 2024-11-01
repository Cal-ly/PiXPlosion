import socket
from socket import *
from sense_hat import SenseHat

serverHost = "192.168.1.127"
serverPort = 13000

udpClient = socket(AF_INET, SOCK_DGRAM)


message = input("Enter Message: ").encode("utf-8")
udpClient.sendto(message, (serverHost, serverPort))