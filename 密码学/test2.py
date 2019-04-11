A= [[],[],[]]
str1='123'
for k in str1:
    A[0].append(k)

str2='456'
for j in str2:
    A[1].append(j)

str3='789'
for l in str3:
    A[2].append(l)
print(A)

str4 = input("请输入一串明文：")
o=str4.replace(' ','')
print(o)
