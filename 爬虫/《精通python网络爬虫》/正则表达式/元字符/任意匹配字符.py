import re

pattern = ".python..."
string = "abdcfphp345pythony_py"
result1 = re.search(pattern,string)
print(result1)