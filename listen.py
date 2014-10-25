#!/bin/python
import socket
import sys
import os
HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'SOCKET CREATED'

try: 
    s.bind((HOST, PORT))
except socket.error , msg: 

    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'
s.listen(10)
print 'Socket now listening'
#wait to accept a connection - blocking call
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data:
        break
    if data == '1': 
	# we write out to a file to let other scripts know. 
        os.system("cat open > /home/pi/doorstatus")
    else: 
	os.system("cat close > /home/pi/doorstatus")

    conn.sendall(reply)
conn.close()
s.close()

