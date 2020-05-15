import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1',43))


print(sk.recv(1024).decode('utf-8'))
username = input('>>>')
sk.send(username.encode('utf-8'))
print(sk.recv(1024).decode('utf-8'))
password = input('>>>')
sk.send(password.encode('utf-8'))

login_code = sk.recv(1024).decode('utf-8')
flag = True
if login_code.isdigit() and int(login_code) == 100:
	print('登陆成功')
elif login_code.isdigit() and int(login_code) == 101:
	print('登陆失败')
	flag = False

while flag:
	sk.send(b'hello')
	msg = sk.recv(1024).decode('utf-8')
	print(msg)
	time.sleep(0.5)
else:
	sk.close()

