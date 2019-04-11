n=int(input())
n_str=str(n)
sum=0
b=[]
if(n<10000):
    for i in range(n):
        for j in range(3):
            a=i+j
            a=str(a)
            for k in range(len(a)):
                b.append(a[k])

        print(b)

