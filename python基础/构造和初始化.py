class User(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

use = User('两点水',23)

#############################################

class User1(object):
    def __new__(cls,*args,**kwargs):
        #打印__new__方法中的相关信息
        print('调用了def __new__方法')
        print(args)
        #最后返回父类的方法
        return super(User1,cls).__new__(cls)

    def __init__(self,name,age):
        print('调用了 def __init__方法')
        self.name = name
        self.age = age

if __name__ == "__main__":
    user1 = User1('两点水',23)

