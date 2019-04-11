"""
def __setattr__(self,name,value):
    self.name = value
    #每当属性被赋值的时候，"__setatr__()"会被调用，这样就造成了递归调用
    #这意味这会调用"self.__setattr__('name',value)",每次方法会调用自己。这样会造成程序崩溃。

def __setattr__(self,name,value):
    #给类中的属性名分配值
    self.__dict__[name] = value
    #定制特有属性
"""

class User(object):
    def __getattr__(self, name):
        print('调用了__getattr__方法')
        return super(User,self).__getattr__(name)

    def __setattr__(self,name,value):
        print('调用了__setattr__方法')
        return super(User,self).__setattr__(name,value)

    def __delattr__(self, name):
        print('调用了__delattr__方法')
        return super(User,self).__delattr__(name)

    def __getattribute__(self, name):
        print('调用了__getattribute__方法')
        return super(User,self).__getattribute__(name)

if __name__ == "__main__":
    user = User()
    #设置属性值，会调用__setattr__
    user.attr1 = True
    #属性存在，只有__getattribute__调用
    user.attr1
    try:
        #属性不存在，先调用__getattribute__，后调用__getattr__
        user.attr2
    except AttributeError:
        pass
    #__delattr__调用
    del user.attr1

