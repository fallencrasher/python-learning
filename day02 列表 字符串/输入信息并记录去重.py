# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 21:44:14
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-03 21:53:36

#2.键盘输入多个人名保存到一个列表中，如果里面有重复的则提示此姓名已经存在

def func():
    name = []
    while True:
        temp = input("输入名字(输入'q'退出)：")
        if temp.lower()=="q":
            return name
            break
        elif temp in name:
            print("重复输入！")
            continue
        else:
            name.append(temp)
            continue



def main():
    name = func()
    print(name)
    print("记录完毕！")



if __name__ == "__main__":
    main()
