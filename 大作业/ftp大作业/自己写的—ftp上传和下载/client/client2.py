import socket
import struct
import hashlib
import os
import json

sk = socket.socket()
sk.connect(('127.0.0.1', 43))

while True:
    while True:
        msg = sk.recv(1024).decode('utf-8')
        print(msg)
        if msg=='登录成功':break
        temp = input('>>>')
        sk.send(temp.encode('utf-8'))

    while True:
        judge = input('1.上传  2.下载（输入序号）')
        if judge.isdigit() and int(judge) in (1, 2):
            if judge == '1':  # 上传
                # 1 发 要上传还是下载
                sk.send(judge.encode('utf-8'))
                filename = input('输入上传文件的绝对路径：')
                filesize = os.path.getsize(filename)
                dic = {'filename': os.path.basename(filename), 'filesize': filesize}
                dic = json.dumps(dic).encode('utf-8')
                m_dic = struct.pack('i', len(dic))
                # 2,3 发 文件头信息
                sk.send(m_dic)
                sk.send(dic)
                with open(filename, 'rb') as f:
                    while filesize > 0:
                        temp = f.read(1024)
                        filesize -= len(temp)
                        # 4. 发 文件内容
                        sk.send(temp)
            elif judge == '2':  # 下载
                # 1 发 告知服务端要下载
                sk.send(judge.encode('utf-8'))
                # 1 收 接收可下载文件的列表
                dirlist = json.loads(sk.recv(1024).decode('utf-8'))
                print(dirlist)
                filename_down = input('请输入要下载的文件名：').strip()
                # 2 发 要下的文件名
                sk.send(filename_down.encode('utf-8'))
                # 2,3 收 文件头信息
                fileheader_len = sk.recv(4)
                fileheader_len = struct.unpack('i',fileheader_len)[0]
                fileheader = json.loads(sk.recv(fileheader_len))
                print(fileheader)
                with open(fileheader['filename'],'wb') as f:
                    # 4.收 文件内容
                    temp = sk.recv(1024)
                    fileheader['filesize'] -= len(temp)
                    print(fileheader['filesize'])
                    f.write(temp)
                    break




        elif judge.lower() == 'q':
            break
        else:
            continue

    break
sk.close()

