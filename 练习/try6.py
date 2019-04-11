a = str(input("请输入一段字符串："))
b=a[::-1]
print(b)
if b==a:
    print("这是回文")
else:
    print("这不是回文")
