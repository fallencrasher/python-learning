import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)

server = ('127.0.0.1',43)

while True:
	sk.sendto(b'hello',server)
	msg = sk.recv(1024)
	print(msg.decode('utf-8'))
	time.sleep(0.5)