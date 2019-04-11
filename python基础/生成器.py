#在 Python 中，这种一边循环一边计算的机制，称为生成器：generator
#在 Python 中，使用了 yield 的函数被称为生成器（generator）
gen = (x*x for x in range(10))
print(gen)

print('-----------------------')

gen1 = (x*x for x in range(10))

for num in gen:
    print(num)

print('-----------------------')

def my_function():
    for i in range(10):
        print(i)

my_function()

print('-----------------------')
def my_function1():
    for i in range(10):
        yield i

print(my_function1())

print('-----------------------')

def fibon(n):
    a = b =1
    for i in range(n):
        yield a
        a,b = b,a+b

for x in fibon(10):
    print(x,end = ' ')

print('-----------------------')
def odd():
    print( 'step 1')
    yield (1)
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)

o = odd()
print(next(o))
print(next(o))
print(next(o))

print('-----------------------')
#打印杨辉三角
def triangles(n):
    L=[1]
    while True:
        yield L
        L.append(0)   #L=[1,2,1,0]
        L = [L[i-1]+L[i] for i in range (len(L))]
n = 0
for t in triangles(10):
    print(t)
    n = n+1
    if n == 10 :
        break
