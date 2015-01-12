#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os

def buttonEventHandler(pin):
    print "handling button event"
    # give terminating command 
    time.sleep(1)
    os.system("^C")
    


def main():

    # tell the GPIO module that we want to use the 
    # chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # Configuring PINS to be input/output
    GPIO.setup(2,GPIO.IN)
    GPIO.setup(3,GPIO.IN)
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)
    
    GPIO.output(25,True)
    GPIO.add_event_detect(23,GPIO.FALLING)
    GPIO.add_event_callback(23,buttonEventHandler)
    while True:
        if GPIO.input(2):
             # the button is being pressed, so turn on the green LED
             # and turn off the red LED
             GPIO.output(4,True)
	     os.system("date")
             print "button true"
        else:
             # the button isn't being pressed, so turn off the green LED
             # and turn on the red LED
             GPIO.output(4,False)
             print "button false"	
	        
	
        time.sleep(0.5)

    print "button pushed"

    GPIO.cleanup()



if __name__=="__main__":
    main()

