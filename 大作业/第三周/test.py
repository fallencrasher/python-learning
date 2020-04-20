# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 21:52:38
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-19 21:55:45

def div(exp):
    exp = exp.split('/',exp.count('/'))
    print(exp)
    exp_int=[]
    for i in exp:
        exp_int.append(int(i))
    print(exp_int)
    ret = exp_int[0]
    for j in range(1,len(exp_int)):
        ret /= exp_int[j]
        print(ret)
    return ret

print(div('8/4/2'))









def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
