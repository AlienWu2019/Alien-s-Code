import re

pattern = "yue" #普通字符作为原子
string = "http://yum.iqianyue.com"
result1 = re.search(pattern,string)
print(result1)