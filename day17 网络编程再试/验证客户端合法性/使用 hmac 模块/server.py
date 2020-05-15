# 生成一个随机字符串
# 密钥定为  043
import os
import hmac
import socket



sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

conn,addr = sk.accept()

rand = os.urandom(32)

h = hmac.new(b'043',rand) #生成一个 参数长度 的随机字符串,并转换为加密二进制
ret_server = h.digest()


conn.send(rand)


ret_client = conn.recv(1024).decode('utf-8')

if ret_client==ret_server:
	print('是合法的客户端')
	conn.send(b'hello')
else:
	conn.close()
