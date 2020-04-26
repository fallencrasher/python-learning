# python基础 13 类命名空间于对象、实例的命名空间，组合方法

## 1.类命名空间于对象、实例的命名空间

**创建一个类就会创建一个类的名称空间，用来存储类中定义的所有名字，这些名字称为类的属性**

而类有两种属性：静态属性和动态属性

- 静态属性就是直接在类中定义的变量
- 动态属性就是定义在类中的方法

```python
#其中类的数据属性是共享给所有对象的
#而类的动态属性是绑定到所有对象的
```

**创建一个对象/实例就会创建一个对象/实例的名称空间，存放对象/实例的名字，称为对象/实例的属性**

在obj.name会先从 obj 自己的名称空间里找name，找不到则去类中找，类也找不到就找父类...最后都找不到就抛出异常

## 2.面向对象的组合用法

**软件重用的重要方式除了继承之外还有另外一种方式，即：组合**

**组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合**

```python
class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性都是狗

    def __init__(self, name, breed, aggressivity, life_value):
        self.name = name  # 每一只狗都有自己的昵称;
        self.breed = breed  # 每一只狗都有自己的品种;
        self.aggressivity = aggressivity  # 每一只狗都有自己的攻击力;
        self.life_value = life_value  # 每一只狗都有自己的生命值;

    def bite(self,people):
        # 狗可以咬人，这里的狗也是一个对象。
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
　　　　 dog.life_value -= self.aggressivit
    
class Weapon:
    def prick(self, obj):  # 这是该装备的主动技能,扎死对方
        obj.life_value -= 500  # 假设攻击力是500

class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name):
        self.name = name  # 每一个角色都有自己的昵称;
        self.weapon = Weapon()  # 给角色绑定一个武器;
xiaobai = Dog('xiaobai','泰迪',100,1000)        
egg = Person('egon')
egg.weapon.prick() 
#egg组合了一个武器的对象，可以直接egg.weapon来使用组合类中的所有方法
```

**圆环是由两个圆组成的，圆环的面积是外面圆的面积减去内部圆的面积。圆环的周长是内部圆的周长加上外部圆的周长。**
**这个时候，我们就首先实现一个圆形类，计算一个圆的周长和面积。然后在"环形类"中组合圆形的实例作为自己的属性来用**

```python
from math import pi

class Circle:
    '''
    定义了一个圆形类；
    提供计算面积(area)和周长(perimeter)的方法
    '''
    def __init__(self,radius):
        self.radius = radius

    def area(self):
         return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi *self.radius


circle =  Circle(10) #实例化一个圆
area1 = circle.area() #计算圆面积
per1 = circle.perimeter() #计算圆周长
print(area1,per1) #打印圆面积和周长

class Ring:
    '''
    定义了一个圆环类
    提供圆环的面积和周长的方法
    '''
    def __init__(self,radius_outside,radius_inside):
        self.outsid_circle = Circle(radius_outside)
        self.inside_circle = Circle(radius_inside)

    def area(self):
        return self.outsid_circle.area() - self.inside_circle.area()

    def perimeter(self):
        return  self.outsid_circle.perimeter() + self.inside_circle.perimeter()


ring = Ring(10,5) #实例化一个环形
print(ring.perimeter()) #计算环形的周长
print(ring.area()) #计算环形的面积
```

**用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系,比如教授有生日，教授教python课程**

```python
class BirthDate:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

class Couse:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period

class Teacher:
    def __init__(self,name,gender,birth,course):
        self.name=name 
        self.gender=gender
        self.birth=birth
        self.course=course
    def teach(self): 
        print('teaching')

p1=Teacher('egon','male', 
            BirthDate('1995','1','27'), 
            Couse('python','28000','4 months')
           ) 

print(p1.birth.year,p1.birth.month,p1.birth.day) 

print(p1.course.name,p1.course.price,p1.course.period)
''' 
运行结果: 
27 
python 28000 4 months 
'''
```

**当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好**