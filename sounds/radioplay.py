# https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/radio.html

import radio
import music
from microbit import *

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('C4:2')
    if button_b.was_pressed():
        radio.send('E4:2')

    incoming = radio.receive()

    if incoming is not None:
        music.play([incoming])