#############################################
# 了解数据在程序中的应用
#############################################
'''
记录：1 朱葛 13234567890 22（多个字段的信息组成一条记录，即文件中的一行内容）

表：userinfo,studentinfo,courseinfo（即文件）

数据库：db（即文件夹）

数据库管理系统：如mysql（是一个软件）

数据库服务器：一台计算机（对内存要求比较高）

总结：

    数据库服务器-：运行数据库管理软件

    数据库管理软件：管理-数据库

    数据库：即文件夹，用来组织文件/表

    表：即文件，用来存放多行内容/多条记录
'''

#############################################
# 了解关系型和非关系型数据库
#############################################
'''
可以简单的理解为，关系型数据库需要有表结构，非关系型数据库是key-value存储的，没有表结构

关系型：如sqllite，db2，oracle，access，sql server，MySQL，注意：sql语句通用
    相对慢
    各种对应表
非关系型：mongodb，redis，memcache
    快，不能用存储内容来查找关键字
    例如 快递 快递单号
'''

#############################################
# mysql 安装
#############################################

'''
解压
下载的zip文件解压，将解压之后的文件夹放到任意目录下，这个目录就是mysql的安装目录。

配置
打开目录，会看到my-default.ini配置文件，复制这个配置文件可以重命名为my.ini或者my.cnf

# 在配置文件夹里写入一下东西，注意修改 basedir  datadir
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8 
[mysqld]
#设置3306端口
port = 3306 
# 设置mysql的安装目录
basedir=C:\Program Files\mysql-5.6.39-winx64 
# 设置mysql数据库的数据的存放目录
datadir=C:\Program Files\mysql-5.6.39-winx64\data 
# 允许最大连接数
max_connections=200
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB

环境变量
在系统变量PATH后面添加: 你的mysql bin文件夹的路径（如C:\Program Files\mysql-5.6.41-winx64\bin）

安装MySQL服务
以管理员身份打开cmd窗口后，将目录切换到你解压文件的bin目录，输入
mysqld install  #回车运行
这样，mysql服务就注册写入到了操作系统中，在windows  服务 中可以查找到


启动mysql服务
以管理员身份在cmd中输入:
net start mysql
这样我们就开启了 mysql 服务，而且以后他就自己会开机自启动了


服务启动成功之后，就可以登录了，输入
mysql -u root -p（第一次登录没有密码，直接按回车过）


net stop mysql # 停止mysql

#在windows操作系统上没有重启mysql服务的命令
#如果要重启服务，只能先stop再start
'''
