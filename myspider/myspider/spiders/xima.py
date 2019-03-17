# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from myspider.settings import DEFAULT_REQUEST_HEADERS
from myspider.items import XimaItem,MyspiderItem
import requests
class XimaSpider(scrapy.Spider):
    name = 'xima'
    allowed_domains = ['ximalaya.com']
    start_urls = ['http://m.ximalaya.com']
    # def start_requests(self):
    #     for i in self.start_urls:
    #         url = i
    #         yield scrapy.Request(url,callback=self.parse, dont_filter=True)
    def parse(self, response):
        response = Selector(response)
        url_list = response.xpath("//div/ul/li[@class='item j-candies']/a/@href")
        # print('url_list',url_list.getall())
        # print('url_list',url_list.get())

        real_url_list = []
        for i in url_list:
            # a=i.extract()
            # print('a',a)
            i= 'http://m.ximalaya.com'+i.get()
            # print(type(a))
            # b =i.get()
            # print('b',b)
            # print(type(b))
            # c = i.getall()
            # print('',c)
            real_url_list.append(i)
        url =real_url_list[0]
        item = MyspiderItem()
        item['url_1']=url
        print('url',url)
        print(item)
        # print(DEFAULT_REQUEST_HEADERS)
        # response= requests.get(url=url,headers=DEFAULT_REQUEST_HEADERS)
        # print('respnse',response.content)
        yield scrapy.Request(url=url,callback=self.parse_detail,headers=DEFAULT_REQUEST_HEADERS,dont_filter=True,meta=item)
    def parse_detail(self,response):
        print('start')
        item = response.meta
        print(item)
        response= Selector(response)
        node_list = response.xpath("//div[@class='list list2 list2-2']/a[@class='item cl block']")
        # print('node_list',node_list)
        item['detail'] = []
        for node in node_list:
            item1 = XimaItem()
            item1['url_1']=node.xpath("./@href").get()
            item1['name']=node.xpath("./div[@class='info wrapper2']/p/text()").get().strip()
            item['detail'].append(item1)
        print('whole_list',item)
        yield item


