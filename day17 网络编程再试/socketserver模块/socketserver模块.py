# socketserver 模块 基于 socket 模块
# 处理并发的tcp协议客户端请求
import time
import socketserver

class Myserver(socketserver.BaseRequestHandler):
	def handle(self):
		conn = self.request
		while True:
			try:
				content = conn.recv(1024).decode('utf-8')
				conn.send(content.upper().encode('utf-8'))
				time.sleep(0.5)
			except ConnectionResetError:
				break

server = socketserver.ThreadingTCPServer(('127.0.0.1',43),Myserver)
server.serve_forever()

