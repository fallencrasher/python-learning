import socket
import pickle


sk = socket.socket(type=socket.SOCK_DGRAM)

sk.bind(('127.0.0.1',43))

def loadfile(file):
	with open(file,'rb') as f:
		while True:
			try:
				yield pickle.load(f)
			except:
				break

while True:
	msg,addr = sk.recvfrom(1024)
	print(msg.decode('utf-8'),addr)
	with open('client_ip_port','ab') as f:
		temp = loadfile('client_ip_port')
		l = []
		for i in temp:
			l.append(i)
		if addr not in l:
			pickle.dump(addr,f)
	sk.sendto(msg.decode('utf-8').upper().encode('utf-8'),addr)
