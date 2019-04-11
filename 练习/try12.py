def fib():
    x=int(input("请问要生成多少个斐波那契数列:"))
    a=0
    b=1
    f=[]
    f.append(b)

    for i in range(1,x):
       a,b=b,a+b
       f.append(b)
    print(f)

fib()

#递归
def fib1(n):
    if n<1:
        return -1
    elif n==1 or n==2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

for i in range(6):
    print(fib1(i+1))

