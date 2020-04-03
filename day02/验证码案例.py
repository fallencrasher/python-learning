'''
@Author: FALLEN
@Date: 2020-04-03 09:49:14
@LastEditTime: 2020-04-03 10:09:37
@LastEditors: Please set LastEditors
@Description: 字符串内建函数的练习，验证码案例
@FilePath: \day02\验证码案例.py
'''
# 验证码就是一般四个字符的的字符串
s ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print(len(s))

# 如何随机从这里取出来4个字符呢，我们随机产生4个索引就成了

import random



# 在s里随机取四个值
code = ""
for i in range(0,4):
    ranIndex = random.randint(0,len(s)-1)
    code += s[ranIndex]

print(code)

# 还可以提醒用户输入并判断对错,并且忽略大小写
x = input("请输入验证码：")
print(x.lower(),code.lower())
if x.lower()==code.lower():
    print("验证码正确")
else:
    print("验证码错误")