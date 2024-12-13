import time
import explorerhat as eh

# Define the analog input channel (0-3)
channel = 0  # Use 0 for AN0, 1 for AN1, etc.

while True:
    try:
        # Read the analog value (0-1023)
        analog_value = eh.analog[channel].read()
        # Convert to voltage (Explorer pHAT uses a 3.3V reference)
        voltage = analog_value * 3.3 / 1023
        print(f"Analog Value: {analog_value:.2f} | Voltage: {voltage:.2f}V")
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break