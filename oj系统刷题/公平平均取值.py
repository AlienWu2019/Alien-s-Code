
for i in range(2):
    x=input()
    a=x.split()
    n=int(a[0])
    a.remove(a[0])
    for j in range(len(a)):
        a[j]=int(a[j])
    a.sort()
    a.remove(a[0])
    a.remove(a[n-1-1])
    sum=0
    for i in a:
        sum=sum+i
    print('%.2f'%(sum/(n-2)))
