
import re
from urllib import request

def getBookUrl():
    urls = []
    url = 'https://book.douban.com/top250?start=0'
    html = request.urlopen(url).read().decode('utf-8')
    # print(html)
    bookUrl = re.findall('<a href="https://book.douban.com/subject/(.*?)/"',html)
    for a in bookUrl:
        bookUrls = ("https://book.douban.com/subject/%s/" %a)
        urls.append(bookUrls)
        # print(bookUrls)
    # print(urls)
    return urls

def getBookInfo(bookUrl):
	try:
	    list =[]
	    print(bookUrl)
	    html = request.urlopen(bookUrl).read().decode('utf-8')
	    # print(html)
	    reg = r'<span property="v:itemreviewed">(.*?)</span>'
	    reg1='<span class="pl">.*?</span>(.*?)<br/>'
	    result = re.findall(reg, html)
	    result1 = re.findall(reg1, html)
	    list.append(result[0])
	    for i in range(len(result1)):
	        list.append(result1[i])
	    print(list)
	except:
		print('something wrong')

if __name__ == '__main__':
    bookUrls = getBookUrl()
    for bookUrl in bookUrls:
        getBookInfo(bookUrl)

