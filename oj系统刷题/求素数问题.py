N=int(input())
a=[]
for i in range(1,N+1):
    if(i==1):
        continue
    elif(i==2):
        a.append(str(2))
    else:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            a.append(str(i))
b=' '.join(a)
print(b)
