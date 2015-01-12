#/bin/python

import socket
import sys
import os

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket, Error code: ' + str(msg[0] + ' , Error messsage: ' + msg[1]
    sys.exit(1)
print 'socket created' 
host = 'www.google.com'
port = 80
try: 
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    print 'Hostname could not be resolved'
    sys.exit(1)
print 'IP address of ' + host + 'is ' + remote_ip
message = "GET /HTTP/1.1"
try: 
    s.sendall(message)
except socket.error:
    print 'send failed'
    sys.exit(1)
print 'message sent'
