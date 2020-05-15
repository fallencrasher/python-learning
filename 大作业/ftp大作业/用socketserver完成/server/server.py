import os
import sys
import json
import struct
import socket
import hashlib
import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while 1:
            try:
                # 登录
                self.login(conn)
                # 上传下载
                while True:
                    opt_dic = self.my_recv(conn)
                    if opt_dic['operate'] == 'download':
                        self.download(conn)
                    elif opt_dic['operate'] == 'upload':
                        self.upload(conn)
            except:
                continue


    def my_send(self,conn,dic):
        str_dic = json.dumps(dic)
        b_dic = str_dic.encode('utf-8')
        mlen = struct.pack('i',len(b_dic))
        conn.send(mlen)
        conn.send(b_dic)

    def my_recv(self,conn):
        msg_len = conn.recv(4)
        dic_len = struct.unpack('i',msg_len)[0]
        msg = conn.recv(dic_len).decode('utf-8')
        msg = json.loads(msg)
        return msg

    def get_md5(self,username,password):
        md5 = hashlib.md5(username.encode('utf-8'))
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()

    def login(self,conn):
        #def register():

        flag = True
        while flag:
            msg = self.my_recv(conn)
            print(msg['username'], msg['password'])
            with open('userinfo') as f:
                for line in f:
                    name,pwd = line.strip().split('|')
                    print(name,pwd)
                    print(msg['username'],msg['password'])
                    if name==msg['username'] and pwd ==self.get_md5(name,msg['password']):
                        res,flag = True, False
                        break
                else:
                    res = False
                dic = {'operate':'login','result':res}
                self.my_send(conn,dic)



    def download(self,conn):
        database = r'D:\programming_with_python\043从零开始学python\大作业\ftp大作业\用socketserver完成\server\database'
        dirlist = os.listdir(database)
        self.my_send(conn,dirlist)
        file2down = self.my_recv(conn)
        file2down_abs_path = os.path.join(database,file2down)
        if not os.path.exists(file2down_abs_path): conn.send(b'101')
        else:
            # filename = os.path.basename(abs_path)
            filesize = os.path.getsize(file2down_abs_path)
            dic = {'filename':file2down,'filesize':filesize}
            self.my_send(conn,dic)
            md5 = hashlib.md5()
            with open(file2down_abs_path,mode='rb') as f:
                while filesize>0:
                    content = f.read(1024)
                    md5.update(content)
                    filesize -= len(content)
                    conn.send(content)
                self.my_send(conn,md5.hexdigest())
    def upload(self,conn):
        database = r'D:\programming_with_python\043从零开始学python\大作业\ftp大作业\用socketserver完成\server\database'
        msg = self.my_recv(conn)
        file2up_abs_path = os.path.join(database, msg['filename'])
        md5 = hashlib.md5()
        with open(file2up_abs_path,'wb') as f:
            while msg['filesize'] > 0:
                content = conn.recv(1024)
                msg['filesize'] -= len(content)
                md5.update(content)
                f.write(content)
            if self.my_recv(conn)==md5.hexdigest():
                self.my_send(conn,'上传成功')
            else:
                self.my_send(conn,'文件上传错误，文件不完整。\n')

    


server = socketserver.ThreadingTCPServer(('127.0.0.1',43),Myserver)
server.serve_forever()

# 主逻辑
# 1.链接

# sk = socket.socket()
# sk.bind(('127.0.0.1',43))
# sk.listen()
#
# conn,addr = sk.accept()

# 2.当有客户端来连接我，要先进行登录
# login(conn)
#
# # 3 上传下载
# opt_dic = my_recv(conn)
# if hasattr(sys.modules[__name__],opt_dic['operate']):
#     getattr(sys.modules[__name__],opt_dic['operate'])(conn)