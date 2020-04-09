# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-09 16:31:25
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-09 16:48:49

'''
a ab a+ a+b
'''
#当文件不存在，就创建一个
f = open('.\\文件的追加',encoding='utf-8',mode='a')
f.write('太白最帅。。。')
f.close()

#有文件，就可以再后边去追加字符
f = open('文件的追加',encoding='utf-8',mode='a')
f.write('大壮，舒淇，b哥，学费')
f.close()



