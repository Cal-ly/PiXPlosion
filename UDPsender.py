#import RPI.GPIO as GPIO
import time
import os

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8,GPIO.IN)

# while(1):
#    input = GPIO.input(8)
#    if(input == 0):
#        print("Alcohol is not detected")
#        print(input)
#     else:
#        print("Alcohol is detected")
#        print(input)
#     time.sleep(1)

# Overstående er til pi målinger på raspberry pien
# Ovenstående er ikke afprøvet



from socket import *
import json
import time
import datetime

serverPort = 12000

clienSocket = socket(AF_INET, SOCK_DGRAM)

buttonPressed = True

while 1==1:
    
    while buttonPressed:
        clienSocket = socket(AF_INET, SOCK_DGRAM)
        clienSocket.connect(("10.200.162.74",serverPort))
        promillereading = 0.5
        timestamp = int(time.time())
        clienSocket.send((json.dumps({"promille": promillereading, "timestamp": timestamp})).encode())
        clienSocket.close()
        time.sleep(5)
    time.sleep(5)


