print("*"*30,"捕鱼达人","*"*30)
username = input("输入参与者用户名：")
password = input("输入密码：")
print("%s 请充值才能加入游戏！" % username)
coins = int(input("您充值的金额为："))
print("%s 元充值成功！当前游戏币是：%d" % (username,coins))


