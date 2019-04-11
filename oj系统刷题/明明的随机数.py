N=int(input())
if N<=100:
    x=input()
    a=x.split()
    if len(a)==N:
        b=list(set(a))
        for i in range(len(b)):
            b[i]=int(b[i])
        b.sort()
        for j in range(len(b)):
            b[j]=str(b[j])
        print(len(b))
        print(" ".join(b))





