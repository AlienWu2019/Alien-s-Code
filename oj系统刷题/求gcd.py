# encoding:utf-8
a=int(input("请输入一个数："))
b=int(input("请输入另外一个数："))
while(a%b!=0):
    MOD=a%b
    a=b
    b=MOD

print("gcd(a,b)=",b)



