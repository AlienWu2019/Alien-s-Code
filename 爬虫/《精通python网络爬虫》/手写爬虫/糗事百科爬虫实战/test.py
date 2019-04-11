import urllib.request
import os
path = 'C:/Users/58294/Documents/Python File/picture'
os.makedirs(path)
imagename = "C:/Users/58294/Documents/Python File/picture/"+'1'+".jpg"
imageurl = "http://img5.dwstatic.com/df/1811/405080793013/405081046793.jpg"
urllib.request.urlretrieve(imageurl,filename=imagename)