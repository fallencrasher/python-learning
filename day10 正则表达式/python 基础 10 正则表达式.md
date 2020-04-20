# python 基础 10 正则表达式

## 1.模块和实际工作的关系

- time 模块与时间没啥关系，有没有 time 模块，时间都存在，time模块只是让我们在脚本里更容易去显示和计算时间
- re 模块和正则表达式: 有了re模块就可以在 python 里更方便的操作正则表达式了，没有这个模块，正则表达式也是存在的

## 2.正则表达式--regex  ***

### 1. 什么是正则表达式？

   正则表达式是一套规则，用来匹配字符串。

### 2. 能做什么？

   1.检测一个输入的字符串是否合法

   		- 用户输入内容，我们要提前做检测
            		- 能够提高程序的效率并且减轻服务器的压力

   2.从一个大文件中找到所有符合规则的内容 --日志分析、爬虫

### 3.[正则的匹配规则](http://tool.chinaz.com/regex)  

#### 1.字符组 [],只表示一个字符上出现的内容

字符组描述的是一个位置上能出现的所有可能性。

接受范围上，可以描述多个范围，连着写就可以了

```python
- [abc] 匹配 a 或者 b  或者 c，而不是 字符串 'abc',只能匹配到一个字符
- [0-9]  (根据ASCII码范围进行匹配)匹配一个数字
- [a-z] 匹配一个小写字母
- [A-Z] 匹配一个大写字母
- [A-Za-z] 匹配一个任意字母，大小写。只有 '-' 左右 才有大小关系。中间不用加空格
- [0-9a-zA-Z] 匹配一个数字或字母
- [0-9][0-9] 匹配一个两位数

```

#### 2.元字符

正则表达式中，能帮助我们表示匹配内容的符号，叫元字符. 一般情况下，一个元字符就表示要匹配一个字符，需要用 * ? + {} 来说名要匹配的重复个数

| 元字符           | 匹配内容                                                     |
| ---------------- | ------------------------------------------------------------ |
| \w               | 匹配字母(包含中文)或数字或下划线[0-9a-zA-Z_]  w-->word       |
| \W               | 匹配非字母（包含中文）或数字或下划线                         |
| \s               | 匹配任意的空白符 [ /\t/\n],包括空格，换行符和制表符          |
| \S               | 匹配任意非空白符                                             |
| \n               | 回车，换行符                                                 |
| \t               | 匹配一个制表符                                               |
| 空格             |                                                              |
| \d               | 数字[0-9]   d-->digit                                        |
| \D               | 匹配非数字                                                   |
| ^                | 匹配字符串的开始 (^abc   以abc开头的)                        |
| $                | 匹配字符串的结尾( abc$   以abc结尾的)                        |
| .                | 匹配任意字符，除了换行符。当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符，此时等同于[\d\D] 或者[\w\W]或者[\s\S] |
| [...]            | 匹配字符组中的字符  [\d\D]-->匹配所有                        |
| [^...]           | 匹配除了字符组中的字符的所有字符,[^] 这个东西表示‘非’，就是匹配除了 ^ 后边的东西 |
| *                | 匹配 0 个或多个左边的字符(量词)                              |
| +                | 匹配 1 个或多个左边的字符(量词)                              |
| ？               | 匹配 0 个或1个左边的字符，非贪婪方式                         |
| {n}              | 精准匹配连续出现的 n 个前面的表达式                          |
| {n,m}            | 匹配连续出现的 n 到 m 次由前面的正则表达式定义的片段，贪婪方式 |
| {n,}             | 匹配连续出现的，至少 n 次前面的表达式                        |
| a表达式\|b表达式 | 匹配 a或者 b，如果匹配a成功了，不会再匹配b，所以如果两个表达式有重叠部分，长的最好写在前边   abc\|ab |
| （）             | 匹配 括号内的表达式，也表示一个组,比如，匹配网址，百度，京东，淘宝的，(www\.baidu\|jd\|taobao\.com) |
| \b               | 匹配单词的结尾  o\b  就可以匹配 以 ‘o' 结尾的单词，比如 hello |

#### 3.实例

```python
#匹配整数
\d+
#匹配小数
\d+\.\d+
#匹配整数或小数
\d(\.\d+)?
#匹配手机号码
## 应用于让用户输入正确的手机号，我们要限制他们输入的长度，用 ^ $来约束
^1[3-9]\d{9}$
## 应用于在大文件里寻找手机号码，就不用约束了
1[3-9]\d{9}

#匹配一个15位或18位的身份证号
[1-9]\d{14}(\d{2}(\d|x))?  # ^([1-9]\d{14}(\d{2}(\d|x))?)$
##或者
[1-9]\d{14}(\d{2}[\dx])?   # ^([1-9]\d{14}(\d{2}[\dx]?)$
##或者
[1-9]\d{16}[\dx]|[1-9]\d{14}  # ^([1-9]\d{16}[\dx]|[1-9]\d{14})$

#匹配年月日日期 格式2018-12-6，或者2018.12.6或者2018/12/6
'\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}'   # 这里的  \1  是前引用，就引用前边括号里的东西
## 或者
'\d{4}-\d{1,2}-\d{1,2}'

#匹配qq号
# 首位不是0，长度为 5-10 个数字
'[1-9]\d{4,9}'

# 匹配邮箱地址
# 下边这俩，不对
# '\w+((-\w+)|(\.\w+))*\@[0-9a-zA-Z]+([\.-+|](0-9a-zA-Z)+)*\.[0-9a-zA-Z]+)'
# '(\w+([+.-]*\w+)*\@\w+([+.-]*\w+)*\.([+.-]*\w+)+'
# 邮箱规则
# @之前必须有内容且只能是字母（大小写）、数字、下划线(_)、减号（-）、点（.）
# @和最后一个点（.）之间必须有内容且只能是字母（大小写）、数字、点（.）、减号（-），且两个点不能挨着
# 最后一个点（.）之后必须有内容且内容只能是字母（大小写）、数字且长度为大于等于2个字节，小于等于6个字节
[-\w.]+@([-\da-zA-Z]+\.)+[a-zA-Z\d]{2,6}

# 从类似

a = '<a>wahaha</a><b>banana</b><h1>qqxing</h1>'
# 这样的字符串中，
# 1）匹配出wahaha，banana，qqxing内容。
# 2）匹配出a,b,h1这样的内容

import re
ret = re.findall('<(\w+)>(\w+)</(\w+)>',a)
print(ret)

# 1)
ret = re.findall('<\w+>(\w+)</\w+>',a)
print(ret)

# 2)
ret = re.findall('<(\w+)>\w+</\w+>',a)
print(ret)

# 
x = '1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))'
# 1）从上面算式中匹配出最内层小括号以及小括号内的表达式
# '\(-?(\d+[+\-*/]*)*\)'
ret = re.findall('\(-?(?:\d+[+\-*/]*)*\)',x)
ret2 = re.findall('\([^()]+\)',x)  # 这个更好，逻辑就是找到内部不含括号的括号
print(ret) #['(-40/5)', '(9-25/3+7/399/42998+10568/14)', '(-43)', '(16-3*2)']
print(ret2)

# 从类似9-25/3+7/399/42998+10568/14的表达式中匹配出从左到右第一个乘法或除法
x = '9-25/3+7/399/42998+10568/14'
ret = re.search('[1-9]\d*[*|/]-?[1-9]\d*',x)
print(ret.group())
## 要是匹配小数呢？
'\d+(\.\d+)+[*|/]-?\d(\.\d+)+'


#链家网匹配房源信息
import requests

import re
import json


def getPage(url):
    response = requests.get(url)
    return response.text


def parsePage(s):
    com = re.compile(
        '<a class="title" href=.*?data-el="ershoufang">(?P<title>.*?)</a>.*?<div class="info">(?P<region>.*?)<span>/</span>(?P<style>.*?)<span>/</span>(?P<size>.*?)<span>/</span>(?P<direction>.*?)<span>/</span>(?P<decoration>.*?)</div>', re.S)
    ret = com.finditer(s)
    for i in ret:
    	print(i.group())
    	yield {"title": i.group("title"),"region": i.group("region"),"style": i.group("style"),"size": i.group("size"),"direction": i.group("direction"),"decoration": i.group("decoration"),}


def main():
    url = r'https://lf.lianjia.com/ershoufang/rs%E5%9B%BA%E5%AE%89%E5%8E%BF/' 
    response_html = getPage(url)
    ret = parsePage(response_html)
    f = open('lianjia',mode='a',encoding='utf-8')
    for obj in ret:
    	print(obj)
    	data = json.dumps(obj,ensure_ascii=False)
    	f.write(data + "\n")




if __name__ == '__main__':
    main()

    #
# 从类似9-25/3+7/399/42998+10*568/14的表达式中匹配出乘法或除法
s = '9-25/3+7/399/42998+10*568/14'
ret = re.findall('([1-9]\d*[\*|\/][1-9]\d*?)[+\-*/]?',s)
print(ret) #['25/3', '7/3', '99/4', '10*5', '68/1']

```

#### 4.贪婪匹配

在量词范围允许的情况下，尽量多的匹配内容。

```python
# 12316126361361623
\d{3,9} #这里，如果数字一多，就会先匹配位数多的 (贪心算法) 123161263
\d{3,}6 #这里，会匹配到最后一个 6 (回溯算法) 123161263613616

## 也可以进行惰性（非贪婪）匹配，就是尽量少的匹配
## 元字符 量词？
## 量词后边加？，就是非贪婪模式
\d{3,}?6 # 这里，就会匹配到第三个数字以后的第一个6，12316

# 134
1\d??3  # 13
# 这里，2个问号放在一个元字符后边，后边这？就是表示非贪婪，尽量少的匹配，前边这个？就是表示量词匹配1个或0个，在非贪婪模式下，就是匹配0个，所以就匹配到了前两个数字


## 非贪婪模式最多用的一个情况
.*?x #表示匹配 任意字符 任意多次，但是一旦遇到x，就停下来
.+?x #表示匹配 任意字符 至少一次，但是一旦遇到x，就停下来
.*x  #表示匹配 任意字符 任意多次，遇到最后一个x，才停下来
.*x  #表示匹配 任意字符 至少一次，遇到最后一个x，才停下来
```

#### 5.转义字符

就是加个 \ 来让元字符失去匹配效力.

有一些有特殊意义的内容，放在字符中，会取消他的特殊意义。

```python
# 匹配 ()
\(\)

# . 表示匹配任何一个字符，但是，[.] 表示就匹配 '.' 本身
# 这个规律适用于更多元字符 [()?*.+]

# - 在字符组里，如果出现在，两个字符之间的时候才表示范围
[a-c] # 表示范围
[a\-c] #表示 a|-|c
[-ac]  #表示 —|a|c

#但是 \d  \w  \s 、\t \n  在字符组里[\d\w\s\t\n] ，依然是他原本的匹配意义


#所以取消一个元字符的特殊意义有两种方法
## 元字符前面加 \
## 对一部分字符生效，把这个元字符放在字符组里
### [.()?+*]

# 匹配 1+2 或者 1-2
1[+-]2

#
```

  



## 3.re模块



```python

import re
# ret = re.findall('\d+','19740ash93010uru')
# print(ret)   # ['19740', '93010']

# ret = re.search('\d+','19740ash93010uru')
# print(ret)  # 变量，<re.Match object; span=(0, 5), match='19740'>
# if ret:
#     print(ret.group())  #19740

# 一个现象 - 分组()
# findall 还是按照完整的正则进行匹配,只是显示括号里匹配到的内容
ret = re.findall('9(\d)\d','19740ash93010uru')
print(ret) #['7', '3'],用 '9(\d)\d'去匹配，然后返回()里的内容

# search 还是按照完整的正则进行匹配,显示也显示匹配到的第一个内容,但是我们可以通过给group方法传参数
# 来获取具体文组中的内容
ret = re.search('9(\d)(\d)','19740ash93010uru')
print(ret)  # 变量，<re.Match object; span=(1, 4), match='974'>
if ret:
    print(ret.group())  #974
    print(ret.group(0)) #974
    print(ret.group(1))  #7
    print(ret.group(2))  #4

# findall
    # 取所有符合条件的,优先显示分组中的
# search 只取第一个符合条件的,没有优先显示这件事儿
    # 得到的结果是一个变量
        # 变量.group() 的结果 完全和 变量.group(0)的结果一致
        # 变量.group(n) 的形式来指定获取第n个分组中匹配到的内容

# 为什么在search中不需要分组优先 而在findall中需要?

# 加上括号 是为了对真正需要的内容进行提取
ret = re.findall('<\w+>(\w+)</\w+>','<h1>askh930s02391j192agsj</h1>')
print(ret)  #['askh930s02391j192agsj'] #去掉了两端的<h1> </h1>

# search
ret = re.search('<(\w+)>(\w+)</\w+>','<h1>askh930s02391j192agsj</h1>')
print(ret.group())  #<h1>askh930s02391j192agsj</h1>
print(ret.group(1)) #h1
print(ret.group(2)) #askh930s02391j192agsj
#print(ret.group(3)) # 这个就会报错了，没有group(3)

# 为什么要用分组,以及findall的分组优先到底有什么好处
exp = '2-3*(5+6)'
# a+b 或者是a-b 并且计算他们的结果
# ret = re.search('\d+[+]\d+',exp)
# print(ret)
# a,b = ret.split('+')
# print(int(a)+int(b))


# ret = re.search('(\d+)[+](\d+)',exp)
# print(ret)
# print(ret.group(1))
# print(ret.group(2))
# print(int(ret.group(1)) + int(ret.group(2)))


# with open('douban.html',encoding='utf-8') as f:
#     content = f.read()
# ret = re.findall('<span class="title">(.*?)</span>(?:\s*<span class="title">.*?</span>)?',content)
# print(ret)
# 如果我们要查找的内容在一个复杂的环境中
# 我们要查的内容并没有一个突出的 与众不同的特点 甚至会和不需要的杂乱的数据混合在一起
# 这个时候我们就需要把所有的数据都统计出来,然后对这个数据进行筛选,把我们真正需要的数据对应的正则表达式用()圈起来
# 这样我们就可以筛选出真正需要的数据了



# 什么是爬虫
    # 通过代码获取到一个网页的源码
    # 要的是源码中嵌着的网页上的内容   -- 正则表达式
# import requests
# ret = requests.get('https://baidu.com')
# a = ret.content.decode('utf-8')
# open('a.html',encoding='utf-8',mode='a').write(a)
# print(a,type(a))

# 分组和findall的现象
    # 为什么要用分组?
        # 把想要的内容放分组里
# 如何取消分组优先
    # 如果在写正则的时候由于不得已的原因 导致不要的内容也得写在分组里
    # (?:)  取消这个分组的优先显示



# split 匹配一个字符窜，以该字符串为分隔符，将整个字符串分成n个部分
# 并返回一个分好的列表，类似与字符串的 .split()方法
ret = re.split('\d+','hhhhhhh2222xxxxxx')
print(ret) #['hhhhhhh', 'xxxxxx']

## 用分组保留 一部分匹配到的分隔符字符串，但仍然分割整个字符串
ret = re.split('\d(\d{2})\d','hhhhhhh2222xxxxxx')
print(ret)  #['hhhhhhh', '22', 'xxxxxx']


# sub 替换，把匹配到的东西用别的东西替换
ret = re.sub('\d+','H','fojfio7423sjfwij374289sjdfo')
print(ret)  #fojfioHsjfwijHsjdfo

## re.sub() 还有个参数，可以指定替换次数，比如传入 1，就是只把第一次匹配到的替换了
## 别的都不动
ret = re.sub('\d+','H','fojfio7423sjfwij374289sjdfo',1)
print(ret)   #fojfioHsjfwij374289sjdfo


# subn 功能与sub 类似，但是返回一个元组，('替换后的字符串',替换次数)
ret = re.subn('\d+','H','fojfio7423sjfwij374289sjdfo')
print(ret) #('fojfioHsjfwijHsjdfo', 2)

# match 匹配以。。。开头的字符串，其他的功能跟 search 一样
# match 用来规定，你输入的字符串必须是这样的
ret = re.match('\d+','sfoejw12332533sfojw32435')
print(ret) #None

ret =  re.match('\d+','123sfoejw12332533sfojw32435')
print(ret) #<re.Match object; span=(0, 3), match='123'>
print(ret.group())  #123

# compile
# 如果一个正则表达式要被使用多次
# 我们可以先用 ret =re.compile('\d+') 来预编译正则
# 这样不仅可以节省写代码时间，也节省程序重复识别正则表达式的时间
# 但是如果一个正则，就用一次，那 compile 就不能帮助节省时间
ret = re.compile('\d+')  # 这个就类似 hashlib.md5() 的使用方法
res1 = ret.search('23425jdfsjfo')
res2 = ret.findall('23408dsjfos')
print(res1.group())
print(res2)

# finditer -- 节省空间
#
ret = re.finditer('\d+','3234dsjfoj4234')
for i in ret:
    print(i.group())


# compile 与 finditer 的配合使用，既节省时间又节省空间（内存）

ret = re.compile('\d+')
res = ret.finditer('284293djsfsjl239048sdfjkj')
for i in res:
    print(i.group())


# 分组命名 (?P<名字>正则)   (?P=名字)    (\1)(前引用)
# ret.group('名字')

# import re
# ret = re.search('\d(\d)\d(\w+?)(\d)(\w)\d(\d)\d(?P<name1>\w+?)(\d)(\w)\d(\d)\d(?P<name2>\w+?)(\d)(\w)',
#           '123abc45678agsf_123abc45678agsf123abc45678agsf')
#
# print(ret.group('name1'))
# print(ret.group('name2'))

# (?P<名字>正则表达式)
# ret.group('名字')

# 分组命名的引用
# import re
# exp= '<abc>akd7008&(&*)hgdwuih</abb>008&(&*)hgdwuih</abd>'
# ret= re.search('<(?P<tag>\w+)>.*?</(?P=tag)>',exp)
# print(ret)

import re
# exp= '<abc>akd7008&(&*)hgdwuih</abc>008&(&*)hgdwuih</abd>'
# ret= re.search(r'<(\w+)>.*?</\1>',exp)
# ret= re.search('<(\w+)>.*?</\\1>',exp)
# print(ret)

import re
# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret = ['1', '2', '60', '', '5', '4', '3','','']
# ret.remove('')
# print(ret)
# ret = filter(lambda n:n,ret)
# print(list(ret))

# 分组命名(?P<组名>正则) (?P=组名)
# 有的时候我们要匹配的内容是包含在不想要的内容之中的,
    # 只能先把不想要的内容匹配出来,然后再想办法从结果中去掉


# 功能
# 性能
    # 时间 ：你要完成一个代码所需要的执行的代码行数
    #        你在执行代码的过程中，底层程序是如何工作的
    # 比如 for i in range(1000):
    #           print(i)
    # 这是1000行代码
    # 空间 ：程序内数据都存储在内存里
        # 占用了宝贵的内存条资源
        # 影响程序的执行效率

```

## 4.规范性总结

```python
##规范性总结 来自 Eva-J 的博客

import re

ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
print(ret) #结果 : ['a', 'a']

ret = re.search('a', 'eva egon yuan').group()
print(ret) #结果 : 'a'
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

ret = re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配
print(ret)
#结果 : 'a'

ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  #结果 ： 123

import re
ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())  #查看第一个结果
print(next(ret).group())  #查看第二个结果
print([i.group() for i in ret])  #查看剩余的左右结果
```

