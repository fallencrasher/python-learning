'''
@Author: Fallen
@Date: 2020-04-02 09:17:32
@LastEditTime: 2020-04-02 15:25:15
@LastEditors: Please set LastEditors
@Description: 练习循环和if语句的逻辑
@FilePath: \043从零开始学python\day02\赌场游戏.py
'''
print("""
***************************************************************
			欢迎进入游戏
***************************************************************					       
	""")

username = input("请输入用户名：")
print("欢迎您，{}".format(username))

inform = input("您当前的游戏币余额0，请充值。充值金额须是100的倍数，充值成功可以再次充值。100元30个游戏币。\n您是否选择充值？（yes/no）：")	

def coinsplus():
	coins = 0
	while True:	
		
		chongzhi = input("请输入充值金额：")
		
		
		if int(chongzhi)%100==0 and (int(chongzhi) !=0 and int(chongzhi) > 0) :
			coins += int(chongzhi)//100*30
			loop = input("充值成功，当前余额{}个游戏币。继续充值吗?(yes/no)".format(coins))
			if loop.lower()=="yes":
				continue
			elif loop.lower() == "no":
				return coins
			else:
				loop=input("请输入yes或no:")
				continue
		else:
			print("请输入充值金额，充值金额必须为100倍数。")
	




# 充值
def chongzhi(inform):
	while True:
		global coins		
		if inform.lower()=="yes":
			coins = coinsplus()
			return coins
			break
		elif inform.lower()=="no":
				
			print("你当前的余额为0，请充值。")
			coins = coinsplus()
			return coins
			break
		
		else:
			inform = input("请输入yes或no:")
			continue
			
	
	
	
#玩游戏

import random




def game(inform):
	conisleft = chongzhi(inform)
	inform2 = input("要开始游戏吗？(yes/no):")
	while True:
		if inform2.lower()=="yes":
			conisleft -= 2
			if conisleft >=2:
				# 问题，如何添加更多的操作性？
				computer = random.randint(0,6)
				yourdacer = random.randint(0,6)
				if computer < yourdacer:
					conisleft += 6
					a = input("电脑是{}，你是{}。你赢了！得到了6个游戏币的奖励。你还有{}个游戏币。再来一局吗？(yes/no):".format(computer,yourdacer,conisleft))
					if a.lower()=="yes":
						continue
					elif a.lower()=="no":
						print("欢迎再次光临！")
						break
					else:
						a = input("请输入yes或no：")
						continue
				elif computer > yourdacer:	
					b = input("电脑是{}，你是{}。你输了！你还有{}个游戏币。再来一局吗？(yes/no):".format(computer,yourdacer,conisleft))
					if b.lower()=="yes":
						continue
					elif b.lower()=="no":
						print("欢迎再次光临！")
						break
					else:
						b = input("请输入yes或no：")
						continue
				elif computer == yourdacer:
					c = input("电脑是{}，你是{}。平局！你还有{}个游戏币。再来一局吗？(yes/no):".format(computer,yourdacer,conisleft))
					if c.lower()=="yes":
						continue
					elif c.lower()=="no":
						print("欢迎再次光临！")
						break
					else:
						c = input("请输入yes或no：")
						continue
			else:
				print("余额不足，请充值！")
				conisleft=conisleft+chongzhi(inform)
				continue
		elif inform2.lower()=="no":
			print("欢迎下次再来！")
			break
		else:
			inform2=input("请输入yes或no:")
			continue



if __name__=="__main__":
	game(inform)




