import socket
import hmac


sk = socket.socket()

sk.connect(('127.0.0.1',43))

rand = sk.recv(1024)

h = hmac.new(b'043',rand)
ret_client = h.digest()

sk.send(ret_client)

msg = sk.recv(1024)
print(msg)