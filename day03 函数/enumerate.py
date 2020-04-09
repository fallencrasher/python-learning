# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-05 09:50:32
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-05 22:27:29


dict2 = {"jack": 78, "hanmeimei": 99, "lilei": 60}
t1 = (10, 20, 30, 10)
s1 = {10, 20, 30}
l1 = [10, 20, 30]

for i, j in enumerate(dict2):
    print(i, j)

for i, j in enumerate(t1):
    print(i, j)

for i, j in enumerate(s1):
    print(i, j)

for i, j in enumerate(l1):
    print(i, j)

for i in enumerate(l1):
    print(i)

print(enumerate(l1))


