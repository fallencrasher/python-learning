import os
import sys
import json
import struct
import socket
import hashlib


def my_send(sk, dic):
	str_dic = json.dumps(dic)
	b_dic = str_dic.encode('utf-8')
	mlen = struct.pack('i', len(b_dic))
	sk.send(mlen)
	sk.send(b_dic)


def my_recv(sk):
	msg_len = sk.recv(4)
	dic_len = struct.unpack('i', msg_len)[0]
	msg = sk.recv(dic_len).decode('utf-8')
	msg = json.loads(msg)
	return msg


def login(sk):
	while True:
		usr = input('用户名：').strip()
		pwd = input('密码  ：').strip()
		dic = {'username': usr, 'password': pwd}
		my_send(sk, dic)
		ret = my_recv(sk)
		if ret['operate'] == 'login' and ret['result']:
			print('登陆成功')
			break
		else:
			print('登陆失败')


def download(sk):
	opt_dic = {'operate': 'download'}
	my_send(sk, opt_dic)
	dirlist = my_recv(sk)
	print(f'可供下载的文件有:\n{dirlist}')
	file2down = input('请选择你要下载的文件：')
	# try:
	my_send(sk, file2down)
	msg = my_recv(sk)
	filesize = msg['filesize']
	if msg == b'101':
		print('不存在该文件。')
	else:
		md5 = hashlib.md5()
		num = 0
		with open(msg['filename'], 'wb') as f:
			while msg['filesize'] > 0:
				content = sk.recv(1024)
				md5.update(content)
				msg['filesize'] -= len(content)
				f.write(content)
				num += len(content)
				process_bar(num,filesize)
			if md5.hexdigest() == my_recv(sk):
				print('下载完成\n\n')
			else:
				print('文件传输发生错误，文件不完整\n\n')
	# except:
	# 	pass


def upload(sk):
	opt_dic = {'operate': 'upload'}
	my_send(sk, opt_dic)
	abs_path = r'D:\programming_with_python\2020老男孩\31-40\day32 课上视频\3.multiprocessing模块.mp4'
	filename = os.path.basename(abs_path)
	filesize = os.path.getsize(abs_path)
	filesize2 = filesize
	dic = {'filename': filename, 'filesize': filesize}
	my_send(sk, dic)
	md5 = hashlib.md5()
	num = 0
	with open(abs_path, mode='rb') as f:
		while filesize > 0:
			content = f.read(1024)
			filesize -= len(content)
			md5.update(content)
			sk.send(content)
			num += len(content)
			process_bar(num,filesize2)
		my_send(sk,md5.hexdigest())
		print(my_recv(sk))


def process_bar(num, total):
	rate = num / total
	rate_num = int(rate * 100)
	if rate_num == 100:
		r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
	else:
		r = '\r%s>%d%%' % ('=' * rate_num, rate_num)
	print(r, flush=True, end='')


# 1 连接
sk = socket.socket()
sk.connect(('127.0.0.1', 43))

# 2.login
login(sk)

# 上传/下载
flag = True
while True:

	opt_lst = ['upload', 'download']
	for index, opt in enumerate(opt_lst, 1):
		print(index, opt)
	num = input('请输入您要操作的序号：')
	if num.isdigit() and int(num) in (1, 2):
		if hasattr(sys.modules[__name__], opt_lst[int(num) - 1]):
			getattr(sys.modules[__name__], opt_lst[int(num) - 1])(sk)
	elif num.lower() == 'q':
		# flag = False
		break
	else:
		print('指令输入有误。')
		continue

sk.close()
