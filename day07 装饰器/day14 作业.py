# 看代码写结果：
# def wrapper(f):
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         print(222)
#         return ret
#     return inner
#
# @wrapper
# def func():
#     print(333)
#
# print(444)
# func()
# print(555)

# 444
# 111
# 333
# 222
# 555

# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。
def wrapper(f):
    def inner(*args,**kwargs):
        print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
        ret = f(*args,**kwargs)
        return ret 
    return inner
@wrapper
def func2():
    print('111')

func2()





# def wrapper(f):
#     def inner():
#         print ('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         ret = f()
#         return ret

#     return inner
#
# @wrapper
# def func():
#     print (111)

# 为函数写一个装饰器，把函数的返回值 +100 然后再返回。
def wrapper2(f):
    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret + 100
    return inner 

@wrapper2
def func3():
    return 100
a = func3()
print(a)








# def wrapper(f):
#     def inner():
#         ret = f()
#         ret += 100
#         return ret
#     return inner

# @wrapper
# def func():
#     return 7
# result = func()
# print(result)

# 请实现一个装饰器，通过一次调用是函数重复执行5次。

def wrapper3(f):
    def inner(*args,**kwargs):
        for i in range(5):
            ret = f(*args,**kwargs)
        return ret
    return inner 
@wrapper3
def func4():
    print('hhhhh')
func4()




# def wrapper(f):
#     def inner():
#         for i in range(5):
#             ret = f()
#         return ret
#     return inner

# 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
# 可用代码：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
# def wrapper():
#     pass
# def func1(f):
#     print(f.__name__)
# func1(wrapper)
# # 函数名通过： 函数名.__name__获取。
import time
def wrapper4(f):
    def inner(*args,**kwargs):
        struct_time = time.localtime()
        temp_time = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
        print(temp_time,type(temp_time))
        ret = f(*args,**kwargs)
        with open('log.txt',encoding='utf-8',mode='a') as f1:
            f1.write(f.__name__ +'\t'+ temp_time + '\n')
        return ret
    return inner

@wrapper4
def func5():
    print("mohaha")
func5()



# import time
# def func1(f):
#     def inner():
#         ret = f()
#         print(f.__name__)
#         n1 = f.__name__
#         struct_time = time.localtime()
#         t1 = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
#         print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))
#         with open('时间表.txt',encoding = 'utf-8',mode = 'a')as f1:
#             f1.write(n1 + '|' + t1 + '\n')
#         return ret
#     return inner
#
# @func1
# def func():
#     print (111)
# func()

# 将课上模拟博客园登录的装饰器的认证的代码完善好，整清楚。
#登陆认证

def get_user_pwd():
    usr_dict = {}
    with open('register.txt',encoding='utf-8',mode='r') as f:
        for i in f:
            i = i.strip().split('|',1)
            usr_dict[i[0]]=i[1]
    return usr_dict


def login():
    count = 0
    dict1=get_user_pwd()
    while count<4:
        username = 'fallen' #input('username:')
        password = 'wangyishan043000' #input('password:')                
        if username not in list(dict1.keys()):
            print('您还没有注册！') 
        else:
            if dict1[username]!=password:
                print('username or password error!')
            else:
                print('login successfully!')
                return True
        count += 1

def register():
    while True:
        username =  input('username:')
        password =  input('password:')
        with open('register.txt',encoding='utf-8') as f, open('register.txt',encoding='utf-8',mode='a') as f1:
            dict1 = {}
            for i in f:
                i = i.strip().split('|',1)
                dict1[i[0]]=i[1]
            if username in list(dict1.keys()):
                print('you already have a accout!Please login.')
                login()
           
            else:
                f1.write('\n'+username+'|'+password)
                return True

status_dict = {
    'username' : None,
    'status': False,
}

def auth(f):
    '''
    你的装饰器完成：访问被装饰函数之前，写一个三次登陆认证的功能。
    登录成功，让其访问被装饰的函数；登陆不成功，不让访问
    '''
    def inner(*args,**kwargs):
        '''访问之前的操作'''
        if status_dict['status']:
            ret = f(*args,**kwargs)
            return ret
        else:
            login()
            if login():
                ret = f(*args,**kwargs)
                return ret
            else:
                print('opration error,please flash the page.')
            # username=input('username:')
            # password = input('password:')
            # if username=='fallen' and password == '123456':
            #   print('登录成功')
            #   status_dict['username']=username
            #   status_dict['status']=True
            #   ret = f(*args,**kwargs)
            #   return ret
            # else:
            #   print('登录失败')
    return inner 

@auth
def article():
    print('欢迎访问文章页面！')
article()

@auth
def comment():
    print('欢迎访问评论页面')
comment()

@auth
def dariy():
    print('欢迎访问日记页面')
dariy()


# def login():
#     count = 0
#     while 1:
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         count += 1
#         with open('register.txt') as f:
#             for line in f:
#                 if username + '/' + password == line.strip():
#                     print ('登陆成功！')
#                     return True
#         print('用户名密码错误请重新输入！')
#         if count == 3:
#             return False


status_dict = {
    'username': None,
    'status': False,
}

def auth(f):
    def inner():
        if status_dict['status']:
            ret = f()
            return ret
        else:
            count = 0
            while 1:
                username = input('请输入用户名：')
                password = input('请输入密码：')
                count += 1
                with open('register.txt') as f1:
                    for line in f1:
                        if username + '/' + password == line.strip():
                            print ('登陆成功！')
                            status_dict['username'] = username
                            status_dict['status'] = True
                            ret = f()
                            return ret
                print('用户名密码错误请重新输入！')
                if count == 3:
                    return False
    return inner

@auth  # article = auth(article)
def article():
    print('欢迎访问文章页面')
@auth
def comment():
    print('欢迎访问评论页面')
@auth
def dariy():
    print('欢迎访问日记页面')

article()
comment()
dariy()