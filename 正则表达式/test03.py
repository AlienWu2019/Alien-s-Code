import re
string = '加           油'
regex_str='(加\s*油)'
f=re.match(regex_str,string)
if f:
    print(f.group(1))

string1 = 'xx graduates from 清华大学'
regex_str1='.*?([\u4E00-\u9FA5]+大学)'
f1=re.match(regex_str1,string1)
if f1:
    print(f1.group(1))
