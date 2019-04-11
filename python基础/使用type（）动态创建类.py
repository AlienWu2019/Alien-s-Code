def printHello (self,name = 'Py'):
    #定义一个打印Hello的函数
    print('Hello',name)


#创建一个Hello类
Hello = type('Hello',(object,),dict(hello = printHello))

#实例化Hello类
h = Hello()
#调用Hello类的方法
h.hello()
#查看Hello class的类型
print(type(Hello))
#查看实例h的类型
print(type(h))
