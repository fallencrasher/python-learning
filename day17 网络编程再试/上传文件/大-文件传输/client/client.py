import os
import socket
import json
import struct

#发送
sk = socket.socket()
sk.connect(('127.0.0.1',43))

#文件名/文件大小
abs_path = r'D:\programming_with_python\2020老男孩\21-30\day30 课上视频\2.tcp协议完成文件上传.mp4'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)
dic = {'filename':filename,'filesize':filesize}
str_dic = json.dumps(dic)
# 避免粘包##############################
b_dic = str_dic.encode('utf-8')
msg_len = struct.pack('i',len(b_dic))
sk.send(msg_len)#4个字节 表示字典的长度
###########################################
sk.send(str_dic.encode('utf-8')) # 字典本身
with open(abs_path,'rb') as f:
	while filesize>0:
		content = f.read(1024)
		filesize -= len(content)
		sk.send(content)

sk.close()