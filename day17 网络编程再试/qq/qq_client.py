import socket
BUFSIZE = 1024
udp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

qq_name_dic={
	'金老板':('127.0.0.1',43),
	'哪吒':('127.0.0.1',43),
	'egg':('127.0.0.1',43),
	'yuan':('127.0.0.1',43),

}

while True:
	qq_name = input('请选择聊天对象：').strip()
	while True:
		msg = input('请输入消息，回车发送，输入q结束和他的聊天：').strip()
		if msg.lower()=='q':break
		if not msg or not qq_name or qq_name not in qq_name_dic:continue
		udp_client_socket.sendto(msg.encode('utf-8'),qq_name_dic[qq_name])

		back_msg,addr = udp_client_socket.recvfrom(BUFSIZE)
		print('来自[%s:%s]的一条消息：\033[1;44m%s\033[0m'%(addr[0],addr[1],back_msg.decode('utf-8')))

udp_client_socket.close()