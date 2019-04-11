N=int(input())
sum=1
if(0<=N<=12):
    for i in range(1,N+1):
        sum=sum*i
    print(sum)
