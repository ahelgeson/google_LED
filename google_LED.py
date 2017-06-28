#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  google_LED.py
#
# Python program to sequentially turn on 8 LEDs
# connected to GPIO 18, 23, 24, 25, 12, 16, 17, and 27
# until the word 'Google' is spelled, and then turn them off
# and reverse the procedure
 
# Import the modules used in the script
import time
import RPi.GPIO as GPIO
 
# Define Constants
RUNNING = True
led_list = [18, 23, 24, 25, 12, 16, 17, 27]
 
# Configure the GPIO to BCM numbering scheme and set pins to output mode
GPIO.setmode(GPIO.BCM)
for x in range(0, 8):
    GPIO.setup(led_list[x], GPIO.OUT)
    GPIO.output(led_list[x], GPIO.LOW)
 
print("Begin flashing Google sequence.")
print("Press CTRL + C to quit.")
 
# Main loop
try:
    while RUNNING:
        for x in range(0, 8):
            GPIO.output(led_list[x], GPIO.HIGH)
        for x in range(7, 0, -1):
            GPIO.output(led_list[x], GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(led_list[x], GPIO.LOW)
 
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"
 
# Actions under 'finally' will always be called
# regardless of what stopped the program
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    GPIO.cleanup()