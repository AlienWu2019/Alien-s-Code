n=int(input())
a=input()
b=a.split()
count=0
temp=0
for i in range(len(b)):
    for j in range(i,len(b)):
        b[j]=int(b[j])
        b[i]=int(b[i])
        if(b[j]<b[i]):
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
            count=count+1
print(b)
print(count)


