# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-04 21:37:47
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-05 22:59:20

# 先中断，以后有时间再写

'''
王者荣耀游戏,要有一下功能：
1.选择人物
2.花掉金币购买武器，卖出武器得到金币
3.可以去打架，打架可以获得金币
4.可以查看都有什么武器
5.可以退出游戏
'''


def choose_hero():
    # 选英雄
    hero_list = ["鲁班", "后羿", "李白", "孙尚香", "貂蝉", '诸葛亮']
    choice = ""
    while True:
        choice = input("请选择人物：(1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮)：")
        if choice not in hero_list:
            print("必须选给定的英雄！")
            continue
        else:
            return choice


def buy_weapon(coins, weapon_list):
    # 买武器
    weapon_store = [["饮血剑", 2850], ["宗师之力", 2600], [
        '破军', 3200], ['冰心', 2800], ['电刀', 2100], ['天绝大典太', 4000]]
    weapon_store = dict(weapon_store)
    coins = coins
    while True:
        print("武器商店：{}".format(weapon_store))
        weapon_choice = input("您当前拥有的金币为{}，请输入你要购买的武器:".format(coins))
        if weapon_choice in weapon_store.keys() and coins >= weapon_store[weapon_choice]:
            weapon_list.append(weapon_choice)
            coins -= weapon_store[weapon_choice]
            judge = input(
                "购买{}成功，您当前剩余金币为{}。继续购买吗？(yes/no):".format(weapon_choice, coins))
            if judge.lower() == 'yes':
                continue
            elif judge.lower() == "no":
                return weapon_list, coins
                break
            else:
                print("输入错误，系统将回到主界面。")
                return weapon_list, coins
                break

        elif weapon_choice not in weapon_store.keys():
            print("必须选择武器商店里的武器！")
            continue
        elif coins < weapon_store[weapon_choice]:
            print("金币不足！请打架赚取金币！")
            return weapon_list, coins


def sale_weapon(weapon_list, coins):
    # 卖武器
    weapon_store = [["饮血剑", 2850], ["宗师之力", 2600], [
        '破军', 3200], ['冰心', 2800], ['电刀', 2100], ['天绝大典太', 4000]]
    weapon2sale = []
    while True:
        print(weapon_list)
        weapon2sale = input("请选择你要卖出的武器：")
        if weapon2sale in weapon_list:
            weapon_list.remove(weapon2sale)
            coins += weapon_store[weapon2sale]
            judge = input(
                "卖出{}成功，您当前剩余金币为{}。继续购买吗？(yes/no):".format(weapon2sale, coins))
            if judge.lower() == 'yes':
                continue
            elif judge.lower() == "no":
                return weapon_list, coins
                break
            else:
                print("输入错误，系统将回到主界面。")
                return weapon_list, coins
                break
        elif weapon2sale not in weapon_list:
            print("你只能卖出你拥有的武器。")


def main():
    # 欢迎界面
    print("*"*40)
    print("\t 欢迎来到王者荣耀")
    print("*"*40)
    # 初始金币
    global coins
    coins = 800
    global weapon_list
    weapon_list = []
    while True:
        judge = int(input(
            "请选择您要进行的操作：\n1.选择人物\n2.购买武器\n3.卖出武器\n4.打架获得金币\n5.查看已经拥有的武器\n6.退出游戏\n(请输入数字代码):"))
        if judge in (1, 2, 3, 4, 5, 6):
            if judge == 1:
                # 选人
                hero = choose_hero()
                print("您选择了{}。当前金币为{}。".format(hero, coins))

            elif judge == 2:
                # 购买武器
                weapon_list, coins = buy_weapon(weapon_list, coins)
                print("您当前拥有的武器有：{}。\n您当前拥有的金币为：{}。".format(weapon_list, coins))

            elif judge == 3:
                # 卖出武器
                weapon_list, coins = sale_weapon(weapon_list, coins)
                print("您当前拥有的武器有：{}。\n您当前拥有的金币为：{}。".format(weapon_list, coins))

            elif judge == 4:
                # 打架获得金币
                pass
            elif judge == 5:
                # 查看所有拥有的武器
                pass
            elif judge == 6:
                # 退出游戏
                judge = input("退出游戏吗？(yes/no):")
                if judge == "yes":
                    break
        else:
            print("必须输入数字代码！")
            continue


if __name__ == "__main__":
    main()
