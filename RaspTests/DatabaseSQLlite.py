import sqlite3
from sense_hat import SenseHat
from Repository import Repo
import time

sence = SenseHat()
Dbconn = Repo()
sqliteConnection = sqlite3.connect('sql.db')

while True:
    temp = round(sence.temp,2)
    humi = round(sence.humidity,2)
    pres = round(sence.pressure,2)
    print("Temp: "+str(temp)+" Pressure: "+str(pres)+" Humidity: "+str(humi))
    Dbconn.InsertRowMeasure(sence.temp, sence.humidity, sence.pressure)
    time.sleep(10)
