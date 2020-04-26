# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-21 19:28:11
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-21 21:07:17
#!/usr/bin/env python

# sys.argv练习
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23
import sys
import shutil
import time
import os
dic = {'uid':'fallen','passwd':'123456'}




def login(username,password):
	# username = input("username:").strip()
	# password = input("password:").strip()
    if username==dic['uid'] and password==dic['passwd']:
        print('登陆成功')
        return True
    else:
        print('login failed.')
        return False
	



def cp(s_path,t_path):
    filename = os.path.basename(s_path)
    _filename = os.path.join(t_path,filename)
    shutil.copy2(s_path,_filename)
    

def rm(s_path):
    if os.path.isfile:
        os.remove(s_path)
    else:
        shutil.rmtree(s_path)
def rename(s_path,t_path):
    os.rename(s_path,t_path)
    



def main():
    
    username = sys.argv[1]
    password = sys.argv[2]
    function = sys.argv[3]
    source_path = sys.argv[4]
    target_path = sys.argv[5]
    
    if login(username,password):
        if function == 'cp':
            if os.path.exists(source_path) and os.path.exists(target_path):
                cp(source_path,target_path)
        elif function == 'rm':
            if os.path.exists(source_path):
                rm(source_path)
        elif function == 'rename':
            if os.path.exists(source_path):
                rename(source_path,target_path)
        else:
            print('NO SUCH FUNCTION!')
            time.sleep(0.6)
    else:
        print('用户名或密码错误')
    



if __name__=='__main__':
    main()