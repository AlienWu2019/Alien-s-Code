x=int(input())
while(x!=1):
    if(x%2==0):
        a=x
        x=x/2
        print('{0}/2={1}'.format(int(a),int(x)))
    else:
        b=x
        x=x*3+1
        print('{0}*3+1={1}'.format(int(b),int(x)))
