from sense_hat import SenseHat
import time
import json

# Initialize Sense HAT and buffer
sense = SenseHat()
data_buffer = []

def collect_data():
    # Collect data
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    timestamp = time.time()

    # Structure data as JSON
    data = {
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    }

    # Append data to buffer
    data_buffer.append(data)
    print(f"Data collected: {data}")

while True:
    collect_data()
    time.sleep(1)
