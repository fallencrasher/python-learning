# python基础 14 类的三大特性 （继承，多态，封装）

## 1.继承

### ①什么是继承

继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类

 

python中类的继承分为：单继承和多继承

```python
class ParentClass1: #定义父类
    pass

class ParentClass2: #定义父类
    pass

class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
    pass

class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
    pass
    


```

查看继承

```python
>>> SubClass1.__bases__ #__base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
(<class '__main__.ParentClass1'>,)
>>> SubClass2.__bases__
(<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)
```

提示：如果没有指定基类，python的类会默认继承object类，object是所有python类的基类，它提供了一些常见方法（如__str__）的实现。

```python
>>> ParentClass1.__bases__
(<class 'object'>,)
>>> ParentClass2.__bases__
(<class 'object'>,)
```

 ### ②**继承与抽象（先抽象再继承）**

抽象即抽取类似或者说比较像的部分。

抽象分成两个层次： 

1.将奥巴马和梅西这俩对象比较像的部分抽取成类； 

2.将人，猪，狗这三个类比较像的部分抽取成父类。

抽象最主要的作用是划分类别（可以隔离关注点，降低复杂度）

![img](https://images2017.cnblogs.com/blog/827651/201708/827651-20170809205054370-2144865424.png)

 

**继承：是基于抽象的结果，通过编程语言去实现它，肯定是先经历抽象这个过程，才能通过继承的方式去表达出抽象的结构。**

抽象只是分析和设计的过程中，一个动作或者说一种技巧，通过抽象可以得到类

![img](https://images2017.cnblogs.com/blog/827651/201708/827651-20170809205126886-720065307.png)

### ③**继承与重用性**

```python
==========================第一部分
例如

　　猫可以：吃、喝、爬树

　　狗可以：吃、喝、看家

如果我们要分别为猫和狗创建一个类，那么就需要为 猫 和 狗 实现他们所有的功能，伪代码如下：


#猫和狗有大量相同的内容
class 猫：

    def 吃(self):
        # do something

    def 喝(self):
        # do something

    def 爬树(self):
        # do something



class 狗：

    def 吃(self):
        # do something

    def 喝(self):
        # do something

    def 看家(self):
        #do something


==========================第二部分
上述代码不难看出，吃、喝是猫和狗都具有的功能，而我们却分别的猫和狗的类中编写了两次。如果使用 继承 的思想，如下实现：

　　动物：吃、喝

　　   猫：爬树（猫继承动物的功能）

　　   狗：看家（狗继承动物的功能）

伪代码如下：
class 动物:

    def 吃(self):
        # do something

    def 喝(self):
        # do something

# 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
class 猫(动物)：

    def 爬树(self):
        print '喵喵叫'

# 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
class 狗(动物)：

    def 看家(self):
        print '汪汪叫'


==========================第三部分
#继承的代码实现
class Animal:

    def eat(self):
        print("%s 吃 " %self.name)

    def drink(self):
        print ("%s 喝 " %self.name)

class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def climb(self):
        print('爬树')

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed='狗'

    def look_after_house(self):
        print('汪汪叫')


# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()


```

 在开发程序的过程中，如果我们定义了一个类A，然后又想新建立另外一个类B，但是类B的大部分内容与类A的相同时

我们不可能从头开始写一个类B，这就用到了类的继承的概念。

通过继承的方式新建类B，让B继承A，B会‘遗传’A的所有属性(数据属性和函数属性)，实现代码重用

```python
class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'%self.name)

class Dog(Animal):
    pass

class Person(Animal):
    pass

egg = Person('egon',10,1000)
ha2 = Dog('二愣子',50,1000)
egg.eat()
ha2.eat()
```

 提示：用已经有的类建立一个新的类，这样就重用了已经有的软件中的一部分设置大部分，大大生了编程工作量，这就是常说的软件重用，不仅可以重用自己的类，也可以继承别人的，比如标准库，来定制新的数据类型，这样就是大大缩短了软件开发周期，对大型软件开发来说，意义重大.

### ④派生

当然子类也可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了。

```python
class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'%self.name)

class Dog(Animal):
    '''
    狗类，继承Animal类
    '''
    def bite(self, people):
        '''
        派生：狗有咬人的技能
        :param people:  
        '''
        people.life_value -= self.aggressivity

class Person(Animal):
    '''
    人类，继承Animal
    '''
    def attack(self, dog):
        '''
        派生：人有攻击的技能
        :param dog: 
        '''
        dog.life_value -= self.aggressivity

egg = Person('egon',10,1000)
ha2 = Dog('二愣子',50,1000)
print(ha2.life_value)
print(egg.attack(ha2))
print(ha2.life_value)
```

注意：像ha2.life_value之类的属性引用，会先从实例中找life_value然后去类中找，然后再去父类中找...直到最顶级的父类。

 

在子类中，新建的重名的函数属性，在编辑函数内功能的时候，有可能需要重用父类中重名的那个函数功能，应该是用调用普通函数的方式，即：类名.func()，此时就与调用普通函数无异了，因此即便是self参数也要为其传值.

在python3中，子类执行父类的方法也可以直接用super方法.

#### super

1. 什么是super方法？

   按照mro顺序来寻找当前类的下一个类

   ```python
   class A(object):
       def func(self):
           print('A')
   class B(A):
       def func(self):
           super().func()
           print('B')
   class C(A):
       def func(self):
           super().func()
           print('C')
   class D(B,C):
       def func(self):
           super().func()
           super(D,self).func()
           print('D')
   D().func() # ACBD  但打印出来是反顺序
   ```

2. super在py3与py2中使用方法不一样

   1. 在py3中：不是必须传参数，自动就帮我们寻找当前类的mro顺序的下一个类中的同名方法
   2. 在py2中：新式类中，需要我们主动传递参数super(子类的名字，子类的对象).函数名()，这样才能够帮我们调用到这个子类的mro顺序的下一个类中的方法（为什么不说经典类？因为经典类只有深度优先）

3. 在单继承中执行父类的同名方法

   在D类中找super的func，那么可以这样写 super().func()

   也可以这样写 super(D,self).func() (并且在py2的新式类中必须这样写)

   ```python
   class User:
       def __init__(self,name):
           self.name = name
   class VIPUser(User):
       def __init__(self,name,level,strat_date,end_date):
           # User.__init__(self,name)          # 原始的
           super().__init__(name)              # 推荐的
           # super(VIPUser,self).__init__(name)# py2用的
           self.level = level
           self.strat_date = strat_date
           self.end_date = end_date
   
   太白 = VIPUser('太白',6,'2019-01-01','2020-01-01')
   print(太白.__dict__)
   ```

#### 更多例子

```python
class A:
    def hahaha(self):
        print('A')

class B(A):
    def hahaha(self):
        super().hahaha()
        #super(B,self).hahaha()
        #A.hahaha(self)
        print('B')

a = A()
b = B()
b.hahaha()
super(B,b).hahaha()


```

```python
class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'%self.name)

class Dog(Animal):
    '''
    狗类，继承Animal类
    '''
    def __init__(self,name,breed,aggressivity,life_value):
        super().__init__(name, aggressivity, life_value) #执行父类Animal的init方法
        self.breed = breed  #派生出了新的属性

    def bite(self, people):
        '''
        派生出了新的技能：狗有咬人的技能
        :param people:  
        '''
        people.life_value -= self.aggressivity

    def eat(self):
        # Animal.eat(self)
        #super().eat()
        print('from Dog')

class Person(Animal):
    '''
    人类，继承Animal
    '''
    def __init__(self,name,aggressivity, life_value,money):
        #Animal.__init__(self, name, aggressivity, life_value)
        #super(Person, self).__init__(name, aggressivity, life_value)
        super().__init__(name,aggressivity, life_value)  #执行父类的init方法
        self.money = money   #派生出了新的属性

    def attack(self, dog):
        '''
        派生出了新的技能：人有攻击的技能
        :param dog: 
        '''
        dog.life_value -= self.aggressivity

    def eat(self):
        #super().eat()
        Animal.eat(self)
        print('from Person')

egg = Person('egon',10,1000,600)
ha2 = Dog('二愣子','哈士奇',10,1000)
print(egg.name)
print(ha2.name)
egg.eat()
```

**通过继承建立了派生类与基类之间的关系，它是一种'是'的关系，比如白马是马，人是动物。**

**当类之间有很多相同的功能，提取这些共同的功能做成基类，用继承比较好，比如教授是老师**

```python
>>> class Teacher:
...     def __init__(self,name,gender):
...         self.name=name
...         self.gender=gender
...     def teach(self):
...         print('teaching')
... 
>>> 
>>> class Professor(Teacher):
...     pass
... 
>>> p1=Professor('egon','male')
>>> p1.teach()
teaching
```

### ⑤抽象类与接口类

#### （1）接口类

继承有两种用途：

一：继承基类的方法，并且做出自己的改变或者扩展（代码重用）  

二：声明某个子类兼容于某基类，定义一个接口类Interface，接口类中定义了一些接口名（就是函数名）且并未实现接口的功能，子类继承接口类，并且实现接口中的功能

```python
class Payment:     # 抽象类
    def pay(self,money):
        '''只要你见到了项目中有这种类,你要知道你的子类中必须实现和pay同名的方法
        如果子类没有实现同名方法，在调用子类方法的时候就会报错'''
        raise NotImplementedError('请在子类中重写同名pay方法')

class Alipay(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'uname':self.name,'price':money}
        # 想办法调用支付宝支付 url连接 把dic传过去
        print('%s通过支付宝支付%s钱成功'%(self.name,money))

class WeChat(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'username':self.name,'money':money}
        # 想办法调用微信支付 url连接 把dic传过去
        print('%s通过微信支付%s钱成功'%(self.name,money))

class Apple(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'name': self.name, 'number': money}
        # 想办法调用苹果支付 url连接 把dic传过去
        print('%s通过苹果支付%s钱成功' % (self.name, money))

aw = WeChat('alex')
aw.pay(400)
aa = Alipay('alex')
aa.pay(400)
#归一化设计
def pay(name,price,kind):
    if kind == 'Wechat':
        obj = WeChat(name)
    elif kind == 'Alipay':
        obj = Alipay(name)
    elif kind == 'Apple':
        obj = Apple(name)
    obj.pay(price)

pay('alex',400,'Wechat')
pay('alex',400,'Alipay')
pay('alex',400,'Apple') 

```

接口初成：手动报异常：NotImplementedError 来解决开发中遇到的问题

```python
# 实现抽象类的另一种方式,约束力强,依赖abc模块
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod #用这个装饰器来约束子类中必须有同名方法，否则在实例化阶段就会报错
    def pay(self,money):
        '''只要你见到了项目中有这种类,你要知道你的子类中必须实现和pay同名的方法'''
        raise NotImplementedError('请在子类中重写同名pay方法')

class Alipay(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'uname':self.name,'price':money}
        # 想办法调用支付宝支付 url连接 把dic传过去
        print('%s通过支付宝支付%s钱成功'%(self.name,money))

class WeChat(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'username':self.name,'money':money}
        # 想办法调用微信支付 url连接 把dic传过去
        print('%s通过微信支付%s钱成功'%(self.name,money))

WeChat('alex') #如果 WeChat 类中没有 pay 方法，那么在实例化这一步就会报错
```

#### （2）抽象类

**什么是抽象类**

  *与java一样，python也有抽象类的概念但是同样需要借助模块实现，**抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化***

**为什么要有抽象类**

  *如果说**类是从**一堆**对象**中抽取相同的内容而来的，那么**抽象类**就**是从**一堆**类**中抽取相同的内容而来的，内容包括数据属性和函数属性。*

　 *比如我们有香蕉的类，有苹果的类，有桃子的类，从这些类抽取相同的内容就是水果这个抽象的类，你吃水果时，要么是吃一个具体的香蕉，要么是吃一个具体的桃子。。。。。。你永远无法吃到一个叫做水果的东西。*

  *从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的。*

　 *从实现角度来看，抽象类与普通类的不同之处在于：抽象类中有抽象方法，该类不能被实例化，只能被继承，且子类必须实现抽象方法。这一点与接口有点类似，但其实是不同的，即将揭晓答案*

*抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如read、write），而接口只强调函数属性的相似性。*

***抽象类是一个介于类和接口直接的一个概念，同时具备类和接口的部分特性，可以用来实现归一化设计*** 

在python中，并没有接口类这种东西，即便不通过专门的模块定义接口，我们也应该有一些基本的概念。

***在python中实现抽象类***

```python
#一切皆文件
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)
```

#### （3）多继承问题

在继承抽象类的过程中，我们应该尽量避免多继承；
而在继承接口的时候，我们反而鼓励你来多继承接口

```
接口隔离原则：
使用多个专门的接口，而不使用单一的总接口。即客户端不应该依赖那些不需要的接口。
```

#### （4）方法的实现

在抽象类中，我们可以对一些抽象方法做出基础实现；
而在接口类中，任何方法都只是一种规范，具体的功能需要子类实现

### ⑥钻石继承

#### （1）继承顺序

![img](https://images2017.cnblogs.com/blog/827651/201708/827651-20170812154958413-730706385.png)

```python
class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
#python3中统一都是新式类
#pyhon2中才分新式类与经典类


```

#### （2）继承原理

python到底是如何实现继承的，对于你定义的每一个类，python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表，例如

```
>>> F.mro() #等同于F.__mro__
[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

 

为了实现继承,python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止。
而这个MRO列表的构造是通过一个C3线性化算法来实现的。我们不去深究这个算法的数学原理,它实际上就是合并所有父类的MRO列表并遵循如下三条准则:
1.子类会先于父类被检查
2.多个父类会根据它们在列表中的顺序被检查
3.如果对下一个类存在两个合法的选择,选择第一个父类

### ⑦继承小结

#### 继承的作用

```
减少代码的重用
提高代码可读性
规范编程模式
```

#### 几个名词

```
抽象：抽象即抽取类似或者说比较像的部分。是一个从具题到抽象的过程。
继承：子类继承了父类的方法和属性
派生：子类在父类方法和属性的基础上产生了新的方法和属性
```

#### 抽象类与接口类

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
1.多继承问题
在继承抽象类的过程中，我们应该尽量避免多继承；
而在继承接口的时候，我们反而鼓励你来多继承接口


2.方法的实现
在抽象类中，我们可以对一些抽象方法做出基础实现；
而在接口类中，任何方法都只是一种规范，具体的功能需要子类实现
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### **钻石继承**

```
新式类：广度优先
经典类：深度优先
```

## 2.多态

### **多态**

多态指的是一类事物有多种形态

动物有多种形态：人，狗，猪



```python
import abc
class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')
```



文件有多种形态：文本文件，可执行文件



```python
import abc
class File(metaclass=abc.ABCMeta): #同一类事物:文件
    @abc.abstractmethod
    def click(self):
        pass

class Text(File): #文件的形态之一:文本文件
    def click(self):
        print('open file')

class ExeFile(File): #文件的形态之二:可执行文件
    def click(self):
        print('execute file')
```



 

### **多态性**

**一 什么是多态动态绑定（在继承的背景下使用时，有时也称为多态性）**

**多态性是指在不考虑实例类型的情况下使用实例**



```
在面向对象方法中一般是这样表述多态性：
向不同的对象发送同一条消息（！！！obj.func():是调用了obj的方法func，又称为向obj发送了一条消息func），不同的对象在接收时会产生不同的行为（即方法）。
也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。

比如：老师.下课铃响了（），学生.下课铃响了()，老师执行的是下班操作，学生执行的是放学操作，虽然二者消息一样，但是执行的效果不同
```



 

**多态性**



```python
peo=People()
dog=Dog()
pig=Pig()

#peo、dog、pig都是动物,只要是动物肯定有talk方法
#于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
peo.talk()
dog.talk()
pig.talk()

#更进一步,我们可以定义一个统一的接口来使用
def func(obj):
    obj.talk()
```



 

**鸭子类型**

逗比时刻：

　　Python崇尚鸭子类型，即‘如果看起来像、叫声像而且走起路来像鸭子，那么它就是鸭子’

python程序员通常根据这种行为来编写程序。例如，如果想编写现有对象的自定义版本，可以继承该对象

也可以创建一个外观和行为像，但与它无任何关系的全新对象，后者通常用于保存程序组件的松耦合度。

例1：利用标准库中定义的各种‘与文件类似’的对象，尽管这些对象的工作方式像文件，但他们没有继承内置文件对象的方法

例2：序列类型有多种形态：字符串，列表，元组，但他们直接没有直接的继承关系





```python
#二者都像鸭子,二者看起来都像文件,因而就可以当文件一样去用
class TxtFile:
    def read(self):
        pass

    def write(self):
        pass

class DiskFile:
    def read(self):
        pass
    def write(self):
        pass
```



## 3.封装

### 封装

1. 广义上的封装：把属性和方法装起来，外面不能直接调用了，要通过类的名字来调用

2. 狭义上的封装：把属性和方法藏起来,外面不能调用,只能在内部偷偷调用（私有）

   ```python
   # class User:
   #     def __init__(self,name,passwd):
   #         self.usr = name
   #         self.__pwd = passwd  # 私有的实例变量/私有的对象属性
   # alex = User('alex','sbsbsb')
   # print(alex.__pwd)  # 报错
   # print(alex.pwd)    # 报错
   ```

   给一个名字前面加上了双下划线的时候，这个名字就变成了一个私有的所有的私有的内容或者名字都不能在类的外部调用，只能在类的内部使用了

3. 使用私有有三种情况

   1. 不想让你看也不想让你改

   2. 可以让你看，但不让你改

   3. 可以看也可以改，但是要求你按照我的规则改

      ```python
      # class User:
      #     def __init__(self,name,passwd):
      #         self.usr = name
      #         self.__pwd = passwd  # 私有的实例变量/私有的对象属性
      #     def get_pwd(self):       # 表示的是用户不能改只能看，这里我们定义一个get方法实现的
      #         return self.__pwd
      #     def change_pwd(self,new_value):    # 表示用户必须调用我们自定义的修改方式来进行变量的修改，这里我们用change方法实现
      #         self.__pwd = new_value
      ```

4. 封装的语法

   1. 私有的静态变量

   2. 私有的实例变量

   3. 私有的绑定方法

      ```python
      # class User:
      #     __Country = 'China'   # 私有的静态变量
      #     def func(self):
      #         print(User.__Country)  # 在类的内部可以调用
      # print(User.Country)  # 报错 在类的外部不能调用
      # print(User.__Country)# 报错 在类的外部不能调用
      # User().func()
      ```

      ```python
      # import  hashlib
      # class User:
      #     def __init__(self,name,passwd):
      #         self.usr = name
      #         self.__pwd = passwd  # 私有的实例变量
      #     def __get_md5(self):     # 私有的绑定方法
      #         md5 = hashlib.md5(self.usr.encode('utf-8'))
      #         md5.update(self.__pwd.encode('utf-8'))
      #         return md5.hexdigest()
      #     def getpwd(self):
      #         return self.__get_md5()
      # alex = User('alex','sbsbsb')
      # print(alex.getpwd())
      ```

5. 私有的特点

   1. 可以在类的内部使用

   2. 不可以在类的外部使用

   3. 类的子类中也不能使用

      ```python
      # class Foo(object):
      #     def __func(self):
      #         print('in Foo')
      # class Son(Foo):
      #     def __init__(self):
      #         self.__func()
      # Son() # 报错
      ```

6. 封装的原理

   变形，在哪里变形？

   在类的内部使用的时候，自动的把当前这句话所在的类的名字拼在私有变量前完成变形

   ```python
   # class User:
   #     __Country = 'China'   # 私有的静态变量
   #     __Role = '法师'   # 私有的静态变量
   #     def func(self):
   #         print(self.__Country)  # 在类的内部使用的时候,自动的把当前这句话所在的类的名字拼在私有变量前完成变形
   # print(User._User__Country)
   # print(User._User__Role)
   # __Country -->'_User__Country': 'China'
   # __Role    -->'_User__Role': '法师'
   # User.__aaa = 'bbb'  # 在类的外部根本不能定义私有的概念
   ```

7. 类中变量的三个级别

   + 公有的public：类内外都能用，父类子类都可以用
   + 保护的protect：类内可以用，父类子类都可以用，类外不能用
   + 私有的private：本类的类内部能用，其他地方都不能用

   python只支持**公有的**与**私有的**

### 类中的三个装饰器

##### property

1. 作用是什么？

   1. 把一个方法伪装成一个属性，在调用这个方法的时候不需要加()就可以直接得到返回值

      ```python
      # import time
      # class Person:
      #     def __init__(self,name,birth):
      #         self.name = name
      #         self.birth = birth
      #     @property
      #     def age(self):   # 装饰的这个方法 不能有参数
      #         return time.localtime().tm_year - self.birth
      #
      # 太白 = Person('太白',1998)
      # print(太白.age)
      ```

   2. 和私有的属性合作

      ```python
      # class User:
      #     def __init__(self,usr,pwd):
      #         self.usr = usr
      #         self.__pwd = pwd
      #     @property  # 这里完成了只能看不能改的作用
      #     def pwd(self):
      #         return self.__pwd
      #
      # alex = User('alex','sbsbsb')
      # print(alex.pwd)
      ```

      ```python
      # class Goods:
      #     discount = 0.8
      #     def __init__(self,name,origin_price):
      #         self.name = name
      #         self.__price = origin_price
      #     @property
      #     def price(self):
      #         return self.__price * self.discount
      #
      # apple = Goods('apple',5)
      # print(apple.price)
      ```

   3. property进阶：改变私有属性（用的时候必须有property修饰的同名方法）

      ```python
      # class Goods:
      #     discount = 0.8
      #     def __init__(self,name,origin_price):
      #         self.name = name
      #         self.__price = origin_price
      #     @property
      #     def price(self):
      #         return self.__price * self.discount
      #
      #     @price.setter
      #     def price(self,new_value):
      #         if isinstance(new_value,int):
      #             self.__price = new_value
      #
      # apple = Goods('apple',5)
      # print(apple.price)   # 调用的是被@property装饰的price
      # apple.price = 10     # 调用的是被setter装饰的price
      # print(apple.price)
      ```

      ```python
      class Goods:
          discount = 0.8
          def __init__(self,name,origin_price):
              self.name = name
              self.__price = origin_price
          @property
          def price(self):
              return self.__price * self.discount
      
          @price.setter
          def price(self,new_value):
              if isinstance(new_value,int):
                  self.__price = new_value
      
          @price.deleter
          def price(self):
              del self.__price
      apple = Goods('apple',5)
      print(apple.price)
      apple.price = 'ashkaksk'
      del apple.price   # 并不能真的删除什么,只是调用对应的被@price.deleter装饰的方法而已
      print(apple.price)
      ```

### 反射

1. 反射对象的实例变量/绑定方法

   ```python
   class A:
       Role = '治疗'
       def __init__(self):
           self.name = 'alex'
           self.age = 84
       def func(self):
           print('wahaha')
           return 666
   
   a = A()
   print(getattr(a,'name')) # 反射对象的实例变量
   print(getattr(a,'func')()) # 反射对象的绑定方法
   ```

2. 反射类的静态变量/（其他方法）

   ```python
   class A:
       Role = '治疗'
       def __init__(self):
           self.name = 'alex'
           self.age = 84
       def func(self):
           print('wahaha')
           return 666
   
   a = A()
   print(getattr(A,'Role'))
   ```

3. 反射模块中的所有变量

   1. 被导入的模块

      ```python
      import a   # 引用模块中的任意的变量
      print(getattr(a,'sww'),a.sww)
      getattr(a,'sww')()
      print(getattr(a,'lst'),a.lst)
      print(getattr(a,'dic'),a.dic)
      print(getattr(a,'we'),a.we)
      ```

      ```python
      #a 模块
      def sww():
          print('wahaha')
         
      lst = [1,23]
      dic = {1:2,3:4}
      we = 'wahaha'
      ```

      

   2. 当前执行的模块—脚本

      ```python
      import sys # 反射本模块中的名字
      cat = '小a'
      dog = '小b'
      def pig():
          print('小p')
      print(getattr(sys.modules['__main__'],'cat'))
      print(getattr(sys.modules['__main__'],'dog'))
      getattr(sys.modules['__main__'],'pig')()
      ```

4. 判断这个被反射的内容是否存在或者是否可被调用

   ```python
   class A:
       Role = '治疗'
       def __init__(self):
           self.name = 'alex'
           self.age = 84
       def func(self):
           print('wahaha')
           return 666
   
   a = A()
   # print(hasattr(a,'sex'))
   # print(hasattr(a,'age'))
   # print(hasattr(a,'func'))
   # if hasattr(a,'func'):
   #     if callable(getattr(a,'func')):
   #         getattr(a,'func')()
   ```



 