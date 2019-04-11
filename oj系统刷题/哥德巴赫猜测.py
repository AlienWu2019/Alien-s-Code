x=int(input())
a=[]
count=0
if(6<x<32767):
    p=[True]*x
    p[0]=p[1]=False
    for i in range(2,x):
        if (p[i]):
            for j in range(2,int(x/i)):
                p[i*j]=False
    for i in range(0,x):
        if (p[i]):
            a.append(i)
    for i in a:
        if (i<x and x-i<=i and p[x-i] ):
            count=count+1
    print(count)

