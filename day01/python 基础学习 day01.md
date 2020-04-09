# python 基础学习

声明：我对自己说，学习python这个东西，最重要的不是所有东西都记住，而是知道有这么个知识，有这么回事，然后知道知识具体都记录在哪就行了。比如，当我们用正则匹配一个字符串，最后还不想要字符串里的空格，那字符串里就有方法，是什么方法？去找！反正有这个方法。找到以后有很多关于去除字符串空格的方法，看说明就用就好。像 `rstrip(), lstrip(), strip()`,看一眼啥意思，咋用，用多了就记住了。

## 1. DOS 命令

```dos
# 切换目录
cd [dir]
cd        #进入指定目录
cd ..      # 退回到上一级目录
cd ..\..  #  向上退回两级目录
cd \      # 切换到根目录
## 切换盘符，直接写盘符名称+：
d：

#显示当前目录内容
dir

# 创建目录
mkdir [dirname] #这就是新建文件夹

# 删除目录
rmdir [dirname] #删除文件夹

#清空控制台
cls

# 获取本机网络ip
ipconfig

# 测试网络是否畅通
ping [地址]

# 重定向
pip freeze > req.txt  # 是不是很想linux

```

## 2. windows 下的环境变量添加

我们需要把python添加到环境变量，这个在安装时候就有个选项，选上就行。或者右键我的电脑——>属性——>高级系统设置——>环境变量——>双击系统变量里的path——>添加python.exe所在目录(../python3.8)和pip所在目录（../python3.8/Scripts/)到环境变量

## 3. 包管理

```DOS
# pip [command] [options]
# 安装一个包,默认最新版本
pip install redis
# 指定安装包版本
pip install redis==3.2.0  #两个等号哦，不是--
# 卸载包
pip uninstall redis
# 看看自己都有啥包啊
pip list
# pip 对包进行版本更新，这个命令对pip自己也管用
pip Install --upgrade redis
pip install --upgrade  #要是你不指定宝名，就是所有包都更新
# 查看pip版本
pip --version
# 更新pip版本,dos下
python -m pip intall --upgrade pip

# 查看pip使用帮助 
pip freeze --help  # 如果我们不会用 pip 下freeze这个命令，可以--help
# 输出所有包名和版本号,并重定向输出到 一个文件，文件不存在就自动创建
pip freeze > requirements.txt  #方便以后再安装包的时候方便，可以一行命令装所有包
# 根据给定的报名列表和版本号，安装多个包
pip install -r requirements.txt  #你看这刚才那个导出的文件就用上了，这个用在开发环境迁移

# 注意：所有的pip安装的包都在目录 ..\python3.8\lib\site-packages里边

##配置pip镜像，就换换清华源什么的
pip install pip -U #先升级pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

##要是只是想临时是由什么源进行包的安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U #也可以用来进行pip升级
```

## 4.转义字符

| 转义字符   | 描述          | 转义字符 | 描述       |
| ------ | ----------- | ---- | -------- |
| `\'`   | 表示一个普通字符单引号 | \r   | 回车       |
| `\"`   | 表示一个普通字符双引号 | \n   | 换行       |
| `\'''` | 一个普通的三单引号   | `\\` | 一个普通的字符\  |
| `\"""` | 一个普通的三双引号   | \a   | 响铃       |
| \t     | tab键        | \b   | 回删一个字符   |

## 5. print()函数使用

```python
# 这里只说print()里参数
name = "JOhn"
age = 18
gender = "male"
# print()函数可以打印多个变量，逗号分隔就好
# print()函数参数一，sep="",就是指定我们打印的多个内容用什么分隔
print(name,age,gender,sep="\t")
print(name,age,gender,sep="#")

# print()函数参数二，end="",就是指定打印完成后的结尾是什么，默认是end="\n"
# 所以，如果调用一个 不给参数的 print() 函数，就会换行，哈哈
print("AAAA",end="\t")
print("BBBB",end="\t")
print("CCCC",end="\t")
```

## 6.格式化输出

```python
# % 的格式化
person = "John"
address = "北京市海淀区中关村智诚科技大厦4层"
phone = "13888888888"
num = 5
price = 26.578
print("订单收件人：%s,\n收货地址：%s，\n电话：%s,\n商品数量是：%d,单价是:%.2f"%(person,address,phone,num,price))

## %s 说明 ： 如果我们前面占位的是 %s，后边无论输入的是啥类型的东西，都会被强制转换为字符串
print("订单收件人：%s,\n收货地址：%s，\n电话：%s,\n商品数量是：%s"%(person,address,phone,num))

## %d 说明，类似的如果我们前面占位的是 %d，后边无论输入的是什么数字，都会被强制转换为整型
## %f 说明，浮点型， %.2,保留两位小数
movie = "大侦探皮卡丘"
ticket = 45.9
count = 35
print("电影：%s\n票价：%.1f\n观看人数：%d\n总票价：%.1f" % (movie,ticket,count,ticket*count))


# "{}".format()的格式化输出,这种比 % 占位的方便，就字符串里用 {} 占位，后边 .format()加上对应位置的变#  量名就行了，不用管变量类型
age = 2
school = "蓝天幼儿园"
money = 10.5
message = "John 今年{}岁了，上的是{},每天有{}元零花钱。".format(age,school,money)
print(message)


##还有一个更牛逼的 f''
name = '太白金星'
age = 18
sex = '男'
msg = F'姓名：{name},性别：{age}，年龄：{sex}'  # 大写字母也可以
msg = f'姓名：{name},性别：{age}，年龄：{sex}'  
print(msg)
'''
输出结果：
姓名：太白金星,性别：18，年龄：男
'''

#可以加任意表达式
print(f'{3*21}')  # 63

name = 'barry'
print(f"全部大写：{name.upper()}")  # 全部大写：BARRY

# 字典也可以
teacher = {'name': '太白金星', 'age': 18}
msg = f"The teacher is {teacher['name']}, aged {teacher['age']}"
print(msg)  # The comedian is 太白金星, aged 18

# 列表也行
l1 = ['太白金星', 18]
msg = f'姓名：{l1[0]},年龄：{l1[1]}.'
print(msg)  # 姓名：太白金星,年龄：18.

#可以用函数完成相应的功能，然后将返回值返回到字符串相应的位置
def sum_a_b(a,b):
    return a + b
a = 1
b = 2
print('求和的结果为' + f'{sum_a_b(a,b)}')
##

##多行 f' '      
name = 'barry'
age = 18
ajd = 'handsome'

# speaker = f'''Hi {name}.
# You are {age} years old.
# You are a {ajd} guy!'''

speaker = f'Hi {name}.'\
          f'You are {age} years old.'\
          f'You are a {ajd} guy!'
print(speaker)

##其他细节
print(f"{{73}}")  # {73}
print(f"{{{73}}}")  # {73}
print(f"{{{{73}}}}")  # {{73}}
m = 21
# ! , : { } ;这些标点不能出现在{} 这里面。
# print(f'{;12}')  # 报错
# 所以使用lambda 表达式会出现一些问题。
# 解决方式：可将lambda嵌套在圆括号里面解决此问题。
x = 5
print(f'{(lambda x: x*2) (x)}')  # 10
```

## 7.输入 input()

```python
# 从input()输入的，默认都是字符串类型
namprint("*"*30,"捕鱼达人","*"*30)
username = input("输入参与者用户名：")
password = input("输入密码：")
print("%s 请充值才能加入游戏！" % username)
coins = int(input("您充值的金额为："))
print("%s 元充值成功！当前游戏币是：%d" % (username,coins))e = input("请输入您的用户名：")
print(name)

#哈哈哈英雄联盟
print('''
*********************************
			英雄联盟
*********************************
	''')

role = input("输入角色：")
equipment = input("输入拥有的装备：")
upgrade_equipment = input("输入想要购买的装备：")
pay = input("输入付款金额：")

#变量的赋值替换
equipment = upgrade_equipment

print("{}拥有{}装备，购买此装备花了{}钱。".format(role,equipment,pay))


```

## 8.比较运算符

```python

# >  <  >=  <=  ==  !=
n1 = int(input("请输入第一个数："))
n2 = int(input("请输入第二个数："))

#判断 n1 和 n2，这里result获得的值是True or  False

result = n1 > n2
print('n1 > n2:', result)

m1 = 'hello'
m2 = 'hello'
## ==  ！=  不仅可以应用于数字，字符串也行
result2 = m1 == m2
print("m1==m2:",result2)

username=input('请输入用户名：')
uname = 'admin123'
result3 = username != uname
print('用户名验证结果：',result3)

# is        is not

age = 20
age1 = 20
# python 自带一个内部函数 id()，可以判断变量在内存中的位置，如果两个变量是相等的，
# 那其实这两个变量就是同一个东西，他们储存在内存的同一个地方
print(id(age))
print(id(age1))
print(age is age1)

money = 2000000
salary = 600000
print(id(money))
print(id(salary))
print(money is salsry)
print(money is not salary)
# 这个现象只出现在当你把一堆代码同时提交给解释器时，你在交互界面就不一样了
# 当赋值超过【-5，256】，每次都会重新创建新的内存地址
```

## 9.逻辑运算符

```python
# and or not  与或非
# 当运用这三个运算符的时候，若有返回值，返回值是布尔类型
```

## 10.进制转换

```
# bin() 把对象转换为二进制  0b——>二进制 ，浮点数不能通过bin()来进行二进制转换
a = 13
print(bin(a))# 这几把a转换为二进制数了，答案是 0b1101

#如何定义一个二进制数呢
b = 0b1011  # 数字前面加上 0b 就可以直接定义二进制数
#二进制,八进制，十六进制咋转换成十进制数呢
print(int(b))  # 直接用int()转化为整数，
#负数整数咋转换为二进制————正数取反加一
# 取反就是把二进制数里的0，1互换，
# 比如 -13，转换过程就是 13 ——> 0b1101(0000 1101) ——> 1111 0010 ——> 1111 0011
# 那这个 1111 0011 就是 -13的 二进制位，但是python给我门返回的
print(bin(-13)) ————> -0b1101
# 0o6430 八进制 ——> 0b 110 100 011 000(每一位数字分别转换为三位的二进制，拼一起)
# 0x9ab16 十六进制 0-9 a-f  ——> 0b 1001 1010 1011 0110  (每一位数字分别转换为四位的二进制，拼一起)

```

## 11.位运算

位运算是个傻逼知识，我不学，也不写，活该我不会！

## 12.if语句

```python
#判断用户登录
#先定义数据库里的用户名密码
uid = "admin123"
password = "123456"
#再输入用户名密码
username = input("输入用户名：")
passwd = input("输入密码：")
if username != "" and passwd != "":
	if username == uid and passwd == password:
		print("登陆成功！")
	else:
		print("用户名或密码错误！")
else:
	print("用户名或密码不能为空！")

    
#还有个 elif：就不说了
```

## 13.while 语句

```python
# 这里有个死循环的操作
while True:
	...
    
#break , continue  分别是结束所有循环，结束当前循环开始下一循环

#这里有个组合
while []:
    ...
else:
    
#还有
for i in range():
    ...
else:
    
#else 语句也可以与循环语句尽心搭配，其实else语句是个相对独立的语句
#举个栗子
'''
小易喜欢的单词具有以下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母

例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词。

'''
def func():
    #现有个单词
    word = input("请输入一个单词：")
    for i in range(len(word)):
        if not word.isupper():
            print("小明不喜欢。没大写~")
            break
        elif i<(len(word)-1)  and word[i]==word[i+1]:
            print("小明不喜欢。叠词~")
            break
    else:
        print("小明喜欢。")
 
def main():
    func()


if __name__ == "__main__":
    main()
```

## 14.列表

```python
# 列表有几个共同操作
- 成员关系运算（ in,not in)
if a in list1:
- 连接操作（+）
list3 = list1 + list2
- 重复操作（*）
list2 = list1 * 3
- 切片操作（[::]）
#语法：列表名[开始下标:结束下标：步长]，表示按指定步长获取从开始下标到结束下标之间的元素，
#     结果为一个新的列表
#注意：包头不包尾【前闭后开区间】   [开始下标,结束下标)
#步长：默认是1，正数表示从左向右取，负数表示从右向左取
list1 = [10,20,30,40,50,60]
print(list1[0:3])   #[10,20,30]
print(list1[:3])    #[10,20,30]
print(list1[:])     #[10,20,30,40,50,60] 从头取到尾
print(list1[::2])     # [10,30,50] 隔一个取一个
print(list1[3::-1])  #[40, 30, 20, 10]  从右向左取
print(list1[-1:-3:-1]) #[60, 50] 从右向左取
print(list1[2:]) #[30, 40, 50, 60] 从下标为2的元素开始取到末尾
print(list1[-3::-1])#[40, 30, 20, 10] 从右向左取到第一个元素
print(list1[-3:]) #[40,50,60] 最后三个元素

#列表长度
len(list1)

#列表内极值与求和
max(list1)
min(list1)
sum(list1)

# 凡是列表，字典，这种数据集合都面临差不多固定几个操作，就是增删改查

## 增
list.append() #将元素增至列表末尾
list.insert(index,obj) #将元素插入到指定 index位置
list.extend(list2) #列表的尾部延申，类似于 list=list+list2

##删
list.pop(index) #删除指定index的元素，如果不指定index，默认最后一个元素
list.remove(obj) #删除列表中第一个等于 obj 的元素
list.clear() #清空列表
###del 语句，这个语句厉害了，可以用在几乎所有的这种数据集合类型里
del list1  #就直接删掉这个列表
del list1[0] #指定index删除元素
del list1[0:2] #删除连续的元素，这个也可以使用切片操作
del list1[0:6:2]

##改
list1[indext]=obj  #指定元素index改
list1.reverse()  #反序
##list1.sort()
##list.sort(key=None,reverse=None) 列表方法，实现列表就地排序，不产生新列表
###参数：key参数指明用哪个函数进行排序()，默认值是None，用<进行比较  可选参数
###     reserse：布尔值，默认值是None，也就是假，从小到大排序，如果设置为True，则从大到小排序，可选参数
l1 = [90,30,70,20,10,60]
print(l1)  # [90, 30, 70, 20, 10, 60]
l1.sort()
print(l1)  # [10, 20, 30, 60, 70, 90]
l1.sort(reverse=Trur) # ][90,70,60,30,20,10]
## list.sort()方法没有返回值，它直接就改变原来的列表，要想新建一个排序好的，新的list，可以用 sorted()函数，
list5 = sorted(list1)

##查
##list.index(x,start,end) 在[start  end)范围内查找第一个等于x的元素的下标
#参数说明： x 要查找的元素； start，开始下标；end 结束下标，不包含结束下标
#返回值：如果有值等于x的元素，返回其下标，如果不存在值等于x的元素，会引发ValueError
print(l1.index(10))    #1
print(l1.index(30,2,5))  #4

##list.count(x) 查找列表中x出现的次数，如果没有x，返回0
print(l1.count(30))   #2
print(l1.count(99))   #0 不存在99

##遍历
for i in list1:
    ...
###那如果是二维数组呢，咋整
l = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for i in l:
    for j in i:
        print(j)
###升级一下，打印个小时候的九九乘法表
## #这里，里边那个循环，为啥是range(1,i+1)呢，不加1会怎么样呢，不+1,就是range(1,i),当i=1的时候，就变成的range(1,1),这个区间左闭右开，就是[1,1),所以就不好含1了，就缺个循环了
for i in range(1,10):
	for j in range(1,i+1):
		print("{}*{}={}".format(j,i,i*j),end=" ")
		if i == j:
			print()        
```

注：[list.sort()和sorted()函数的key参数具体方法](https://www.runoob.com/python3/python3-att-list-sort.html)

