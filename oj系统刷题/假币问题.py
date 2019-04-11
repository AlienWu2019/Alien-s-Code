while True:
    sum=0
    n=int(input())
    while n!=2 and n!=3 and n!=1 and n!=0:
        if n%2==0:
            n=int(n/2)
            sum+=1
        else:
            n=int((n-1)/2)
            sum+=1
    if n==2 or n==3 or n==1:
        sum+=1
        print(sum)
    elif n==0:
        break

