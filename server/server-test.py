# quick server connection test. attempts to connect to local host 

import socket
import time
import os

sock = socket.socket()

# eth0 IP
f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
host = f.read().strip()
f.close()

print('Hostname: ',host)
address = (host, 9999)
sock.connect(address)

sock.send('Hello from client')
#data = sock.recv(1024)
time.sleep(10)
sock.close()
