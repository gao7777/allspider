# -*- coding: utf-8 -*-
import json
import math
import re

from scrapy.selector import Selector
import pymysql
import scrapy
import pandas as pd



num = 0


class XimaSpider(scrapy.Spider):
    name = 'taihe'
    allowed_domains = ['taihe.com']
    start_urls = ['http://www.taihe.com/tag']
    custom_settings = {
        "DOWNLOAD_DELAY" :0.2,
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        # "Host": "music.migu.cn",
        'Referer':'http://music.taihe.com/tag',
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES": {
            'myspider.pipelines.MyspiderPipeline': 500,
            'myspider.pipelines.TaihePipeline': 508,
        }
    }

    def parse(self,response):
        request_url = response.url
        response = Selector(response)
        tag_list = response.xpath("//span[contains(@class,'tag-list')]")
        base_url = "http://www.taihe.com"
        for i in tag_list:
            tag_name = i.xpath("./a/text()").get()
            tag_url = i.xpath("./a/@href").get()
            cur_url = base_url+tag_url
            cur_meta = dict()
            cur_meta['tag'] = tag_name
            yield scrapy.Request(cur_url,callback=self.parseone,meta=cur_meta)

    def parseone(self,response):
        request_url = response.url
        meta= response.meta
        response = Selector(response)
        tag_name = meta['tag']
        total_num = response.xpath("//span[@class='nums']/text()").get()
        base_url = "http://www.taihe.com/tag/{}?start={}&size=20&third_type=0"
        if total_num is not None:
            int_total_num = int(total_num)
            total_page = math.ceil(int_total_num/20)
            for page in range(total_page):
                cur_page_url = base_url.format(tag_name,page*20)
                yield scrapy.Request(cur_page_url,callback=self.parsetwo,meta=meta)

    def parsetwo(self,response):
        request_url = response.url
        meta = response.meta
        response = Selector(response)
        li_list = response.xpath("//ul/li[contains(@class,'bb-dotimg')]")
        cur_dict = dict()
        cur_dict[meta['tag']] = list()
        # print("parsetwo start")
        for cur_li in li_list:
            title = cur_li.xpath("./div/span[@class='song-title']/a/text()").get()
            # print(title)
            singer = cur_li.xpath("./div/span[@class='singer']/span/a/text()").get()
            album = cur_li.xpath("./div/span[@class='album-title']/a/@title").get()
            cur_li_dict = dict()
            cur_li_dict['title'] = title
            cur_li_dict['singer'] = singer
            cur_li_dict['album'] = album
            cur_dict[meta['tag']].append(cur_li_dict)
            # print(cur_dict)
        yield cur_dict

























