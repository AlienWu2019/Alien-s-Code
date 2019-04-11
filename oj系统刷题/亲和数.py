M=int(input())
b=[]
sum1=0
sum2=0
for i in range(M):
    a=input()
    x=a.split()
    for rw1 in range(1,int(x[0])):
        if(int(x[0])%rw1==0):
            sum1=sum1+rw1
    for rw2 in range(1,int(x[1])):
        if(int(x[1])%rw2==0):
            sum2=sum2+rw2
    if(sum1==int(x[1]) and sum2==int(x[0])):
        print('YES')
    else:
        print('NO')






