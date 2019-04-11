#运算符重载
class opera:
    def __init__(self,a,b):
        self.a = a;
        self.b = b;
    def __str__(self):
        return 'opera(%d,%d)'%(self.a,self.b)
    def __add__(self,other):
        return opera(self.a+other.a,self.b+other.b)
v1 = opera(2,10)
v2 = opera(5,-2)
print (v1 + v2)
