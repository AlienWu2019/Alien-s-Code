print(1+2+3)
names=['Michael','Bob','Tracy']
for name in names:
    print(name)
sum1=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum1=sum1+x
print(sum1)
sum2=0
n=99
while n>0:
    sum2=sum2+n
    n=n-2
print(sum2)
sum3=0
n=0
while n<=100:
    sum3=sum3+n
    n=n+2
print(sum3)
L=['Bart','Lisa','Adam']
for x in L:
    print('Hello,',x,'!')
n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print('END')
n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)
