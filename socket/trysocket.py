#!/usr/bin/python

import RPi.GPIO as GPIO
import socket
HOST='192.168.0.106'
PORT=5002
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr=s.accept()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print 'Connected by', addr
GPIO.setmode(GPIO.BCM)
GPIO.setup(04, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
while True:
    if GPIO.input(4):
        if not GPIO.input(17):
                if not GPIO.input(27):
                        conn.send('0')
                else:
                        conn.send('1')
        elif GPIO.input(17):
                if not GPIO.input(27):
                        conn.send('2')
                else:
                        conn.send('3')
    elif (GPIO.input(04)==False):
        conn.send('5')
s.close()
