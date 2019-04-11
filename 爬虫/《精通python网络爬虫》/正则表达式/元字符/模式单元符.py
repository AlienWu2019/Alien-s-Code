import re

pattern1 = "(cd){1,}"
pattern2 = "cd{1,}"
string = "abcdcdcdcdfphp345pythony_py"
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)