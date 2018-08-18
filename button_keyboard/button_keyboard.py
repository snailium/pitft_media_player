#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 12)
import uinput

#      +--------------------------------+
#      |                                |
#   #4 |                      #5        |
#      |                                |
#      |                      #24       |
#      |                                |
#      |                      #22       |
#      |                                |
#  #17 |                      #23       |
#      |                                |
#      +--------------------------------+
#
keymap = {  4: uinput.KEY_UP,     # UP       button (on the side)
           17: uinput.KEY_DOWN,   # DOWN     button (on the side)
            5: uinput.KEY_ESC,    # CROSS    button (on the front)
           24: uinput.KEY_P,      # TRIANGLE button (on the front)
           22: uinput.KEY_S,      # SQUARE   button (on the front)
           23: uinput.KEY_ENTER } # CIRCLE   button (on the front)

device = uinput.Device(keymap.values())


GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
for pin in keymap.keys():
    GPIO.setup(pin,  GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO4 as input

# Define a threaded callback function to run in another thread when events are detected
def my_callback(pin):
    print("FALLING edge detected on ", pin)
    device.emit_click(keymap[pin])

# when a changing edge is detected on port 25, regardless of whatever 
# else is happening in the program, the function my_callback will be run
for pin in keymap.keys():
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=my_callback, bouncetime=200)

try:
    sleep(30)         # wait 30 seconds
    print ("Time's up. Finished!")

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
