import re

string = "hellomypythonhispythonourpythonend"
pattern = ".python."
result = re.search(pattern,string)
result1 = re.search(pattern,string).span()
print(result)
print(result1)