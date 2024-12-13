import RPi.GPIO as GPIO
import time

# Pin configuration
MQ3_DOUT_PIN = 17  # Replace with your GPIO pin number

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(MQ3_DOUT_PIN, GPIO.IN)

try:
    while True:
        # Read the digital output
        sensor_value = GPIO.input(MQ3_DOUT_PIN)
        if sensor_value == GPIO.HIGH:
            print("Alcohol detected!")
        else:
            print("No alcohol detected.")
        time.sleep(1)  # Delay to avoid spamming the console
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()  # Reset GPIO settings