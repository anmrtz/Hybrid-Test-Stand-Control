#server


import socket

#creating a socket
sock = socket.socket()
sock.bind(('', 9999))
sock.listen(1)
conn, addr = sock.accept()

#connecting
print ('connected:', addr)
conn.send(b"connected")

while True:
    data = conn.recv(1024)
    print(data.decode())
