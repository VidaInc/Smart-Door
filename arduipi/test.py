#!/usr/bin/env python
# LED with 560 Ohm resistor on Pin 10 to GND
# Tony Goodhew - 10 May 2013
#from nanpy import ArduinoApi
import time,sys,serial
#from nanpy import SerialManager
#time.sleep(2)
#version
#connection = SerialManager()
serp = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.1)
time.sleep(2)
ser.writelines('1234567890')
time.sleep(2)
print(ser.readline())


#print"Starting"
#a = ArduinoApi(connection = connection)
#a.pinMode(13, a.OUTPUT)
#a.digitalWrite(13, a.HIGH)
#time.sleep(1)
#print"done"
