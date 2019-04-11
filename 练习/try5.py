import random
x=int(input("你希望列表A有多少个元素： "))
y=int(input("你希望列表B有多少个元素： "))
a=[]
testA=[]
b=[]
testB=[]
for i in range(1,x+1):
    a.append(random.random())
for j in range(1,y+1):
    b.append(random.random())

for i in a:
    if not i in testA:
        testA.append(i)

for j in b:
    if not j in testB:
        testB.append(j)

print(testA)
print(testB)
