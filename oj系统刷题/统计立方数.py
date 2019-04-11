import numpy
x=input()
a=x.split()
sum=0
for i in a:
    i=int(i)
    if i==0:
        break
    elif i<2**32 and int(numpy.cbrt(i))**3==i:
        sum=sum+1
print(sum)
