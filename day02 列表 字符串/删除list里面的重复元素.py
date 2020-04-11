# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 20:20:05
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-03 21:43:03

#1.写出一段Python代码实现删除一个list里面的重复元素
# 这里提供四种方法 分别为 func1()  func2()  func3()  func4()

originList = [1,2,3,3,4,4,5,5,42,6,23]


def func1(a_list):
    #一个一个往空列表加，加过的就不加了
    formatList = []
    for i in a_list:
        if i not in formatList:
            formatList.append(i)
    return formatList


def func2(a_list):
    #先用 集合格式化 set(),集合化后，自动去重，但是顺序就变了，在按照
    #之前的列表的索引进行排序，列表格式化 list()
    formatList = list(set(originList))
    formatList.sort(key=originList.index)
    return formatList


def func3(a_list):
    #直接set()集合格式化，再list()列表格式化回来
    formatList = list(set(a_list))
    return formatList


def func4(a_list):
    #使用字典的  fromkeys()  keys() 方法
    formatList = list({}.fromkeys(a_list).keys())
    return formatList





def main():
    formatList = func1(originList)
    print("去重完成！")
    print(formatList)

if __name__ == "__main__":
    main()
 