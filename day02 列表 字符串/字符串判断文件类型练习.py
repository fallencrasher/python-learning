'''
@Author: Fallen
@Date: 2020-04-03 13:51:25
@LastEditTime: 2020-04-03 14:06:49
@LastEditors: Please set LastEditors
@Description: 字符串判断文件格式
@FilePath: \day02\字符串判断文件类型练习.py
'''
'''
练习：
 给定一个路径，上传文件（记事本txt或者是图片jpg,png）
 如果不是对应格式的，允许重新指定上传文件，
 如果符合上传的规定则提示上传成功

'''

#允许重复，就是个循环，一般是死循环然后设置个跳出机制,可以写成一个函数

def upfilePic():
    while True:
        path = input("请选择文件：") #"D:\pictures\background.jpg"
        p = path.rfind("\\")
        filename = path[p+1:]
        if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("bmp"):
            print("确实是图片，可以上传。")
        else:
            a = input("格式错误，重新上传嘛？(yes/no):")
            if a.lower()=="yes":
                continue
            if a.lower()=="no":
                break
            else:
                b = input("请输入yes或no：")
                continue

#调用函数
upfilePic()



