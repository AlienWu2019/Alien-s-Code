N=int(input("输入一个整数N（N<40）:"))
a=0
b=1
if(N>=40):
    print("超出范围，请重新输入！")
else:
    for i in range(1,N):
        a,b=b,a+b
        print(b)
