"""
   文件的读写函数：
"""



#1.写的操作     write（str）：接收字符串参数 ，丙炔指针的位置开始，向后覆盖内容
f = open("D:/test/笔记.txt","r+")

f.write("\nnihaoshijie\n")   #\n代表换行

f.close()
