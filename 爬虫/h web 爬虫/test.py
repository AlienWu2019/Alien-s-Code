import urllib.request

url = "https://www.youtube.com/results?search_query="
key = "华农兄弟"
key_code = urllib.request.quote(key)
url_new = url+key_code
req = urllib.request.Request(url_new)
print(req)