"""
    文件的信息处理
"""

f = open("D:/test/笔记.txt","r")


#查看文件编码

print(f.encoding)

#查看文件名
print(f.name)

#查看文件是否关闭，如果文件已经关闭，返回True，否则返回False
print(f.closed)

#查看文件的读写权限
print(f.mode)
