x=input()
a=x.split()
if(int(a[0])<=1000 and int(a[1])<1000):
    q=int(a[0])
    w=int(a[1])
    if q>w:
        greater = q
    else:
        greater = w
    while True:
        if(greater%q==0)and(greater%w==0):
            lcm=greater
            break
        greater+=1

    print(lcm)
