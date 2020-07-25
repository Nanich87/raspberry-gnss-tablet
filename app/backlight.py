#!/usr/bin/python
from rpi_backlight import Backlight
from gpiozero import Button
from signal import pause
import time

backlight = Backlight()
button = Button(21)

power = True

def toggleDisplayPower():
        global power
        if power == True:
                power = False
                backlight.power = False
        else:
                power = True
                backlight.power = True
        time.sleep(1)

button.when_pressed = toggleDisplayPower

pause()