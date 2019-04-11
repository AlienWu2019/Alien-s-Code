a=int(input())
sum=1
for i in range(2,a+1):
    sum=sum-1/(i*i)
print('%.6f'%sum)