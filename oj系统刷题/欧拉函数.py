#欧拉函数的定义：小于或等于n的正整数中与n互质的个数
def Oula():
    n=int(input("请输入一个数："))
    count=0
    for b in range(1,n+1):
        if(n%b==0):
            continue
        else:
            count=count+1
    print("求得欧拉结果φ(n)=",count)

Oula()
