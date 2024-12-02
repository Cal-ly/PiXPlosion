import random

# Simulate sensor data
def get_mock_sensor_bac():
    print("Simulating BAC sensor data...")
    # Random BAC value between 0.02 and 0.1
    return round(random.uniform(0.02, 0.1), 2)
