# https://microbit-micropython.readthedocs.io/en/latest/pin.html

from microbit import *

while True:
    reading = pin0.read_analog() - 200

    '''if reading > 350:
        display.show(Image.HEART)
    else:
        display.show(Image.HEART_SMALL)'''

    reading = round(reading / 100)
    if reading == 10:
        reading = 9

    if reading < 0:
        reading = 0

    output = ""

    for y in range(5):
        for x in range(5):
            output = output + str(reading)

        if y < 4:
            output = output + ":"

    display.show(Image(output))