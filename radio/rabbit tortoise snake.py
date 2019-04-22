from microbit import *
import random

# Image.RABBIT < Image.TORTOISE < Image.SNAKE <

animals = [Image.RABBIT, Image.TORTOISE, Image.SNAKE]

while True:

    clock_timer = 100

    display.show(Image.CLOCK12)
    sleep(clock_timer)
    display.show(Image.CLOCK1)
    sleep(clock_timer)
    display.show(Image.CLOCK2)
    sleep(clock_timer)
    display.show(Image.CLOCK3)
    sleep(clock_timer)
    display.show(Image.CLOCK4)
    sleep(clock_timer)
    display.show(Image.CLOCK5)
    sleep(clock_timer)
    display.show(Image.CLOCK6)
    sleep(clock_timer)
    display.show(Image.CLOCK7)
    sleep(clock_timer)
    display.show(Image.CLOCK8)
    sleep(clock_timer)
    display.show(Image.CLOCK9)
    sleep(clock_timer)
    display.show(Image.CLOCK10)
    sleep(clock_timer)
    display.show(Image.CLOCK11)
    sleep(clock_timer)
    display.show(Image.CLOCK12)
    sleep(clock_timer)

    micro_choice = random.choice([0, 1, 2])
    own_choice = 0

    if button_a.was_pressed():
        own_choice = 1
    if button_b.was_pressed():
        own_choice = 2
    
    display.show(animals[own_choice])

    sleep(2000)

    display.scroll("vs.")

    sleep(250)

    display.show(animals[micro_choice])

    sleep(2000)

    if own_choice == 0 and micro_choice == 1 or (own_choice == 1 and micro_choice == 2) or (own_choice == 2 and micro_choice == 0):
        display.show(Image.NO)
    elif micro_choice == 0 and own_choice == 1 or (micro_choice == 1 and own_choice == 2) or (micro_choice == 2 and own_choice == 0):
        display.show(Image.YES)
    else:
        display.show(Image.MEH)

    sleep(5000)