def add(x,y):
    z=x+y
    return z
def minus(x,y):
    z=x-y
    return z
if __name__=="__main__":#如果模块独立运行不被调用，则__name__属性为"__main__"，否则为："__addMinus__"
    print("this is a testing file,not  be used")
    print(__name__)
elif  __name__=="addMinus":
    print("addMinus.py be used")