# Proxy server som modtager readings fra raspberry pi'en via UDP. Og som poster dem til vores API via HTTP POST requests.


import requests # requests bruges til at kunne sende http requests til vores api
from socket import * # socket bruges til at kunne sende og modtage data til vores api
import json # json bruges til at konvertere data til json format
url = 'https://promillepartnerbackend.azurewebsites.net/api/pireading' #api
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) # 
serverAddress = ("10.200.162.74", serverPort) # ip og port kombineret

serverSocket.bind(serverAddress) # bind serveren til en ip og port
print("The server is ready") #status besked

while True: #Looper så længe scriptet kører
    #print("looping")
    message, clientAddress = serverSocket.recvfrom(2048) #modtager besked fra client
    promillemåling = json.loads(message.decode()) #afkoder beskeden og laver aonymt objekt
    print(promillemåling)
    #tager properties fra anonymt objekt og sender til REST API
    #man tilgår properties på et anonymt objekt som var det et dictionary
    #vigtigt at du bruger ' ' til at kalde nøglen " " fungerer ikke
    requests.post(url, json={"promille":promillemåling['promille'], 'timestampmiliseconds':promillemåling['timestamp']}) 