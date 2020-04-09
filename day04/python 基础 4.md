# python 基础 4

## 1.递归

1.递归就是函数自己调用自己，递归必须设置弹出条件。就是结束条件

2.每次进入更深一层的递归，问题规模必须比上一次小

3.

```python
def calc(n):
	print(n)
	if int(n/2)==0:
		return n
	res = calc(int(n/2))
	return res

calc(10)
a = calc(10)
print(a)
```



## 2.文件

```python
# 要知道文件的路径 path
# 文件的打开方式 r w 
# 编码方式 encoding  decode 

```

## 3. 迭代器

```python
#判断一个对象是不是可迭代对象，可以用 dir() 函数 来获取这个对象的所有方法，如果里边#有 "___iter__",他就是可迭代对象
s1 = 'fjdskd'
#print(dir(s1))
print('__iter__' in dir(s1)) #返回的布尔值为True就是可迭代的

# 可迭代对象有 str  list  tuple  dict  set  range  文件句柄等
# 可迭代对象优点
# 1.存储的数据直接可以显示，比较直观
# 2.拥有的方法比多，操作方便
# 缺点：
# 1.占用内存高
# 2.不能直接通过 for 循环，不能直接取值，必须先转化成迭代器


# 啥是迭代器？
# 内部含有'__iter__' 并且含有 '__next__' 方法的对象就是迭代器
# 判断是否是迭代器，就判断'__iter__'和'__next__' 在不在dir(对象)中
# 判断文件句柄是不是迭代器
#判断对象是否是迭代器
with open('file1',encoding='utf-8',mode='w') as f1:
	print(('__iter__' in dir(f1)) and ('__next__' in dir(f1)))

#可迭代对象可以转化为迭代器
s1 = 'jofjs'
obj = iter(s1) #或者 s1.__iter__() 都可以
print(obj)

#迭代器可以一个一个取值,下边这俩都行，每写一次迭代代码，就弹出来一个值
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__()) 
print(next(obj)) #print(obj.__next__())
#如果迭代超出范围了，就会报错

l1 = [1,2,3,4,5,6,7]
obj2 = iter(l1)
print(next(obj2))
print(next(obj2))
print(next(obj2))
print(next(obj2))
print(next(obj2))
print(next(obj2))
print(next(obj2))
print(next(obj2))
#for i in range(7):
#	print(next(obj2))

##迭代器有啥用呢？
##迭代器的优点：
##1.节省内存！
##2.惰性机制，执行一个next()就取一个值，不next()就不取值。有一个迭代器模式可以很好的解释上面这两条：迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。这就是迭代器模式。
##缺点：
##1.速度慢
##2.不走回头路的，他会记住你当前取值的位置，你下一次取值不执行，就一直在这停留



#可迭代对象于迭代器的对比
1. 可迭代对象是一个操作方法比较多，比较直观，存储数据相对少的数据集
2. 当你侧重于对数据的灵活处理，并且内存足够多的时候，可迭代对象是好的选择

1.是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。
2当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。（可参考为什么python把文件句柄设置成迭代器）。

#while 循环模拟 for循环对可迭代对象的取值
l1 = [1,2,3,4,5,6,7,8]
#将可迭代对象转化为迭代器
obj = iter(l1)
while True:
	try:
		print(next(obj))
	except StopIteration:
		break

```

