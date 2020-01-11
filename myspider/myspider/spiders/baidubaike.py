# -*- coding: utf-8 -*-
import json
import re

from scrapy.selector import Selector
import pymysql
import scrapy
import pandas as pd

num = 0


class XimaSpider(scrapy.Spider):
    name = 'baidubaike'
    allowed_domains = ['baidu.com']
    start_urls = ["https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2%E4%BA%8B%E4%BB%B6/1432920#4"]
    custom_settings = {
    "DOWNLOAD_DELAY":0.01,
    # "HTTPERROR_ALLOWED_CODES" :[301, 302],
    'DEFAULT_REQUEST_HEADERS': {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Host": "baike.baidu.com",
            "Referer": "https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2%E4%BA%8B%E4%BB%B6/1432920#4",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        },
        "ITEM_PIPELINES": {
            'myspider.pipelines.MyspiderPipeline': 500,
            'myspider.pipelines.BaidubaikePipeline': 508,
        }
    }

    # def parse(self,response):
    #     print("start")
    #     response= Selector(response)
    #     tr_list = response.xpath("//tr")
    #     # print(tr_list)
    #     total_data_list =list()
    #     for tr in tr_list:
    #         td_title = tr.xpath("string(./td[last()-1])").get()
    #         td_str = tr.xpath("string(./td[last()])").get()
    #         if td_title and td_str:
    #             print(td_title)
    #             # cur_list
    #             re_str=re.sub("[前中后]期\s",'',td_str).strip()
    #             # print(re_str)
    #             cur_dict = dict()
    #             title_list = re_str.split("·")
    #             cur_dict[td_title.strip()] = [re.sub('\s','',i) for i in title_list]
    #             total_data_list.append(cur_dict)
    #             # print(title_list)
    #     print(total_data_list)
    #     with open("/home/gaozhiwei/Desktop/baibubaikefirstpage.json",'w')as f:
    #         f.write(json.dumps(total_data_list,indent=1,ensure_ascii=False))

    def parse(self, response):
        response = Selector(response)
        base_url = "https://baike.baidu.com"
        td_a_list = response.xpath("//tr/td/a")
        for a in td_a_list:
            a_name = a.xpath("./text()").get()
            a_url = a.xpath("./@href").get()
            # print(a_name,a_url)
            cur_dict = dict()
            cur_dict['title'] = a_name

            cur_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Host": "baike.baidu.com",
            "Referer": "",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }

            yield scrapy.Request(url=base_url + a_url, meta=cur_dict,callback=self.parseone,headers=cur_header.update({"Referer":base_url+a_url}))

    def parseone(self, response):
        print("onestart")
        meta = response.meta
        response = Selector(response)
        final_dict =dict()

        para_list = response.xpath("//div[@class='para']")
        page_str = ''
        page = page_str.join(re.sub('\s','',i.xpath("string(.)").get()) for i in para_list)
        page = re.sub('\s','',page)
        title_src = meta['title']
        title_cur = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()").get()
        infobox_dl_list = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        # print(infobox_dl_list)

        info_dict = dict()
        for infobox_dl in infobox_dl_list:
            dt_list = infobox_dl.xpath("./dt")
            dd_list = infobox_dl.xpath("./dd")
            # print(dd_list)
            # print(len(dt_list),len(dd_list))
            if len(dt_list) == len(dd_list):
                for i in range(len(dt_list)):
                    # print(dt_list[i])
                    # print(i,"ssssssssssssssssssssssssssssss")
                    cur_dt_name= re.sub('\s','',dt_list[i].xpath("string(.)").get())
                    cur_dd_name = re.sub('\s','',dd_list[i].xpath("string(.)").get())
                    # print(cur_dd_name,cur_dt_name)
                    info_dict[cur_dt_name] = cur_dd_name
        tag_list = response.xpath("string(//dd[@id='open-tag-item'])").get().split('，')
        tag_list = [re.sub('\s','',i) for i in tag_list]

        # print(info_dict)
        final_dict[title_src] = dict()
        final_dict[title_src]['title'] = title_cur
        final_dict[title_src]['infobox'] = info_dict
        final_dict[title_src]['page'] = page
        final_dict[title_src]['tag_list'] = tag_list
        # print(final_dict)

        yield final_dict




