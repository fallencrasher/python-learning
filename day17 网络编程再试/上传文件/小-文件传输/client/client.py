import os
import socket
import json
#发送
sk = socket.socket()
sk.connect(('127.0.0.1',43))

#文件名/文件大小
abs_path = r'D:\programming_with_python\2020老男孩\21-30\day30 课上视频\2.tcp协议完成文件上传.mp4'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)
dic = {'filename':filename,'filesize':filesize}
str_dic = json.dumps(dic)
sk.send(str_dic.encode('utf-8'))
with open(abs_path,'rb') as f:
	content = f.read()
	sk.send(content)
sk.close()