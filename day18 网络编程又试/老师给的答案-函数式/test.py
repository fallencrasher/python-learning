import hashlib

def get_md5(username,password):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())

get_md5('alex','3714')