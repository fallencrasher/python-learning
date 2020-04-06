# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-04 10:51:11
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-04 11:21:42

"""
冒泡排序，虽然，python自带 sort() 方法 和 sorted() 函数，但是还是要会
主要思想就是，一个列表，从前往后遍历，然后判断，要是后边的比前边的小就互换值，嗯，就是这样
"""
def bubbleSort(a_list):
    for i in range(len(a_list)):  #我们可能要循环列表好几遍，为啥呢，你笨想，一遍肯定不能把小值都拖到前边，得好几遍
        for j in range(0,len(a_list)-1-i):  #为啥要 -i ？，当 i = 0 ,第二层循环遍历范围是整个列表；当 i=1，第二层遍历的是没有最后一个元素的列表
            if a_list[j] > a_list[j+1]:     # 为啥要这么干？ 因为，我们遍历换位置操作，其实是将大值向后移动，在第一次遍历，最大值就会被移动到最后完成排序了，就不用再遍历它了
                a_list[j],a_list[j+1]=a_list[j+1],a_list[j]
    return a_list


        



list1 =   [64, 34, 25, 12, 22, 11, 90]
def main():
    new_list = bubbleSort(list1)
    print(new_list)
    print("排序完毕！")


if __name__ == "__main__":
    main()
