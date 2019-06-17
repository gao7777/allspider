# -*- coding: utf-8 -*-
import re
import time

import scrapy
from scrapy.selector import Selector
# from myspider.settings import DEFAULT_REQUEST_HEADERS
from myspider.items import XimaItem,MyspiderItem,ZhidaoItem,XiaopingItem,Kuwo
from fake_useragent import UserAgent
import requests
import scrapy_redis
# def re_url():
#     url_list = []
#     print('uuudsl')
#     with open('./url_list.txt','r') as f:
#         while True:
#             line = f.readline()
#             if line:
#                 url_list.append(line.strip())
#             else:
#                 return url_list

# # 'https://zhidao.baidu.com/search?word=%CA%D6%BB%FA%C9%CF%B5%C4wpsoffice%BF%C9%D2%D4%D7%F6%CA%B2%C3%B4&ie=gbk&site=-1&sites=0&date=0&pn=10',
# 'https://zhidao.baidu.com/search?word=%B3%C9%C4%EA%C8%CB%D1%A7%CE%E8%B5%B8%CA%B1%C8%E7%BA%CE%D5%FD%C8%B7%C1%B7%CF%B0%CF%C2%D1%FC%D1%FC%B2%BF%B1%A3%BD%A1%D6%AA%CA%B6%D4%E7&ie=gbk&site=-1&sites=0&date=0&pn=10']
class ZhidaoSpider(scrapy.Spider):
    name = 'kuwo'
    allowed_domains = ['kuwo.cn']
    # start_urls = ['http://www.kuwo.cn/bang/index']
    # start_urls = ['http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E7%83%AD%E6%AD%8C%E6%A6%9C&bangId=16',
    #               'http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E6%96%B0%E6%AD%8C%E6%A6%9C&bangId=17']
    start_urls = ['http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E7%83%AD%E6%AD%8C%E6%A6%9C&bangId=16',
                  'http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E6%96%B0%E6%AD%8C%E6%A6%9C&bangId=17',
                  'http://www.kuwo.cn/bang/content?name=%E9%85%B7%E6%88%91%E9%A3%99%E5%8D%87%E6%A6%9C&bangId=93']
    custom_settings = {
    "DOWNLOAD_DELAY" : 2,
    'DEFAULT_REQUEST_HEADERS' : {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-HK;q=0.7,zh;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
        "Host": "www.kuwo.cn",
        "Pragma": "no-cache",
        # "If-None-Match":"805a101163ded41:0",
        "Referer": "https://so.gushiwen.org/gushi/songci.aspx",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES":{
        'myspider.pipelines.MyspiderPipeline': 500,
        'myspider.pipelines.KuwoPipeline': 508,
    }
    }

    def parse(self, response):
        # print(response.request.url,'url')
        response = Selector(response)
        # url = response.request.url
        # print(url)
        url_list = response.xpath("//li")

        for i in url_list:
            item = {}
            item['song']= i.xpath("./div[@class='name']/a/text()").get()
            item['singer']= i.xpath("./div[@class='artist']/a/text()").get().strip()
            item['url']= i.xpath("./div[@class='name']/a/@href").get()
            name = item['song']
            flag = re.search('-.+',name)
            if flag:
                name = re.sub('-.+','',name)
            flag = re.search('\(.+\)', name)
            if flag:
                name = re.sub('\(.+\)', '', name)
            flag = re.search('（.+）', name)
            if flag:
                name = re.sub('（.+）', '', name)
            flag = re.search('《.+》', name)
            if flag:
                name = re.sub('《.+》', '', name)
            # try:
            #     a = name.index('-')
            #     name = name[:a]
            # except Exception as e:
            #     pass
            # try:
            #     a = name.index('(')
            #     name = name[:a]
            # except Exception as e:
            #     pass
            item['song']=name.strip()
            # print(item)

            yield item






    # def parse_detail(self,response):
    #     print('start')
    #     item = response.meta
    #     print(item)
    #     response= Selector(response)
    #     node_list = response.xpath("//div[@class='list list2 list2-2']/a[@class='item cl block']")
    #     # print('node_list',node_list)
    #     item['detail'] = []
    #     for node in node_list:
    #         item1 = XimaItem()
    #         item1['url_1']=node.xpath("./@href").get()
    #         item1['name']=node.xpath("./div[@class='info wrapper2']/p/text()").get().strip()
    #         item['detail'].append(item1)
    #     print(item['detail'])
    #     print('whole_list',item)
    #     yield item


    def parse_detail(self, response):
        item = response.meta
        response = Selector(response)
        url_list = response.xpath("//a[@class='ti']")
        # item= ZhidaoItem()
        # item['question']= []
        # for i in url_list:
            # question = i.xpath("./em/text")

            # question2 = i.xpath("./@data-log")
            # question2 = i.xpath("string(.)")
            # item['question'].append(question2.get())
            # print(question2.get())
        for i in url_list:
            url = i.xpath("./@href").get()
            # print(i.get())
            yield scrapy.Request(url=url, callback=self.parse_title, meta=item)
        try:
            next_url = response.xpath("//a[@class='pager-next']/@href")
            next_url = "https://zhidao.baidu.com" + next_url.get()
            print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_detail, meta=item)
            yield item
        except Exception as e :
            print(e)
            yield item
        yield item
    def parse_title(self,response):
        item = response.meta
        response= Selector(response)
        title = response.xpath("//span[@class='ask-title']/text()")
        for i in title:
            print(i.get())
            item['question'].append(i.get())
        yield item

    # def parse(self, response):
    #     response = Selector(response)
    #     url_list = response.xpath("//ul[@class='wt']/li/a")
    #     # for b in url_list:
    #     #     print(b.get())
    #
    #     for i in url_list:
    #
    #         item = XiaopingItem()
    #         item['name']=i.xpath('./text()').get()
    #         item['url']=i.xpath('./@href').get()
    #         # print(item)
    #         real_url = 'http://www.9ixiaopin.com'+item['url']
    #         yield scrapy.Request(url=real_url,callback=self.parse_detail,meta=item)
    #
    #     next_url = response.xpath("//a[@class='pager-next']/@href")
    #     next_url = "https://zhidao.baidu.com" + next_url.get()
    #     # print(next_url)
    #     yield scrapy.Request(url=next_url, callback=self.parse_detail, meta=item)
    # def parse_detail(self,response):
    #     item = response.meta
    #     response= Selector(response)
    #     node_list = response.xpath("//ul/li/p/a/text()")
    #     # print('node_list',node_list)
    #     item['zuopin'] = []
    #     for node in node_list:
    #         item['zuopin'].append(node.get())
    #
    #     yield item





