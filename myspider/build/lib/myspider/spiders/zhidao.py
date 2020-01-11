# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from myspider.items import ZhidaoItem
def re_url():
    url_list = []
    print('uuudsl')
    pass
    # with open('./url_list.txt','r') as f:
    #     while True:
    #         line = f.readline()
    #         if line:
    #             url_list.append(line.strip())
    #         else:
    #             return url_list

# # 'https://zhidao.baidu.com/search?word=%CA%D6%BB%FA%C9%CF%B5%C4wpsoffice%BF%C9%D2%D4%D7%F6%CA%B2%C3%B4&ie=gbk&site=-1&sites=0&date=0&pn=10',
# 'https://zhidao.baidu.com/search?word=%B3%C9%C4%EA%C8%CB%D1%A7%CE%E8%B5%B8%CA%B1%C8%E7%BA%CE%D5%FD%C8%B7%C1%B7%CF%B0%CF%C2%D1%FC%D1%FC%B2%BF%B1%A3%BD%A1%D6%AA%CA%B6%D4%E7&ie=gbk&site=-1&sites=0&date=0&pn=10']
class ZhidaoSpider(scrapy.Spider):
    name = 'zhidao'
    allowed_domains = ['baidu.com']
    start_urls = re_url()


    # start_urls = re_url()
    # def start_requests(self):
    #     for i in self.start_urls:
    #         url = i
    #         yield scrapy.Request(url,callback=self.parse, dont_filter=True)
    # def parse(self, response):
    #     response = Selector(response)
    #     url_list = response.xpath("//div/ul/li[@class='item j-candies']/a/@href")
    #     # print('url_list',url_list.getall())
    #     # print('url_list',url_list.get())
    #
    #     real_url_list = []
    #     for i in url_list:
    #         # a=i.extract()
    #         # print('a',a)
    #         i= 'http://m.ximalaya.com'+i.get()
    #         # print(type(a))
    #         # b =i.get()
    #         # print('b',b)
    #         # print(type(b))
    #         # c = i.getall()
    #         # print('',c)
    #         real_url_list.append(i)
    #     url =real_url_list[0]
    #     item = MyspiderItem()
    #     item['url_1']=url
    #     print('url',url)
    #     print(item)
    #     # print(DEFAULT_REQUEST_HEADERS)
    #     # response= requests.get(url=url,headers=DEFAULT_REQUEST_HEADERS)
    #     # print('respnse',response.content)
    #     yield scrapy.Request(url=url,callback=self.parse_detail,headers=DEFAULT_REQUEST_HEADERS,dont_filter=True,meta=item)
    def parse(self, response):
        pass
        response = Selector(response)
        url_list = response.xpath("//a[@class='ti']")
        item= ZhidaoItem()
        item['question']= []
        # for i in url_list:
            # question = i.xpath("./em/text")

            # question2 = i.xpath("./@data-log")
            # question2 = i.xpath("string(.)")
            # item['question'].append(question2.get())
            # print(question2a.get())
        # print(item)
        # print(response.request.url)
        for i in url_list:
            url = i.xpath("./@href").get()
            print(i)
            yield scrapy.Request(url=url,callback=self.parse_title,meta=item)
        try:
            next_url = response.xpath("//a[@class='pager-next']/@href")
            next_url = "https://zhidao.baidu.com" + next_url.get()
            # print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_detail, meta=item)
        except Exception as e:
            print(e)




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





