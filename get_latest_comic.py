# -*- coding: utf-8 -*-
# Description: 下载最新的海贼王漫画

import requests
import re
import time
import os
from random import choice

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

def getTitle(url, headers):
    response = requests.get(url, headers = headers)
    response.encoding = 'gbk'
    html = response.text
    reTitleObj = re.search(r"class='txtA'>(.*?) \| ", html)
    if reTitleObj:
        chaptername = re.sub(r'\[|\]| ', '', reTitleObj.groups()[0])
        return chaptername

def downloadFile(url, localfile):
    try:
        r = requests.get(url, headers = headers, timeout=(3,7)) 
        with open(localfile, "wb") as f:
            time.sleep(choice(range(500,3500))/1000)
            f.write(r.content)
    except Exception as err:
        print(err)

def getImages(url, headers, imgindex):
    response = requests.get(url, headers = headers)
    #response.encoding = 'utf-8'
    response.encoding = 'gbk'
    html = response.text
    reImgObj = re.search(r"(newkuku.*?.(jpg|png))", html)
    if reImgObj: imageuri = reImgObj.groups()[0]
    imageurl = imgsite + imageuri
    savefilename = str(imgindex) + '.jpg'

    if not os.path.isfile(savefilename):
        downloadlog = '[%s] saving %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), imageurl)
        print(downloadlog)
        downloadFile(imageurl, savefilename)

    reNextpageObj = re.search(r">上一页.*?<a href='(.*?)'><span ", html)
    if reNextpageObj:
        nexpageuri = reNextpageObj.groups()[0]
        if nexpageuri != '/exit/exit.htm':
            nexpageurl = site + nexpageuri
            imgindex += 1
            getImages(nexpageurl, headers, imgindex)

def getChapterComic(uri):
    url = site + uri
    imgindex = 1
    chaptername = getTitle(url, headers)
    if not os.path.isdir(chaptername): os.mkdir(chaptername)
    os.chdir(cwd + os.sep + chaptername)
    getImages(url, headers, imgindex)
    os.chdir(cwd)

site = 'https://wap.kukudm.com'
imgsite = 'https://tu.kukudm.com/'
headers ={ 'User-Agent': getRandomUserAgent() }
cwd = os.path.split(os.path.realpath(__file__))[0]

if __name__ == '__main__':
    #uri = '/comiclist/4/66397/1.htm'
    #uri = '/comiclist/4/88248/1.htm'
    uri = ''
    getChapterComic(uri)


'''
环境：
'''
