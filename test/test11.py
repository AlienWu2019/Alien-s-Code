d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for ch in 'ABC':
    print(ch)
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
for i,value in enumerate(['A','B','C']):
    print(i,value)
for x,y in [(1,1),(2,4),(3,9)]:
    print((x,y))
def findMinAndMax(L):
    if L==[]:
        print('测试失败!')
    else:
        max=0
    for x in L:
        if x>max:
            max=x
        min=max
    for y in L:
        if y<min:
            min=y
    return print(min,max)
findMinAndMax([9,2,3,4,7,6])
