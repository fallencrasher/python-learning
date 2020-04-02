l = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for i in l:
    for j in i:
    	print(j)

###升级一下，打印个小时候的九九乘法表
for i in range(1,10):
	for j in range(1,i+1):
		print("{}*{}={}".format(j,i,i*j),end=" ")
		if i == j:
			print()

