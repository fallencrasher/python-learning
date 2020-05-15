import socket
import hashlib

sk = socket.socket()

sk.connect(('127.0.0.1',43))

yanzheng = sk.recv(1024)

sha = hashlib.sha1(b'043')
sha.update(yanzheng)
ret = sha.hexdigest().encode('utf-8')

sk.send(ret)

msg = sk.recv(1024)
print(msg)