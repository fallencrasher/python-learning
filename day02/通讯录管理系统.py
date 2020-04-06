# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 20:13:47
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-04 01:33:28

'''
通讯录管理系统：
1.增加姓名和手机
2.删除姓名
3.修改手机
4.查询所有用户 ??
5.根据姓名查找手机
6.推出
'''

def collect_name_and_phone_number(address_book):
    #添加姓名和手机信息，并记录

    dic = address_book
    name = []
    phone_number = []
    while True:
        temp_name = input("输入名字(长度不超过20位，超过20位，就只保留20位)(输入'q'退出)：")
        
        if temp_name.lower()=="q":
            return dic
            break
        # elif temp_name != "q":
        #     temp_phone = input("输入手机号码(输入'q'退出):")
        #     if temp_phone =="q":
        #         return dic
        #         break       
        elif temp_name in name:
            print("重复输入！")
            continue
        else:
            temp_phone = input("输入手机号码:")
            temp_phone = temp_phone[0:13]
            temp_name = temp_name[0:20]
            name.append(temp_name)
            phone_number.append(temp_phone)
            dic[temp_name]=temp_phone
            continue


def delete(x,address_book):
    #删除姓名
    x=str(x)
    del address_book[x]

def fix_phone(name,new_phone,address_book):
    #修改手机，修改谁的手机
    name = str(name)
    new_phone = str(new_phone)
    address_book[name]=new_phone

def search(name,address_book):
    #查询目标用户手机是啥
    name=str(name)
    result = address_book[name]
    print("{}的手机号码是：{}".format(name,result))

def list_all_users(address_book):
    #看看都有那些用户
    print(address_book)





def main():
    global address_book
    address_book={}
    while True:
        
        judge = input('''
            请输入您想进行的操作：
            1.增加姓名和手机
            2.删除姓名
            3.修改手机
            4.查询所有用户 
            5.根据姓名查找手机
            6.退出
            请输入相应数字代号行驶功能！
            想要有完整体验，请先运行1。
        :''')
        if judge.isdigit() and int(judge) in (1,2,3,4,5,6):

            if int(judge)==1:
                
                address_book = collect_name_and_phone_number(address_book) 
                judge1 = input("回到上一层吗？(yes/no):")
                if judge1.lower()=='yes':
                    continue
                elif judge1.lower()=="no":
                    print("谢谢使用！")
                    break
                else:
                    judge1=input("输入非yes或no，系统将自动退回主界面。")
                    continue
            elif int(judge)==2:
                name2delete = input("请输入要删除的姓名：")
                if name2delete in address_book:
                    delete(name2delete,address_book)
                    judge2 = input("回到上一层吗？(yes/no):")
                    if judge2.lower()=='yes':
                        continue
                    else:
                        print("谢谢使用！")
                        break
                else:
                    judge22 = input("没有这个姓名！回到上一层吗？(yes/no):")
                    if judge22.lower()=='yes':
                        continue
                    else:
                        print("谢谢使用！")
                        break
            elif int(judge)==3:
                name2fix = input("请输入要修改手机人的姓名：")
                if name2fix in address_book:
                    phone2fix = input("请输入修改后的手机号码：")
                    fix_phone(name2fix,phone2fix,address_book)
                    judge3 = input("回到上一层吗？(yes/no):")
                    if judge3.lower()=='yes':
                        continue
                    else:
                        print("谢谢使用！")
                        break
                else:
                    judge33 = input("没有这个姓名！回到上一层吗？(yes/no):")
                    if judge33.lower()=='yes':
                        continue
                    else:
                        print("谢谢使用！")
                        break
            elif int(judge)==4:
                list_all_users(address_book)
                judge4 = input("回到上一层吗？(yes/no):")
                if judge4.lower()=='yes':
                    continue
                else:
                    print("谢谢使用！")
                    break
            elif int(judge)==5:
                name2search = input("请输入要查找人的姓名：")
                if name2search in address_book:
                    search(name2search,address_book)
                    judge5 = input("回到上一层吗？(yes/no):")
                    if judge5.lower()=='yes':
                        continue
                    else:
                        print("谢谢使用！")
                        break
                else:
                    judge55 = input("没有这个姓名！回到上一层吗？(yes/no):")
                    if judge55.lower()=='yes':
                        continue
                    else:
                        print("谢谢使用！")
                        break
            elif int(judge)==6:
                break
        else:
            print("必须输入数字0-6！")
            continue

if __name__ == "__main__":
    main()
