# python 基础 day03

## 1.冒泡排序

```python
"""
冒泡排序，虽然，python自带 sort() 方法 和 sorted() 函数，但是还是要会
主要思想就是，一个列表，从前往后遍历，然后判断，要是后边的比前边的小就互换值，嗯，就是这样
"""
def bubbleSort(a_list):
    for i in range(len(a_list)):  #我们可能要循环列表好几遍，为啥呢，你笨想，一遍肯定不能把小值都拖到前边，得好几遍
        for j in range(0,len(a_list)-1-i):  #为啥要 -i ？，当 i = 0 ,第二层循环遍历范围是整个列表；当 i=1，第二层遍历的是没有最后一个元素的列表
            if a_list[j] > a_list[j+1]:     # 为啥要这么干？ 因为，我们遍历换位置操作，其实是将大值向后移动，在第一次遍历，最大值就会被移动到最后完成排序了，就不用再遍历它了
                a_list[j],a_list[j+1]=a_list[j+1],a_list[j]
    return a_list

list1 =   [64, 34, 25, 12, 22, 11, 90]
def main():
    new_list = bubbleSort(list1)
    print(new_list)
    print("排序完毕！")

if __name__ == "__main__":
    main()

```

## 2. 函数

## 一、集合（set)

特点:不允许有重复元素，如果添加重复元素，则会自动过滤，可以进行交集、并集的运算。

本质：无序且无重复元素的数据结构

### 1 创建集合

~~~python
s1 = set()  #空集合  不能是{}，这是字典
s2 = {1,2,3,4}
print(s1)
print(set([30,40,50]))  #通过列表创建
print(set((11,22,33)))  #通过元组创建
print(set('hello'))     #通过字符串创建  
print(set({'name':'大宝','age':20}))   #通过字典创建,得到一个键的集合

#注意：重复元素在set中会被自动过滤
#set 不支持 +  和 *  的运算
~~~

### 2 集合操作

~~~python
#1 增加
#add添加不可变元素
s1.add(5)
# s1.add([6,7]) #不能添加列表，列表和字典都是不可哈希的
s1.add((6,7))  #可以添加元组元素，元组是可哈希的
print(s1)

#set.update(s) s必须是可迭代的对象：列表、元组、字符串、字典
#update会把列表、元组、字符串打碎添加到集合中
s1 = {1,2,3,4}
s1.update([5,6])
s1.update((7,8))
s1.update('hello')
s1.update({'1':10,'2':20})  #将字典的键添加到s1
print(s1)

#2 删除
#set.remove(elem)，如果没有该元素也不报错
set3 = {1,2,3,4,5,6}
set3.remove(4)  #直接删除指定元素
print(set3)

print(set3.pop()) #删除任意元素，并返回该元素的值
print(set3)
#set.discard() #删除的元素不存在，不会报错
set3.discard(10) 
#set3.remove(10) #如果元素不存在，则报错：KeyError

#3元素个数
print(len(set3))

#4 成员操作
print(2 in set3)  #True

#5 并、交、差集
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1 | s2)  #并集
print(s1.union(s2))  #并集
s1.union_updaet(s2) #这表示求并集，并把并集赋值给s1
print(s1 & s2)  #交集
print(s1.intersection(s2)) #交集
s1.intersection_update(s2) #这表示求交集，并把交集赋值给s1
print(s1 - s2)  #差集
print(s1.difference(s2)) #差集 
s1.difference_update(s2) #这表示求差集，并把差集赋值给s1

#6.亦或 "^" 和对称差集
#对称差集和 "^" 求的是两个序列除去交集以后的部分
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2) ##这表示求对称差集，并把对称差集赋值给s1

#7.子集于超集
set1 = {1,2,3}
set2 = {1,2,3,4,5,6}

print(set1 < set2)
print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

print(set2 > set1)
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集。


~~~

## 二、补充

### 2.1数据类型的转换

|  函数名  |           函数值            |
| :------: | :-------------------------: |
|  int(x)  |      将x转换为int类型       |
| float(x) |       将x转换成浮点型       |
|  str(x)  |       将x转换成字符串       |
| bool(x)  | 转换成bool类型 的True False |
| dict(x)  |      将序列x转换成字典      |
| list(x)  |      将序列x转换成列表      |
|  set(x)  |      将序列x转换成集合      |
| tuple(x) |      将序列x转换成元组      |

### 2.2布尔值

在python中，能够解释为假的值有：None、0、0.0、False、所有的空容器（空列表、空元组、空字典、空集合、空字符串），其它是真

### 2.3 zip函数

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

语法：zip(iterable1,iterable2, ...)

参数说明：iterable -- 一个或多个可迭代对象（字符串、列表、元祖、字典）

~~~python
a = [1,2,3,4]
b = [2,3,4]
res = zip(a,b)
print(list(res))  #[(1, 2), (2, 3), (3, 4)]
# 可以使用for-in 遍历
for x,y in zip(a,b):
    print(x,y)
~~~

### 2.4 列表推导式

运用列表推导式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

```python
#列表推导式语法：
[exp for iter_var in iterable] 
执行for-in循环时，通过iter_var遍历iterable每一项，exp表达式中可以直接使用iter_var，每遍历一项，产生一个新的列表元素。
#生成[0,1,4,9,16,25]
[x*x for x in range(6)]

#生成[0,4,16,36,64]
l2 = [x*x for x in range(9) if x % 2 ==0]
print(l2)

#可以使用双重循环
suit = ['♥','♦','♣','♠']
face = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
poke = [(x,y) for x in suit for y in face]

#字典推导式
#列表生成式可以使用两个变量,实现字典的键值交换
d = {"X":"A","Y":"B","Z":"C"}
list5 = {v:k for k,v in d.items()}
print(list5)

#集合推导式
print({x for x in range(10)})

#练习：
1.将一个列表中所有的字符串变成小写
  l = ["Hello","World","IBM","Apple"]
如果是这样的列表呢
  l =  ["Hello","World",10,"IBM","Apple"]
```

### 2.5 可变与不可变对象

```python
# 不可变
指向内存的值是不变的 int float str tutle 
# 可变
该对象指向的内存的值是可变的
可变类型：字典 列表 集合  list  dict  set
 
```

### 2.6 判断是不是各种类型

```python
# isinstance()
isinstance(2,int)
isinstance(a_list,list)
isinstance(a_tuple,tuple)
isinstance(a_set,set)
isinstance(a_dict,dict)

```



## 三、函数引入

前面我们写过九九乘法表，但如果我要七七乘法表或五五乘法表的话，你会看到三者代码极其类似，只是循环变量不同，那么如何做到代码重用，而不是简单拷贝黏贴修改呢，其实可是使用函数完成这一功能

~~~python
def table(row,col,sep=3):
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if j <= i:
                print("%d*%d = %2d" % (i, j, i * j), end='%*s'%(sep,' '))
        print('')
#一次编码，到处运行
table(8,8)
table(5,5,8)
~~~

函数的优点：

- 代码可复用
- 代码可维护性高
- 容易排错
- 可读性好
- 利于团队开发

### 1.函数定义

函数就是完成特定功能的代码块，本质上是对代码的封装。 语法格式

~~~python
def 函数名（[参数1],[参数2]....[参数n]）:
	函数体
~~~

- 函数名命名规则同变量名，要满足标识符命名规则
- 不能和系统函数重名，否则系统函数无法使用
- 函数定义分两部分函数头和函数体
- 函数体，就是实现功能的代码段，以：开头，必须缩进
- 函数名的命名风格：一般建议用下划线分隔的小写单词组成：say_hello

### 2 函数参数

#### 2.1 实参和形参

- 形参：就是函数定义时小括号里的变量
- 实参：函数调用的时候，小括号里的表达式
- 函数可以没有形参和实参

#### 2.2 参数分类

- 位置参数，要求实参顺序必须和形参顺序完全一致，由形参顺序决定实参顺序

  ~~~python
  def say_hello(name,age,home):
      print('大家好，我是{},我今年{}岁了，我来自{}'.format(name,age,home))
  
  say_hello('王二妮',18,'湖北武汉') #实参个数、顺序必须和形参一致
  ~~~

- 关键字参数，函数调用时，实参可以是键值对，键就是形参名字，这样的调用，实参不必关心形参的顺序。

  ~~~python
  def say_hello(name,age,home):
      print('大家好，我是{},我今年{}岁了，我来自{}'.format(name,age,home))
  
  say_hello(name='王二傻',home='大连',age=20)  #三个关键字参数
  say_hello('大傻',home='美国',age=30)  #两个关键字参数
  sya_hello('二傻',24,home='何方')    #一个关键字参数
  ~~~

- 默认值，如果形参在定义的时候给定一个值，那么函数在调用时就可以不传实参，可以简化调用

  - 默认值参数必须放到最右边
  - 如果传了实参，那么实参优先，不会使用默认值
  - 默认值只计算一次
  - 默认值必须是不可变对象
  - 如果默认参数指向的是一个可变数据类型，那你无论调用多少次默认参数，都是同一个对象，除非你给它传个参数,你给他穿个参数，也只是你这一次调用不一样了，原来的还在，如果你继续默认调用，就还是他

  ~~~python
  def my_power(x,n=2):
  	return (x) ** n
  my_power(3)
  my_power(4,0.5)
  
  def test(a=[]):
      a.append('end')
      print(a)
  test([1,2,3])
  test()   #['end']
  test()   #['end','end']
  #默认值参数指向一个可变类型
  def func(a,list=[]):
      list.append(a)
      return list
  ret1 = func(10,) # ret1 = [10,]
  ret2 = func(20,[]) # ret2 = [20,]
  ret3 = func(100,) # ret3 = [10,100]
  print(func(10,)) #[10,100]
  print(func(20,[])) #[20]
  print(func(100,))#[10,100]
  ~~~

- 可变参数，传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

  ~~~python
  #使用*接收任意数量的位置参数
   #注意：*的不定长参数被当做元组处理
  def demo(a,b,*args):
      print(a,b,args)
  
  demo(12,33,90)
  demo(1,2,3,4,5)
  a=(1,2,3)
  demo(*a)
  
  #使用**接收任意数量的关键字参数
  #注意:**的不定长参数被当做字典处理
  def demo1(a,**args):
      print(a,args)
  demo1(1,name='kk',age=3)
  b = {'a':20,'b':12,'c':32}
  demo(**b)
  
  ## 定义函数参数时，用*args 和 **keargs 就是在装包
  # 调用函数时，传输入参数，用 *args 和 **kwargs 就是在解包
  ~~~


#### 2.3 参数组合

- 形参顺序须按照以下顺序：位置参数、默认值参数、*args,**kwargs

#### 2.4 命令行参数（了解）

如果要获取命令行下传给python文件的参数可以使用体统模块sys的argv来获取

参数个数：len(sys.argv)

文件名：sys.argv[0]

参数：sys.argv[1],sys.argv[2].....

~~~python
# 文件名: 1.py
import sys
print(len(sys.argv))
print(sys.argv[0])
print(sys.argv[1])
~~~

在命令行下执行：python 1.py 2 3 4

### 3 函数调用

- 函数调用必须在函数定义之后

- 函数调用必须能够正确传递实参

  ~~~python
  def demo(a,b,c=0,*arg1,**arg2):
  	print(a,b,c,arg1,arg2)
  demo(1,3,k=4)
  demo(1,2,3,4,5)
  demo(1,b=3,c=3,d=5)
  demo(*(1,2,3),**{'name':12})  #任何函数都可通过这种形式传递参数
  ~~~

### 4 返回值

可以通过return语句返回计算结果。语法：  return 表达式

- return的作用一个是终止函数的执行，所有执行了return后，其后的语句不会被执行

- 如果没有return语句，则默认返回的是None

- return还可以返回给调用者数值

- return可以返回一个值，如果要返回多个值，那么返回的是一个元组

  ~~~python
  def demo2():
      return 1
  def demo3():
      return 1,2,3
  print(demo2())
  print(demo3())  #(1,2,3)
  ~~~

### 5 文档字符串

函数文档字符串documentation string （docstring）是在函数开头，用来解释其接口的字符串。简而言之：帮助文档

- 包含函数的基础信息
- 包含函数的功能简介
- 包含每个形参的类型，使用等信息

文档字符串书写规则：

- 必须在函数的首行

- 使用三引号注解的多行字符串(''' ''') 或(""" """)

- 函数文档的第一行一般概述函数的主要功能，第二行空，第三行详细描述。

  ~~~python
  def test():
      """
          函数名：test
          功能：测试
          参数：无
          返回值：无
      """
      print("函数输出成功")
  
  #使用__doc__属性查看文档字符串
  print(test.__doc__)
  ~~~


### 6.参数传递(**)

python的参数传递是简单的值传递，当然这里的值是指变量的引用（地址），不是变量的值。不存在值传递和引用传递的区分。简而言之，python的参数传递可以称之为对象引用传递，对象可以分为：

- 不可变对象：int、float、None、complex、bool、tuple、str,range
  - 在函数内部不可能修改函数外部的变量
- 可变对象: dict、list
  - 可以在函数内部修改

### 7 空函数

借助于pass语句实现，函数体不完成任何功能，只有一个pass语句

~~~python
def test():
    pass # 占位符
~~~



### 8 全局变量与局部变量

- 如果你在定义变量之前引用变量，会报错，变量必须先定义，后引用

```python
# global 
# 当全局变量是不可变类型的时候，我们还想要在函数里对他进行修改，就得在函数里进行global声明
# 当全局变量是可变类型的时候，我们即使不在函数里进行global声明，也可以在函数里对它进行修改
# 一般golbal 声明都要在函数一开始的时候，global 也可以直接在函数里新声明一个变量
a = "外部定义的变量"
list1 = ['外部定义的变量']
def func():
    print(a)
    print(list1)
def func1():
    global a 
    #我们在函数里声明将要修改全局变量，那我们在函数内的修改不需要返回值就可以改变外部变量
    a = a + "hhhhh"
    list1.append(a)
    print(a)
    print(list1)

def func2():
    #如果我们声明要使用全局变量，我们函数里用的各种变量都随便是什么名字，跟外边都没关系
    a = "莫哈哈"
    list1 = [1,2,3,4]
    print(a)
    print(list1)
 

func()  # 这个打印出来的是 "外部定义的变量" ["外部定义的变量"]
func1() # 这个打印出来的是 "外部定义的变量hhhhh" ["外部定义的变量","外部定义的变量hhhhh"]
func2()  # 这个打印出来的是 "莫哈哈" [1,2,3,4]



## 所以还是要注意，全局变量名和函数内部的变量名还是整成不一样的好。起名字是程序员最大的难点。

#内部函数
#1.内部函数可以访问外部函数的变量
#2.内部函数可以修改外部函数可变类型的变量
#3.内部函数在无声明情况下不可修改外部函数的不可变类型变量
#4.这个声明 是 nonlocal,要加在内部函数里，nonlocal 不能影响全局变量。
#5.内部函数修改全局的不可变类型变量，需要在内部函数内部声明 global
#locals()函数返回一个字典，包含当前函数内声明的内容有什么
#globals()函数返回一个字典，包含当前的全局变量有什么
#调用外部函数


m = 2020
def func():
	#声明变量,都是局部变量
	n = 100
	list1 = [1,2,3,4]

	#内部函数
	#在函数内部声明另外一个函数
	def inner_func():
		#声明要对全局变量m进行修改
		global m
		#声明要对外部函数不可变类型变量n进行修改
		nonlocal n  
		#对list1里面的元素进行加5操作
		for index,i in enumerate(list1):
			list1[index]=i+n

		list1.sort()
		n +=1
		m += 1
	#调用内部函数
	inner_func()
	print(list1)
	print(n)
	print(m)
	print(locals()) #locals()函数返回一个字典，包含当前函数内声明的内容有什么
	print(globals()) #globals()函数返回一个字典，包含当前的全局变量有什么
#调用外部函数
func()



```

### 9.闭包

```python
#当函数定义内部函数，且返回值时内部函数名，就叫闭包
#1.闭包必须是外部函数种定义了内部函数
#2.外部函数是有返回值的，且该返回值就是内部函数名，不能加括号
#3.内部函数引用外部函数的变量值
'''
闭包格式：

def 外部函数()：
	...
	def 内部函数():
		...
	return 内部函数
'''
def func():
	a = 100

	def inner_func():
		b = 99
		print(a,b)

	print(inner_func)
	return inner_func


#调用函数时，用对象接住函数返回的内部函数，那其实，这个对象x就变成了func()的内部函数，当使用 x() 是可以调用它
x = func()

x()
```

