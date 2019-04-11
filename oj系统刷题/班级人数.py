for i in range(2):
    x=int(input())
    a=''
    if(x<0):
        x=abs(x)
        while True:
            x,b=divmod(x,2)
            a=a+str(b)
            if(x==0):
                break
        print('-'+a[::-1])
    else:
        while True:
            x,b=divmod(x,2)
            a=a+str(b)
            if(x==0):
                break
        print(a[::-1])



