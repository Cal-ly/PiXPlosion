import time

def StartTimer(data):
    for value in data:
        try:
            # Try to parse the value to an integer
            convertedData = int(value)
            print(f"Sleeping for {convertedData} seconds")  # Optional: print the sleep duration

            #Send notification, time to drink!
            
            time.sleep(convertedData)  # Sleep for the number of seconds specified by the current value
        except ValueError:
            # If conversion fails, print an error message
            print(f"Error: '{value}' could not be converted to an integer.")