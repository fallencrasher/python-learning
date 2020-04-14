# 看代码分析结果 @@@
# func_list = []
# for i in range(10):
#     func_list.append(lambda :i)
# print(list(func_list))
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1,v2)
# func_list = []
# for i in range(10):
#     def func():
#         print(i)
#         return i
#     func_list.append(func)
# print(i)
# print(func_list)
# print(func_list[0]())
# print(func_list[5]())
# print(func_list[9]()) 
## 解释：每一次的循环，都是把 lambda :i 这个函数计入到了列表中，但是，函数内部代码并没有执行，func_list 列表里的每一个元素
##      都是 lambda :i .当调用这些函数的时候，才会给 lambda :i 里的i进行赋值。那我们看，调用的时候，并未给他传任何参数，那这个
##      i 是谁给赋值的呢？你看，我们循环的时候不是，用 i 进行遍历的吗，实际上这就是一种赋值，我们打印一下这个 i ，是确实存在的，
##      而且他的值就是最后一次遍历后所获得的值，就是9.当我们调用 func_list 里边的 lambda :i 函数的时候，lambda :i 函数要返回 i
##      值了，那他返回的 i 值，就是在遍历中最后一次遍历的值，所以每次执行，结果都是9
# 9,9    # 就是个函数  每次调用i都等于9  所以返回的i为9

# 看代码分析结果 @@@
# func_list = []
# for i in range(10):
#     func_list.append(lambda x:x+i)
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1,v2)

# 11，10

# 看代码分析结果 @@@
# func_list = []
# for i in range(10):
#     func_list.append(lambda x:x+i) 
# print(func_list)
# 注意，这里再说一遍：上边这几行代码，把 lambda x:x+i 放进了 func_list,func_list 里边的元素，都是一样的 lambda x:x+i
# 只要没有进行调用, 那 lambda x:x+i 里边的代码就不会运行。
# 而且，要注意，此时的 i 在经历过最后一次遍历后， i=9
# for i in range(0,len(func_list)):
#     result = func_list[i](i)
#     print(result)
# 再次注意，上边这三行代码，重新将 i 进行遍历赋值，所以，此时 i 有了新的值，i 不再是刚才的 i=9了
# 所以在调用 lambda x:x+i 时，传入的是实时遍历的 i 的值，不是 i = 9


# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

# 看代码写结果（面试题）：
# def func(name):
#     v = lambda x:x+name
#     return v
# v1 = func('太白') # v1 = lambda x:x+'太白'
# v2 = func('alex') # v2 = lambda x:x+'alex'
# v3 = v1('银角') # v3 = (lambda x:x+'太白')('银角')
# v4 = v2('金角') # v4 = (lambda x:x+'alex')('金角')
# print(v1,v2,v3,v4)

# 函数地址，函数地址，银角太白，金角alex

# 看代码写结果【面试题】
# result = []
# for i in range(10):
#     func = lambda : i      # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1,v2)

# 9
# 9个函数地址
# 9,9

# 看代码分析结果【面试题】
# def func(num):
#     def inner():
#         print(num)
#     return inner
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1,v2)

# 9
# 10个函数地址
# 0
# 9
# None
# None

# 看代码写结果【新浪微博面试题】
# def func():
#     for num in range(10):
#         pass
#     v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]
#     result1 = v4[1]()
#     result2 = v4[2]()
#     print(result1,result2)
# func()

# 109,109

# 请编写一个函数实现将IP地址转换成一个整数。【面试题，较难,可以先做其他题】
# 如 10.3.9.12 转换规则为二进制：
#         10            00001010
#          3            00000011
#          9            00001001
#         12            00001100
# 再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
# 这东西是可行的，因为 255 刚好变成二进制是 11111111
#方法一：
# ip = '10.3.9.12'#input("ip:")
# ip = ip.split('.',3)
# ip2 =[]
# for i in ip:
#     _i = int(i.strip())
#     ip2.append(_i)
# print(ip2)
# ip3=list(map(bin,ip2))
# print(ip3)
# ip4 = []
# for i in range(len(ip3)):
#     temp = ip3[i].replace('0b','')
#     ip4.append(temp)
# print(ip4)
# for i in range(len(ip4)):
#     ip4[i] = '0'*(8-len(ip4[i])) + ip4[i]
# print(ip4)
# ip4 = ''.join(ip4)
# print(ip4,type(ip4))
# sum = 0
# for i in range(len(ip4)):
#     sum += int(ip4[i])*(2**(len(ip4)-i-1))
# print(sum)

#方法二：
# content = input('请输入IP地址：')
# ip_add = content.split('.')
# ip_bin = []
# for i in ip_add:
#     s2 = (8-len(bin(int(i.strip()))[2:]))*'0'+bin(int(i.strip()))[2:]
#     print(s2)
#     ip_bin.append(s2)
# s = ''
# for count in ip_bin:
#     s += count
# sum_1 = 0
# for o in range(len(s)):
#     sum_1 += int(s[o])*(2**(len(s)-o-1))
# print(sum_1)

# 都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=['oldboy','alex','wusir']
# print(list(map(lambda x:x+'_sb',name)))
# ret = map(lambda n:n + '_sb',name)
# print(list(ret))

# 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l = [{'name':'alex'},{'name':'y'}]
# print(list(map(lambda x:x['name']+'_sb',l)))

# ret = map(lambda n:n['name']+'_sb',l)
# print(list(ret))

# 用filter来处理,得到股票价格大于20的股票名字
# shares={
# 'IBM':36.6,
# 'Lenovo':23.2,
# 'oldboy':21.2,
# 'ocean':10.2,
# }
# print(list(filter(lambda a:shares[a]>20,shares)))

# ret = filter(lambda n:shares[n]>20,shares)
# print(list(ret))

# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0,......]
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# ret = map(lambda x:x['shares']*x['price'],portfolio)
# print(list(ret))


# ret = map(lambda dic:dic['shares']*dic['price'],portfolio)
# print(list(ret))

# 还是上面的字典，用filter过滤出单价大于100的股票。
# print([i['name'] for i in list(filter(lambda a:a['price']>100,portfolio))])
# ret = filter(lambda dic:dic['price']>100,portfolio)
# print(list(ret))

# 有下列三种数据类型，
# l1 = [1,2,3,4,5,6]
# l2 = ['oldboy','alex','wusir','太白','日天']
# tu = ('**','***','****','*******')
# # ​	写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）		[(3, 'wusir', ''), (4, '太白', '*******')]这样的数据。

# tu2 = [i for i in zip(list(filter(lambda x:x>2,l1)),l2,list(filter(lambda x:len(x)>=4,tu)))]
# print(tu2)
# print(filter(lambda x:x[0]>2 and len(x[-1]>=4,zip(l1,l2.tu))))

# ​	7. 有如下数据类型(实战题)：
# l1 = [ {'sales_volumn': 0},
# {'sales_volumn': 108},
# {'sales_volumn': 337},
# {'sales_volumn': 475},
# {'sales_volumn': 396},
# {'sales_volumn': 172},
# {'sales_volumn': 9},
# {'sales_volumn': 58},
# {'sales_volumn': 272},
# {'sales_volumn': 456},
# {'sales_volumn': 440},
# {'sales_volumn': 239}]
# # ​	将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# ret = sorted(l1,key=lambda a:a['sales_volumn'])
# ret2 = sorted(l1,key=lambda a:a['sales_volumn'],reverse=True)
# print(ret,ret2)




# ret = sorted(l1,key=lambda n:n['sales_volumn'])
# print(list(ret))

# 求结果(面试题)
# v = [lambda :x for x in range(10)]
# print(v)
# print(v[0])
# print(v[0]())
# def func():
#     def inner():
#         for x in range(10):
#             return x 
#     return inner

# 十个函数地址
# 一个函数地址
# 9

# 求结果(面试题)
# v = (lambda :x for x in range(10))
# print(v)
# # print(v[0])
# # print(v[0]())
# print(next(v))
# print(next(v)())

# 一个生成器内存地址
# 报错
# 报错
# 一个lambda 函数生成器地址
# 1

# map(str,[1,2,3,4,5,6,7,8,9])输出是什么? (面试题)
# print(map(str,[1,2,3,4,5,6,7,8,9]))
# #输出的是一个 map 对象生成器
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# # 求结果：（面试题，比较难，先做其他题）
# def num():
# 	return [lambda x:i*x for i in range(4)]
# print([m(2) for m in num()])

# def func(x):
#     def inner():
#         for i in range(4):
#             return i*x
#     return inner

# [6,6,6,6]

# 有一个数组[3,4,1,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数
# 的总和（上面数据的么有重复的总和为1+2=3)(面试题)
# l1 = [3,4,1,2,5,6,6,5,4,3,3]
# print(dir(l1)) #经过查看，发现列表是有 count 方法的
# def func6(lst):
#     l = []
#     sum = 0
#     for i in lst:
#         if lst.count(i)==1:
#             l.append(i)
#             sum += i
#     print(l,sum)
# func6(l1)

# mul = lambda l:sum([i for i in l if l.count(i)==1])
# print(mul(l1))

# 写一个函数完成三次登陆功能：
# 用户的用户名密码从一个文件register中取出。
# register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# 登陆成功返回True。
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

login()


# def land():
#     count = 0
#     while 1:
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         count += 1
#         with open('register.txt') as f:
#             for line in f:
#                 if username + '/' + password == line.strip():
#                     print(True)
#                     return True
#         print('用户名密码错误请重新输入！')
#         if count == 3:
#             print(False)
#             return False
# land()

# 再写一个函数完成注册功能：
# 用户输入用户名密码注册。
# 注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# 注册成功后，返回True,否则返回False。
def registe():
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
                return False
            else:
                f1.write('\n'+username+'|'+password)
                return True

registe()





# def land():
#     while 1:
#         l2 = []
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         with open('register.txt') as f,open('register.txt',mode='a') as f1:
#             for line in f:
#                 l1 = line.strip().split('/')
#                 if username == l1[0]:
#                     l2.append(username)
#                     print(False)
#                     print('用户名已存在请重新输入！')
#             if l2 == []:
#                 print('注册成功')
#                 s = '\n' + username + '/' + password
#                 f1.write(s)
#                 return True
# land()

# 用完成一个员工信息表的增删功能（选做题，有时间做，没时间周末做）。
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,太白,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
# 现在要让你实现两个功能：
# 第一个功能是实现给文件增加数据，用户通过输入姓名，年龄，电话，工作，给原文件增加数据（增加的数据默认追加到原数据最后一行的下一行），但id要实现自增（id自增有些难度，id是不需要用户输入的但是必须按照顺序增加）。
# 第二个功能是实现给原文件删除数据，用户只需输入id，则将原文件对应的这一条数据删除（删除后下面的id不变，比如此时你输入1，则将第一条数据删除，但是下面所有数据的id值不变及太白，nezha的 id不变）。

def add_message():
    with open('message.txt',encoding='utf-8',mode='r+') as f1:
        name = input('请输入名字：')
        age = input('请输入年龄：')
        phone = input('请输入电话：')
        job = input('请输入工作：')
        for line in f1:
            s= line
        count = str(int(s.strip()[0]) + 1)
        l = []
        l.append(count)
        l.append(name)
        l.append(age)
        l.append(phone)
        l.append(job)
        s1 ='\n' + ','.join(l)
        f1.write(s1)
    return

import os
def del_message():
    order = input('请输入序号：')
    with open ('message.txt',encoding='utf-8',mode='r')as f1,open('message.txt.bak',encoding='utf-8',mode='w')as f2:
        for line in f1:
            if line[0] != order.strip():
                f2.write(line)
    os.remove('message.txt')
    os.rename('message.txt.bak','message.txt')
    return
