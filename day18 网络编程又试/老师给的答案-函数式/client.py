import os
import sys
import json
import struct
import socket



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
	msg = my_recv(sk)
	with open(msg['filename'], 'wb') as f:
		while msg['filesize'] > 0:
			content = sk.recv(1024)
			msg['filesize'] -= len(content)
			f.write(content)

def upload(sk):
	opt_dic = {'operate':'upload'}
	my_send(sk,opt_dic)
	abs_path = r'D:\programming_with_python\2020老男孩\31-40\day32 课上视频\3.multiprocessing模块.mp4'
	filename = os.path.basename(abs_path)
	filesize = os.path.getsize(abs_path)
	dic = {'filename':filename,'filesize':filesize}
	my_send(sk,dic)
	with open(abs_path,mode='rb') as f:
		while filesize>0:
			content = f.read(1024)
			filesize -= len(content)
			sk.send(content)



# 1 连接
sk = socket.socket()
sk.connect(('127.0.0.1', 43))

# 2.login
login(sk)

# 上传/下载
opt_lst = ['upload', 'download']
for index, opt in enumerate(opt_lst, 1):
	print(index, opt)
num = int(input('请输入您要操作的序号：'))
if hasattr(sys.modules[__name__], opt_lst[num - 1]):
	getattr(sys.modules[__name__], opt_lst[num - 1])(sk)

sk.close()
