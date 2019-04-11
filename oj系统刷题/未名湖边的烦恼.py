x=input()
a=x.split()
m=int(a[0])
n=int(a[1])
def list1(a,b):
    sum=0
    if(b==0):
        sum=1
    elif(a<b):
        sum=0
    else:
        sum=list1(a-1,b)+list1(a,b-1)
    return sum
print(list1(m,n))
