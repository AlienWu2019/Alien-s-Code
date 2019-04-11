def x(a):
    def y(b):
        return print(a+b)
    return y
xx=x(5)

xx(10)

xx(6)
