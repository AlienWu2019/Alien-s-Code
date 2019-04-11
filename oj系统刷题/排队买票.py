#递归算法，最后一个人如是2元，则他前面一定有K-1个2元和N个一元，若最后一个人是1元，则他前面一定有N-1个一元和K个2元
x=str(input())
a=x.split()
N=int(a[1])
K=int(a[2])
count1=1
count2=1
def f(a,b):
    sum=0
    if(b==0):
        sum=1
    elif(a<b):
        sum=0
    else:
        sum=f(a-1,b)+f(a,b-1)
    return sum
for i in range(1,N+1):
    count1=count1*i
for j in range(1,K+1):
    count2=count2*j
print(f(N,K)*count1*count2)

