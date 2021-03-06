"""
    文件操作的权限：
        文件操作权限主要有：读数据（read），写数据（write），追加数据（append）

        r:读取文件：如果文件存在，则可以读取文件，如果文件不存在，则直接宝座
              如果权限只有r 的时候，是只能读，不能写。
                  r：文件的操作权限是只读
                  r+：文件的操作权限是可读可写
                  rb：按照只能的模式打开二进制文件，例如音频，视频，图片等
                  rb+：安扎可读可写的方式打开二进制数据

        w：写入文件：如果文件存在，可以写入数据（但是会将之前文件的内容清空），如果文件不存在
            如果权限只有w的时候，是只能写，不能读。
                w:文件的操作权限是只写
                w+：文件的操作权限是可读可写
                wb：按照只写的模式打开二进制文件，例如音频，视频，图片等
                wb+：按照可读可写的方式打开二进制数据

        a:追加数据: 如果文件存在，则在文件末尾追加数据，如果文件不存在，则创建文件，然后写入数据
             a:文件的操作权限是只能追加
             a+：可读可写的追加文本数据
             ab：按照只写的模式追加二进制文件，例如音频，视频，图片等
             ab+:按照可读可写的方式追加二进制数据
"""

#1.写入文件
f = open("D:/test/test.jpg","wb")
f.write()
f.close()

#2.读取文件内容
f = open("D:/test/test.jpg","rb")
text = f.read()
print(text)
f.close()

#3.追加数据
f = open("D:/test/萤草.jpg","ab")
f.write()
f.close()

#4.读取追加过后的数据
f = open("D:/test/test.jpg","rb")
text = f.read()
print(text)
f.close()
