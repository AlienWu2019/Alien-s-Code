#reduce是累积函数,lambda是匿名函数
from functools import reduce
n=5
result=reduce(lambda x,y:x*y,range(1,n+1))
print(result)

def add(x,y):
    return x+y
result_add=reduce(add,[1,2,3,4,5])
result_add_lambda=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(result_add)
print(result_add_lambda)