import re

string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python."
result = re.match(pattern,string)
result2 = re.match(pattern,string).span()
print(result)
print(result2)