from datetime import datetime
from sense_hat import SenseHat
import time
import decimal
from Repository import Repo

sence = SenseHat()
Dbconn = Repo()
while True:
    temp = round(decimal.Decimal(sence.temp),2)
    humi = round(decimal.Decimal(sence.humidity),2)
    pres = round(decimal.Decimal(sence.pressure),2)
    print("Temp: "+str(temp)+" Pressure: "+str(pres)+" Humidity: "+str(humi))
    Dbconn.InsertRowMeasure(sence.temp, sence.humidity, sence.pressure)
    time.sleep(120)
