# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 19:09:03
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-03 21:43:08

'''
小易喜欢的单词具有以下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母

例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词。

'''
def func():
    #现有个单词
    word = input("请输入一个单词：")
    for i in range(len(word)):
        if not word.isupper():
            print("小明不喜欢。没大写~")
            break
        elif i<(len(word)-1)  and word[i]==word[i+1]:
            print("小明不喜欢。叠词~")
            break
    else:
        print("小明喜欢。")
    

def main():
    func()


if __name__ == "__main__":
    main()
