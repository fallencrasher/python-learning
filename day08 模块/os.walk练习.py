# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-21 19:44:34
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-21 20:17:57

# 使用walk来计算文件夹的总大小
import os
import sys

def getsize(path):
    sum = 0
    g = os.walk(path)
    print(g)
    #print(next(g))
    for i in g:
        _path,dir_lst,file_name_lst=i
        print(_path,file_name_lst)
        for j in file_name_lst:
            abs_path = os.path.join(_path,j)
            sum += os.path.getsize(abs_path)
    return sum




def main():
    path = sys.argv[1]
    #path = 'D:\\programming_with_python\\043从零开始学python\\day08 模块'
    print(f"{path}  的总大小为{getsize(path)}.")


if __name__ == "__main__":
    main()
