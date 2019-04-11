import random
a=[]
for i in range(0,10):
    a.append(random.randint(1,15))
#去重
a=list(set(a))
a.sort()
print(a)
