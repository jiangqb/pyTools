# -*- coding:utf-8 -*-

import scrapy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading
import time
import os

class BaiduSpider():
    '''
    爬取百度图片中的图片

    '''
    def __init__(self, search_keys):
        self.search_keys = search_keys
        self.url = 'http://image.baidu.com'
        #self.page_total = 6
        #self.url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%D6%A4%BC%FE%D5%D5&hs=0&fr=ala&ori_query=%E8%AF%81%E4%BB%B6%E7%85%A7&ala=0&alatpl=sp&pos=0"

        # set profile
        fp = webdriver.FirefoxProfile()
        fp.set_preference('browser.download.folderList', 2)
        fp.set_preference('browser.download.manager.showWhenStarting', False)
        downDir = 'D:/frontal/' + self.search_keys
        fp.set_preference('browser.download.dir', downDir)
        fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/jpeg')
        #fp.set_preference('browser.helperApps.neverAsk.saveToDisk', ['image/jpeg','image/jpg', 'image/png', 'image/gif'])
        self.fp = fp
        if not os.path.exists(downDir):
            os.makedirs(downDir)

    def Search(self):
        # 打开浏览器 ， 并在百度图片搜索中输入关键字
        driver = webdriver.Firefox(firefox_profile = self.fp)
        driver.maximize_window()
        driver.get(self.url)
        # print driver.title
        inputElement = driver.find_element_by_name('word')
        inputElement.send_keys(self.search_keys)
        inputElement.submit()
        time.sleep(20)
        return driver

    def download(self):
        driver = self.Search()
        #获取 n pagedown 个页面的内容
        for i in range(100):
            action = ActionChains(driver).send_keys(Keys.PAGE_DOWN)
            action.perform()

        page_total = 100
        page_i = 1
        total_elements = 0
        remained_pics = [] # 标记已经处理过的图片元素

        while page_i < page_total:

            elements_all = driver.find_elements_by_xpath('//ul/li/div/a/img')  # 一定是单引号
            elements = elements_all

            # print elements
            i = 0
            while i < (len(elements)):
                print i
                try:
                    element = elements[i]
                    # 去除重复图片
                    if element in remained_pics:
                        i += 1
                        continue
                    print "pic element : ", element


                    # 激活 hover
                    action = ActionChains(driver).move_to_element(element)
                    action.perform()

                    # 查找 a.down
                    hover = driver.find_element_by_class_name("down")
                    print "hover element: ", hover

                    start = time.clock()
                    action = ActionChains(driver).move_to_element(hover)
                    action.click()      # 点击下载
                    action.perform()
                    i = i + 1
                    end = time.clock()
                    downloadtime = end - start
                    if downloadtime > 60:
                        continue
                except:
                    threading._sleep(1)
            page_i += 1
            remained_pics.extend(elements)
            action = ActionChains(driver).send_keys(Keys.DOWN)
            action.perform()


if __name__ == "__main__":
    spider = BaiduSpider("zhengjianzhao")
    spider.download()