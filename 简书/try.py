def foo(x):
    sum = 0
    a=1
    b=2
    c=4
    while x>3:
        sum=a+b+c
        a=b
        b=c
        c=sum
        x-=1
    return sum
print(foo(1000000)%65536)

