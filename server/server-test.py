# quick server connection test

import socket
import time
import sys
import os

sock = socket.socket()

if len(sys.argv) > 1:
	host = sys.argv[1]
else:
	# eth0 IP
	f = os.popen('ip addr show eth0')
	host = f.read().split("inet ")[1].split("/")[0]
	f.close()

print('Connecting to: ' + host)
address = (host, 9999)

try:
	sock.connect(address)
	sock.send('Hello from client')
except Exception as e:
	print(e)
	sys.exit()

#data = sock.recv(1024)
time.sleep(10)
sock.close()
