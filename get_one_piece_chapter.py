# -*- coding: utf-8 -*-
# Description: 获取海贼王漫画章节

import requests
import re
import sys
import time
from bs4 import BeautifulSoup
from random import choice
from urllib.parse import urlparse
import get_latest_comic
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 随机获取UserAgent
def getRandomUserAgent():
    agents = [
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
             'Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36',
             'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/79.0.3945.73 Mobile/15E148 Safari/605.1',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/71.0',
             'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
             'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
             ]

    return choice(agents)   

def getChapterLists(url,headers,chapter_cout,downloadflag):
    response = requests.get(url, headers = headers, verify =False)
    response.encoding = 'gbk'
    html = response.text
    bsObj = BeautifulSoup(html, 'lxml')
    ObjChapters = bsObj.findAll('div', class_="classopen")
    listObjChapter = ObjChapters[0].findAll(name = 'a')

    index = 1
    for ObjChapter in listObjChapter:
        chaptername = re.sub(r'\[|\]| ', '', ObjChapter.text)
        chapterhref = ObjChapter.attrs['href']
        uri = urlparse(chapterhref).path
        print(site + uri, chaptername, sep="\t")
        if downloadflag == 1:
            time.sleep(choice(range(500,3500))/1000)
            get_latest_comic.getChapterComic(uri)
        index += 1
        # 定义查看最近多少话漫画
        if index > chapter_cout: break

if __name__ == '__main__':
    '''
    site = 'https://wap.kukudm.com'
    imgsite = 'https://tu.kukudm.com/'
    headers ={ 'User-Agent': getRandomUserAgent() }
    # url = 'https://127.0.0.1/op.html'
    url = 'https://wap.kukudm.com/comiclist/4/'
    '''

    site = 'http://1pc570gfrd9z.ihhmh.com'
    imgsite = 'http://tu.ihhmh.com/'
    headers ={ 'User-Agent': getRandomUserAgent() }
    url = 'http://1pc570gfrd9z.ihhmh.com/comiclist/4'

    if len(sys.argv) == 1:
        chapter_cout = 1
        downloadflag = 0
    elif len(sys.argv) == 2:
        chapter_cout = int(sys.argv[1])
        downloadflag = 0
    elif len(sys.argv) == 3:
        chapter_cout = int(sys.argv[1])
        downloadflag = 1

    getChapterLists(url,headers,chapter_cout,downloadflag)


