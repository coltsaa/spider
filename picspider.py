# -*- coding:utf-8 -*-
#url 统一资源定位符
#http请求 get post
#ajax 不刷新网页的条件下 发送http请求

import requests
import re
import json
import time
import os

def strip(path):
    path = re.sub(r'[? \\*|"<>:/]', '', str(path))
    return path

class spider:#爬虫类
    def __init__(self):
        self.session = requests.Session()

    def run(self,start_url):
        img_ids = self.get_img_item_ids(start_url)
        #print(img_ids)
        for img_id in img_ids:
            img_item_info = self.get_img_item_info(img_id)
            self.save_img(img_item_info)

    def get_img_item_ids(self,start_url):
        response = self.download(start_url)
        if response:
            html = response.text
            ids = re.findall(r'http://tu.duowan.com/gallery/(\d+).html',html)
            return set(ids)

    def get_img_item_info(self,img_id):
        img_item_url="http://tu.duowan.com/index.php?r=show/getByGallery/&gid=%s&_=%s" %(img_id,int(time.time()*1000))
        response = self.download(img_item_url)
        if response:
            #data = json.loads(response.text)
            #print(data)
            return json.loads(response.text)

    def save_img(self,img_item_info):
        dir_name = strip(img_item_info['gallery_title'])####
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for img_info in strip(img_item_info['picInfo']):
            img_name = img_info['title']####
            img_url = img_info['url']
            pix = (img_url.split('/')[-1]).split('.')[-1]
            img_path = os.path.join(dir_name,"%s%s" % (img_name,pix))
            if not os.path.exists(img_path):
                response = self.download(img_url)
                print(img_url)
                if response:
                    img_data = response.content
                    with open(img_path,'wb') as f:
                        f.write(img_data)


    def download(self,url):
        try:
            return self.session.get(url)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    spider = spider()
    start_url = 'http://tu.duowan.com/m/meinv'
    spider.run(start_url)