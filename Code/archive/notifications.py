import time
from sensehat_display import display_message

def trigger_notifications(plan):
    print("Starting notifications...")
    for interval, drink in zip(plan["timeIntervals"], plan["drinks"]):
        display_message(f"Time for {drink}!")
        time.sleep(60)  # Replace with actual interval logic
