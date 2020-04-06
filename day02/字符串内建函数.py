# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 19:52:43
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-04 10:45:43
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
# encode()  decode() 汉字-encode--》字节    字节--decode--》汉字
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
##isalpha() isdigit()  这俩都返回布尔类型的结果

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



