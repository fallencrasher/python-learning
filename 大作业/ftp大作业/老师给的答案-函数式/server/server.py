import os
import sys
import json
import struct
import socket
import hashlib

def my_send(conn,dic):
    str_dic = json.dumps(dic)
    b_dic = str_dic.encode('utf-8')
    mlen = struct.pack('i',len(b_dic))
    conn.send(mlen)
    conn.send(b_dic)

def my_recv(conn):
    msg_len = conn.recv(4)
    dic_len = struct.unpack('i',msg_len)[0]
    msg = conn.recv(dic_len).decode('utf-8')
    msg = json.loads(msg)
    return msg

def get_md5(username,password):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def login(conn):
    flag = True
    while flag:
        msg = my_recv(conn)
        print(msg['username'], msg['password'])
        with open('userinfo') as f:
            for line in f:
                name,pwd = line.strip().split('|')
                print(name,pwd)
                print(msg['username'],msg['password'])
                if name==msg['username'] and pwd ==get_md5(name,msg['password']):
                    res,flag = True, False
                    break
            else:
                res = False
            dic = {'operate':'login','result':res}
            my_send(conn,dic)


def download(conn):
    database = r'D:\programming_with_python\043从零开始学python\大作业\老师给的答案-函数式\server\database'
    dirlist = os.listdir(database)
    my_send(conn,dirlist)
    file2down = my_recv(conn)
    file2down_abs_path = os.path.join(database,file2down)
    if not os.path.exists(file2down_abs_path): conn.send(b'101')
    else:
        # filename = os.path.basename(abs_path)
        filesize = os.path.getsize(file2down_abs_path)
        dic = {'filename':file2down,'filesize':filesize}
        my_send(conn,dic)
        with open(file2down_abs_path,mode='rb') as f:
            while filesize>0:
                content = f.read(1024)
                filesize -= len(content)
                conn.send(content)

def upload(conn):
    msg = my_recv(conn)
    with open(msg['filename'],'wb') as f:
        while msg['filesize'] > 0:
            content = conn.recv(1024)
            msg['filesize'] -= len(content)
            f.write(content)





# 主逻辑
# 1.链接

sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

conn,addr = sk.accept()

# 2.当有客户端来连接我，要先进行登录
login(conn)

# 3 上传下载
opt_dic = my_recv(conn)
if hasattr(sys.modules[__name__],opt_dic['operate']):
    getattr(sys.modules[__name__],opt_dic['operate'])(conn)