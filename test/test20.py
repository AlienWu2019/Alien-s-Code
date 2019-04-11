##python批量更改后缀名

import os
import sys  #引入python模块
path0=r"D:\C语言作业"
path1=r"D:\C语言作业"+'\\'

sys.path.append(path1)
#print(sys.path)

#列出当前目录下所有的文件
files = os.listdir(path0)
#files=os.listdir('.')
print('files',files)
for filename in files:
    portion = os.path.splitext(filename)#os.path.splitext()将文件名和扩展名分开
    #如果后缀是.dat
    if portion[1] == ".txt":
        #重新组合文件名和后缀名
        newname = portion[0]+".cpp"
        filenamedir = path1+filename
        newnamedir = path1+newname
        #os.rename(filename,newname)
        os.rename(filenamedir,newnamedir)#更改文件的名字

