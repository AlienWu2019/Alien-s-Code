from pytube import YouTube
import urllib.request

"""
设置代理
"""
def download(url):
    proxy_addr = "http://127.0.0.1:1080"
    proxy = urllib.request.ProxyHandler({'https':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

    path = r'D:\电影' #视频保存路径
    yt = YouTube(url)
    yt.streams.first().download(path)


url=input()
download(url)
print("下载完成！")