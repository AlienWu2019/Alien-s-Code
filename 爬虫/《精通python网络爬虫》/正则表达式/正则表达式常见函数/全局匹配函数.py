import re

string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.") #预编译
result = pattern.findall(string) #找出符合模式的所有结果
print(result)