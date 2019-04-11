import sys
x=int(input())
if(x<=50000):
    a=[]
    r=[]
    temp=0
    for i in range(x):
        a.append(int(input()))
    for j in range(len(a)):
        b=a.count(a[j])
        if (b>temp):
            temp=b
    for k in range(len(a)):
        if(a.count(a[k])==temp):
            r.append(a[k])
    r=list(set(r))
    for i in r:
        print(i)
    print(temp)
else:
    sys.exit()
