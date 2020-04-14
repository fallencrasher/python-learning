# python 基础 day02

# 1. 字符串操作

主要说说内建函数。

字符串类型，就像列表一样，可以进行切片，排序等等操作。

但是这里就专门说内建函数哦。

```python
'''
@Author: Fallen
@Date: 2020-04-03 10:30:20
@LastEditTime: 2020-04-03 15:33:44
@LastEditors: Please set LastEditors
@Description: 字符串内建函数
@FilePath: \day02\字符串内建函数.py
'''

l = "abcdif geheEdjfoaae ifXlji felkkNOFWIjsk"

#1.大小写相关
# capitalize()  title() istitle()   upper()  isupper()   lower()  islower（）
print(l.capitalize())  #第一个字母大写
print(l.title())  # 每个单词首字母都大写
print(l.upper())  # 全改成大写
print(l.lower())  # 全改成小写
print(l.isupper())  #判断是不是都是大写
print(l.islower())  # 判断是不是都是小写

#2.查找替换相关
#  find()   rfind()     index()  rindex()     replace()
a = l.find("a",0,len(l)-1)  #找到具体内容的索引，没找到就返回 -1
print(a)

b = l.rfind("a",0,len(l)-1) #从右开始find()
print(b)

d = l.index("a",0,len(l)-1) #跟find()一样功能，不过，要是没找到，就报错
print(d)

e = l.rindex("a",0,len(l)-1) # 从右边开始 index()
print(e)


g = l.replace("a","##") # 用后边的东西替换前边的东西
print(g)

#3.编码与解码
# encode()  decode()
# 有  gbk 中文   gb2312 简体中文  unicode  utf-8  什么的
l2 = "我爱你中国！莫哈哈哈！"
h = l2.encode("utf-8")
h = l2.decode("utf-8")

##4.字符串内建函数： startswith()   endswith()  返回值都是布尔类型True False
# startswith判断是否是以xxx开头的，或者 endswith判断是否是以xxx结尾的
# 应用： 文件上传 ,识别文件类型，比如： 只能上传图片(jpg,png,bmp,gif)
filename = "note.doc"
result = filename.endswith('doc') # 瞅瞅，filename 是不是以doc结尾的啊
print(result)

s = "hello"
result2 = s.startswith('he') #瞅瞅，s 是不是以 he 开头的啊
print(result2)

##那咋识别文件格式呢？其实这个识别文件格式就是识别文件名，然后看看
##文件名是不是以 啥啥后缀结尾的
## 那咋识别文件名啊
path = input("输入文件路径：") #比如我们给一个：D:\pictures\backgroud.jpg
###有了文件路径，就可以用字符串匹配啥的找到文件名
p = path.rfind('\\') #在给定的文件路径从右向左找到第一个"\",
                      
filename = path[p+1:]#那它后边的不就是文件名
### 咋判断是不是图片类型
if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('bmp'):
    print("确实是图片！")
else:
    print("不是图片！")


##5.判断是不是数字，字母
##isalpha()  isdigit()    isalnum()  isnumeric() isdecimal() 这几个都返回布尔类型的结果
##字母        数字(可byte)  数字或字母  数字（可汉字） 数字
##6.连接字符元素或字符串
##join()  join()方法，使用它前边的字符当作间隔符，括号里便的字符串活着列表内的单个字符连接起来
new_str = '@'.join('def')
print(new_str)

###还有一个厉害的，它可以对列表里的元素进行合并
list1 = ["a","b","c","d",1,2,3,4,5]
list2 = []
for i in list1:
    a = str(i)
    list2.append(a)
print(list2)
result = "".join(list2)
print(result)
print(type(result))


##7.分割
##split() splitlines()  count()
##split(‘分隔符’，次数)  分割字符串,将分割后的字符串保存到列表中
s ='hello world hello kitty'
result = s.split(' ',2) 
print(result)
#上边这个 表示按照空格作为分隔符，分割字符串2次,这个两次，就是它只作用两次。就是，它只把字符串s分割成['hello', 'world', 'hello kitty']
# 最后一个空格的地方他没分割，那要想全都分割了怎么整？那就 2 改成 3 呗。
# 那如果是一个特别长的字符串呢？数不过来分割符怎么办？可以用 count()方法数，数完了再分割 
s ='hello world hello kitty'
n = s.count(' ')  # count(args)  求字符串中指定args的个数
print('个数:',n)
result = s.split(' ',n)
print(result)

##splitlines() 方法，就是把字符串分成几行,那你这么聪明，其实可以知道，其实就是以'\n'为分割符，然后覆盖到全部字符串的每一个'\n'，他的返回值是把每一行都保存到一个新的列表里
s ='''hello world hello kitty,hello world hello kitty,
hello world hello kitty,
hello world hello kitty,
hello world hello kitty,

'''
result = s.splitlines()
print(result)


##8.去除空格
## strip()  rstrip() lstrip()
s =' hello world hello kitty '
print(s.lstrip())  #去除左边空格
print(s.rstrip())  #去除右边空格
print(s.strip())  #去除左右边空格，但是去除不了中间的空格
##那，怎么才能去除字符串中间的空格呢？可以把空格替换为 ""
print(s.replace(" ",""))  #无敌！！！！！





```

除了常用的内建函数，还有一些个别的操作，用的时候去查就好

```python
#eval，将字符串当做代码执行
age = 1
print(eval('age + 3'))  # 4
print(eval('+123'))   #123
print(eval('3 + 2'))   #5

#有安全问题
eval("__import__('os').system('dir')") #显示当前目录的文件列表

# repr(x)  返回一个对象的String格式，适合机器执行
a = [20,30]
s1 = repr(a)
list1 = eval(s1)
list2 = str(a)
print(a == list1)
print(a == list2)
```

## 2.元组

元组（tuple)的操作，跟列表基本一样。包括，元素访问，链接，重复，切片，in/not in, 长度（len()），最值（max(),min()）。

```python
#定义元组的时候，不能括号里只放一个元素，识别不了，如果只有一个元素，就得加个"," 
t1 = ("hello",)
#查找（列表也可）
t1 = (10,20,30,10)
print(t1.index(20))  #查找值等于20的第一个元素
print(t1.count(10))  #返回元组中10的个数

#遍历（列表也可）
##同时获取下标和值
## enumerate() 这函数，可以同时获取序列的值和索引，对于字典就是键值对
for index,value in enumerate(t1):
    print(index, value)
    
### enumerate() 适用于各种数据封装格式：
dict2 = {"jack":78,"hanmeimei":99,"lilei":60}
t1 = (10,20,30,10)
s1 = {10,20,30}
l1 = [10,20,30]

for i,j in enumerate(dict2):
    print(i,j)

for i,j in enumerate(t1):
    print(i,j)

for i,j in enumerate(s1):
    print(i,j)

for i,j in enumerate(l1):
    print(i,j)
#这个打印的就是，一堆元组，每个小元组2个值，形成(index,value)的对
for i in enumerate(l1):  
    print(i)

##直接打印 emumerate(l1) ，会返回enumerate对象
print(enumerate(l1))


##通过下标遍历（列表也可）
for i in range(len(t1)):
    print(t1[i])
    
##最大最小值,求和
max(t1)
min(t1)
sum(t1)
# 可以进行 + * 操作,但是这个操作，只能赋予新的变量，不能修改
t1 = (1,2)
t2 = (4,5)
t3 = t1+t2
t4 = t2 * 3
#可以进行排序 sorted()
t3 = (4,5,1,2)
print(sort(t3))  #这个打印出来是个列表，再次强调，不能对元组进行修改
```

## 3.解包

```python
#重要操作：解包！！
#解包就是把序列里的元素，分别拿出去给外边变量赋值的过程，活着就是把这个序列去除，把元素都释放出去， #嗯，就是这样，我就这么理解，哈哈哈哈
#变量个数和元素个数一致
t1 = (11,20)
a, b = t1
print(a,b)  #11 20

a, b = 2, 3  
a,b,c = (1,2,3) 

#变量个数和元素个数不同
#a=10,c=50,_获取（20,30）
a, *_, c = 10,20,30,50
print(a,c,_) #10 50 [20, 30]

#a=10，b=20,c获得剩余的元素
a, b, *c = 10,20,30,50
print(a,b,c) #10 20 [30, 50]

#*解包，这个就是把元组元素都释放出来
print(*(1,2,3))  # 1 2 3

#range解包
a, b, c = range(3)  #a=0,b=1,c=2

#列表解包
a,*_b,c = [1,2,3,4,5]
print(a,_b,c) # 1 [2, 3, 4] 5

#字符串解包
a,b,c = '123'
print(a,b,c) # a='1',b='2',c='3'
```

## 4.字典

```python
#基本赋值，下边这样都成
d1 = {}  #空字典
d1 = dict()  #空字典
d2 = {'name':'麻辣龙虾','taste':'美味'}
d3 = dict(a=1,b=2)
d4 = dict([('a', 1),('b', 2)])
d5 = dict({'a':1,'b':2})

##存储多个学生的成绩
dict1 = {"jack":78,"hanmeimei":99,"lilei":60}
print(dict1)

#1.元素访问
#获取   语法：字典名[key]
print(dict1["hanmeimei"])

#print(dict1["tom"]) #KeyError: 'tom'

#字典名.get(key)
result = dict1.get("lilei",'1')  # 如果没有lilei这个键，返回默认值None，不会报错
print(result)

#2.添加:当指定的键不存在的时候，则表示添加
dict1["tom"]  = 70
print(dict1)
#但是，如果键已经存在，则表示修改value
dict1["jack"]  = 50
print(dict1)

#3. 删除 pop 删除并返回指定键对应的值
#注意：通过键，直接删除整个键值对
dict1.pop("jack")
#pop有返回值，返回的时删除成功的时候，对应键的值
result = dict1.pop("jack")  
print(result)
print(dict1)
#pop可以设置默认值，当想要删除的键值对不存在，可以是设置一个默认的返回值，告诉你出问题了
dict1 = {"jack":78,"hanmeimei":99,"lilei":60}
result = dict1.pop("hhhhhhh","不存在这样的元素")
print(result)

del dict1['lilei'] #删除键值对，不返回值
dict1.clear()  #清空字典
del dict1  #删除整个字典

#4 字典合并
a = {1:'hello'}
b = {2:'world'}
a.update(b)
print(a)

#5.遍历
dict2 = {"jack":78,"hanmeimei":99,"lilei":60}

#方式一：只获取键
#当你就这样简单的用一个变量去遍历字典，你遍历出来的是字典的键
for key in dict2:
    value = dict2[key]
    print(key,value)

print(dict2.keys())
#使用 dict2.keys()方法获取的，是存放所有 键的一个  "dict_key" 对象，要想获取每一个键
#还需要进行遍历
#方式二：只获取值
#values,得到的结果是一个列表，当做列表处理
print(dict2.values())

for value in dict2.values():
    print(value)


#方式三：同时获取键和值
#items,得到的结果是一个列表，列表中的元素是元组
print(dict2.items())  #[('jack', 78), ('hanmeimei', 99), ('lilei', 60)]

for key,value  in dict2.items():
    print(key,value)

#方式四
for index,key in enumerate(dict2):
    value = dict2[key]
    print(index,key,value)

#6.获取键值对的个数
print(len(dict1))

#7.成员操作
d2 = {'name':'麻辣龙虾','taste':'美味'}
print('name' in d2) #判断某个键是否在列表中

#8.其他内置函数
#update()  类似于列表中的 “+”，但是加完了还能去重，字典本身不支持符号运算
dict1.update(dict2) 

#fromkeys() 就是指定key来生成或转换为新字典的方法，如果指定了默认值，那就把它赋予每一个value
#注意，即使你默认值传的是个列表，里边好多值，也是把整个列表当作value去赋值的，这方法可以说很难用了
list1 = ['aa','bb','cc']
dict3.fromkeys(list1,10)
```

## 5.随机数

```python
import  random
```



|          函数名           |                           函数说明                           |
| :-----------------------: | :----------------------------------------------------------: |
|        choice(seq)        |     返回一个序列（列表、元组，字符串）中返回一个随机元素     |
| randrange(start,end,step) | start 指定范围的起始值 包含本身   end 指定范围的结束值 不包含本身 step 步长 |
|         randint()         |                       返回一个随机整数                       |
|       shuffle(seq)        |                将序列元素随机排列（打乱顺序）                |

## 