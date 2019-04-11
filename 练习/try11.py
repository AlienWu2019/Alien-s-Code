import random
a=[]
b=[]
for i in range(1,random.randint(2,10)):
    a.append(random.randint(1,100))
a.sort()
b.append(a[0])
b.append(a[-1])
print(a)
print(b)
