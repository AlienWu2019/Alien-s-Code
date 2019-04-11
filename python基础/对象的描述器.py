class User(object):
    def __init__(self,name = '两点水',sex = '男'):
        self.sex = sex
        self.name = name

    def __get__(self,obj,objtype):
        print('获取name值')
        return self.name

    def __set__(self, obj, val):
        print('设置name值')
        self.name = val

class MyClass(object):
    x = User('两点水','男')
    y = 5

if __name__ == "__main__":
    m = MyClass()
    print(m.x)
    print('\n')

    m.x = '三点水'
    print(m.x)

    print('\n')

    print(m.x)

    print('\n')

    print(m.y)

################################################
print('-----------------------------------------------')

class Meter(object):
    def __init__(self,value = 0.0):
        self.value = float(value)

    def __get__(self,instance,owner):
        return self.value

    def __set__(self,instance,value):
        self.value = float(value)

class Foot(object):
    def __get__(self,instance,owner):
        return instance.meter *3.2808

    def __set__(self,instance,value):
        instance.meter = float(value)/3.2808

class Distance(object):
    meter = Meter()
    foot = Foot()

if __name__ == "__main__":
    d = Distance()
    print(d.meter,d.foot)
    d.meter = 1
    print(d.meter,d.foot)
    d.meter = 2
    print(d.meter,d.foot)
    d.foot = 6
    print(d.meter,d.foot)
