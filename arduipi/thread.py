import threading 
import sys
import serial
import time 

def connect (): 
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.1)
    time.sleep(1)
def in_out ():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 0.1)
    time.sleep(1)
    ser.write('1')
    print("sent stuff to arduino")
    print (ser.readline())
    print("reading")
    #print(serial_line)
    time.sleep(0.1)
t1 = threading.Thread(target=connect)
t2 = threading.Thread(target=in_out)
t1.start()
t2.start()
