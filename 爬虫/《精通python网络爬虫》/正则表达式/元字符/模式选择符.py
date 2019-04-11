import re

pattern1 = "python|php"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1,string)
print(result1)