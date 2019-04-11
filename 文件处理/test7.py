#2.读的操作：
#           read(num):从文件指针位置开始，读取指定的字节数的内容，如果空参，则默认读取全部内容，并返回字符串
#           readline(num):从文件指针位置开始，向后读取一行内容，并返回字符串，readline()读玩当前一行，默认将指针指向下一行开始
#                         带参数是读取一行中指定的字节数的内容，如果字节数超出内容数，则忽略参数
#           readlines():读取文件内容，返回一个列表，列表的每个元素都是文件每行的内容
f = open("D:/test/笔记.txt","r+")

print(f.read(10))
print(f.readline(1000))
print(f.readlines())

f.close()
