'''
@Author: Fallen
@Date: 2020-04-03 14:14:14
@LastEditTime: 2020-04-03 14:30:47
@LastEditors: Please set LastEditors
@Description: 连续相加计算器
@FilePath: \day02\连续相加计算器.py
'''

#连续二字，告诉我，这是个循环
#有个问题，isnumeric() 和 isdigit() 只能判断是不是字符都是数值的，所以如果是个浮点数，有小数点，就会告诉你不是数值类型的咋整
#所谓数字相加，浮点数也是数字呢，咋办
#这就需要，正则表达式 来匹配了，这个以后细学，现在还不太会，所以只做整型的

def sum():
    sum = 0
    while True:
        plus = input("请输入数字(输入'q'退出):")
        if plus == "q":
            return sum
        elif plus.isdigit():
            plus = int(plus)
            sum += plus
            print("相加和是：{}。".format(sum))
        else:
            print("不是数字！")
            continue

a = sum()
print(a)