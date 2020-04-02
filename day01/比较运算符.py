
# >  <  >=  <=  ==  !=
n1 = int(input("请输入第一个数："))
n2 = int(input("请输入第二个数："))

#判断 n1 和 n2，这里result获得的值是True or  False

result = n1 > n2
print('n1 > n2:', result)

m1 = 'hello'
m2 = 'hello'
## ==  ！=  不仅可以应用于数字，字符串也行
result2 = m1 == m2
print("m1==m2:",result2)

username=input('请输入用户名：')
uname = 'admin123'
result3 = username != uname
print('用户名验证结果：',result3)

# is  

age = 20
age1 = 20
# python 自带一个内部函数 id()，可以判断变量在内存中的位置，如果两个变量是相等的，
# 那其实这两个变量就是同一个东西，他们储存在内存的同一个地方,
print(id(age))
print(id(age1))
print(age is age1)

money = 2000000
salary = 600000
print(id(money))
print(id(salary))
print(money is salsry)
print(money is not salary)

# 这个现象只出现在当你把一堆代码同时提交给解释器时，你在交互界面就不一样了
# 当赋值超过【-5，256】，每次都会重新创建新的内存地址



