"""
   文件的编码问题：
      问题引出：在项目下创建一个"笔记.txt"文件，在文件中存入中文
      使用open最简单的方法打开文件，读取文件内容
      此时，会报错如下：
         Traceback (most recent call last):
           File "D:/test/文件操作"........
"""

#1.打开文件
f = open("D:/test/笔记.txt","r")

#2.读取文件内容
print(f.encoding)  #cp936,该行可以输出当前文件内容的编码格式
text = f.read();
print(text)

#3.关闭文件
f.close()
