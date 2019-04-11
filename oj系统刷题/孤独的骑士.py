N=int(input())
L=['','a','b','c','d','e','f','g','h']
for i in range(N):
    a=input()
    sum=0
    if(L.index(a[0])+1<=8 and int(a[1])+2<=8):
        sum=sum+1
    if(L.index(a[0])-1>=1 and int(a[1])-2>=1):
        sum=sum+1
    if(L.index(a[0])+1<=8 and int(a[1])-2>=1):
        sum=sum+1
    if(L.index(a[0])-1>=1 and int(a[1])+2<=8):
        sum=sum+1

    if(L.index(a[0])+2<=8 and int(a[1])+1<=8):
        sum=sum+1
    if(L.index(a[0])-2>=1 and int(a[1])-1>=1):
        sum=sum+1
    if(L.index(a[0])+2<=8 and int(a[1])-1>=1):
        sum=sum+1
    if(L.index(a[0])-2>=1 and int(a[1])+1<=8):
        sum=sum+1
    print(sum)


