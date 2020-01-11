# -*- coding: utf-8 -*-
import json
from scrapy.selector import Selector
import pymysql
import scrapy
num = 0


class XimaSpider(scrapy.Spider):
    name = 'jiyici'
    allowed_domains = ['xpcha.com']
    # start_urls = ['https://www.ximalaya.com/revision/category/allCategoryInfo']
    # start_urls = ['http://jinyici.xpcha.com/list_0.html']
    # start_urls = ['http://fanyici.xpcha.com/list_0.html']
    # start_urls = ['http://jinyici.xpcha.com/list_0_{}.html'.format(i) for i in range(2,174)] +["http://jinyici.xpcha.com/list_0.html"]
    start_urls = ['http://fanyici.xpcha.com/list_0_{}.html'.format(i) for i in range(2,132)] +["http://fanyici.xpcha.com/list_0.html"]
    # start_urls = re_url()
    custom_settings = {
        "DOWNLOAD_DELAY" : 0.01,
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
        "Host": "fanyici.xpcha.com",
        "Pragma": "no-cache",
        # "If-None-Match":"805a101163ded41:0",
        "Referer": "http://fanyici.xpcha.com/list_0_2.html",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES": {
            'myspider.pipelines.MyspiderPipeline': 500,
            'myspider.pipelines.JinyiciPipeline': 508,
        }
    }





    def parse(self,response):

        response = Selector(response)
        data_list = response.xpath("//div[@class='cidian_shaixuan']/dl[@class='shaixuan_5']/dd/a")
        for i in data_list:
            name = i.xpath("./text()").get()
            front_url = "http://jinyici.xpcha.com/"
            url= i.xpath("./@href").get()
            complete_url= front_url+url
            cur_dict = dict()
            cur_dict['name'] = name
            cur_dict['url']= complete_url
            # print(complete_url)
            yield scrapy.Request(url=complete_url,callback=self.parseone,meta=cur_dict)


    def parseone(self,response):

        meta = response.meta
        response = Selector(response)

        values=response.xpath("//div[@class='left_leirong']/dl[@class='shaixuan_1']/dd/span/text()").getall()
        filter_values = [i[:-1] for i in values]
        meta['values']= filter_values
        yield meta
        # print(meta)
        # # print(filter_values)



















