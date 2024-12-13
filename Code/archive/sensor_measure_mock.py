from datetime import datetime, timedelta
import time
from sense_hat import SenseHat
import random

# Initialize Sense HAT
sense = SenseHat()

def generate_mock_measurements():
    """
    Generates three mock BAC measurements with timestamps.
    """
    print("Starting mock BAC measurements...")
    
    # Get the current time
    start_time = datetime.now()
    
    # Define measurement intervals (in seconds)
    intervals = [30, 60, 90]
    
    # Store measurements
    measurements = []
    
    for interval in intervals:
        # Calculate the timestamp for this measurement
        measurement_time = start_time + timedelta(seconds=interval)
        
        # Generate a random BAC value
        bac = round(random.uniform(0.02, 0.1), 3)  # BAC between 0.02 and 0.1
        
        # Append to measurements list
        measurements.append((measurement_time.strftime("%H:%M:%S"), bac))
        
        # Wait for the interval before proceeding to the next measurement
        time.sleep(interval - (time.time() % interval))
        
        # Display measurement on Sense HAT
        message = f"BAC: {bac} @ {measurement_time.strftime('%H:%M:%S')}"
        print(message)  # Print to console for reference
        sense.show_message(message, scroll_speed=0.05)
    
    return measurements

if __name__ == "__main__":
    measurements = generate_mock_measurements()
    print("Mock BAC Measurements:")
    for timestamp, bac in measurements:
        print(f"{timestamp}: BAC {bac}")
