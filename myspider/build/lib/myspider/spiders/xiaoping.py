# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from myspider.items import XimaItem,MyspiderItem,ZhidaoItem,XiaopingItem


def re_url():
    return [
        'https://zhidao.baidu.com/search?word=%C7%A9%CE%DE%B9%CC%B6%A8%C6%DA%CF%DE%C0%CD%B6%AF%BA%CF%CD%AC%D3%D0%CA%B2%C3%B4%BA%C3%B4%A6%0A&ie=gbk&site=-1&sites=0&date=0&pn=10',
        'https://zhidao.baidu.com/search?word=%C7%A9%B6%A9%CE%DE%B9%CC%B6%A8%C6%DA%CF%DE%C0%CD%B6%AF%BA%CF%CD%AC%D3%D0%CA%B2%C3%B4%BA%C3%B4%A6%B0%A1%3F%0A&ie=gbk&site=-1&sites=0&date=0&pn=10']
class XimaSpider(scrapy.Spider):
    name = 'xima'
    allowed_domains = ['xiaopin5.com']
    # start_urls = ['http://m.ximalaya.com']
    # start_urls = ['http://www.9ixiaopin.com/']
    start_urls = ['https://www.xiaopin5.com/daohang/']

    # start_urls = re_url()
    def re_url(self):
        return ['https://zhidao.baidu.com/search?word=%CC%EC%CE%AA%CA%B2%C3%B4%CA%C7%C0%B6%C9%AB%B5%C4&ie=gbk&site=-1&sites=0&date=0&pn=10',
                  'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%CA%B1%BC%E4%B5%C4%B5%BD%C0%B4']
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
    # def parse(self, response):
    #     response = Selector(response)
    #     url_list = response.xpath("//a[@class='ti']")
    #     item= ZhidaoItem()
    #     item['question']= []
    #     # for i in url_list:
    #         # question = i.xpath("./em/text")
    #
    #         # question2 = i.xpath("./@data-log")
    #         # question2 = i.xpath("string(.)")
    #         # item['question'].append(question2.get())
    #         # print(question2a.get())
    #     # print(item)
    #     # print(response.request.url)
    #     for i in url_list:
    #         url = i.xpath("./@href").get()
    #
    #         print(i)
    #         yield scrapy.Request(url=url,callback=self.parse_title,meta=item)
    #
    #     next_url = response.xpath("//a[@class='pager-next']/@href")
    #     next_url = "https://zhidao.baidu.com" + next_url.get()
    #     # print(next_url)
    #     yield scrapy.Request(url=next_url, callback=self.parse_detail, meta=item)



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


    # def parse_detail(self, response):
    #     item = response.meta
    #     response = Selector(response)
    #     url_list = response.xpath("//a[@class='ti']")
    #     # item= ZhidaoItem()
    #     # item['question']= []
    #     # for i in url_list:
    #         # question = i.xpath("./em/text")
    #
    #         # question2 = i.xpath("./@data-log")
    #         # question2 = i.xpath("string(.)")
    #         # item['question'].append(question2.get())
    #         # print(question2.get())
    #     for i in url_list:
    #         url = i.xpath("./@href").get()
    #
    #         # print(i.get())
    #         yield scrapy.Request(url=url, callback=self.parse_title, meta=item)
    #     try:
    #         next_url = response.xpath("//a[@class='pager-next']/@href")
    #         next_url = "https://zhidao.baidu.com" + next_url.get()
    #         print(next_url)
    #         yield scrapy.Request(url=next_url, callback=self.parse_detail, meta=item)
    #         yield item
    #     except Exception as e :
    #         print(e)
    #         yield item
        # yield item
    # def parse_title(self,response):
    #     item = response.meta
    #     response= Selector(response)
    #     title = response.xpath("//span[@class='ask-title']/text()")
    #     for i in title:
    #         print(i.get())
    #         item['question'].append(i.get())
    #     # yield item

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
    def parse(self, response):
        response = Selector(response)
        url_list = response.xpath("//ul[@class='xin_list']/li/a")
        # for b in url_list:
        #     print(b.get())

        for i in url_list:
            item = XiaopingItem()
            item['name']=i.xpath('./text()').get()
            item['url']=i.xpath('./@href').get()
            # print(item)
            real_url = 'https://www.xiaopin5.com'+item['url']
            print('sfsdfsfsdfsfsfdssfsdfsdfsfsdffdsaaadsgasg')
            print('fdfdff',real_url,'fasfrealssue')
            yield scrapy.Request(url=real_url,callback=self.parse_detail,meta=item)


    def parse_detail(self,response):
        print('ffsfsfsfsfsfsfsfsfsffsfsfs')
        item = response.meta
        current_url= response.request.url
        response= Selector(response)
        node_list = response.xpath("//ul[@class='article-list float']/li/p[@class='title']/a/text()")
        print('nnnnnnnnnnnnnnnnnn',node_list)
        # print('node_list',node_list)
        item['zuopin'] = []
        for node in node_list:
            print('sdfsfsfsfsfsfsfsfdsfsdfadsfadsfadsfadsf')
            print(node.get(),'nodedfafdadf')
            item['zuopin'].append(node.get())

        try:
            next_url = response.xpath("//div[@class='page-nav']/li/a/@href")
            url_set = set()
            for i in next_url.getall():
                url_set.add(i)
            print(url_set)
            for i in url_set:
                b_url = current_url+i
                yield scrapy.Request(url=b_url,meta=item,callback=self.parse_title)
        except Exception as e:
            print(e)
            yield item
    def parse_title(self,response):
        item = response.meta
        response= Selector(response)
        node_list = response.xpath("//ul[@class='article-list float']/li//p/a/@text()")
        # print('node_list',node_list)
        for node in node_list:
            item['zuopin'].append(node.get())

        yield item

