from operator import mod
import numpy as np

#创建空白矩阵A
A = [[],[],[]]
str1 = input("请输入矩阵第一行数据:")
#把矩阵第一行数据存进空白矩阵中
for a in str1:
    A[0].append(a)
str2 = input("请输入矩阵第二行数据:")
#把矩阵第二行数据存进空白矩阵中
for b in str2:
    A[1].append(b)
str3 = input("请输入矩阵第三行数据:")
#把矩阵第三行数据存进空白矩阵中
for c in str3:
    A[2].append(c)
#此时矩阵A已经完成
print(A)

#创建空白矩阵B
B = [[],[],[]]
B[0].append(input("请输入第一个数据:"))
B[1].append(input("请输入第二个数据:"))
B[2].append(input("请输入第三个数据:"))
#此时矩阵B已完成
print(B)

P = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str4 = input("请输入一串明文(9个数):")
o = str4.replace(' ','')
#print(len(o))
x = list(o)
#print(x)
Y=[]
for g in x:
    r = P.index(g)
    Y.append(r)
#print(Y)
first = np.array(A)
second = np.array([Y[0],Y[1],Y[2]])
C1 = first * second
print(C1)

