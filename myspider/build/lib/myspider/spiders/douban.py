# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy.selector import Selector
from myspider.items import XimaItem,MyspiderItem,ZhidaoItem,XiaopingItem,DoubanItem
num = 0
def re_url():
    url_list = []
    # str="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start={}"
    str="https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start={}"
    for i in range(30):
        url = str.format(i)
        url_list.append(url)
    return url_list

class XimaSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    # start_urls = ['http://m.ximalaya.com']
    # start_urls = ['http://www.9ixiaopin.com/']
    # start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=0']
    # start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=2000&page_start=0']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=1000&page_start=0']
    # start_urls = re_url()
    custom_settings = {

        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
        "Host": "movie.douban.com",
        "Pragma": "no-cache",
        # "If-None-Match":"805a101163ded41:0",
        "Referer": "https://movie.douban.com/explore",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }
    }




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
    # def parse(self,response):
    #     ur_list = re_url()
    #     for i in ur_list:
    #         print(i)
    #         yield scrapy.Request(i,callback=self.parse_one,dont_filter=True)
    def parse(self, response):

        # response = Selector(response)
        # # a=response.xpath("//div[@id='info']/text()").get()
        # a=response.xpath("string(//div[@id='info'])").get()
        # a=response.xpath("//div[@id='info']/span[2]/span/a")
        # for i in a:
        #     text = i.xpath("./text()")
        #     print(text.get())

        json_data=response.body.decode('utf-8')
        dict_data= json.loads(json_data)
        url_list = dict_data["subjects"]
        j=0
        for i in url_list:
            j+=1
            item = DoubanItem()
            item['move_detail_url']=i["url"]
            item['move_title']=i["title"]
            # print(j)
            # print(item['move_detail_url'])
            yield scrapy.Request(url=item['move_detail_url'],callback=self.parse_detail,meta=item)
    def parse_detail(self,response):
        print('detailkaishi')
        item = response.meta
        response = Selector(response)
        dayan_list=response.xpath("//div[@id='info']/span[1]/span/a")
        item['daoyan'] =[]
        for i in dayan_list:
            text = i.xpath("./text()").get()
            item["daoyan"].append(text)
        item['bianju']=[]
        bianju_list = response.xpath("//div[@id='info']/span[2]/span/a")
        for i in bianju_list:
            text = i.xpath("./text()").get()
            item["bianju"].append(text)
        zhuyan_list = response.xpath("//div[@id='info']/span[@class='actor']/span[@class='attrs']/span/a")
        item['yuyan']=[]
        for i in zhuyan_list:
            text = i.xpath("./text()").get()
            item['yuyan'].append(text)
        item['leixing']=[]
        leixing_list = response.xpath("//div[@id='info']/span[@property='v:genre']")
        for i in leixing_list:
            text = i.xpath("./text()").get()
            item['leixing'].append(text)
        item['yanyuan']=''
        yanyuan=response.xpath("string(//div[@id='info']/span[3]/span[@class='attrs'])").get()
        # print(yanyuan)
        # print(type(yanyuan))
        # str=re.match('(.+)更多',yanyuan)
        item['yanyuan']=yanyuan
        item['yuyan']=''
        item['diqu']=''
        all_data = response.xpath("string(//div[@id='info'])").get()
        # print(all_data,'dsfadsfaf')
        all_data = re.sub('\s', ',', all_data)
        all_data = re.sub(',+', ',', all_data)

        index_yuyan = all_data.index('语言')
        str_yuyan = all_data[index_yuyan:]
        str_yuyan = re.search(':,([\u4e00-\u9fa5]*),', str_yuyan)
        item['yuyan']=str_yuyan.group(1)

        index_diqu = all_data.index('地区')
        str_diqu = all_data[index_diqu:]
        str_diqu = re.search(':,([\u4e00-\u9fa5]*),', str_diqu)
        item['diqu']=str_diqu.group(1)
        # print(item,'itemm')
        yield item









