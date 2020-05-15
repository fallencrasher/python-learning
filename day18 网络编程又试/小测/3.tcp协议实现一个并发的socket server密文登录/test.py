import hashlib


def get_md5(username, password):
	md5 = hashlib.md5(username.encode('utf-8'))
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

print(get_md5('qing','123456'))
