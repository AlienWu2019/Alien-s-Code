import re
print(re.match('www','www.runoob.com').span()) #在起始位置匹配
print(re.match('com','www.runoob.com'))        #不在起始位置匹配

print(re.search('www','www.runoob.com').span())  #在起始位置匹配
print(re.search('com','www.runoob.com').span())  #不在起始位置匹配
