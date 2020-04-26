# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-26 13:53:02
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-26 13:53:02
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-26 13:50:05
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

import socket

sk = socket.socket()
sk.connect(('127.0.0.1',43))

msg = sk.recv(1024)
print(msg)
sk.send(b'byebye')

sk.close()

