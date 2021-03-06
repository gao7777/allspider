# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy.selector import Selector
from myspider.items import XimaItem,MyspiderItem,ZhidaoItem,XiaopingItem,DoubanItem,Kuwoall


class KuwoSpider(scrapy.Spider):
    name = 'kuwoall'
    allowed_domains = ['kuwo.cn']
    # start_urls = ['http://m.ximalaya.com']
    # start_urls = ['http://www.9ixiaopin.com/']
    start_urls = ['http://yinyue.kuwo.cn/yy/cate_27.htm']
    # start_urls = ['https://movie.douban.com/subject/3927789/']
    # start_urls = re_url()
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
        "Host": "yinyue.kuwo.cn",
        "Pragma": "no-cache",
        # "If-None-Match":"805a101163ded41:0",
        "Referer": "http://yinyue.kuwo.cn/yy/cate_28.htm",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
        # "X-Requested-With":"XMLHttpRequest"
    }


    def parse(self,response):
        response= Selector(response)
        category_one_list = response.xpath("//ul[@class='clearfix']/li/a")
        for i in category_one_list:
            data_dict = dict()
            houzhui = i.xpath("./@href").get()
            url = "http://yinyue.kuwo.cn"+i.xpath("./@href").get()
            category_one = i.xpath("./text()").get()
            data_dict['url_1'] = url
            data_dict['category_one'] = category_one
            # print(data_dict)
            Header= {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
                # "Host": "yinyue.kuwo.cn",
                "Pragma": "no-cache",
                # "If-None-Match":"805a101163ded41:0",
                "Referer": "http://yinyue.kuwo.cn/yy/cate_28.htm",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
            Header["Referer"]=url
            # print(url)
            yield scrapy.Request(url,callback=self.parse_one,meta=data_dict,headers=Header)
    def parse_one(self,response):
        print('paseone')
        dict_one =response.meta
        response= Selector(response)
        category_two_list = response.xpath("//ul[contains(@class,'singer_list')]/li")
        Header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
            # "Host": "yinyue.kuwo.cn",
            "Pragma": "no-cache",
            # "If-None-Match":"805a101163ded41:0",
            "Referer": "http://yinyue.kuwo.cn/yy/cate_28.htm",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

        for i in category_two_list:
            dict_two = {}
            for key,value in dict_one.items():
                dict_two[key] = value
            category_two = i.xpath("./a[@class='m_name']/text()").get()
            url_2 = i.xpath("./a[@class='m_name']/@href").get()
            url_2 = "http://yinyue.kuwo.cn"+url_2
            dict_two['url_2'] = url_2
            dict_two['category_two']= category_two
            # print(dict_two)
            Header["Referer"]=url_2
            yield scrapy.Request(url_2,callback=self.parse_two,meta=dict_two,headers=Header)

    def parse_two(self,response):
        dict_two = response.meta
        print("parse_two")
        html_text = response.text
        data = re.search('var jsonm = {"stat":200,"musiclist":(.+}])?', html_text)
        dict_data = data.group(1)
        # print(dict_data,'dict_data')
        dict_data = json.loads(dict_data)
        # print(type(dict_data))
        for i in dict_data:
            dict_there = dict()
            item = Kuwoall()
            for key,values in dict_two.items():
                dict_there[key] = values
            song_title = i['name']
            album_name = i["album"]
            singer_name = i["artist"]
            url_3 = "http://www.kuwo.cn/yinyue/{}/".format(i['musicrid'])
            dict_there['song_title']= song_title
            dict_there['album_name']= album_name
            dict_there['singer_name']= singer_name
            dict_there['url_3']= url_3
            item["song_title"]=dict_there["song_title"]
            item["album_name"]=dict_there["album_name"]
            item["category_two"]=dict_there["category_two"]
            item["category_one"]=dict_there["category_one"]
            item["url_1"]=dict_there["url_1"]
            item["url_2"]=dict_there["url_2"]
            item["url_3"]=dict_there["url_3"]
            item["singer_name"]=dict_there["singer_name"]
            yield item
            # print(dict_there)
            # yield scrapy.Request(url_3,callback=self.parse_there,meta=dict_there)
        # dict_two = response.meta
        # response= Selector(response)
        # songs_list = response.xpath("//ul[@id='musicList']/li[contains(@class,'clearfix')]")
        # for i in songs_list:
        #     dict_there = dict()
        #     for key,values in dict_two.items:
        #         dict_there[key] = values
        #     song_title = i.xpath("./p[@class='m_name']/a/text()").get()
        #     album_name = i.xpath("./p[@class='a_name']/a/text()").get()
        #     singer_name = i.xpath("./p[@class='s_name']/a/text()").get()
        #     url_3 = i.xpath("./p[@class='m_name']/a/@href").get()
        #     dict_there['song_title']= song_title
        #     dict_there['album_name']= album_name
        #     dict_there['singer_name']= singer_name
        #     dict_there['url_3']= url_3
        #     yield scrapy.Request(url_3,callback=self.parse_there,meta=dict_there)
    def parse_there(self,response):
        print('parse_there')
        dict_there = response.meta
        response= Selector(response)
        item = Kuwoall()
        for key,values in dict_there.items:
            item[key] = values
        geci = response.xpath("//div[@id='llrcId']/p/text()")
        item['geci']=geci
        print('dd',item,'item')
        # yield item



    # start_urls = re_url()
    # def start_requests(self):
    #     start_urls = re_url()
    #     for i in start_urls:
    #         url = i
    #         print(url)
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








