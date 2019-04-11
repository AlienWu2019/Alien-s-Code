import os
dynamic = input()

try:
    result = eval(dynamic.lstrip().rstrip("="))
    print(str(result))
except:
    print('计算表达式输入有误！')


