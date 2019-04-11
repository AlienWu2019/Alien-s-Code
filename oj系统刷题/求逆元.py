def niyuan():
    def gcd(a,b):
        if b!=0:
            return gcd(b,a%b)
        else:
            return a
    a=int(input("请输入一个数a："))
    b=int(input("请输入另外一个数b："))
    gcd(a,b)
    if gcd(a,b)==1:
    #有扩展欧几里得算法得a*x+b*y=gcd(a,b)---->a*x%b==1
        for x in range(1,100):
            if a*x%b==1:
                break
    else:
        print("由于gcd（a,b）!=1,所以不存在逆元！")
    print("a的逆元是：",x)

#调用求逆元函数
niyuan()

