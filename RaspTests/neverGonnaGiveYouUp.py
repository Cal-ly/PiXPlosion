from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.low_light = True

# Define a set of colors for the frogs
colors = [
    (255, 0, 0),    # red
    (255, 127, 0),  # orange
    (255, 255, 0),  # yellow
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (75, 0, 130),   # indigo
    (148, 0, 211),  # violet
    (255, 105, 180),# pink
    (0, 255, 255),  # cyan
    (255, 20, 147)  # deep pink
]

# Define a basic frog shape with a main color
frog = [
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0,
    1, 1, 2, 1, 1, 2, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0
]

# Function to color the frog pattern with a random color
def color_frog(color):
    return [(color if pixel == 1 else (255, 255, 255) if pixel == 2 else (0, 0, 0)) for pixel in frog]

# Function to display colored frogs in different rotations
def frog_flash():
    for _ in range(10):  # Flash pattern 10 times
        color = random.choice(colors)  # Random color for the frog
        s.set_pixels(color_frog(color))
        time.sleep(0.2)
        s.clear()
        time.sleep(0.2)
        for rotation in [90, 180, 270]:  # Rotate frog in different directions
            s.set_rotation(rotation)
            s.set_pixels(color_frog(color))
            time.sleep(0.2)
            s.clear()
            time.sleep(0.2)
        s.set_rotation(0)  # Reset to original orientation

# Main loop to continuously flash frogs in random colors and rotations
if __name__ == "__main__":
    while True:
        frog_flash()
