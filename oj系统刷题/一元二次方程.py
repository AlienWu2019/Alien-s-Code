from mpmath import math2
y=input()
list1=y.split()
a=float(list1[0])
b=float(list1[1])
c=float(list1[2])
if b*b-4*a*c<0:
    pass
elif b*b-4*a*c==0:
    x1=x2=-b/(2*a)
    print('%.2f'%x1,'%.2f'%x2)
else:
    x1=(-b+math2.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math2.sqrt(b*b-4*a*c))/(2*a)
    print('%.2f'%x1,'%.2f'%x2)

