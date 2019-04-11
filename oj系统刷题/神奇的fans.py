n=int(input())
for i in range(n):
    L=[]
    sum=0
    x=input()
    x_list=x.split()
    m=int(x_list[0])
    x_list.remove(x_list[0])
    for i in range(len(x_list)):
        x_list[i]=int(x_list[i])
    x_list.sort()
    for j in range(len(x_list)-1):
        num=x_list[j+1]-x_list[j]
        L.append(num)
    for k in L:
        sum+=k
    if sum/(m-1)==L[0]:
        print('yes')
    else:
        print('no')
