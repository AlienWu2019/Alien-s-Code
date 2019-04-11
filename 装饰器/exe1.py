def func(*args,**kwargs):
    """定义一个函数，引入参数，第一个为元组，第二个为字典"""
    print(args,kwargs)

func(1,2,3,4,x=1,y=2) #结果以元组，字典的形式返回