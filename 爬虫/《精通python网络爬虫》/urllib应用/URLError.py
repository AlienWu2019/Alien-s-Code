import urllib.request
import urllib.error

try:
    urllib.request.urlopen("https://blog.baiduss.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)

"""
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)
"""