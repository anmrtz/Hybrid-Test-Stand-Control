# quick server connection test. attempts to connect to local host 

import socket
import time

sock = socket.socket()
host = socket.gethostname()
print('Hostname: ',host)
address = (host, 9999)
sock.connect(address)

sock.send('Hello from client')
#data = sock.recv(1024)
time.sleep(5)
sock.close()