import socket

sk = socket.socket()

sk.connect(('127.0.0.1',43))


while True:
	msg = sk.recv(1024).decode('utf-8')
	print(msg)
	if msg.upper()=='Q':
		break
	send_msg = input('>>>')
	sk.send(send_msg.encode('utf-8'))
	if send_msg.upper()=='Q':
		break

sk.close()