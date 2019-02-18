# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'EiJi'
import urllib2,urllib
import re


def getNovelListUrl():
    html = urllib.urlopen('http://www.quanshuwang.com/list/1_1.html').read().decode('gbk').encode('utf-8')
    reg = r'<a target"_blank" title=".*?" href="(.*?)" class="clearfix stitle">(.*?)</a>作者:<a href=".*?">(.*?)</a>'
    urlList = re.findall(reg,html)
    return urlList

def getChapterList(url):
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<a href="(.*?)"  class=""l mr11">'
    chapterUrl = re.findall(reg,html)[0]
    html = urllib.urlopen(chapterUrl).read().decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)"  title=".*?">(.*?)</a></li>'
    chapterList = re.findall(reg,html)
    return chapterList,chapterUrl

def getChapterContent(url):
    html= urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
    reg = re.compile(reg,re.S)
    content = re.findall(reg,html)[0]
    return content

for novel in getNovelListUrl():
    chapterList,url = getChapterList(novel[0])
    for chapter in getChapterList:
        url = '%s%s' %(url,chapter[0])
        print url
        content = getChapterContent(url)
        print content
        break
    break
