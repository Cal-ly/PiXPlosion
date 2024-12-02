from sense_hat import SenseHat

sense = SenseHat()

def display_drinking_plan(plan):
    if not plan:
        sense.show_message("No plan available")
        return
    
    for interval, drink in zip(plan["timeIntervals"], plan["drinks"]):
        message = f"Drink: {drink} @ {interval}"
        sense.show_message(message)
