from sense_hat import SenseHat

sense = SenseHat()

def display_message(message):
    print(f"Displaying message: {message}")
    sense.show_message(message)

def display_drinking_plan(plan):
    for interval, drink in zip(plan["timeIntervals"], plan["drinks"]):
        message = f"Drink: {drink} @ {interval}"
        display_message(message)
