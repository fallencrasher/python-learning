import socketserver
import hashlib

class Myserver(socketserver.BaseRequestHandler):
	def handle(self):
		conn = self.request
		while True:
			username = self.login(conn)
			print('333333')
			while username:
				print('44444')
				msg = conn.recv(1024).decode('utf-8')
				conn.send(msg.upper().encode('utf-8'))

	def get_md5(self,username,password):
		md5 = hashlib.md5(username.encode('utf-8'))
		md5.update(password.encode('utf-8'))
		return md5.hexdigest()

	def login(self,conn):
		'''login'''
		conn.send('请输入用户名:'.encode('utf-8'))
		username = conn.recv(1024).decode('utf-8')
		conn.send('请输入密码:'.encode('utf-8'))
		password = conn.recv(1024).decode('utf-8')
		print("1111111")
		with open('userinfo') as f:
			for i in f:
				name,pwd = i.strip().split('|')
				print(name,pwd)
				print(username,password)
				if name == username and pwd == self.get_md5(username,password):
					conn.send(b'100')
					print('222222')
					return username
			else:
				conn.send(b'101')



server = socketserver.ThreadingTCPServer(('127.0.0.1',43),Myserver)
server.serve_forever()