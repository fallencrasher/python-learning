import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',43))

while True:
	msg,addr = sk.recvfrom(1024)
	print(msg.decode('utf-8'))
	#if msg.upper()=='Q':break
	sk.sendto(msg)
	#if send_msg.upper()=='Q':break