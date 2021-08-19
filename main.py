import urllib.request
re=urllib.request.urlopen('http://www.baidu.com')
print(re.read().decode('utf-8'))