import re
string='dcpen123'
regex_str='.*3$'
math_obj=re.match(regex_str,string)
if math_obj:
    print('yes')

string1='pccccccccpppppeng123'
regex_str1='(p.*p).*'
math_obj1=re.match(regex_str1,string1)
if math_obj1:
    print(math_obj1.group(1))

regex_str2='.*?(p.*?p).*'
math_obj2=re.match(regex_str2,string1)
if math_obj2:
    print(math_obj2.group(1))
