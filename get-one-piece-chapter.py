# -*- coding: utf-8 -*-
# Description: 获取海贼王漫画章节

import urllib2
import ssl
from bs4 import BeautifulSoup

# 表示忽略未经核实的SSL证书认证
context = ssl._create_unverified_context()

url = 'https://one-piece.cn/comic/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request, context = context).read()
bsObj = BeautifulSoup(response, "html.parser")

urls_list = bsObj.findAll("a", {"target": {"_blank"}})
len = len(urls_list)
for i in range(len):
    try:
        comic_name = urls_list[i].get_text()
        comic_url = 'https://one-piece.cn' + urls_list[i].attrs['href']
        print comic_name, comic_url
    except:
        print '#### Name Error ####', comic_url
#    print urls_list[i].attrs['src']

'''
环境：
	python2.7
	bs4
'''

