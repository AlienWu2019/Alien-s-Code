#定义两个闭包函数作为装饰器，然后主体函数使用两个装饰器
def outer1(func):
    """定义第一个装饰器"""
    def inner1():
        print ("hello")
        return func()
    return inner1

def outer2(func):
    """定义第二个装饰器"""
    def inner2():
        print("world")
        return func()
    return inner2

#主体函数使用2个装饰器
@outer1
@outer2  #outer1-》outer2-》foo
def foo():
    print ("我使用了两个装饰器")

#实例化主体函数
foo()