import socket
import struct
import hashlib
import os
import json
import time

sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()


def login():
	def register():
		'''
		注册
		'''
		count = 0
		while count < 4:
			conn.send('请输入注册用户名：'.encode('utf-8'))
			username = conn.recv(1024).decode('utf-8')
			print(username)
			conn.send('请输入注册密码：'.encode('utf-8'))
			password = conn.recv(1024).decode('utf-8')

			with open('user_msg.txt', encoding='utf-8', mode='r') as f1, open('user_msg.txt', encoding='utf-8',
			                                                                  mode='a') as f2:
				lst1 = []
				for line in f1:
					lst1.append(line.strip().split('|')[0])
				if username.strip() not in lst1:
					md5 = hashlib.md5()
					md5.update(username.encode('utf-8'))
					md5.update(password.encode('utf-8'))
					ret = md5.hexdigest()
					f2.write(username + '|' + ret + '\n')
					# f2.write(username + '\n')
					conn.send(f'{username},恭喜您，注册成功！即将返回主界面！请登陆！'.encode('utf-8'))
					time.sleep(0.5)
					return True
				elif username.strip() in lst1:
					count += 1
					conn.send(f'用户名已存在！请重新注册。你还有{3 - count}次注册机会。'.encode('utf-8'))
					time.sleep(0.5)

	'''
	登录
	'''
	count = 0
	while count < 4:
		conn.send('请输入用户名：'.encode('utf-8'))
		print('111111')
		username = conn.recv(1024).decode('utf-8')
		print(username)
		conn.send('请输入密码：'.encode('utf-8'))
		password = conn.recv(1024).decode('utf-8')
		md5 = hashlib.md5()
		md5.update(username.encode('utf-8'))
		md5.update(password.encode('utf-8'))
		ret = md5.hexdigest()
		with open('user_msg.txt', encoding='utf-8') as f:
			l = []
			for i in f:
				l.append(i.strip().split('|')[0])
				if i.strip().split('|')[0] == username and i.strip().split('|')[1] == ret:
					conn.send('登录成功'.encode('utf-8'))
					return username
			else:
				if username not in l:
					count += 1
					conn.send('不存在用户{},请注册！请按回车键'.format(username).encode('utf-8'))
					register()
				else:
					count += 1
					conn.send(f'用户名或密码错误！请重新登陆！你还有{3 - count}次机会。'.encode('utf-8'))
					time.sleep(0.6)




while True:

	database = r'D:\programming_with_python\043从零开始学python\day18\ftp上传和下载\server\database'
	while True:
		conn,addr = sk.accept()
		username = login()
		while True:
			try:
				# 1 收 判断要上传还是下载
				judge = conn.recv(2).decode('utf-8')
				if judge=='1': #上传
					# 2,3 收 文件头信息，包括文件名和文件大小
					fileheader_len = conn.recv(4)
					fileheader_len = struct.unpack('i',fileheader_len)[0]
					fileheader = json.loads(conn.recv(fileheader_len).decode('utf-8'))
					print(fileheader)
					with open(os.path.join(database,fileheader['filename']),'wb') as f:
						while fileheader['filesize']>0:
							# 4.收 文件内容
							temp = conn.recv(1024)
							fileheader['filesize'] -= len(temp)
							print(fileheader['filesize'])
							f.write(temp)
				elif judge=='2': #下载
					#
					try:
						dirlist_o = os.listdir(database)
						dirlist_o = json.dumps(dirlist_o).encode('utf-8')
						# 1 发 可下载文件列表
						conn.send(dirlist_o)
						# 1 收 要下载的文件名
						filename_down = conn.recv(1024).decode('utf-8')
						print('filename_down:',filename_down)
						filesize = os.path.getsize(os.path.join(database, filename_down))
						print('filesize:',filesize)
						dic = {'filename': filename_down, 'filesize': filesize}
						dic = json.dumps(dic).encode('utf-8')
						m_dic = struct.pack('i', len(dic))
						print('m_xic',m_dic)
						# 2,3 发 文件头信息
						conn.send(m_dic)
						conn.send(dic)
						print("m_dic",m_dic)
						with open(os.path.join(database,filename_down),'rb') as f:
							while filesize > 0:
								temp = f.read(1024)
								filesize -= len(temp)
								# 4. 发 文件内容
								conn.send(temp)
						conn.close()
						break
					except Exception:
						break
				elif judge.lower()=='q':
					break

			except Exception:
				continue
		conn.close()

sk.close()

