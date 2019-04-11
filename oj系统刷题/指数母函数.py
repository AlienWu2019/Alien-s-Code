#数学公式：EG（an，x）=求和(an*x^n/n!)
def zhishu():
    n = int(input("请输入n的数值:"))
    an = list(input("请输入n+1个数据:"))
    x = int (input("请输入x的数值:"))

    sum=0
    m=1
    for b in range(0,n+1):
        #求n的阶乘
        if(b==0):
            m=1
        else:
            m=m*b
        sum = sum+(int(an[b])*(x**b))/m

    print(sum)

zhishu()
