"""
    文件的路径：
        绝对路径：从磁盘根目录开始，到指定文件的完整路径
        相对路径，相对于某个目录位置的路径，..表示上一级目录，.表示当前目录
"""
#文件操作

import os
f = open("D:/test/笔记.txt","r")

#1.获取当前的文件所在文件夹的绝对路径
filePath = os.getcwd()
print(filePath)


#2.判断相对于当前文件所在的文件夹中是否存在某个指定的文件，返回的是布尔值
isHave = os.path.exists("test.txt")
print(isHave)
#如果文件名是带路径的，可能会遇到转义字符，如：\r \n等，在字符串最前面加上r即可表示对后面带\的不做转意
print(os.path.exists(r"D:/test/test.txt"))

#----------------------------------------------------------------------
#目录操作

#1.os.listdir(path):获取指定目录的所有文件，返回一个列表，空参方法表示返回当前目录下的所有文件
fileList = os.listdir()
print(fileList)

if "test9.py" in os.listdir():
    f = open("test9.py","r",encoding="UTF-8")
    print(f.read())
    f.close()

#------------------------------------------------------------
os.mkdir(r"D:/2333")
#---------------------------------------------------------
os.makedirs(r"D:/test/aa")
