#!/usr/bin/env python2.7
# demo of "BOTH" bi-directional edge detection
# script by Alex Eames https://raspi.tv
# https://raspi.tv/?p=6791

import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 12)

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(28, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set GPIO25 as input (button)

# Define a threaded callback function to run in another thread when events are detected
def my_callback(channel):
    print "FALLING edge detected on ", channel

# when a changing edge is detected on port 25, regardless of whatever 
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(2, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(3, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(4, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(5, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(7, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(8, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(9, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(10, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(11, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(13, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(14, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(15, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(19, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(20, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(21, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(27, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(28, GPIO.FALLING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(29, GPIO.FALLING, callback=my_callback, bouncetime=200)

print "Program will finish after 30 seconds or if you press CTRL+C\n"
print "Make sure you have a button connected, pulled down through 10k resistor"  
print "to GND and wired so that when pressed it connects"  
print "GPIO port 25 (pin 22) to GND (pin 6) through a ~1k resistor\n"  
  
print "Also put a 100 nF capacitor across your switch for hardware debouncing"  
print "This is necessary to see the effect we're looking for"  
raw_input("Press Enter when ready\n>")  
  
try:  
    print "When pressed, you'll see: FALLING Edge detected on 25"  
    print "When released, you'll see: Falling Edge detected on 25"  
    sleep(30)         # wait 30 seconds  
    print "Time's up. Finished!"  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
