# 8点之前 统计作业完成度,难点
# 作业笔记
    # 写每一个题的用时
    # 遇到的问题
    # 解决思路


#第一大题 : 读程序,标出程序的执行过程,画出内存图解,说明答案和为什么
# 请不要想当然,执行之后检查结果然后再确认和自己的猜想是不是一致
(1)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)
#日本
#英国
#英国
(2)
class A:
    Country = ['中国']     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
a.Country[0] = '日本'
print(a.Country)
print(b.Country)
print(A.Country)
#['日本']
#['日本']
#['日本']
(3)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(4)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def Country(self):
        return self.Country

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
print(a.Country)
print(a.Country())
#<bound method A.Country of <__main__.A object at 0x007AFF88>>
#<bound method A.Country of <__main__.A object at 0x007AFF88>>
# 这个解释下： 这里 a.Country 指的是 类 A 里边的绑定方法 Country,就是下边定义的那个方法，他是方法名，不是静态变量名
# a.Country() 是在调用 类 A 里边的 Country() 方法，这个方法返回的是 self.Country ,也就是 a.Country, 就还是这个方法名


# 第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长(公式自己上网查)
# 要求,借助组合,要求组合圆形类的对象完成需求
from math import pi
class Circle(object):
    """docstring for Circle"""
    def __init__(self, r):
        super(Circle, self).__init__()
        self.r = r
    def measure(self):
        return pi*self.r*self.r 
    def zhouchang(self):
        return 2*pi*self.r

class C_circle(object):
    """docstring for C_circle"""
    def __init__(self,outer_r,inner_r):
        super(C_circle, self).__init__()
        # 注意，这个是三元运算，这里就记住了啊
        outer_r,inner_r = (outer_r,inner_r) if outer_r > inner_r else (inner_r,outer_r)
        self.c1 = Circle(outer_r)
        self.c2 = Circle(inner_r)
    def measure(self):
        area = self.c1.measure()-self.c2.measure()
        print(area)
        return area
    def zhouchang(self):
        zc = self.c1.zhouchang()+self.c2.zhouchang()
        print(zc)
        return zc


c3 = C_circle(10,5)
x=c3.measure()
y=c3.zhouchang()





# 第三大题:继续完成计算器和优化工作