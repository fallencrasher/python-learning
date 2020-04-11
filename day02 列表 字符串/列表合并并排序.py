# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 21:54:32
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-03 22:46:12

#4.	两个列表[1,3,5,7,9]和[2,2,6,8]合并并排序
#结果为:[1,2,2,3,6,7,8,9]

l1 = [1,3,5,7,9]
l2 = [2,2,6,8]

def func(a,b):
    l = []
    l = a+b
    print(l)
    l.sort()
    return l



def main():
    l = func(l1,l2)
    print(l)
    print("完毕！")


if __name__ == "__main__":
    main()
