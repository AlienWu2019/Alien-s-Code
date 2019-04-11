"""
  写文件操作：
         1.打开文件
         2.写入内容
         3.关闭文件

    打开文件的方法：open(fileName,operation)
                        fileName:要操作的文件名(字符串)
                        operation： 要执行的操作，w代表写，r代表读(字符串)
                该方法返回一个文件对象
"""

#1.打开alien的python应用之文件篇.txt
f = open("D:/test/alein的python应用之文件篇.txt","w")

#2.文件对象吊用write（）方法向文件中写入字符串
f.write(input("清输入要写进文件的内容:"))

#3.关闭文件，否则程序不节俗内容无法写入到文件中
f.close()   #close()方法将缓冲区的数据写入磁盘，并情况缓冲区
