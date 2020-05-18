#############################################
# 环境变量
#############################################

# 在cmd 命令行中输入 python 打开 python.exe
# 在任何目录下都能找到 python.exe 文件，才能在任意位置打开命令行输入python打开python.exe

#############################################
# 启动数据库，登录
#############################################

# mysql -uroot -p xxx -h 192.168.14.12
# mysql> select user();  # 查看当前登录的用户，不要忘记写 “;”


#############################################
# 给自己设置密码，创建用户，授权
#############################################
#进入mysql客户端
$mysql
mysql> select user();  #查看当前用户
mysql> exit     # 也可以用\q quit退出

# 默认用户登陆之后并没有实际操作的权限
# 需要使用管理员root用户登陆
$ mysql -uroot -p   # mysql5.6默认是没有密码的
#遇到password直接按回车键
mysql> set password = password('root'); # 给当前用户设置密码

# 创建账号
mysql> create user 'eva'@'192.168.10.%'   IDENTIFIED BY '123';# 指示网段
mysql> create user 'eva'@'192.168.10.5'   # 指示某机器可以连接
mysql> create user 'eva'@'%'                    #指示所有机器都可以连接
mysql> show grants for 'eva'@'192.168.10.5';查看某个用户的权限
# 远程登陆
$ mysql -uroot -p123 -h 192.168.10.3

# 给账号授权
mysql> grant all on *.* to 'eva'@'%';
mysql> flush privileges;    # 刷新使授权立即生效

# 创建账号并授权
mysql> grant all on *.* to 'eva'@'%' identified by '123'

# 查看所有数据库
mysql> show databases;

# 创建数据库
mysql> create database 数据库名


#############################################
# 第一次登陆设置密码问题
#############################################
问题重现（以下讨论范围仅限Windows环境）：

C:\AppServ\MySQL > mysql -uroot -p
Enter password:
ERROR 1045(28000): Access denied for user 'root' @ 'localhost'(using password: YES)



编辑mysql配置文件my.ini（不知道在哪请搜索），在[mysqld]这个条目下加入
skip-grant-tables
保存退出后重启mysql

1.点击“开始”->“运行”(快捷键Win + R)。

2.停止：输入net stop mysql

3.启动：输入net start mysql

这时候在cmd里面输入mysql -uroot -p 就可以不用密码登录了，出现password：的时候直接回车可以进入，不会出现ERROR
1045(28000)，但很多操作都会受限制，因为我们不能grant（没有权限）。按下面的流程走（红色部分为输入部分，粉红色的是执行后显示的代码不用输入）：

1.进入mysql数据库：

mysql > use mysql;
Database changed

2.给root用户设置新密码，蓝色部分自己输入：
mysql > update user set password = password("新密码") where user = "root";
Query OK, 1 rows affected(0.01 sec)
Rows matched: 1 Changed: 1 Warnings: 0

3.刷新数据库
mysql > flush privileges;
Query OK, 0 rows affected(0.00 sec)

4.退出mysql：
mysql > quit
Bye

改好之后，再修改一下my.ini这个文件，把我们刚才加入的
"skip-grant-tables"
这行删除，保存退出再重启mysql就可以了。

#############################################
# 操作数据库
#############################################

# 查看数据库
mysql>show databases;

# 创建数据库
mysql>create database 数据库名;

# 切换到某个数据库下
mysql>use 数据库名

# 查看数据库下有多少表
mysql>show tables;

# 删除一个数据库
mysql>drop database 数据库名;

#############################################
# 表操作
#############################################

# 创建一张表
mysql>use day37 # 先指明要在那个数据库里操作
mysql>create table 表名(字段名1 数据类型(如果是字符串类型，直接指定长度上限，如果是int，就直接写),name char(12));
mysql>create table student(name,char(13),age int);

# 查看表结构
mysql>desc student;

# 插入数据 :
mysql>insert into student values ('alex',84); # 有两列，就按顺序添加两个数据
mysql>insert into student values ('wusir',86); # 有两列，就按顺序添加两个数据

# 查询数据 :
mysql>select * from student; # * 代表所有，也可以指定列名，一个或多个，用‘，’隔开

# 修改数据 ：
mysql>update student set age=86 where name='alex';

# 删除数据
mysql>delete from student where name='alex';