# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 14:47:28
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-19 14:51:13


# def fib(num):
#     if num == 1: return num
#     else: num+fib(num-1)
def fib(num):
    if num == 1 or num == 2: return 1
    else: 
        return fib(num-2)+fib(num-1)
   

# 找第100个数
# 1 1 2 3 5



def main():
    print("Hello, World!")
    print(fib(100))

if __name__ == "__main__":
    main()
