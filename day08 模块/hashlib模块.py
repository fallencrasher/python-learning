#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-16 14:50:41
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
hashlib模块：用于加密
封装了一些加密的类
加密的目的适用于判断和验证 最多用 md5()

特点：
	- 把一个大的数据且奉承不同小块，分别对不同小块进行加密，在汇总结果，和直接对整体加密的结果是一致的
	- 单项加密，一般不可逆
	- 演示数据的一点小变化，将导致结果的非常大的差异
'''

# 那，这么牛逼，怎么用呢
import hashlib

# 先看看他都有啥方法啊
print(dir(hashlib))

'''
['__all__', '__block_openssl_constructor', '__builtin_constructor_cache', '__builtins__', '__cached__', '__doc__', '__file__', '__get_builtin_constructor', '__loader__', '__name__', '__package__', '__spec__', '_hashlib', 'algorithms_available', 'algorithms_guaranteed', 'blake2b', 'blake2s', 'md5', 'new', 'pbkdf2_hmac', 'scrypt', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256']
'''
# 给一个数据加密的三大步骤：
# 获取一个加密对象
m = hashlib.md5()

# 使用加密对象的 update 方法 ,对目标进行加密，加密方法 update
# 可以加密多次
m.update('abc中文'.encode('utf-8'))
m.update('def'.encode('utf-8'))

#通过 hexdigest 获取加密结果 或直接用 digest()来获取，但 digest()获取的是二进制，所以少用

res = m.hexdigest()
print(res) #2f1b6e294e72d25ae196fe4ac2d27de6

# 给一个数据加密
# 验证：用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同

'''
它通过一个函数，把任意长度的数据按照一定规则转换为一个固定长度的数据串（通常用16进制的字符串表示）。

比如：之前我们在一个文件中存储用户的用户名和密码是这样的形式：

    太白|123456

有什么问题？你的密码是明文的，如果有人可以窃取到这个文件，那么你的密码就会泄露了。所以，一般我们存储密码时都是以密文存储，比如：

    太白|e10adc3949ba59abbe56e057f20f883e

那么即使是他窃取到这个文件，他也不会轻易的破解出你的密码，这样就会保证了数据的安全。

hashlib模块就可以完成的就是这个功能。

hashlib的特征以及使用要点：

bytes类型数据 ---> 通过hashlib算法 ---> 固定长度的字符串

不同的bytes类型数据转化成的结果一定不同。

相同的bytes类型数据转化成的结果一定相同。

此转化过程不可逆。

那么刚才我们也说了，hashlib的主要用途有两个：

    密码的加密。

    文件一致性校验。

hashlib模块就相当于一个算法的集合，这里面包含着很多的算法，算法越高，转化成的结果越复杂，安全程度越高，相应的效率就会越低。
'''
# 1.密码的加密
# 以常见的 md5 为例，计算出一个字符串的 md5 值
import hashlib

md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
res = md5.hexdigest()
print(res)

## 计算结果如下
## 'e10adc3949ba59abbe56e057f20f883e'

## 验证：相同 bytes 数据转化的结果一定相同
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
res = md5.hexdigest()
print(res)

## 计算结果如下
## 'e10adc3949ba59abbe56e057f20f883e'

## 验证：不同 bytes 数据转化的结果一定不同

md5 = hashlib.md5()
md5.update('12345'.encode('utf-8'))
res = md5.hexdigest()
print(res)

## 计算结果如下
## '827ccb0eea8a706c4c34a16891f84e7b'

'''
上面就是普通的md5加密，非常简单，几行代码就可以了，但是这种加密级别是最低的，相对来说不很安全。虽然说hashlib加密是不可逆的加密方式，但也是可以破解的，那么他是如何做的呢？你看网上好多MD5解密软件，他们就是用最low的方式，空间换时间。他们会把常用的一些密码比如：123456,111111,以及他们的md5的值做成对应关系，类似于字典，

dic = {'e10adc3949ba59abbe56e057f20f883e': 123456}

然后通过你的密文获取对应的密码。

只要空间足够大，那么里面容纳的密码会非常多，利用空间换取破解时间。 所以针对刚才说的情况，我们有更安全的加密方式：加盐。
'''
#2.加盐加密,就是在创建加密对象的时候给 hashlib.md5()传个参数
##2.1 固定的盐
'''
什么叫加盐？加盐这个词儿来自于国外，外国人起名字我认为很随意，这个名字来源于烧烤，俗称BBQ。我们烧烤的时候，一般在快熟的时候，都会给肉串上面撒盐，增加味道，那么这个撒盐的工序，外国人认为比较复杂，所以就讲比较复杂的加密方式称之为加盐
'''
ret = hashlib.md5('一山一晴'.encode('utf-8')) #这个'一山一晴'就是固定的盐
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())
'''
上面的'一山一晴'就是固定的盐，比如你在一家公司，公司会将你们所有的密码在md5之前增加一个固定的盐，这样提高了密码的安全性。但是如果黑客通过手段窃取到你这个固定的盐之后，也是可以破解出来的。所以，我们还可以加动态的盐。
'''

## 2.2 动态的盐
username = 'fallen'
ret = hashlib.md5(username[::2].encode('utf-8')) #这样针对每个账户，每个账户 盐都不一样
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())
'''
这样，安全性能就大大提高了。

那么我们之前说了hahslib模块是一个算法集合，他里面包含很多种加密算法，刚才我们说的MD5算法是比较常用的一种加密算法，一般的企业用MD5就够用了。但是对安全要求比较高的企业，比如金融行业，MD5加密的方式就不够了，得需要加密方式更高的，比如sha系列，sha1,sha224,sha512等等，数字越大，加密的方法越复杂，安全性越高，但是效率就会越慢。
sha1,sha224,sha512等都是算法名称，跟 md5 是一样的。用法也一样
但我们多数就用 md5 就行了
'''
ret = hashlib.sha1()
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())

##也可以加盐
ret = hashlib.sha384('爱你么么哒'.encode("utf-8"))
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())

##也可以加动态的盐
dongtai = 'qingtianyigepili'
ret = hashlib.sha224(dongtai[::2].encode('utf-8'))
ret.update('要加密的东西'.encode('utf-8'))
print(ret.hexdigest())

# 3.文件的一致性校验
'''
以下说明，抄自太白金星老师的博客：这个文档里的大段文字都是从他那抄的
hashlib模块除了可以用于密码加密之外，还有一个常用的功能，那就是文件的一致性校验。

    linux讲究：一切皆文件，我们普通的文件，是文件，视频，音频，图片，以及应用程序等都是文件。我们都从网上下载过资源，比如我们刚开学时让大家从网上下载pycharm这个软件，当时你可能没有注意过，其实你下载的时候都是带一个MD5或者shax值的，为什么？ 我们的网络世界是很不安全的，经常会遇到病毒，木马等，有些你是看不到的可能就植入了你的电脑中，那么他们是怎么来的？ 都是通过网络传入来的，就是你在网上下载一些资源的时候，趁虚而入，当然大部门被我们的浏览器或者杀毒软件拦截了，但是还有一部分偷偷的进入你的磁盘中了。那么我们自己如何验证我们下载的资源是否有病毒呢？这就需要文件的一致性校验了。在我们下载一个软件时，往往都带有一个MD5或者shax值，当我们下载完成这个应用程序时你要是对比大小根本看不出什么问题，你应该对比他们的md5值，如果两个md5值相同，就证明这个应用程序是安全的，如果你下载的这个文件的MD5值与服务端给你提供的不同，那么就证明你这个应用程序肯定是植入病毒了（文件损坏的几率很低），那么你就应该赶紧删除，不应该安装此应用程序。

我们之前说过，md5计算的就是bytes类型的数据的转换值，同一个bytes数据用同样的加密方式转化成的结果一定相同，如果不同的bytes数据（即使一个数据只是删除了一个空格）那么用同样的加密方式转化成的结果一定是不同的。所以，hashlib也是验证文件一致性的重要工具。
'''

## 3.1 文件校验函数 low 版
f = open('hashlib_file1','w')
f.write('abcd')
f.close()
def func(file):
	with open(file,mode='rb') as f1:
		ret = hashlib.md5()
		ret.update(f1.read())
		return ret.hexdigest()
print(func('hashlib_file1'))
'''
这样就可以计算此文件的MD5值，从而进行文件校验。但是这样写有一个问题，类似我们文件的改的操作，有什么问题？如果文件过大，全部读取出来直接就会撑爆内存的，所以我们要分段读取，那么分段读取怎么做呢？
'''
## 3.2 hashlib 分段读取文件
### 直接读取
md5obj = hashlib.md5()
md5obj.update('一山是个大帅哥'.encode('utf-8'))
print(md5obj.hexdigest()) #ffe423b0b5b717c937be394c6860a6c0

### 分段读取
md5obj = hashlib.md5()
md5obj.update('一山'.encode('utf-8'))
md5obj.update('是'.encode('utf-8'))
md5obj.update('个'.encode('utf-8'))
md5obj.update('大'.encode(('utf-8')))
md5obj.update('帅'.encode('utf-8'))
md5obj.update('哥'.encode('utf-8'))
print(md5obj.hexdigest()) #ffe423b0b5b717c937be394c6860a6c0

### 文件校验函数 高大上版
def file_check(file_path):
	with open(file_path,mode='rb') as f1:
		sha256 = hashlib.sha256()
		while 1:
			content = f1.read(1024)
			if content:
				sha256.update(content)
			else:
				return sha256.hexdigest()
print(file_check(r'D:\科研软件\geek.exe'))


#练习：注册后保存用户信息，登录时验证

def get_md5(username,password):
	m = hashlib.md5()
	m.update(username.encode('utf-8'))
	m.update(password.encode('utf-8'))
	return m.hexdigest()


def register(username,password):
	# 加密
	res = get_md5(username,password)
	# 写入文件
	with open('login',mode='a',encoding='utf-8') as f,open('user',mode='a',encoding='utf-8') as f2, \
		open('user',mode='r',encoding='utf-8') as f3:
		lst = []
		for u in f3:
			lst.append(u.strip())
		if username not in lst:
			f.write(res+'\n')
			f2.write(username+'\n')
		else:
			print('已注册过，请登录')

def login(username,password):
	# 获取输入的信息的加密信息
	res = get_md5(username,password)
	# 读文件
	with open('login',mode='rt',encoding='utf-8') as f:
		for line in f:
			if res == line.strip():
				return True




def main():
	while True:

		judge = input('1.注册 2.登录 3.退出：')
		if judge.isdigit() and int(judge) in (1,2,3):
			if int(judge)==3:
				print('quit~')
				break
			elif int(judge)==1:
				username = input('username:')
				password = input('password:')
				register(username,password)
			elif int(judge)==2:
				username = input('username:')
				password = input('password:')
				with open('user',mode='r',encoding='utf-8') as f2:
					lst1 = []
					for u in f2:
						lst1.append(u.strip())
					if username not in lst1:
						print('please register first!')
					else:
						res = login(username,password)
						if res==True:
							print('login successfully!')
						else:
							print('username or password error. \n')
		else:
			print("你必须输入给定的序号！")


if __name__ == '__main__':
	main()



