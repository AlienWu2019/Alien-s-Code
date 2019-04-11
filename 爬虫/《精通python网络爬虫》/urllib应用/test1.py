import urllib.request

file = urllib.request.urlopen("https://www.baidu.com")
data = file.read()
print(data)