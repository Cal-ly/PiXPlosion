from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def Color_logo(color):
    c = color
    logo = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    ]
    return logo

def TurnLight(color):
    s.set_pixels(Color_logo(color))

def DetectMove():
    acc= s.get_accelerometer_raw()
    x = abs(acc['x'])
    y = abs(acc['y'])
    z = abs(acc['z'])

    if x>1 or y>1 or z>1:
        TurnLight(yellow)
        time.sleep(.75)
    else:
        TurnLight(pink)
            


if __name__ == "__main__":
    count = 0
    color = red 
    while True:
        DetectMove()
       