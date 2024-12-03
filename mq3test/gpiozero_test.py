from gpiozero import Button
from signal import pause

mq3_sensor = Button(23)  # Replace with your GPIO pin number

def alcohol_detected():
    print("Alcohol detected!")

def no_alcohol():
    print("No alcohol detected.")

mq3_sensor.when_pressed = alcohol_detected
mq3_sensor.when_released = no_alcohol

pause()  # Keep the script running