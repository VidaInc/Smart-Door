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
    # PIN2 is the vibration sensor 
    GPIO.setup(2,GPIO.IN)
    # PIN3 is presence sensor 
    GPIO.setup(3,GPIO.IN)
    # PIN4 is LED control
    GPIO.setup(4,GPIO.OUT)
    # PIN17 is Transister control 1 
    GPIO.setup(17,GPIO.OUT)
    # PIN27 is Transister control 2
    GPIO.setup(27,GPIO.OUT)
    # PIN22, 10, 9 are pins without sensors attached. 
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(10,GPIO.IN)
    GPIO.setup(9,GPIO.OUT)
    
    # Access card sensor PINS
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(20,GPIO.IN)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(7,GPIO.IN)
    GPIO.setup(8,GPIO.OUT)
 
    
    # GPIO.add_event_detect(23,GPIO.FALLING)
    # GPIO.add_event_callback(23,buttonEventHandler)
    while True:
        if GPIO.input(2):
             # the button is being pressed, so do whatever, should be that
             # raspberry pi will turn off, or enter standby 
             # and turn off the red LED
             GPIO.output(4,True)
	     GPIO.output(17,True)
             # The following line calls bash functions. 
	     # os.system("date")
             print "button true"
        else:
             # the button isn't being pressed, so turn off the green LED
             # and turn on the red LED
             GPIO.output(4,False)
	     GPIO.output(17,False)
             print "button false"	
	        
	
        time.sleep(0.1)

    GPIO.cleanup()



if __name__=="__main__":
    main()

