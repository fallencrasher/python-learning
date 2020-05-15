import socket

sk = socket.socket(type = socket.SOCK_DGRAM)

server = ('127.0.0.1',43)

while True:
	send_msg = input('>>>')
	sk.sendto(('fallen>>'+send_msg).encode('utf-8'),server)
	if send_msg.upper()=='Q':break
	msg = sk.recv(1024)
	print(msg.decode('utf-8'))
	if msg.upper()=='Q':break