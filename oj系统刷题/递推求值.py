n=int(input())
def F(n,a):

    if a==1:
        return F(n-1,2)+2*F(n-3,1)+5
    elif a==2:
        return F(n-1,1)+3*F(n-3,1)+2*F(n-3,2)+3


F(n,1)
