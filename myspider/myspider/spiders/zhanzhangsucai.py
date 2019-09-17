# -*- coding: utf-8 -*-
import json
from scrapy.selector import Selector
import pymysql
import scrapy
import pandas as pd



num = 0


class XimaSpider(scrapy.Spider):
    name = 'zhanzhangsucai'
    allowed_domains = ['chinaz.com']
    start_urls = ["http://sc.chinaz.com/yinxiao/index_{}.html".format(i) for i in range(2,570)]+['http://sc.chinaz.com/yinxiao/index.html']
    custom_settings = {
        "DOWNLOAD_DELAY" :0.1,
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "sc.chinaz.com",
        "Pragma": "no-cache",
        "Referer": "http://sc.chinaz.com/yinxiao/index.html",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES": {
            'myspider.pipelines.MyspiderPipeline': 500,
            'myspider.pipelines.ZhanzhangPipeline': 508,
        }
    }

    def parse(self,response):
        response= Selector(response)
        div_list = response.xpath("//div[@class='text_left']/div[@class='music_block']")
        for i in div_list:
            title = i.xpath("./p[@class='z']/a/text()").get()
            mp3_url= i.xpath("./p[@class='n1']/@thumb").get()
            cur_dict = dict()
            cur_dict['title']= title
            cur_dict['mp3_url'] = mp3_url
            yield cur_dict































