import RPi.GPIO as GPIO

TEST_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(TEST_PIN, GPIO.IN)

try:
    print("Testing GPIO pin. Connect it to GND to change state.")
    while True:
        state = GPIO.input(TEST_PIN)
        print(f"Pin State: {'HIGH' if state else 'LOW'}")
except KeyboardInterrupt:
    print("Exiting.")
finally:
    GPIO.cleanup()
