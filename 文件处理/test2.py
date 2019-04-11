"""
   读文件的操作:
               1.打开文件
               2.读取内容
                     read（num）：读取指定字节数的文件内容，空参则读取所有文件内容
                     readline:读取一行数据
               3.关闭文件
"""

#1.打开文件，设置操作为r
f = open("D:/test/test.txt","r")

#2.读取文件内容，read（num），该方法如果传参，则表示读取多少个字符，如果不传参数，，默认读取所有数据
text1 = f.readline()
text2 = f.read()
print(text1)
print(text2)

#3.关闭文件
f.close()
