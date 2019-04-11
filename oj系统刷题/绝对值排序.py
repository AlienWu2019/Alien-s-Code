while(True):
    a=[]
    n=input()
    x=n.split(' ')
    temp=0
    for i in range(1,int(x[0])):
        for j in range(i,int(x[0])+1):
            if(abs(int(x[i]))<abs(int(x[j]))):
                temp=x[i]
                x[i]=x[j]
                x[j]=temp
    x.remove(x[0])
    b=' '.join(x)
    print(b)








