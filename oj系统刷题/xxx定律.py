while(True):
    n=int(input())
    if(n==0):
        break
    count=0
    while(n!=1):
        if(n%2==0):
            n=n/2
            count=count+1
        else:
            n=(3*n+1)/2
            count=count+1
    print(count)

