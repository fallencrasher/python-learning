# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 17:48:43
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-03 19:08:48

'''
1.输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
例如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”

'''

def func():
        #先输入两个字符串
    s1 = input("输入第一个字符串:")
    s2 = input("输入第二个字符串:")
    #在s1里匹配s2里所有的单个字符，并删除
    #嗯，所有的，就是个循环呗
    for i in s2:
        if i in s1:
            s1=s1.replace(i,"")
        else:
            continue
    print(s1)

    #活着都不用if语句判断
    # for i in s2:
    # 	s1= s1.replace(i,'')
    # print(s1)

def main():
    func()


if __name__ == "__main__":
    main()
