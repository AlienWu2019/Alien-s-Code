#ftp演示，手先要在本机或者远程服务器开启ftp功能
import sys,os,ftplib,socket
print("===============FTP客户端===============")

HOST = '172.28.89.9'  #FTP主机
user = 'username'
password = 'pwd'
buffer_size = 8192

#连接登录
def connect():
    try :
        ftp = ftplib.FTP(HOST)
        ftp.login()#登录，参数user，password，acct均是可选参数
        return ftp
    except (socket.error,socket.gaierror):
        print("FTP登录失败，请检测主机号，用户名，密码是否正确")
        sys.exit(0)
    print('已连接到： "%s"' % HOST)

#中断并退出
def disconnect(ftp):
    ftp.quit()  #FTP.close():单方面的关闭连接，FTP.quit()：发送QUIT命令给服务器并关闭


#上传文件
def upload(ftp,filepath):
    f = open(filepath,"rb")
    file_name = os.path.split(filepath)[-1]
    try:
        ftp.storbinary('STOR "%s"' % file_name)
    except ftplib.error_perm:
        return True

#下载文件
def download(ftp,filename):
    f = open(filename,"wb").write
    try:
        ftp.retrbinary("RETR %s" %filename,f,buffer_size)
        print('成功下载文件： "%s"' % filename)
    except ftplib.error_perm:
        return False
    return  True

#获取目录下文件或文件夹详细信息
def listinfo(ftp):
    ftp.dir()


#查找是否存在指定文件
def find(ftp,filename):
    ftp_f_list = ftp.nlst() #获取目录下文件，文件夹列表
    if filename in ftp_f_list:
        return True
    else:
        return False

def main():
    ftp = connect()  #连接登录ftp
    dirpath = 'lp'   #目录，不能使用lp/lp1这种多级创建，而且要保证你的ftp
    try : ftp.mkd(dirpath)  #新建远程目录
    except ftplib.error_perm:
        print("目录已经存在或无法创建")
    try:ftp.cwd(dirpath) #重定向到指定路径
    except ftplib.error_perm:
        print('不可进入目录 ： "%s"' % dirpath)
    print(ftp.pwd())   #返回当前所在位置
    try: ftp.mkd("李伟研pytho应用之FTP篇") #在当前路径下创建dir1文件夹
    except ftplib.error_perm:
        print("目录已经存在或无法创建")
    upload(ftp,"D:/test/李伟研pytho应用之FTP篇.txt")  #上传本地文件
    filename="李伟研pytho应用之FTP篇1.txt"
    ftp.rename("李伟研pytho应用之FTP篇.txt",filename) #文件改名
    if os.path.exists(filename): #判断本地文件是否存在
        os.unlink(filename) #如果存在就删除
    download(ftp,filename)  #下载ftp文件
    listinfo(ftp)   #打印目录下每个文件或文件夹的详细信息
    files = ftp.nlst()  #获取路径下文件或文件列表
    print(files)

    ftp.delete(filename)  #删除远程文件
    ftp.rmd("李伟研pytho应用之FTP篇")     #删除远程目录
    ftp.quit() #退出

if __name__ == '__main__':
    main()
