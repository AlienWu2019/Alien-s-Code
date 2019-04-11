def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-9))

def nop():
    pass

age=19
if age>=18:
    pass

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-8))

import cmath

def move(x,y,step,angle=0):
    nx=x+step*cmath.cos(angle)
    ny=y-step*cmath.sin(angle)
    return nx,ny
r=move(100,100,60,cmath.pi/6)
print(r)

def quadratic(a,b,c):
    if a!=0:
      x1=((-b)+cmath.sqrt(b*b-4*a*c))/(2*a)
      x2=((-b)-cmath.sqrt(b*b-4*a*c))/(2*a)
      return x1,x2
print(quadratic(1,4,3))



