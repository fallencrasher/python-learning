#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/6 0006 21:41
# @File : func04.py
# @Software : PyCharm


"""
找出列表最大值
自己封装函数 不用 max()

"""


def max2(iterable):
    max = iterable[0]
    for i in iterable:
        if i > max:
            max = i
    print("max value is:", max)


list1 = [1, 5, 3, 6, 5, 7, 4, 8, 4, 10]
tuple1 = (1, 2, 6, 3, 5, 3, 7, 4, 2)
max2(list1)
max2(tuple1)

# sort min reverse
# how to know if it is a list?
# isinstance()

isinstance(2, int)


# sort

def sort2(list1):
    if isinstance(list1, list):
        for i in range(len(list1)):
            for j in range(0, len(list1) - i - 1):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        return list1
    else:
        print("not iterable!")


list1 = [1, 5, 3, 6, 5, 7, 4, 8, 4, 10]
list2 = sort2(list1)
print(list2)
