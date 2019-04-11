import sys
x=input()
w=x.split()
a=int(w[0])
b=int(w[1])
o=[]
if(5<=a<b<=100000000):
    for i in range(a,b+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            o.append(str(i))
    for i in o:
        i_fan=i[::-1]
        if(i_fan==i):
            print(int(i))
else:
    sys.exit()


