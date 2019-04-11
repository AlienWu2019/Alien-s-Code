L=[x*x for x in range(10)]
print(L)
g=(x*x for x in range(10))
print(g)
for n in g:
    print(n)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
fib(6)

def fib1(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
g=fib1(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

def triangles(x):
    a,n=[1],0
    while n<x:
        yield a
        a=[1]+[a[i]+a[i+1]for i in range(len(a)-1)]+[1]
        n=n+1
g=triangles(6)
while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print('到此为止')
        break

