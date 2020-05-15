import socket
import struct
import json

sk = socket.socket()

sk.connect(('127.0.0.1',43))

while True:
	# _ip = input('请输入服务端ip：').strip()
	# _port = input('请输入服务端口：').strip()
	# if _ip.lower()=='q' or _port.lower()=='q':break
	# sk.connect((_ip,int(_port)))
	# username = input('登录用户名：')
	while 1:
		# 告诉服务端想要上传还是下载
		# judge = input('1.上传文件 or 2.下载文件(输入序号)：')
		# if not (judge.isdigit() and int(judge) in (1,2)):break
		# m_len = struct.pack('i',len(judge.encode('utf-8')))
		# sk.send(m_len)
		# 告知服务端，我们要下载还是上传
		sk.send(judge.encode('utf-8'))
		if judge=='1':
			pass
		elif judge=='2':
			# 下载
			# dirlist_len = sk.recv(4)
			# dirlist_len = struct.unpack('i',dirlist_len)[0]
			dirlist = json.loads(sk.recv(100).decode('utf-8'))
			print(dirlist)
			filename_down = input('想要下载的文件名称：').strip()
			sk.send(filename_down.encode('utf-8'))
			filesize_len = sk.recv(4)
			filesize_len = struct.unpack('i',filesize_len)[0]
			filesize = sk.recv(filesize_len)

			with open(filename_down, 'wb') as f:
				while filesize > 0:
					content = sk.recv(1024)
					filesize -= len(content)
					f.write(content)

sk.close()