import re
line="bobby123"
regex_str="^b.*"
if re.match(regex_str,line):
    print("yes")

#以字符b开头.任意字符匹配0或者多个
