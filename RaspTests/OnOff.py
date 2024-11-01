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

def Booking_logo():
    r = red
    c = green
    n = nothing
    logo = [
    c, c, r, r, c, c, c, c,
    c, c, r, r, c, c, c, c,
    n, n, n, n, n, n, n, n,
    c, c, c, c, c, c, r, r,
    c, c, c, c, c, c, r, r,
    n, n, n, n, n, n, n, n,
    c, c, c, c, r, r, c, c,
    c, c, c, c, r, r, c, c,
    ]
    return logo

def TurnLight(color):
    s.set_pixels(Color_logo(color))

def Booking_logo():
    s.set_pixels(Booking_logo())

if __name__ == "__main__":
    count = 0
    color = red 
    while True:
        #s.set_pixels(Color_logo(color))
        TurnLight(color)
        if ((count % 2) == 0):
            color = green
        else:
            color = red    
        time.sleep(.75)
        count += 1
       
       