x=int(input())
if x>=1:
    def f(x):
        sum=0
        if x==1:
            sum=10
        elif x>1:
            sum=f(x-1)+2
        return sum
    print(f(x))
