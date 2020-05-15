# 生成一个随机字符串
# 密钥定为  043
import os
import hashlib
import socket



sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

conn,addr = sk.accept()

ret = os.urandom(32) #生成一个 参数长度 的随机字符串
print(ret)
conn.send(ret)

sha = hashlib.sha1(b'043')
sha.update(ret)
yanzheng = sha.hexdigest()

yansheng2 = conn.recv(1024).decode('utf-8')

if yansheng2==yanzheng:
	print('是合法的客户端')
	conn.send(b'hello')
else:
	conn.close()
