import socket

sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

while True:
	conn,addr = sk.accept()
	print('conn:',conn)
	while True:
		msg = conn.recv(1024).decode('utf-8')
		print(msg)
		if msg.upper()=='Q':
			break
		send_msg = input('>>>')
		conn.send(send_msg.encode('utf-8'))
		if send_msg.upper()=='Q':
			break
	conn.close()

sk.close()