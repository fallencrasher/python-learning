# python 基础 08 模块

声明：那么多模块，不可能都说了，一些常用的，甚至不常用的，举举例子，熟悉一下。

想要更多，可以去看 python 的官方文档，在 ../python/doc/ 目录下，或者去菜鸟教程看。

## 1.自定义模块

```python
#模块
#模块的的本质就是 .py 文件，是封装语句的最小单位
#模块注释，建议用多行注释 就是 '''  '''
#模块中出现的变量，for循环，if结构，函数定义等等豆角模块 成员

#模块的运行方式
##1.脚本方式：直接用解释器执行，或者pyCharm中右键执行
##2.模块方式（导入方式）：被其他模块导入，为导入它的模块提供资源(模块中的成员)

#自定义模块
##自定义模块被其他模块导入时，其中的可执行语句会立即执行

#python中，提供一种可以判断自定义模块是开发阶段还是使用阶段
#__name__方法:脚本方式运行时(在本身模块文件里运行)，固定返回 字符串 ‘__mian__’
#			  在别的模块里引用时，则会返回模块名字
print(__name__)

#所以，开发模块时，会在模块里加一个
#在 main() 函数里调用我们开发的方法
def main(): #这个叫测试函数，里边对模块里的方法进行测试
	pass

if __name__ == '__main__':
	main()
	
#自定义模块的使用 我们在外部定义了一个模块 a.py
import a #只有当 a.py 在当前路径或系统模块路径下才可以这么调用

print(a)  #这么这直接打印模块名字，会告诉你模块的存放路径
a.func1() #这个func1()是在 a.py 中有定义的，所以可以如此调用

#内置模块，系统自带
import time
print(time)
print(time.time()) #时间戳，格林威治时间

#系统导入模块的路径
## 内存里：如果已经导入了模块，直接就在内存里调用了
## 系统内置模块目录： ../python/python(版本号)/lib/
## 第三方模块(pip 下载): ../python/python(版本号)/lib/site-packages
## sys 模块，比较重要，嵌入在python中，不在模块列表

##查看 sys.path 内容
# import sys
# print(sys.path)

## 添加 我们写的模块所在路径到系统路径里
# import sys
# sys.path.append(r'自定义模块所在的路径')

##使用相对路径
import sys
import os
###获取文件的绝对路径
print(__file__)

####获取文件的父路径,这行代码，可以获取我们当前的文件所在的目录路径，如果我们的
###自定义模块在项目里的某个目录里，给加到后边就行。
### os.path.dirname(__file__) 是动态的，文件在哪就输出哪，不用记绝对路径
### 要记得区分在 linux 和 windows 下的 \\ 和 /，然而我发现，pycharm里，windows下也可以用 '/'
# print(os.path.dirname(__file__) + '\\模块所在目录')

### 所以一般操作就是
# sys.path.append(os.path.dirname(__file__) + "/模块所在目录")


#倒入模块的多种方式
## import xxx 导入一个模块的所有成员
## import aaa,bbb,ccc  可以一行语句导入多个模块，不推荐
## from xxx import yyy,zzz 导入一个模块某几个成员或方法
## from xxx import * 导入一个模块的所有成员，区别于 import xxx
## from xxx import yyy as pd  为了不出现名称冲突或者简化使用，可以定义别名
## import xxx as x  这么用也可以
## 最好用什么导入什么，要不会占用好多资源

### from xxx impoort *  与  import xxx 的区别
### 当使用 import xxx 
### 我们调用模块内方法的时候，写法是： xxx.abc()
### 当使用 from xxx import *
### 我们调用模块内方法的时候，写法是： abc(),不用加模块名



## 模块的 __all__方法，提供模块内所有可以导入的成员
print(os.__all__)
## 开发时，使用 __all__ ，可以限制可以被导入的成员
## 但是在导入时，只有使用 from xxx import * 的时候有用
## 当使用 import xxx 的时候就管用了
__all__ = ['func1','func2','fucn3']


## 相对导入
## 针对同一个项目里的不同模块之间的导入
## 这个呢及时要知道相对路径的表示方法，比如：
## 当前目录 '.'
## 父目录 '..'
## from ../aa/aa import func
## 就这样，哈哈哈哈
```

## 2.os 模块

```python
'''
os 模块：和底层操作系统相关的操作被封装在这个模块中
这里只有一部分，也不说是常用的，
当我们有啥需求，就去百度，
去菜鸟教程网站，有的是，我也只是在给自己做笔记

'''

import os

# 和文件操作相关
## 删除文件
#os.remove(r'包含文件名的文件路径')

## 重命名
#os.rename(r'包含文件名的文件路径','改后文件名')

# 目录相关
##删除目录，必须是空目录
#os.removedirs(r'路径')

## 使用 shutil 模块可以删除含有内容的目录
# import shutil
# shutil.rmtree(r'路径')

## 和路径相关的操作，被封装到另一个子模块 os.path 中
### 取文件或目录的父目录名
res = os.path.dirname(r'D:\programming_with_python\043从零开始学python\day08 模块\os模块.py')
print(res) #D:\programming_with_python\043从零开始学python\day08 模块
### 用 os.path.dirname() 配合 __file__方法，可以获得文件的绝对路径,不带文件名
res = os.path.dirname(__file__)
print(res)

### 取文件名(路径的最后一部分)
res = os.path.basename(r'D:\programming_with_python\043从零开始学python\day08 模块\os模块.py')
print(res) #os模块.py

res = os.path.basename(r'D:\programming_with_python\043从零开始学python\day08 模块')
print(res) #day08 模块

### 把路径名和文件名分开(路径的最后一部分和其父目录分开)，返回一个含有两个元素的元组
res = os.path.split(r'D:\programming_with_python\043从零开始学python\day08 模块\os模块.py')
print(res) #('D:\\programming_with_python\\043从零开始学python\\day08 模块', 'os模块.py')

res = os.path.split(r'D:\programming_with_python\043从零开始学python\day08 模块')
print(res) #('D:\\programming_with_python\\043从零开始学python', 'day08 模块')

### 拼接路径,会自动加上 '\'
res = os.path.join('D:\\','aaa','bbb','ccc')
print(res) #D:\aaa\bbb\ccc


### 获取一个路径的绝对路径，
#### 如果我给的相对路径是 有个 '/' 开头的，他会默认你在盘符的根目录下，然后直接加上盘符名称返回
res = os.path.abspath(r'/day08 模块')
print(res) #D:\day08 模块
#### 如果我给的相对路径没有 '/' 开头，默认是当前目录，返回绝对路径
res = os.path.abspath(r'day08 模块')
print(res) #D:\programming_with_python\043从零开始学python\day08 模块\day08 模块

## 判断
### 判断是否是绝对路径,如果给的路径不存在就会报错
res = os.path.isabs(r'D:\programming_with_python\043从零开始学python\day08 模块\day08 模块')
res2 = os.path.isabs(r'os模块.py')
print(res) #True
print(res2) #False

### 判断是否是个文件
res = os.path.isfile(r'D:\programming_with_python\043从零开始学python\day08 模块\day08 模块')
res2 = os.path.isfile(r'os模块.py')
print(res) #False
print(res2) #True

### 判断是否是个路径
os.path.isdir(os.path.dirname(__file__)) #True

### 判断路径是否存在
res = os.path.exists(r'D:\programming_with_python\043从零开始学python\day08 模块')
print(res) #True

'''
***************************************************************
					最后，看一下os模块的总结
***************************************************************							
'''
# 当前执行这个python文件的工作目录相关的工作路径
os.getcwd() #(pwd) 获取当前工作目录，即当前python脚本工作的目录路径  ** 
os.chdir("dirname")  #(cd ) 改变当前脚本工作目录；相当于shell下cd  **
os.curdir  返回当前目录: ('.')  **
os.pardir  获取当前目录的父目录字符串名：('..') **
​
# 和文件夹相关 
os.makedirs('dirname1/dirname2') #(mkdir -p )   可生成多层递归目录  ***
os.removedirs('dirname1') #(rm -r) 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 ***
os.mkdir('dirname')    #(mkdir) 生成单级目录；相当于shell中mkdir dirname ***
os.rmdir('dirname')    #(rmdir) 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname ***
os.listdir('dirname')  #(ls -al)  列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印 **
​os.copy('olddir','newdir/newfile') #(cp olddir newdir) #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
# 和文件相关
os.remove()  删除一个文件  ***
os.rename("oldname","newname")  重命名文件/目录  ***
os.stat('path/filename')  获取文件/目录信息 **
​shutil.copytree("olddir","newdir")   #复制文件夹： olddir和newdir都只能是目录，且newdir必须不存在
shutil.move("oldpos","newpos")    #移动文件（目录）

# 和操作系统差异相关
os.sep    #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/" *
os.linesep    #输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n" *
os.pathsep    #输出用于分割文件路径的字符串 win下为;,Linux下为: *
os.name    #输出字符串指示当前使用平台。win->'nt'; Linux->'posix' *和执行系统命令相关
# os.system("bash command")  #运行shell命令，直接显示  **
# os.popen("bash command").read()  # 运行shell命令，获取执行结果  **
os.environ  获取系统环境变量  **
​
#path系列，和路径相关
os.path.abspath(path) #返回path规范化的绝对路径  ***
os.path.split(path) #将path分割成目录和文件名二元组返回 ***
os.path.dirname(path) #返回path的目录。其实就是os.path.split(path)的第一个元素  **
os.path.basename(path)# 返回path最后的文件名。如何path以'/'或'\\' 结尾，那么就会返回空值，即os.path.split(path)的第二个元素。 **
os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False  ***
os.path.isabs(path)  #如果path是绝对路径，返回True  **
os.path.isfile(path) # 如果path是一个存在的文件，返回True。否则返回False  ***
os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False  ***
os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ***
os.path.getatime(path)  #返回path所指向的文件或者目录的最后访问时间  **
os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间  **
os.path.getsize(path) #返回path的大小 ***

# stat 结构:
# st_mode: inode 保护模式
# st_ino: inode 节点号。
# st_dev: inode 驻留的设备。
# st_nlink: inode 的链接数。
# st_uid: 所有者的用户ID。
# st_gid: 所有者的组ID。
# st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
# st_atime: 上次访问的时间。
# st_mtime: 最后一次修改的时间。
# st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。


```

## 3.sys模块

```python
'''
sys 模块
和python解释器相关的操作
'''

import sys

# 获取命令行方式运行的脚本后面的参数 sys.argv
# sys.argv  这个东西是个列表，他不能调用
# sys.argv[0] 是脚本名称，往后的元素是传入脚本的参数,但是都是字符串类型的
# 这个一般应用于解释器命令行里
# 
# print('脚本名',sys.argv[0])
# print('第一个参数',sys.argv[1])
# print('第二个参数',sys.argv[2])

'''
PS D:\programming_with_python\043从零开始学python\day08 模块> python .\sys模块.py hello world
脚本名 .\sys模块.py
第一个参数 hello
第二个参数 world
'''

# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])
# print(arg1 + arg2)

'''
PS D:\programming_with_python\043从零开始学python\day08 模块> python .\sys模块.py 1 2
脚本名 .\sys模块.py
第一个参数 1
第二个参数 2
3
'''

# 解释器寻找模块的路径
# sys.path
## 如果，我们自己写了模块或者包，想要不通过绝对路径就调用，我们就得把模块所在的路径写入
## sys.path 寻找的那些个目录里
## 先看看 sys.path 里有啥
print(sys.path)

### 返回一个列表，包含所有可以直接调用模块的路径，第一个目录是执行命令的脚本所在目录，当我们编写程序，可以直接调用同意目录下的模块
### 但是这是临时的，我们关了文件，sys.path 里就没有这个目录了，
### 我们可以把包含我们写好的模块的目录，写入 sys.path,这样任何时候都可以直接调用了
'''
['D:\\programming_with_python\\043从零开始学python\\day08 模块', 'C:\\Program Files (x86)\\Python3.8\\python38.zip', 'C:\\Program Files (x86)\\Python3.8\\DLLs', 'C:\\Program Files (x86)\\Python3.8\\lib', 'C:\\Program Files (x86)\\Python3.8', 'C:\\Users\\Wang Yishan\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Program Files (x86)\\Python3.8\\lib\\site-packages']
'''
## 将目标目录写入 sys.path
# import os
# sys.path.append(os.path.dirname(__file__))


# 返回系统已经加载的莫亏啊 sys.modules
print(sys.modules)

## 说点别的，怎么判断，这些个内置的函数方法，调用的时候要不要加括号呢？
## 如果，我们调用的内置变量，是个方法或者类，就要加()才行
## 如果，我们调用的内置变量，是一个属性，就不用了
## 那怎么判断调用的是个啥呢？ 简单的方法就是在pycharm里，如果提示里 提示这个是个 'v' 的，就是属性，不用加括号，其他的都加



sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
sys.version        获取Python解释程序的版本信息
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值  ***
sys.platform       返回操作系统平台名称
```

## 4.time 模块

```python
# time 模块
# time 模块封装了获取时间戳和字符串形式的时间的一些方法
import time

# 获取时间戳
# 返回的是格林威治时间，是从时间元年(1970/01/01/00:00:00)到现在经过的秒数或毫秒数
# python 里是秒数 
print(time.time())
a = int(time.time()/86400/365)
print(a)

# 获取格式化时间对象
# 获取的是格林威治时间,结构化时间对象
# 默认参数是当前时间的时间戳
b = time.gmtime()
print(b)

# 获取当地的格式化时间，结构化时间对象
# 默认参数是当前时间的时间戳
c = time.localtime()
print(c)

# 给参数，就是时间元年后的 参数 秒后的结构化时间对象
# 一般，就默认参数就好
print(time.localtime(1))  

# 格式化时间对象和字符串之间的转换
# 格式化时间对象-->字符串，方便人阅读
# 字符串 --> 格式化时间对象，方便计算机传输
# time.strftime('格式化字符串',时间对象) 首先传格式化字符串，然后传结构化时间
# 如果不传结构化时间参数，就默认当前时间戳
d = time.strftime('%Y/%m/%d %H:%M:%S',)
print(d)

# 可以把时间按转换为格式化时间对象
# time.strptime('时间表示','格式化字符串' )
e = time.strptime('2020/04/15','%Y/%m/%d')
print(e)

# 可以把格式化时间对象转化为时间戳,这个没啥用，完全可以直接用 time.time()生成时间戳
t1 = time.localtime()
print(t1)
t2 = time.mktime(t1)
print(t2)

# 暂停当前的程序，睡眠 xxx 秒
# time.sleep(x)
for i in range(5):
	print(time.strftime('%Y/%m/%d %H:%M:%S'))
	time.sleep(1)

# time 模块的三大对象  相互转化
# 1.格式化时间对象： time.struct_time
# 2.时间字符串 
# 3.时间戳 time.time()

# 相互转化
# 时间戳 --> 格式化时间对象
time.gmtime()
time.localtime()

# 格式化时间对象 --> 时间戳
# time.mktime()

# 格式化时间对象 --> 时间字符串
time.strftime('%Y/%m/%d %H:%M:%S')

# 时间字符串 --> 格式化时间对象
time.strptime('2020/04/15','%Y/%m/%d')
```

## 5.datetime 模块

```python
'''
datetime 模块：日期和时间模块
封装了一些和日期，时间相关的类

四大类：
date 年月日
time 时分秒
datetime
timedelta

'''
import datetime
#date 类：包含很多方法
a= datetime.date(2020,4,15)
print(a)  #2020-04-15

## 获取date对象的各个属性
## 就是分别获取年月日
print(a.year,type(a.year)) #
print(a.month)
print(a.day)

#time 类：
b = datetime.time(10,48,59)
print(b)

#time 类的属性
print(b.hour)
print(b.minute)
print(b.second)

#datetime 类
c = datetime.datetime(2011,11,11,11,11,11)
print(c)  #2011-11-11 11:11:11

#datetime 类的属性
print(c.year,type(c.year))
print(c.month)
print(c.day)
print(c.hour)
print(c.minute)
print(c.second)

#datetime 模块中的类，主要用于数学计算
#datetime 模块中的类属性返回值，一般都是 int 类型，适合计算

#timedelta 类：时间变化量
#创建一个时间的变化量，相当于时间上的步进值，用某个时间减去它，就得到之间的时间点
#用摸个时间加上他，就是未来的时间点
td = datetime.timedelta(days=1)
print(td)

#参与数学运算
#创建时间对象
# date, datetime, timedelta
# 只收上述三类才能进行时间数据运算， time 属性不能进行运算
d = datetime.date(2010,10,10)
res = d + td
res2 = d - td
print(res)
print(res2)

# 时间变化量的计算，会影响进位
# 满60秒会进位一分钟，满60分钟会进位一小时

t = datetime.datetime(2010,10,10,10,10,59)
td = datetime.timedelta(seconds=3)
res = t + td
print(res) # 2010-10-10 10:11:02

#练习：计算二月份有多少天
#普通的算法：根据年份计算是否是闰年

#用 datetime 模块
##首先创建某一年的 3月1日，然后让他往前退一天
year = 2000  # int(input('输入年份：'))

## 创建制定年份的date对象
d = datetime.date(year,3,1)

## 创建一天的时间变化量
td = datetime.timedelta(days=1)

res = d-td
print(res.day) 

#和时间变化量运算的结果类型
# 与 datetime.timedelta 运算的类型是什么类型，结果就是什么类型
# 如果是两个 datetime.timedelta 类型进行运算，结果就是 datetime.timedelta 类型
d = datetime.date(2020,10,10)
td = datetime.timedelta(days=1)
res = d - td
print(type(res))  # <class 'datetime.date'>


d = datetime.datetime(2020,11,11,11,11,11)
td = datetime.timedelta(days=1)
res = d - td
print(type(res))  #<class 'datetime.datetime'>


td1 = datetime.timedelta(seconds=20)
td2 = datetime.timedelta(days=1)
res = td1 + td2 
print(type(res)) #<class 'datetime.timedelta'>




# d1 = datetime.datetime(2020,11,11,11,11,11)
# d2 = datetime.date(2020,10,10)
# res = d1 -d2 #会报错，这俩不能互相运算，类型不同，且不含有 datetiem.timedelta 类型
# print(res,type(res))


# 同类型时间对象之间的计算
# 日期之间只能相减，相减得到的结果类型是 datetime.timedelta
# 而且，结果都包含 时分秒，即使你没定义也有
d1 = datetime.date(2020,10,10)
d2 = datetime.date(2020,11,11)
res = d2 - d1 #这个不会报错
#res2 = d2+d1 # 这个会报错，日期之间不能相加，只能相减
print(res,type(res)) #32 days, 0:00:00 <class 'datetime.timedelta'>
#print(res2,type(res2)) 

d1 = datetime.datetime(2020,11,11,11,11,11)
d2 = datetime.datetime(2019,11,11,11,11,11)
res = d1 - d2
print(res,type(res)) #366 days, 0:00:00 <class 'datetime.timedelta'>



```

## 6.random 模块

```python
# random 模块
import random

# 左闭右开，获取 [0.0,1.0) 范围内的一个浮点数,不接收参数
# random.random()
a = random.random()
print(a)

# 左闭右开， 获取 [a,b) 范围内的一个浮点数
# random.uniform()
b = random.uniform(3,5)
print(b)

# 闭区间， 获取[a,b] 范围内的一个整数
# random.randint(a,b)
c = random.randint(3,10)
print(c)


# 混洗。 把参数指定的数据元素打乱顺序，参数必须是可变类型 [] {}
# random.shuffle(x)
lst1 = list(range(10))
print(lst1)
random.shuffle(lst1)
print(lst1)

# 取样。 从 x 中随机抽取 k 个数据，组成一个列表返回
# random.sample(x,k)
tu1 = (1,2,3,4,5,6,)
lst2 = random.sample(tu1,5)
print(lst2)

```

## 7.json 模块 ***

```python
# random 模块
import random

# 左闭右开，获取 [0.0,1.0) 范围内的一个浮点数,不接收参数
# random.random()
a = random.random()
print(a)

# 左闭右开， 获取 [a,b) 范围内的一个浮点数
# random.uniform()
b = random.uniform(3,5)
print(b)

# 闭区间， 获取[a,b] 范围内的一个整数
# random.randint(a,b)
c = random.randint(3,10)
print(c)


# 混洗。 把参数指定的数据元素打乱顺序，参数必须是可变类型 [] {}
# random.shuffle(x)
lst1 = list(range(10))
print(lst1)
random.shuffle(lst1)
print(lst1)

# 取样。 从 x 中随机抽取 k 个数据，组成一个列表返回
# random.sample(x,k)
tu1 = (1,2,3,4,5,6,)
lst2 = random.sample(tu1,5)
print(lst2)

```

| JSON          | Python |
| ------------- | ------ |
| object        | dict   |
| array         | list   |
| string        | str    |
| number( int ) | int    |
| number(real)  | float  |
| true          | True   |
| false         | False  |
| null          | None   |



## 8.pickle 模块

```python
'''
pickle 模块,将 python 所有数据类型都转化为字节(二进制)(串)，或者反序列化
由于对所有数据类型都有效，所以pickle可以完全保留python的数据类型
但是由于不能与其他语言公用，所以很垃圾，重点还是 json
'''
# pickle 模块的方法与 json 的操作一样
# 都是用 dumps loads  dump load
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  # bytes类型
dic2 = pickle.loads(str_dic)
print(dic2)    #字典

# 还可以序列化对象
import pickle

def func():
	print(666)
ret = pickle.dumps(func)
print(ret,type(ret)) #b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04func\x94\x93\x94.' <class 'bytes'>

f1 = pickle.loads(ret)
print(f1,type(f1)) #<function func at 0x015F94A8> <class 'function'>
f1()

# 文件写入读出
dic = {(1,2):'oldboy',1:True,'set':{1,2,3}}
f = open('pickle序列化.pickle',mode='wb')
pickle.dump(dic,f)
f.close()

with open('pickle序列化.pickle',mode='rb') as f1:
	dic2 = pickle.load(f1)
	print(dic2)


# pickle 序列化可以存储多个数据到一个文件里
dic1 = {'name':'oldboy1'}
dic2 = {'name':'oldboy2'}
dic3 = {'name':'oldboy3'}
f=open('pick多数据.pickle',mode='wb')
pickle.dump(dic1,f)
pickle.dump(dic2,f)
pickle.dump(dic3,f)
f.close()
f=open('pick多数据',mode='rb')
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()



```

## 9.hashlib 模块

```python
'''
hashlib模块：用于加密
封装了一些加密的类
加密的目的适用于判断和验证 最多用 md5()

特点：
	- 把一个大的数据且奉承不同小块，分别对不同小块进行加密，在汇总结果，和直接对整体加密的结果是一致的
	- 单项加密，一般不可逆
	- 演示数据的一点小变化，将导致结果的非常大的差异
'''

# 那，这么牛逼，怎么用呢
import hashlib

# 先看看他都有啥方法啊
print(dir(hashlib))

'''
['__all__', '__block_openssl_constructor', '__builtin_constructor_cache', '__builtins__', '__cached__', '__doc__', '__file__', '__get_builtin_constructor', '__loader__', '__name__', '__package__', '__spec__', '_hashlib', 'algorithms_available', 'algorithms_guaranteed', 'blake2b', 'blake2s', 'md5', 'new', 'pbkdf2_hmac', 'scrypt', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256']
'''
# 给一个数据加密的三大步骤：
# 获取一个加密对象
m = hashlib.md5()

# 使用加密对象的 update 方法 ,对目标进行加密，加密方法 update
# 可以加密多次
m.update('abc中文'.encode('utf-8'))
m.update('def'.encode('utf-8'))

#通过 hexdigest 获取加密结果 或直接用 digest()来获取，但 digest()获取的是二进制，所以少用

res = m.hexdigest()
print(res) #2f1b6e294e72d25ae196fe4ac2d27de6

# 给一个数据加密
# 验证：用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同

'''
它通过一个函数，把任意长度的数据按照一定规则转换为一个固定长度的数据串（通常用16进制的字符串表示）。

比如：之前我们在一个文件中存储用户的用户名和密码是这样的形式：

    太白|123456

有什么问题？你的密码是明文的，如果有人可以窃取到这个文件，那么你的密码就会泄露了。所以，一般我们存储密码时都是以密文存储，比如：

    太白|e10adc3949ba59abbe56e057f20f883e

那么即使是他窃取到这个文件，他也不会轻易的破解出你的密码，这样就会保证了数据的安全。

hashlib模块就可以完成的就是这个功能。

hashlib的特征以及使用要点：

bytes类型数据 ---> 通过hashlib算法 ---> 固定长度的字符串

不同的bytes类型数据转化成的结果一定不同。

相同的bytes类型数据转化成的结果一定相同。

此转化过程不可逆。

那么刚才我们也说了，hashlib的主要用途有两个：

    密码的加密。

    文件一致性校验。

hashlib模块就相当于一个算法的集合，这里面包含着很多的算法，算法越高，转化成的结果越复杂，安全程度越高，相应的效率就会越低。
'''
# 1.密码的加密
# 以常见的 md5 为例，计算出一个字符串的 md5 值
import hashlib

md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
res = md5.hexdigest()
print(res)

## 计算结果如下
## 'e10adc3949ba59abbe56e057f20f883e'

## 验证：相同 bytes 数据转化的结果一定相同
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
res = md5.hexdigest()
print(res)

## 计算结果如下
## 'e10adc3949ba59abbe56e057f20f883e'

## 验证：不同 bytes 数据转化的结果一定不同

md5 = hashlib.md5()
md5.update('12345'.encode('utf-8'))
res = md5.hexdigest()
print(res)

## 计算结果如下
## '827ccb0eea8a706c4c34a16891f84e7b'

'''
上面就是普通的md5加密，非常简单，几行代码就可以了，但是这种加密级别是最低的，相对来说不很安全。虽然说hashlib加密是不可逆的加密方式，但也是可以破解的，那么他是如何做的呢？你看网上好多MD5解密软件，他们就是用最low的方式，空间换时间。他们会把常用的一些密码比如：123456,111111,以及他们的md5的值做成对应关系，类似于字典，

dic = {'e10adc3949ba59abbe56e057f20f883e': 123456}

然后通过你的密文获取对应的密码。

只要空间足够大，那么里面容纳的密码会非常多，利用空间换取破解时间。 所以针对刚才说的情况，我们有更安全的加密方式：加盐。
'''
#2.加盐加密,就是在创建加密对象的时候给 hashlib.md5()传个参数
##2.1 固定的盐
'''
什么叫加盐？加盐这个词儿来自于国外，外国人起名字我认为很随意，这个名字来源于烧烤，俗称BBQ。我们烧烤的时候，一般在快熟的时候，都会给肉串上面撒盐，增加味道，那么这个撒盐的工序，外国人认为比较复杂，所以就讲比较复杂的加密方式称之为加盐
'''
ret = hashlib.md5('一山一晴'.encode('utf-8')) #这个'一山一晴'就是固定的盐
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())
'''
上面的'一山一晴'就是固定的盐，比如你在一家公司，公司会将你们所有的密码在md5之前增加一个固定的盐，这样提高了密码的安全性。但是如果黑客通过手段窃取到你这个固定的盐之后，也是可以破解出来的。所以，我们还可以加动态的盐。
'''

## 2.2 动态的盐
username = 'fallen'
ret = hashlib.md5(username[::2].encode('utf-8')) #这样针对每个账户，每个账户 盐都不一样
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())
'''
这样，安全性能就大大提高了。

那么我们之前说了hahslib模块是一个算法集合，他里面包含很多种加密算法，刚才我们说的MD5算法是比较常用的一种加密算法，一般的企业用MD5就够用了。但是对安全要求比较高的企业，比如金融行业，MD5加密的方式就不够了，得需要加密方式更高的，比如sha系列，sha1,sha224,sha512等等，数字越大，加密的方法越复杂，安全性越高，但是效率就会越慢。
sha1,sha224,sha512等都是算法名称，跟 md5 是一样的。用法也一样
但我们多数就用 md5 就行了
'''
ret = hashlib.sha1()
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())

##也可以加盐
ret = hashlib.sha384('爱你么么哒'.encode("utf-8"))
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())

##也可以加动态的盐
dongtai = 'qingtianyigepili'
ret = hashlib.sha224(dongtai[::2].encode('utf-8'))
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())

# 3.文件的一致性校验
'''
以下说明，抄自太白金星老师的博客：这个文档里的大段文字都是从他那抄的
hashlib模块除了可以用于密码加密之外，还有一个常用的功能，那就是文件的一致性校验。

    linux讲究：一切皆文件，我们普通的文件，是文件，视频，音频，图片，以及应用程序等都是文件。我们都从网上下载过资源，比如我们刚开学时让大家从网上下载pycharm这个软件，当时你可能没有注意过，其实你下载的时候都是带一个MD5或者shax值的，为什么？ 我们的网络世界是很不安全的，经常会遇到病毒，木马等，有些你是看不到的可能就植入了你的电脑中，那么他们是怎么来的？ 都是通过网络传入来的，就是你在网上下载一些资源的时候，趁虚而入，当然大部门被我们的浏览器或者杀毒软件拦截了，但是还有一部分偷偷的进入你的磁盘中了。那么我们自己如何验证我们下载的资源是否有病毒呢？这就需要文件的一致性校验了。在我们下载一个软件时，往往都带有一个MD5或者shax值，当我们下载完成这个应用程序时你要是对比大小根本看不出什么问题，你应该对比他们的md5值，如果两个md5值相同，就证明这个应用程序是安全的，如果你下载的这个文件的MD5值与服务端给你提供的不同，那么就证明你这个应用程序肯定是植入病毒了（文件损坏的几率很低），那么你就应该赶紧删除，不应该安装此应用程序。

我们之前说过，md5计算的就是bytes类型的数据的转换值，同一个bytes数据用同样的加密方式转化成的结果一定相同，如果不同的bytes数据（即使一个数据只是删除了一个空格）那么用同样的加密方式转化成的结果一定是不同的。所以，hashlib也是验证文件一致性的重要工具。
'''

## 3.1 文件校验函数 low 版
f = open('hashlib_file1','w')
f.write('abcd')
f.close()
def func(file):
	with open(file,mode='rb') as f1:
		ret = hashlib.md5()
		ret.update(f1.read())
		return ret.hexdigest()
print(func('hashlib_file1'))
'''
这样就可以计算此文件的MD5值，从而进行文件校验。但是这样写有一个问题，类似我们文件的改的操作，有什么问题？如果文件过大，全部读取出来直接就会撑爆内存的，所以我们要分段读取，那么分段读取怎么做呢？
'''
## 3.2 hashlib 分段读取文件
### 直接读取
md5obj = hashlib.md5()
md5obj.update('一山是个大帅哥'.encode('utf-8'))
print(md5obj.hexdigest()) #ffe423b0b5b717c937be394c6860a6c0

### 分段读取
md5obj = hashlib.md5()
md5obj.update('一山'.encode('utf-8'))
md5obj.update('是'.encode('utf-8'))
md5obj.update('个'.encode('utf-8'))
md5obj.update('大'.encode(('utf-8')))
md5obj.update('帅'.encode('utf-8'))
md5obj.update('哥'.encode('utf-8'))
print(md5obj.hexdigest()) #ffe423b0b5b717c937be394c6860a6c0

### 文件校验函数 高大上版
def file_check(file_path):
	with open(file_path,mode='rb') as f1:
		sha256 = hashlib.sha256()
		while 1:
			content = f1.read(1024)
			if content:
				sha256.update(content)
			else:
				return sha256.hexdigest()
print(file_check(r'D:\科研软件\geek.exe'))


#练习：注册后保存用户信息，登录时验证

def get_md5(username,password):
	m = hashlib.md5()
	m.update(username.encode('utf-8'))
	m.update(password.encode('utf-8'))
	return m.hexdigest()


def register(username,password):
	# 加密
	res = get_md5(username,password)
	# 写入文件
	with open('login',mode='a',encoding='utf-8') as f,open('user',mode='a',encoding='utf-8') as f2, \
		open('user',mode='r',encoding='utf-8') as f3:
		lst = []
		for u in f3:
			lst.append(u.strip())
		if username not in lst:
			f.write(res+'\n')
			f2.write(username+'\n')
		else:
			print('已注册过，请登录')

def login(username,password):
	# 获取输入的信息的加密信息
	res = get_md5(username,password)
	# 读文件
	with open('login',mode='rt',encoding='utf-8') as f:
		for line in f:
			if res == line.strip():
				return True




def main():
	while True:

		judge = input('1.注册 2.登录 3.退出：')
		if judge.isdigit() and int(judge) in (1,2,3):
			if int(judge)==3:
				print('quit~')
				break
			elif int(judge)==1:
				username = input('username:')
				password = input('password:')
				register(username,password)
			elif int(judge)==2:
				username = input('username:')
				password = input('password:')
				with open('user',mode='r',encoding='utf-8') as f2:
					lst1 = []
					for u in f2:
						lst1.append(u.strip())
					if username not in lst1:
						print('please register first!')
					else:
						res = login(username,password)
						if res==True:
							print('login successfully!')
						else:
							print('username or password error. \n')
		else:
			print("你必须输入给定的序号！")


if __name__ == '__main__':
	main()


```

## 10.collections 模块

```Python
'''
collections 模块

在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。

1.namedtuple: 生成可以使用名字来访问元素内容的tuple

2.deque: 双端队列，可以快速的从另外一侧追加和推出对象

3.Counter: 计数器，主要用来计数

4.OrderedDict: 有序字典

5.defaultdict: 带有默认值的字典
'''
import collections
# 1.namedtuple 生成可以使用名字来访问元素内容的tuple
# namedtuple('名称', [属性list])
'''
我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：

p = (1, 2)
但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。

这时，namedtuple就派上了用场：
'''
Point = collections.namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)

## 也可以用坐标和半径表示一个圆：
Circle = collections.namedtuple('Circle',['x','y','r'])
cir = Circle(1,2,3)
print(cir.x,cir.y,cir.r)

# 2.deque 双端队列，可以快速的从另外一侧追加和推出对象
'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
q = collections.deque(['a','b','c'])
q.append('x') #右边加入
q.appendleft('y') # 左边加入
print(q) #deque(['y', 'a', 'b', 'c', 'x'])
q.pop() #右边弹出
q.popleft() #左边弹出
print(q) #deque(['a', 'b', 'c'])

# 3.OrderedDict: 有序字典
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用OrderedDict：
'''
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = collections.OrderedDict([('a',1),('b',2),('c',3)])
print(od) #OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = collections.OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys()) #odict_keys(['z', 'y', 'x']) 按照插入的key的顺序返回

# 4.defaultdict 带有默认值的字典
# defaultdict 接受的第一个参数，这个参数将作为默认键值对的值，这个参数叫做工厂，
# 可以是数据类型转化函数名：list  tuple  dict  str  int float 等等，也可以是我们自己写的构造函数，当我们
# 引用字典中不存在的键，不会报错，会返回一个默认的值，这个默认值就是 [], (), {}, "" ,0 ,0.0
# 创建字典的几种方式
## 普通赋值建立
d = {'name':'Andy','age':18}
d = dict([('name','Andy'),('age',18)])
d = dict(name='Andy',age='18')
d = {k:v for k in range(10) for v in range(10)}
print(d)
d = collections.defaultdict(int,name='Andy',age=18)
print(d) #defaultdict(<class 'str'>, {'name': 'Andy', 'age': 18})
print(d['addr']) #0
'''
这个呢，我也不知道有啥用，可能是为了当你使用字典不存在的键值对的时候
不会报错吧，哈哈哈哈哈哈。但是这么一想，唉，还有点用。
'''
'''
有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。

即： {'k1': 大于66 , 'k2': 小于66}
'''
li = [11,22,33,44,55,77,88,99,90]

## 使用普通字典
dic = {'k1':[],'k2':[]}

for i in li:
	if i > 66:
		dic['k1'].append(i)
	elif i< 66:
		dic['k2'].append(i)

print(dic)

## 使用 defaultdict

dic2 = collections.defaultdict(list)
print(dic2)
for i in li:
	if i > 66:
		dic2['k1'].append(i)
	elif i< 66:
		dic2['k2'].append(i)

print(dic2)

## 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = collections.defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) #abc
print(dd['key2']) #N/A

# 5. Counter 类，计数
## Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。

c = collections.Counter('abcdabcesdfsdzfdfzdfas')
print(c) #Counter({'d': 5, 'f': 4, 'a': 3, 's': 3, 'b': 2, 'c': 2, 'z': 2, 'e': 1})
print(c['a']) #3
print(c.most_common(3)) #[('d', 5), ('f', 4), ('a', 3)] 曲线次数排名前三的

```

## 11.shutil 模块

```python
import shutil



# 拷贝文件
# shutil.copy2('原文件', '现文件')
# shutil.copy2('file', 'temp')

# 拷贝目录
# shutil.copytree("原目录", "新目录", ignore=shutil.ignore_patterns("*.pyc"))
# shutil.copytree("/Users/jingliyang/PycharmProjects/面试题/常用模块/logging模块", "logging模块2", ignore=shutil.ignore_patterns("__init__.py"))

# 删除目录
# shutil.rmtree("temp", ignore_errors=True)
# shutil.rmtree("logging模块2", ignore_errors=True)

# 移动文件/目录
# shutil.move("logging模块", "logging2", copy_function=shutil.copy2)

# 获取磁盘使用空间
# total, used, free = shutil.disk_usage(".")
# print("当前磁盘共: %iGB, 已使用: %iGB, 剩余: %iGB"%(total / 1073741824, used / 1073741824, free / 1073741824))
#
# 压缩文件
shutil.make_archive('压缩文件夹的名字', 'zip','待压缩的文件夹路径')
shutil.make_archive('logging2', 'zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/随机数')

# 解压文件
# shutil.unpack_archive('zip文件的路径.zip'，'解压到目的文件夹路径')
# shutil.unpack_archive('/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/logging2.zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/tmp')
```

## 12. logging 模块-我还不太会，正在学习

```python
# 为什么要写log?
    # log是为了排错
    # log用来做数据分析的

# 购物商城 - 数据库里
    # 什么时间购买了什么商品
    # 把哪些商品加入购物车了

# 做数据分析的内容 - 记录到日志
# 1.一个用户什么时间在什么地点 登录了购物程序
# 2.搜索了哪些信息,所长时间被展示出来了
# 3.什么时候关闭了软件
# 4.对哪些商品点进去看了

# 计算器
    # (1+2)*3/4
    # 计算乘法(表达式):
       # 记录日志:计算乘法表达式是什么,结果是什么
       # return
    # 计算除法
        # 记录日志:表达式是什么,结果是什么
       # return
    # 计算小括号内的
    # 计算加法
    # 计算减法

# 1.用来记录用户的行为 - 数据分析
# 2.用来记录用户的行为 - 操作审计
# 3.排查代码中的错误

import logging
# 输出内容是有等级的 : 默认处理warning级别以上的所有信息
# logging.debug('debug message')          # 调试
# logging.info('info message')            # 信息
# logging.warning('warning message')      # 警告
# logging.error('error message')          # 错误
# logging.critical('critical message')    # 批判性的

# def cal_mul(exp):
#     exp = 4*6
#     logging.debug('4*6 = 24')
#     return 24
# def cal_div():
#     pass
# def cal_add():
#     pass
# def cal_sub(exp):
#     exp = 3-24
#     logging.debug('cal_sub :3-24 = 21')
#     return 21

# def cal_inner_bracket(exp2):
#     exp2 = 3-4*6
#     ret = cal_mul(4*6)
#     exp2 = 3-24
#     ret = cal_sub(3-24)
#     logging.debug('3-4*6 = -21')
#     return -21
#
# def main(exp):
#     exp =(1+2*(3-4*6))/5
#     ret = cal_inner_bracket(3-4*6)
#     return ret
#
# logging.basicConfig(level=logging.DEBUG)
# ret = main('(1+2*(3-4))/5')
# print(ret)

# 1.无论你希望日志里打印哪些内容,都得你自己写,没有自动生成日志这种事儿
# logging.basicConfig
# 输出到屏幕
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')

# 输出到文件,并且设置信息的等级
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     filename='tmp.log',
#     level= logging.DEBUG
#
# )
# logging.debug('debug 信息错误 test2')
# logging.info('warning 信息错误 test2')
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')



# 要记住的
# --------------------------------------------------------------------------------------------------
# 同时向文件和屏幕上输出 和 乱码
# fh = logging.FileHandler('tmp.log',encoding='utf-8')
# # fh2 = logging.FileHandler('tmp2.log',encoding='utf-8')
# sh = logging.StreamHandler()
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level= logging.DEBUG,
#     # handlers=[fh,sh,fh2]
#     handlers=[fh,sh]
# )
# logging.debug('debug 信息错误 test2')
# logging.info('warning 信息错误 test2')
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')

# 做日志的切分
# import time
# from logging import handlers
# sh = logging.StreamHandler()
# rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024,backupCount=5)   # 按照大小做切割
# fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level= logging.DEBUG,
#     # handlers=[fh,sh,fh2]
#     handlers=[fh,rh,sh]
# )
# for i in range(1,100000):
#     time.sleep(1)
#     logging.error('KeyboardInterrupt error %s'%str(i))

—————————————————————————————————————————————————————————————————————-————————
#提供一种字典的方式，创建logger配置文件，这种才是工作中经常使用的实现日志功能的方法，真正的做到   ----- 拿来即用（简单改改）。

"""
logging配置
"""

import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'all2.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态

if __name__ == '__main__':
    load_my_logging_cfg()

#logger配置文件

-----------------------------------------------------------------------------
注意注意注意：


#1、有了上述方式我们的好处是：所有与logging模块有关的配置都写到字典中就可以了，更加清晰，方便管理


#2、我们需要解决的问题是：
    1、从字典加载配置：logging.config.dictConfig(settings.LOGGING_DIC)

    2、拿到logger对象来产生日志
    logger对象都是配置到字典的loggers 键对应的子字典中的
    按照我们对logging模块的理解，要想获取某个东西都是通过名字，也就是key来获取的
    于是我们要获取不同的logger对象就是
    logger=logging.getLogger('loggers子字典的key名')

    
    但问题是：如果我们想要不同logger名的logger对象都共用一段配置，那么肯定不能在loggers子字典中定义n个key   
 'loggers': {    
        'l1': {
            'handlers': ['default', 'console'],  #
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'l2: {
            'handlers': ['default', 'console' ], 
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
        'l3': {
            'handlers': ['default', 'console'],  #
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },

}

    
#我们的解决方式是，定义一个空的key
    'loggers': {
        '': {
            'handlers': ['default', 'console'], 
            'level': 'DEBUG',
            'propagate': True, 
        },

}

#这样我们再取logger对象时
#logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，#但是拿着该名字去loggers里找key名时却发现找不到，于是默认使用key=''的配置

#如何拿到logger对象的详细解释
```



