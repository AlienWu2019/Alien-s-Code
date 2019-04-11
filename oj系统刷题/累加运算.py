def add():
    i = int(input("请输入i的值: "))
    a = list(input("请输入i个数据:"))
    x = int(input("请输入x的值："))
    sum = 0
    print(a)
    for j in range(0,i):
        b = int (a[j])
        sum = sum+b*x**(j)

    print("累加求和的结果是:",sum)


add()

"""
i = int(input("请输入i的值: "))
a=[]
a.append('k')
for q in range(0,i):
    a.append(input("请依次输入i个数据: "))
a.append('l')
x = int(input("请输入x的值："))
sum = 0
print(a)
for j in range(1,i+1):
    b = int (a[j])
    sum = sum+b*x**(j-1)

print("累加求和的结果是:",sum)
"""
