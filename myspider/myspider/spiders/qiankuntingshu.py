# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector


num = 0
def re_url():
    url_list = []
    # str="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start={}"
    str="https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start={}"
    for i in range(30):
        url = str.format(i)
        url_list.append(url)
    return url_list

class GushiciSpider(scrapy.Spider):
    name = 'qiankuntingshu'
    allowed_domains = ['qktsw.com']
    # start_urls = ['http://www.qktsw.com/tingshu/40295.html',"http://www.qktsw.com/tingshu/34501.html"]
    start_urls=["http://www.qktsw.com/tingshu/37760.html",
                "http://www.qktsw.com/tingshu/43602.html",
                "http://www.qktsw.com/tingshu/47257.html",
                "http://www.qktsw.com/tingshu/34216.html",
                "http://www.qktsw.com/tingshu/34215.html",
                "http://www.qktsw.com/tingshu/34265.html",
                "http://www.qktsw.com/tingshu/34412.html",
                "http://www.qktsw.com/tingshu/34501.html",
                "http://www.qktsw.com/tingshu/34500.html",
                "http://www.qktsw.com/tingshu/34536.html",
                "http://www.qktsw.com/tingshu/34599.html",
                "http://www.qktsw.com/tingshu/34654.html",
                "http://www.qktsw.com/tingshu/50693.html",
                "http://www.qktsw.com/tingshu/47307.html",
                "http://www.qktsw.com/tingshu/47300.html",
                "http://www.qktsw.com/tingshu/13142.html",
                "http://www.qktsw.com/tingshu/53564.html",
                "http://www.qktsw.com/tingshu/53563.html",
                "http://www.qktsw.com/tingshu/53562.html",
                "http://www.qktsw.com/tingshu/53450.html",
                "http://www.qktsw.com/tingshu/40293.html",
                "http://www.qktsw.com/tingshu/40292.html",
                "http://www.qktsw.com/tingshu/40294.html",
                "http://www.qktsw.com/tingshu/40295.html",
                "http://www.qktsw.com/tingshu/42679.html"]
    # start_urls = re_url()
    custom_settings = {
    "DOWNLOAD_DELAY" : 0.01,
    'DEFAULT_REQUEST_HEADERS' : {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-HK;q=0.7,zh;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
        "Host": "www.qktsw.com",
        "Pragma": "no-cache",
        # "If-None-Match":"805a101163ded41:0",
        # "Referer": "https://so.gushiwen.org/gushi/songci.aspx",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES":{
        'myspider.pipelines.MyspiderPipeline': 500,
        'myspider.pipelines.QiiankuntingshuPipeline': 508,
    }
    }


    def parse(self, response):
        response= Selector(response)
        category= response.xpath("//div[@class='desc']/h1/text()").get()
        print(category)
        title_list = response.xpath("//div[@class='xinp']/ul/li")
        # print(title_list)
        for i in title_list:
            title_name = i.xpath("./a/text()").get()
            source = 'http://www.qktsw.com'
            url=i.xpath("./a/@href").get()
            url = source+url
            cur_dict = {}
            cur_dict['category']=category
            cur_dict['title']=title_name
            cur_dict['url']=url
            yield cur_dict


    def parseone(self, response):
        meta = response.meta
        response =Selector(response)
        url_list = response.xpath("//div[@class='ui_list_1']/ul/li[2]/div[@class ='detail']/h4/a/@href").get()
        meta['first_url']=response.xpath("//div[@class='ui_list_1']/ul/li[1]/div[@class ='detail']/h4/a/@href").get()
        if not url_list:
            url_list = response.xpath("//div[@class='ui_list_1']/ul/li[1]/div[@class ='detail']/h4/a/@href").get()
        try:
            yield scrapy.Request(url_list,callback=self.parse_one,meta=meta)
        except Exception as e:
            print(e)
        # with open("/home/gaozhiwei/Desktop/caipubuchong.json") as f:
        #     data = f.read()
        #
        # data = json.loads(data)
        # for i in data['dict']:
        #     if i['step'] == '':
        #         cur_dict = {}
        #         cur_dict['name']=i['name']
        #         cur_dict['first_url']=i['first_url']
        #         yield scrapy.Request(cur_dict['first_url'],callback=self.parse_one,meta=cur_dict)




    def parse_one(self,response):
        meta = response.meta
        response=Selector(response)
        item = dict()
        img_list = response.xpath("//div[@class='recipeStep']/ul/li/div[@class='recipeStep_img']/img/@src").getall()
        if len(img_list)==0:
            img_list=response.xpath("//div[contains(@class,'recipeStep')]/ul/li/div[contains(@class,recipeStep_img)]/img/@src").getall()
        # print(img_list,'dfdfdfsfsfsfsfsfdffs')
        # for i in img_list:
        #     print(i)

        step_list = response.xpath("//div[@class='recipeStep']/ul/li")
        stepstr = ''
        for i in step_list:
            str = i.xpath("string(./div[@class='recipeStep_word'])").get()
            if str=='':
                str=i.xpath("string(./div[contains(@class,'recipeStep_word')])").get()
            stepstr= stepstr+str.strip()


        #     print(str,'fsffsfsfs')
        # print(stepstr,'stepstrssssf')
        item['img_list'] = img_list
        item['step'] = stepstr
        item['name'] = meta['name']
        item['first_url']=meta['first_url']
        yield item
















