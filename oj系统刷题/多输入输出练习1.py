for i in range(3):
    a=input()
    x=a.split()
    b=[]
    for j in range(len(x)-1):
        x[j]=int(x[j])
        b.append(x[j])
    b.sort()
    print(b[len(b)-1])