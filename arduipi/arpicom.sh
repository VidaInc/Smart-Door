#!/bin/bash

# test variable 
echo "$1" 
# this bash script is used to send commandline arguements to arduino
# from raspberry pi 


# setup 

stty -F /dev/ttyUSB0 cs8 115200 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke nofish -ixon -crtscts

# sending message to arduino 
echo "$1" > /dev/ttyUSB0

