from time import sleep
def outer(func):
    """闭包函数,作为装饰器,为函数增加功能"""
    def inner():
        print ('this is %s running'%func.__name__) #为函数增加的功能
        return func()
    print ('hello')
    return inner

@outer
def foo():
    print ('i am foo')
@outer
def foo1():
    print ('i am foo1')

@outer
def foo2():
    print ('i am foo2')

"""装饰器的工作：首先把使用装饰器的调用函数都读取进装饰器中，再分别调用装饰器闭包函数"""
foo()
sleep(2)
foo1()
sleep(2)
foo2()