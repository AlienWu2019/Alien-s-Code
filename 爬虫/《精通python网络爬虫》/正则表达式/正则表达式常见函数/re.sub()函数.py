import re

string = "hellomypythonhispythonourpythonend"
pattern = ".python."
result1 = re.sub(pattern,"php",string) #全部替换 "hellomphpiphpuphpnd"
result2 = re.sub(pattern,"php",string,2) #最多替换2次 "hellomphpiphpurpythonend"
print(result1)
print(result2)