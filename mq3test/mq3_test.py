import explorerhat
import time

def read_sensor():
    try:
        while True:
            # Read analog value from ADC0 (connected to MQ3 OUT)
            analog_value = explorerhat.analog.one.read()
            print(f"Analog Value: {analog_value}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting.")

if __name__ == "__main__":
    read_sensor()
