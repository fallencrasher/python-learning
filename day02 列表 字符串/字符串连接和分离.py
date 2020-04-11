'''
@Author: FALLEN
@Date: 2020-04-03 14:51:35
@LastEditTime: 2020-04-03 15:09:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \day02\字符串连接和分离.py
'''
list1 = ["a","b","c","d",1,2,3,4,5]
list2 = []
for i in list1:
    a = str(i)
    list2.append(a)
print(list2)
#join()方法，使用它前边的字符当作间隔符，括号里便的字符串活着列表内的单个字符
#元素连接起来
result = ''.join(list2)
print(result)
print(type(result))

result2 = 'fallen'.join(result)
print(result2)



