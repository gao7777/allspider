# -*- coding: utf-8 -*-
import json
from scrapy.selector import Selector
import pymysql
import scrapy
import pandas as pd



num = 0


class XimaSpider(scrapy.Spider):
    name = 'miguyinyue'
    allowed_domains = ['migu.cn']
    start_urls = ["http://music.migu.cn/v3"]
    custom_settings = {
        "DOWNLOAD_DELAY" :1.5,
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "music.migu.cn",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES": {
            'myspider.pipelines.MyspiderPipeline': 500,
            'myspider.pipelines.MiguMusicPipeline': 508,
        }
    }


    def parse(self,response):
        with open("/home/gaozhiwei/Desktop/judge_title_in.txt") as f:
            data_list = f.readlines()
        for i in data_list:
            i = json.loads(i)
            target_title=i['target_title']
            meta= dict()
            if target_title!='default':
                meta['origin']=target_title
                # base_url = "http://music.migu.cn/v3/search?keyword=%s"
                base_url = "http://www.migu.cn/search.html?content=%s&type=music&pn=1&_ch="
                yield scrapy.Request(base_url%(target_title),callback=self.parseone,meta=meta)
        # base_url = "http://music.migu.cn/v3/search?keyword=%s"
        # meta=dict()
        # meta['origin']="不能说的秘密"
        # yield scrapy.Request(base_url%('不能说秘密'),callback=self.parseone,meta=meta)

    def parseone(self,response):
        meta=response.meta
        response = Selector(response)
        try:

            first_title=response.xpath("string(//div[@class='list']/ul/li[1]/a/div[@class='info']/h3[@class='search-title']/span[@class='search-title-text'])").get()
            meta['search_title']=first_title
            print(meta['origin'],first_title,'ffffffffffffffffffffff')
            yield meta
        except Exception as e:
            meta['search_title']='no message'
            yield meta
























