N=int(input())
sum=0
for i in range(7,N+1):
    i=str(i)
    if int(i)%7==0:
        sum+=1
    else:
        for j in range(len(i)):
            if i[j]=='7':
                sum+=1
print(sum)