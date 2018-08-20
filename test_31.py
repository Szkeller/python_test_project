import requests

r=requests.get("https://www.zhihu.com/")
r.encoding = r.apparent_encoding
print(r.text)