#判断用户登录
#先定义数据库里的用户名密码
uid = "admin123"
password = "123456"
#再输入用户名密码
username = input("输入用户名：")
passwd = input("输入密码：")
if username != "" and passwd != "":
	if username == uid and passwd == password:
		print("登陆成功！")
	else:
		print("用户名或密码错误！")
else:
	print("用户名或密码不能为空！")
