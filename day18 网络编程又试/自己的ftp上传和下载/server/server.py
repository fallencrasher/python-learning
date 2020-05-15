import hashlib
import time
import os
import struct
import socketserver
import json


class Myserver(socketserver.BaseRequestHandler):

	def handle(self):
		conn = self.request

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
							conn.send('登录成功,请输入文件名。'.encode('utf-8'))
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
			username = login()
			# conn.send('请输入文件名'.encode('utf-8'))
			while True:
				if username:
					# m_len = conn.recv(4)
					# judge_len = struct.unpack('i',m_len)[0]
					judge = conn.recv(10).decode('utf-8')
					print(judge)
					if judge == '1':
						# 上传
						pass
					elif judge == '2':
						# 下载
						dirlist = json.dumps(os.listdir(
							r'D:\programming_with_python\043从零开始学python\day18\ftp上传和下载\server\database')).encode(
							'utf-8')
						# dirlist_len = struct.pack('i',len(dirlist))
						# conn.send(dirlist_len)
						conn.send(dirlist)
						filename = conn.recv(1024).decode('utf-8')
						if filename.lower() == 'q':
							break
						elif os.path.exists(filename):
							filesize = os.path.getsize(filename)
							filesize_len = struct.pack('i', filesize)
							conn.send(filesize_len)
							while filesize > 0:
								with open(filename, encoding='utf-8') as f:
									temp = f.read(1024)
									filesize -= len(temp)
									conn.send(temp)
						else:
							conn.send('文件不存在！'.encode('utf-8'))
				else:
					conn.send('请登录！'.encode('utf-8'))
					judge = conn.recv(1024).decode('utf-8')
					if judge.lower() == 'q':
						break
					else:
						continue
			conn.close()


server = socketserver.ThreadingTCPServer(('127.0.0.1', 43), Myserver)
server.serve_forever()


