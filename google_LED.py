#!/usr/bin/env python
# -*- coding: utf-8 -*-
# google_LED.py
# Python program to sequentially turn on 8 LEDs connected to GPIO 18, 23, 24, 25,
# 12, 16, 17, and 27 individually at a 1/7 of a second per letter until the word
# 'Google' is spelled, and then turn them off in reverse order at 1/4 of a second.
# Import time and the RPi modules used in the script

import time
import RPi.GPIO as GPIO

# Define Variable 'RUNNING' as a boolean and set to 'True'.
RUNNING = True

# Define LED list and statically set the 6 GPIO pin numbers
led_list = [16, 25, 24, 23, 27, 17]
 
# Set the GPIO to a BCM numbering scheme and set pins to output mode
GPIO.setmode(GPIO.BCM)
for x in range(0, 6):
    GPIO.setup(led_list[x], GPIO.OUT)
    GPIO.output(led_list[x], GPIO.LOW)

print("Begin flashing Google sequence.")
print("Press CTRL + C to quit.")
 
# Main sequence loop
try:
    while RUNNING:
        for x in range(0, 6):
            GPIO.output(led_list[x], GPIO.HIGH)
            time.sleep(0.7)
        for x in range(6, 0, -1):
            time.sleep(0.25)
            GPIO.output(led_list[x], GPIO.LOW)
 
# CTRL+C will change variable 'RUNNING' to false and break the main loop.
except KeyboardInterrupt:
    RUNNING = False
    print "\Stopping"
 
# Actions under 'finally' will always be called
# regardless of what stopped the program
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()