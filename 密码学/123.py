import random

a = ["1","2","3"]
print("".join(random.sample(a,1)))

l=list(range(2,10))
for n,i in enumerate(l):
    for j in l[n+1:]:
        if j%i==0:
            l.remove(j)


r = "".join(random.sample(l,1))
print(isinstance(r,str))

