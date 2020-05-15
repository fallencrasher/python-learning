import socket
import json
import struct
#接收
sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

conn,addr = sk.accept()
#避免粘包
msg_len = conn.recv(4)
dic_len = struct.unpack('i',msg_len)[0]
#############
msg = conn.recv(dic_len).decode('utf-8')
msg = json.loads(msg)
print(msg)

with open(msg['filename'],'wb') as f:
	while msg['filesize']>0:
		content = conn.recv(1024)
		msg['filesize'] -= len(content)
		f.write(content)


conn.close()
sk.close()