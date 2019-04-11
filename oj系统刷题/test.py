x=input()
a=[]
for i in range(len(x)):
    a.append(int(x[i]))
if(a[0]*100+a[1]*10+a[2]==a[0]**3+a[1]**3+a[2]**3):
    print(1)
else:
    print(0)


