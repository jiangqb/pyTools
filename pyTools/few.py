# -*- coding: utf-8 -*-

import os
import urllib
import urllib2
import re

url = u"http://cameradata.ioz.ac.cn/ano_regions/list_spec.shtml"
outpath = "C:/Users/oops/Desktop/Pic/"


def getHtml(url):
    request = urllib2.Request(url)
    webfile = urllib2.urlopen(request)
    outhtml = webfile.read()
    return outhtml


def getImageList(html):
    restr = ur'('
    restr += ur'http:\/\/[^\s,"]*\.jpg'
    restr += ur'|http:\/\/[^\s,"]*\.jpeg'
    restr += ur'|http:\/\/[^\s,"]*\.png'
    restr += ur'|http:\/\/[^\s,"]*\.gif'
    restr += ur'|http:\/\/[^\s,"]*\.bmp'
    restr += ur'|https:\/\/[^\s,"]*\.jpg'
    restr += ur'|https:\/\/[^\s,"]*\.jpeg'
    restr += ur'|https:\/\/[^\s,"]*\.png'
    restr += ur'|https:\/\/[^\s,"]*\.gif'
    restr += ur'|https:\/\/[^\s,"]*\.bmp'
    restr += ur')'
    htmlurl = re.compile(restr)
    imgList = re.findall(htmlurl, html)
    print imgList
    return imgList


def download(imgList, page):
    x = 1
    for imgurl in imgList:
        filepathname = str(outpath + 'Pic_%d' % x + str(
            os.path.splitext(urllib2.unquote(imgurl).decode('utf8').split('/')[-1])[1])).lower()
        print 'Download file :' + imgurl + ' >> ' + filepathname
        urllib.urlretrieve(imgurl, filepathname)
        x += 1


def downImageNum(pagenum):
    page = 1
    pageNumber = pagenum
    while (page <= pageNumber):
        html = getHtml(url)  # 获得url指向的html内容
        imageList = getImageList(html)  # 获得所有图片的地址，返回列表
        download(imageList, page)  # 下载所有的图片
        page = page + 1

if __name__ == '__main__':
    downImageNum(2)