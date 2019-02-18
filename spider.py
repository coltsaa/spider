import requests
import re

def getMovieList():
    res = requests.get('http://www.dytt8.net/html/gndy/dyzz/index.html')#post get
    res.encoding = 'gb2312'
    result = res.text
    reg = r'<a href="(.*?)" class="ulink"'
    reg = re.compile(reg)
    return re.findall(reg,result)

def getMovieContent(url,title):
    res = requests.get('http://www.dytt8.net'.format(url))
    res.encoding = 'gb2312'
    result = res.text
    print(result)

for url,title in getMovieList():
    print(url,title)

