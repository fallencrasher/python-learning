# pickle 很强大，可以保存python对象，加载出来以后还就可以直接用
# json 就不成，json只能保存成字符串

class Course:
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price

python = Course('python','6 moneth',21800)
linux = Course('linux','5 moneth',19800)
go = Course('go','4 moneth',12800)
import  pickle
with open('pickle_file','ab') as f:
    pickle.dump(linux,f)
    pickle.dump(go,f)
with open('pickle_file','rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            print(obj.name,obj.period)
        except EOFError:
            break
