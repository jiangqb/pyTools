#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from selenium.webdriver.common.keys import Keys
from lxml import etree
import requests
import shutil
import random

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
#替换下边的url，就可以爬你的了
# driver.get('http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=12&spn=0&di=151763776671&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=4271053251%2C2424464488&os=2375022793%2C1835605452&simid=4247939438%2C550168575&adpicid=0&lpn=0&ln=1985&fr=&fmq=1500459419262_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic55.nipic.com%2Ffile%2F20141208%2F19462408_171130083000_2.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bgtrtv_z%26e3Bv54AzdH3Fzi7wgptAzdH3F8c8n9d9_d_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0')
driver.get('http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%88%B4%E7%9C%BC%E9%95%9C%E7%9A%84%E4%BA%BA&step_word=&hs=2&pn=7&spn=0&di=127068576470&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=1738263952%2C1803984339&os=1845275726%2C1715753128&simid=76993243%2C830335916&adpicid=0&lpn=0&ln=1966&fr=&fmq=1500466827517_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fp1.img.cctvpic.com%2Fphotoworkspace%2Fcontentimg%2F2015%2F02%2F06%2F2015020608443512772.png&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bx4pe_z%26e3BvgAzdH3Fda8cAzdH3FadAzdH3FamAzdH3FARTI89dn8bndc9anl99c_z%26e3Bfip4s&gsm=0&rpstart=0&rpnum=0')
time.sleep(1)

#设置爬取的图片张数，这里设置的10
for i in range(50000):
    elem = driver.find_element_by_xpath('//span[@class="img-next"]').click()
    content = etree.HTML(driver.page_source)
    imgSrc = content.xpath('//img[@id="currentImg"]/@src')

    r = requests.get(imgSrc[0], stream=True, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
    if r.status_code == 200:
        picName = './picData/'+str(random.random())+'.jpg'
        with open(picName, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)




