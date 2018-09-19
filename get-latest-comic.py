# -*- coding: utf-8 -*-
# Description: 下载最新的海贼王漫画

import os
import sys
import urllib2
import ssl
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


# 表示忽略未经核实的SSL证书认证
context = ssl._create_unverified_context()

# 获取最新漫画名称以及链接
url = 'https://one-piece.cn/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request, context = context).read()
bsObj = BeautifulSoup(response, "html.parser")
comic_urls = bsObj.findAll("a", {"target": {"_blank"}})
comic_url = url + comic_urls[25].attrs['href']
comic_name = comic_urls[25].attrs['title']

# 获取漫画图片链接
request = urllib2.Request(comic_url, headers = headers)
response = urllib2.urlopen(request, context = context).read()
bsObj = BeautifulSoup(response, "html.parser")
images_list = bsObj.findAll("img", {"alt": {comic_name}})
comic = comic_name.replace(' ','')

# 下载漫画图片
index = 1
if not os.path.isdir(comic): os.makedirs(comic)
for image in images_list:
    image_url = image.attrs['src']
    request = urllib2.Request(image_url, headers = headers)
    response = urllib2.urlopen(request, context = context).read()
    print('正在下载 ' + comic + str(index) + '.jpg')
    with open(comic + '/' + comic + str(index) + '.jpg', 'wb') as f:
        f.write(response)
    f.close()
    index += 1

'''
环境：
	python2.7
	bs4
'''
