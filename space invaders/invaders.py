# https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html

from microbit import *
import random

def generate():
    invader = ""

    for y in range(5):
        
        line = ""

        for x in range(3):

            pixel = "0"

            if random.choice([True, False]):
                pixel = "9"

            line = line + pixel
        
        line = line + line[1] + line[0]
        invader = invader + line

        if y < 4:
            invader = invader + ":"

    return invader

display.show(Image(generate()))

while True:
    if button_a.was_pressed():
        display.show(Image(generate()))

    if button_b.is_pressed():
        display.show(Image(generate()))
        sleep(250)