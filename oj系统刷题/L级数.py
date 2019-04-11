# -*- coding:utf-8 -*-
def Ljisu():
    n = int(input("请输入n的值:"))
    x = int(input("请输入x的值:"))
    if(x==1):
        print("运算失败，无结果!")
    else:
        an=[]
        an.append('p')
        sum=0
        for k in range (1,n+1):
            an.append(input("请依次输入n个元素:"))
            sum=sum+int(an[k])*x**k/(1-x**k)
        print(sum)

Ljisu()
