x=input()
a=x.split()
str1=input()
list1=str1.split()
str2=input()
list2=str2.split()
temp=0
p=[]
if(1<=int(a[0])<=1000 and 1<=int(a[1])<=1000 and len(list1)==int(a[0]) and len(list2)==int(a[1])):
    for i in range(len(list1)):
        for j in range(len(list2)):
            y=abs(int(list1[i])-int(list2[j]))
            p.append(y)
    p.sort()
    print(p[0])
