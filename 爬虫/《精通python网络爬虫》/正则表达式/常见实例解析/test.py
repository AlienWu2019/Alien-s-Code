import re

string = "mailto:c-e+o@iqi-anyue.com.cn"
pattern = "([.+-:]\w+)+"
result = re.search(pattern,string)
print(result)