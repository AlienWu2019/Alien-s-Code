import sys
N=int(input())
a=[[]]*N
sum=0
for i in range(N):
    b=input()
    x=b.split()
    if(len(x)==N):
        a[i]=b.split()
    else:
        print("不符合要求，请重新输入！")
        sys.exit()
if(N%2==0):
    for j in range(N):
        sum=sum+int(a[j][j])+int(a[j][N-j-1])
    print(sum)
else:
    for j in range(N):
        if(j==(N-1)/2):
            sum=sum+int(a[j][j])
        else:
            sum=sum+int(a[j][j])+int(a[j][N-j-1])
    print(sum)
