from sense_hat import SenseHat
import time

S = SenseHat()

drinkPlanen = [
    {"id": 1, "timeDifference": 2, "drinkName": "beer"},
    {"id": 2, "timeDifference": 16, "drinkName": "cider"},
    {"id": 3, "timeDifference": 21, "drinkName": "beer"}
]

WIDTH = 8
HEIGHT = 8
TOTAL_LEDS = WIDTH * HEIGHT

def get_color(percent_left):
    if percent_left > 0.66:
        # Green
        return (0, 255, 0)
    elif percent_left > 0.33:
        # Yellow
        return (255, 255, 0)
    else:
        # Red
        return (255, 0, 0)


while True:
    for plan in drinkPlanen:
        TimeDifference = plan["timeDifference"]
        DrinkName = plan["drinkName"]

        for i in range(TOTAL_LEDS):
            # Calculate percentage of time left
            percent_left = (TimeDifference - (i + 1)) / TimeDifference

            color = get_color(percent_left)

            # Set the current LED
            x = i % WIDTH
            y = i // WIDTH
            S.set_pixel(x, y, color)

            # Wait for the next update
            time.sleep(TimeDifference / TOTAL_LEDS)

        # Show the message after all LEDs are updated
        S.show_message("Time to drink {DrinkName}!")
