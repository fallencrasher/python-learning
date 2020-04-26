# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-26 13:53:09
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-26 13:53:09
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-26 13:47:29
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

conn,addr = sk.accept()
conn.send(b'hello')
msg = conn.recv(1024)
print(msg)
conn.close()

sk.close()


