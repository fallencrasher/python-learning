# python 基础 05

## 1.生成器

```python
#生成器
#生成器的本质就是迭代器。他与迭代器的区别是，生成器是我么自己用py#thon代码构建的数据结构，迭代器是他提供的，或者转化来的

#获取生成器的三种方式：
##生成器函数
##生成器表达式
##python内部提供的一些

#生成器函数获取生成器

def func():
	print(111)
	print(222)
	yield 3
	yield 4
ret = func() 
#ret就变成了生成器对象，因为生成器本质上是个迭代器，所以这个ret就是个迭代器对象，普通打印只能打印内存地址
print(ret)  #<generator object func at 0x01DA83E0>
#要想打印ret，要用到 next() 函数 或 __next__ 方法
print(next(ret))  #或 print(ret.__next__())
print(ret.__next__())


#return yield
#return : 函数中只存在一个return结束函数，并且给函数执行者返回值
#yield  : 只要函数中有 yield ，函数就是生成器函数，yield 不结束
# 函数，一个yield对应一个next()

#吃包子
#用可迭代对象
def func3():
	l1 = []
	for i in range(1,5001):
		l1.append(f"{i}号包子")
	return l1
ret = func3()
print(ret)

#用生成器
def func2():
	for i in range(1,5001):
		yield f"{i}号包子"

ret = func2()

for i in range(200):
	print(next(ret))


#yield from
def func4():
	l1 = [1,2,3,4,5]	
	yield from l1
	#将列表变成迭代器返回
ret =  func4()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))

#如果使用多个 yield from,那就会先把第一个 yield from 迭代完了再执行第二个

def func():
    lst1 = ['卫龙','老冰棍','北冰洋','牛羊配']
    lst2 = ['馒头','花卷','豆包','大饼']
    yield from lst1
    yield from lst2
    
g = func()
#因为，g是个迭代器了，就可以直接用for 循环去遍历他，然后打印，for循环内
#本来就是要把可迭代对象转换为迭代器然后一个一个执行的
for i in g:
    print(i)
    
# 简述一下yield 与yield from的区别。
#
# 看下面代码，能否对其简化？说说你简化后的优点？
#
#
def chain(*args):
    # ('abc',(0,1,2))
    for it in args:
        for i in it:
            yield i
g = chain('abc',(0,1,2))
怎么让生成器产出值？
next ，for 循环, 转化成list
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(list(g))
print(list(g))  # 将迭代器转化成列表


def chain(*args):
    # ('abc',(0,1,2))
    for it in args:
        yield from it  # 'abc'  (0,1,2)
g = chain('abc',(0,1,2))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(list(g))

# yield from 优化了内层循环，提高了效率。
def func():
    # yield [1,2,3]
    yield from [1,2,3]
    '''
    yield 1
    yield 2
    yield 3
    '''
g = func()
print(next(g))
print(next(g))
print(next(g))
```

## 2.列表推导式

```python
#用一行代码构建一个比较复杂且有规律的列表
#列表推导式分为两种：
#1.循环模式：[表达式 for i in iterable] 
#2.筛选模式：[表达式 for i in iterable if 条件]
#列表推倒式只能构建比较复杂且有规律的列表
#超过三层循环才能构建成功的列表不推荐使用
#查找错误能力低，不好看出来错误。debug模式不行
#但是列表推导式更简单，更装逼。

#比如我们创建一个含有1-10的列表，原来都这么干
l1=[]

for i in range(1,11):
	l1.append(i)

print(l1)

#用列表推倒式
l1 = [i for i in range(1,11)]
print(l1)

#循环模式
##将10以内所有整数的平方写入列表
l2 = [i*i for i in range(1,11)]
print(l2)

##100以内所有的偶数写入列表
l3 = [i for i in range(1,101) if i%2==0]
print(l3)

##从'python1期'到'python100期'写入列表lst
l4 = [f'python{i}期' for i in range(1,101)]
print(l4)

#筛选模式
##30以内能被3整除的数
l5 = [i for i in range(1,31) if i%3==0]
print(l5)

#过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
l6 = [i.upper() for i in l if len(i)>=3]
print(l6)

#找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

l7 = [name for i in names for name in i if name.count('e')==2]
print(l7)

#用列表推导式构建一个列表[2,3,4,5,6,7,8,9,10,'J','Q','k','A']
l8 = [i for i in range(2,11)]+list('JQKA')
print(l8)
```

## 3.生成器表达式

```python
#生成器表达式
#与列表推倒式写法几乎一模一样
#就是把列表推倒式的中括号[]改成小括号()
#与列表推导式的区别
#写法上：[] ()
#本质上，列表推导式得到个iterable对象，生成器表达式得到一个生成器iterator


#列表推导式
print([i for i in range(1,11)])

#生成器表达式，有点就是省内存
obj = (i for i in range(1,11))

for i in obj:
	print(i)

```

## 4.字典推导式与集合推导式

```python
#字典推导式
#
lst1 = ['jay','jj','meet']
lst2 = ['周杰伦','林俊杰','郭宝元']

dict1 = {lst2[i]:lst1[i] for i in range(len(lst1))}
print(dict1)

#集合推导式
s1 = {i for i in range(1,11)}
print(s1)
```

## 5.次要的内置函数

```python
#内置函数 68个
#这个文件里边的，了解就好
#次重要的内置函数

# eval() 剥去字符串外衣，把字符串当代码运行,这个东西很危险据说，
# 在网络传输的 str input 输入的时候，sql注入的时候绝对不用
# eval()是有返回值的
s1 = '1 + 3'
print(s1)
print(eval(s1))

s = '{"name":"alex"}'
print(s,type(s))
#print(dict(s)) #会报错
print(eval(s),type(eval(s)))

# exec() 与eval()几乎一样，处理代码流的
msg = '''
for i in range(10):
	print(i)
'''
print(msg)
exec(msg)

#hash() 获取一个对象的哈希值
# 不可变对象才具有哈希值

print(hash('owfjfosjfio'))

# help() 获取方法对象的使用方法
print(help(str))
print(help(str.upper))

# callable() 判断一个对象是否可调用,就是能不能加括号()
s1 = 'jsofjiofjio'
print(callable(s1))
def func():
	pass
print(callable(func))

# int() 将一个字符串或数字转换为整型

# float() 将整数或字符串转换成浮点数

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
print(complex(1,2))

# bin() 将十进制转化为二进制字符串并返回
print(bin(10),type(bin(10)))  # 0b1010 <class 'str'>

# oct() 将十进制转化为八进制字符串并返回
print(oct(10),type(oct(10)))  # 0o12 <class 'str'>

# hex() 将十进制转换为十六进制字符串并返回
print(hex(10),type(hex(10)))  # 0xa <class 'str'>

# divmod() 计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)
print(divmod(7,2))  # (3, 1)

# round() 保留浮点数的小数位数，默认保留整数
print(round(7/3,2))
print(round(7/3))
print(round(3.1415926,3))

# pow() 求x**y次幂，三个参数为 x**y 的结果对 z 取余(取对数)
print(pow(2,3))
print(pow(2,3,3))

# bytes() 用于不同编码之间的转化
s = '你好'
bs = s.encode('utf-8')
print(bs)
s1 = bs.decode('utf-8')
print(s1)
bs = bytes(s,encoding='utf-8')
print(bs)
b = '你好'.encode('gbk')
b1 = b.decode('gbk')
print(b1.encode('utf-8'))

# ord() 输入字符找该字符的编码的位置
print(ord('a'))
print(ord('中'))

# chr 输入位置数字找出其相对应的字符
print(chr(97))
print(chr(20013))

# repr() 返回一个对象的 string 形式，原形毕露
#%r  原封不动的写出来
name = 'taibai'
print('我叫%r'%name)

# repr 原形毕露
print(repr('{"name":"alex"}'))
print('{"name":"alex"}')

# all() 可迭代对象中全是 True 才是 True
print(all([1,2,True,0]))

# any() 可迭代对象中，有一个True 就是 True
print(any([1,'',0]))

```

