# python 基础 06

## 1.匿名函数

匿名函数也叫一句话函数。基础就是列表推导式。

```python
# lambda function
# lambda 参数1，参数2：表达式
# lambda 函数常与内置函数一起用
# 不要硬用，不是非得用，想不通匿名函数就用普通函数就好
#语法:

# 　　函数名 = lambda 参数:返回值

#     1）此函数不是没有名字，他是有名字的，他的名字就是你给其设置的变量，比如func.

#     2）lambda 是定义匿名函数的关键字，相当于函数的def.

#     3）lambda 后面直接加形参，形参加多少都可以，只要用逗号隔开就行。

func1 = lambda a,b:a+b 
print(func1(1,2))

#写匿名函数：接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）。
func2 = lambda a:(a[0],a[2])
print(func2([1,2,3,4]))

#写匿名函数：接收两个int参数，将较大的数据返回。
func3 = lambda a,b:a if a>b else b
print(func3(1,4))
```

## 2. 闭包

```python
#闭包：封闭的东西：保证数据的安全
#闭包是内层函数对外层函数非全局变量的引用
#被引用的外层函数变量称为自由变量，这个自由变量会与内层函数产生一个绑定关系
#自由变量不会消失
#这个自由变量就是我们要保证安全的数据
#闭包只存在于嵌套函数
#判断是不是闭包：
#1.嵌套函数
#2.内层函数必须引用外层函数的变量或者参数
#3.闭包肯定含有自由变量，可以用 .__code__.co_freevars  方法来判断是不是闭包

'''
例如：整个历史中的某个商品的平均收盘价。什么叫平局收盘价呢？就是从这个商品一出现开始，每天记录当天价格，然后计算他的平均值：平均值要考虑直至目前为止所有的价格。

比如大众推出了一款新车：小白轿车。

第一天价格为：100000元，平均收盘价：100000元

第二天价格为：110000元，平均收盘价：（100000 + 110000）/2 元

第三天价格为：120000元，平均收盘价：（100000 + 110000 + 120000）/3 元

........
'''

l1 = [] #全局变量，数据不安全

def make_average(new_value):
	l1.append(new_value)
	total = sum(l1)
	average = total/len(l1)
	return average
print(make_average(10000))
print(make_average(11000))
print(make_average(12000))

#怎么改呢？l1 不能是全局变量
def make_average2():
	l1=[]
	def averager(new_value):
		l1.append(new_value)
		total = sum(l1)
		return total/len(l1)
	return averager

avg = make_average2()
print(list(map(avg,[10000,11000,12000])))
print(avg.__code__.co_freevars)   #('l1',)
#我们可以这样，定义外层函数，在外层函数声明我们想要保护的数据
#在内层函数中对这些数据进行修改，在内层函数中返回处理结果
#然后在外层中返回内层函数名

#判断是是不是闭包的代码
def wrapper(a,b):
	def inner():
		print(a)
		print(b)
	return inner

a = 2 
b = 3 
ret = wrapper(a,b)
print(ret.__code__.co_freevars)  #('a', 'b')

```

## 3. 重要的内置函数

```python
#内置函数
#print(self,*args,sep=' ',end='\n',file=None)
print(1,2,3,4,sep='|')
print(1,2,3,4,end='\t')

#list() 转换为列表
l1 = list('sjfoiwjfosj')
print(l1)

#dict() 转换为字典
#创建字典
dict1 = dict([(1,"one"),(2,"two")])
dict2 = dict(one=1,two=2)
l2 = [1,2,3,4]

dict3 = dict.fromkeys(l2,10)
print(dict1)
print(dict2)
print(dict3)

#abs() 求绝对值 ***
print(abs(-6))

#sum() 求一个可迭代对象的和
l3 = [i for i in range(10)]
print(sum(l3))
#sum() 可以设置初始值
print(sum(l3,100)) #就是，把100加到 l3 的加和里

#reverse() 
#列表的 list.reverse()方法是直接对原列表进行翻转
#reversed() 函数 , 是把对传入列表进行处理，产生一个新的翻转的迭代器
l4 = [i for i in range(10)]
obj = reversed(l4)
print(list(obj))

#zip() 函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,

#然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回 
l5 = [1,2,3,4,5]
tu1 = ('太白','b哥','degang')
s1 = 'abcd'
obj = zip(l5,tu1,s1)
for i in obj:
	print(i) 
#(1, '太白', 'a')
#(2, 'b哥', 'b')
#(3, 'degang', 'c')

print(list(obj)) #[(1, '太白', 'a'), (2, 'b哥', 'b'), (3, 'degang', 'c')]


#*********以下方法超级重要***********

#min() max() 
l6 = [33,2,1,54,7,-1,-9]
print(min(l6))
##以绝对值的方式取最小值,min()和max() 函数,有参数 key=参数名，可以
##对传入的可第二代对象中的每一个量传入 key 指定函数后，再求函数结果的
##最小值，函数名可以直接用匿名函数替代
print(min(l6,key=abs))
print(max(l6,key=abs))

#求出值最小的键
dic = {'a':3,'b':2,'c':1}
#如果直接用min,min()函数会取比较dic的键，而不是值
print(min(dic))
#要这么写，dict类型也是可迭代的，只是迭代的是键，没有值
print(min(dic,key = lambda a:dic[a] ))

#求出年龄最小的那个人的元组
l7 = [('太白',18),('alex',73),('wusir',35),('口天吴',42)]
print(min(l7,key=lambda a:a[1]))

#sorted() 排序，他也有个 key 参数
l8 = [22,33,1,2,8,7,6,5]
print(sorted(l8))

# l7列表中，让列表按年龄从小到大排序
print(sorted(l7,key=lambda a:a[1]))
# l7列表中，让列表按年龄从大到小
print(sorted(l7,key=lambda a:a[1],reverse=True))


#filter() 筛选，可用于列表推导式的筛选模式,返回值是个迭代器
print([i for i in l8 if i>3])
print(list(filter(lambda a:a>3,l8))) #因为filter()返回迭代器，所以打印要加 list()

#map() 函数，有俩参数，第一个参数是个函数名，第二个参数是个可迭代对象，把第二个参数书传入第一个参数的函数，并执行
#map() 返回值是个迭代器
l9 = [1,4,9,16,25]
print([i**2 for i in range(1,6)])
print(list(map(lambda a:a**2,range(1,6))))

##普遍一点,这样
def func3(a):
	return a**2
print(list(map(func3,l9)))


#reduce() 函数 
# reduce 的使用方式:
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行
#reduce() 函数是 functools 包里边的一个函数
#reduce的作用是先把列表中的前俩个元素取出计算出一个值然后临时保存着,
#接下来用这个临时保存的值和列表中第三个元素进行计算,求出一个新的值将最开始
#临时保存的值覆盖掉,然后在用这个新的临时值和列表中第四个元素计算.依次类
from functools import reduce
def func4(x,y):
	return x*10+y
#     # 第一次的时候 x是1 y是2  x乘以10就是10,然后加上y也就是2最终结果是12然后临时存储起来了
#     # 第二次的时候x是临时存储的值12 x乘以10就是 120 然后加上y也就是3最终结果是123临时存储起来了
#     # 第三次的时候x是临时存储的值123 x乘以10就是 1230 然后加上y也就是4最终结果是1234然后返回了
# ​
ret = reduce(func4,[1,2,3,4])
print(ret)

#lambda 
print(reduce(lambda x,y:x*10+y,[1,2,3,4]))
```

