#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @common.author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/17 0017 19:48
# @File : src.py
# @Software : PyCharm


'''
博客系统
'''
import os
import hashlib
import time
import collections
import shutil
from conf import settings
from lib import common
BATH_PATH = os.path.dirname(os.path.dirname(__file__))
status_dic = {
    'username': None,
    'status': False
}





def register():
    '''
    a.用户名、密码要记录在文件中
    b.用户名要求：只能含有字母或者数字，不能含有特殊字符并且确保用户明唯一
    c.密码要求：长度要在 6~14 个字符之间
    d.超过三册登陆还未成功则退出整个程序
    '''
    count = 0
    while count < 4:
        username = input('请输入用户名(只能含有字母或者数字，不能含有特殊字符)：')
        password = input('请输入密码(长度要在 6~14 个字符之间)：')
        if username.strip().isalnum():
            with open(settings.USER_NAME, encoding='utf-8', mode='r') as f1, open(settings.USER_NAME, encoding='utf-8',
                                                                                  mode='a') as f2:
                lst1 = []
                for line in f1:
                    lst1.append(line.strip())
                if username.strip() not in lst1 and (len(password.strip()) >= 6 and len(password.strip()) <= 14):
                    with open(settings.USER_MSG, encoding='utf-8', mode='a') as f3:
                        md5 = hashlib.md5()
                        md5.update(username.encode('utf-8'))
                        md5.update(password.encode('utf-8'))
                        ret = md5.hexdigest()
                        f3.write(ret + '\n')
                        f2.write(username + '\n')
                        print(f'{username},恭喜您，注册成功！即将返回主界面！请登陆！')
                        time.sleep(0.5)
                        return True
                elif username.strip() in lst1:
                    count += 1
                    print(f'用户名已存在！请重新注册。你还有{3 - count}次注册机会。')
                    time.sleep(0.5)
                elif len(password.strip()) < 6 and len(password.strip()) > 14:
                    count += 1
                    print(f'密码不符合要求！密码长度要在 6~14 个字符之间。请重新注册。你还有{3 - count}次注册机会。')
        else:
            count += 1
            print(f'用户名不符合要求。只能含有字母或者数字，不能含有特殊字符。请重新注册。你还有{3 - count}次注册机会。')


def login():
    '''
    a.用户输入用户名、密码进行登陆验证
    b.登录成功后，才可以访问 3~7 选项，如果没有登陆或者登陆不成功时访问3-7选项，不允许访问，让其先登录。（装饰器）
    '''

    count = 0
    while count < 4:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        with open(settings.USER_NAME, encoding='utf-8', mode='r') as f1:
            # lst1 = []
            # for line in f1:
            #     lst1.append(line.strip())
            # if username.strip() in lst1: #是否存在用户名
            md5 = hashlib.md5()
            md5.update(username.encode('utf-8'))
            md5.update(password.encode('utf-8'))
            ret = md5.hexdigest()
            with open(settings.USER_MSG, encoding='utf-8', mode='r') as f2:
                # lst2 = []
                # for line in f2:
                #     lst2.append(line.strip())
                for line in f2:
                    if line.strip() == ret:
                        print('登陆成功！')
                        print(username)
                        global status_dic
                        status_dic['username'] = username.strip()
                        status_dic['status'] = True
                        # print(status_dic)
                        return True
                else:
                    count += 1
                    print(f'用户名或密码错误！请重新登陆！你还有{3 - count}次机会。')
                    time.sleep(0.6)
        # else:
        #     count += 1
        #     print(f'不存在该用户!请先注册！你还有{3 - count}次机会。')
        #     time.sleep(0.6)


@common.auth
def log_out():
    count = 0
    while count < 4:
        judge = input('确定要注销吗?(yes/no):')
        if judge.strip() == 'yes':
            global status_dic
            status_dic['username'] = None
            status_dic['status'] = False
            print('注销成功！返回主界面！')
            time.sleep(0.6)
            return False
        elif judge.strip() == 'no':
            print("即将返回主界面")
            time.sleep(0.6)
            return True
        else:
            count += 1
            print(f'请输入 yes/no !你还有{3 - count}次机会。')


def copyFiles(sourceDir, username, file):
    targetDir = os.path.join(os.path.dirname(__file__), username)
    sourceFile = os.path.join(sourceDir, file)
    targetFile = os.path.join(targetDir, file)
    if os.path.isfile(sourceFile):
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        if not os.path.exists(targetFile) or (
                os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
    else:
        return False


@common.auth
def article():
    '''
    a.提示欢迎 xxx 进入文章页面
    b.此时用户可以选择：直接写入内容，还是导入 .md 文件
            - 如果选择直接写入内容：让他直接写入文件明|文件内容......最后创建一个文章
            - 如果选择导入 .md 文件：让用户输入已经准备好的 .md 文件的文件路径(相对路径即可:比如函数的进阶.md),然后将此 .md 文件的全部内容写入文章(函数的进阶.txt)中
    '''
    print(f"欢迎{status_dic['username']}来到文章页面")
    count = 0
    while count < 4:
        judge = input('想直接写还是导入.md 文件?(1.直接写，2.导入.md文件）:')
        if judge.isdigit() and int(judge) in (1, 2):
            if int(judge) == 1:
                content = input('请开始你的表演：(文件名|文件内容):\n')
                c = collections.Counter(content)
                if c['|'] < 1:
                    count += 1
                    print(f'写入格式错误，正确格式是:(文件名|文件内容).你还有{3 - count}次机会。')
                elif c['|'] >= 1:
                    content_lst = content.split('|', 1)
                    file_name = content_lst[0]
                    file_content = content_lst[1]
                    targetDir = os.path.join(BATH_PATH, 'user', status_dic['username'])
                    print(targetDir)
                    if not os.path.exists(targetDir):
                        os.makedirs(targetDir)
                    lst1 = []
                    for file in os.listdir(targetDir):
                        lst1.append(file)
                    if file_name in lst1:
                        count += 1
                        print(f"已存在相同名称文章！请重新写入！你还有{3 - count}次机会。")
                    else:
                        targetFile = os.path.join(targetDir, file_name)
                        with open(targetFile, encoding='utf-8', mode='w') as f:
                            f.write(file_content)
                            print('写入成功')
                        return True

            elif int(judge) == 2:
                file_dir = input("请输入您文件的绝对路径(包含文件名)：\n")
                judge_if_file = os.path.isfile(file_dir)
                if judge_if_file == True:
                    sourceDir = os.path.split(file_dir)[0]
                    file_name = os.path.split(file_dir)[-1]
                    targetDir = os.path.join(BATH_PATH, 'user', status_dic['username'])
                    print(targetDir)
                    if not os.path.exists(targetDir):
                        os.makedirs(targetDir)
                    lst1 = []
                    for file in os.listdir(targetDir):
                        lst1.append(file)
                    if file_name in lst1:
                        count += 1
                        print(f"已存在相同名称文章！请重新写入！你还有{3 - count}次机会。")
                    else:
                        shutil.copy(file_dir, targetDir)
                        print('上传成功')
                        return True
                    # if copyFiles(sourceDir, username, file_name):
                    #     print('上传成功！')
                    #     return True
                else:
                    print("原文件不存在！请重新上传！")
                    count += 1


@common.auth
def dariy():
    print(f"欢迎{status_dic['username']}来到日记页面,再见！")
    time.sleep(1)


@common.auth
def collection():
    print(f"欢迎{status_dic['username']}来到收藏界面,再见！")
    time.sleep(1)


@common.auth
def comment():
    print(f"欢迎{status_dic['username']}来到评论界面,再见！")
    time.sleep(1)


# def _quit():
#     print('博客园系统将退出。')
#     time.sleep(0.5)


dic_functions = {
    1: login,
    2: register,
    3: article,
    4: comment,
    5: dariy,
    6: collection,
    7: log_out,
}


def run():
    while True:
        print('欢迎来到博客园！')
        judge = input(
            '''
1.	登录
2.	注册
3.	进入文章页面
4.	进入评论页面
5.	进入日记页面
6.	进入收藏页面
7.	注销账号
8.	退出整个程序
请选择要进行的操作(输入序号！)
: '''
        )
        if judge.isdigit() and int(judge) in (1, 2, 3, 4, 5, 6, 7):
            dic_functions[int(judge)]()
        elif judge.isdigit() and int(judge) == 8:
            print('博客园系统将退出。')
            time.sleep(0.5)
            break
            # if int(judge) == 1:
            #     global uname
            #     uname = login()
            #
            # elif int(judge) == 2:  # 注册
            #     register()
            # elif int(judge) == 3:
            #     global status_dic
            #     article(uname)
            # elif int(judge) == 4:
            #     comment(uname)
            # elif int(judge) == 5:
            #     dariy(uname)
            # elif int(judge) == 6:
            #     collection(uname)
            # elif int(judge) == 7:
            #     del_account(uname)
            # elif int(judge) == 8:
            #     print('博客园系统将退出。')
            #     time.sleep(0.5)
            #     break
        else:
            print("输入错误！只能输入序号！系统将回到初始界面")

# if __name__ == '__main__':

# main()
