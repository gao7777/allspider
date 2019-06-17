# -*- coding: utf-8 -*-
import json
import re

import pymysql
import scrapy
from scrapy.selector import Selector
# from myspider.settings import DEFAULT_REQUEST_HEADERS
from myspider.items import XimaItem,MyspiderItem,ZhidaoItem,XiaopingItem,DoubanItem
from fake_useragent import UserAgent
import requests
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
    name = 'ximalaya'
    allowed_domains = ['ximalaya.com']
    # start_urls = ['https://www.ximalaya.com/revision/category/allCategoryInfo']
    start_urls = ['https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category=yinyue&subcategory=liuxing&meta=&sort=0&page=1&perPage=1000']
    # start_urls = re_url()
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-HK;q=0.7,zh;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        # "Cookie": "BAIDUID=10E1906D92C0EEB3E211912D0DA21FED:FG=1; BIDUPSID=10E1906D92C0EEB3E211912D0DA21FED; PSTM=1527256367; BDSFRCVID=DL8sJeCCxG3ZAmj9qvWmhn6jhsddWIA2uibg3J; H_BDCLCKID_SF=tRk8oKPyJKvbfP0k-nOKMJOH-UnLqhbwJT7Z0lOnMp05Oxbb-TraX4Dk3U8tBM6xQRnj_xJO-KbnhDO_e6Lbej3Qja0s-bbfHDJ8sJOOaCvAMM7Ry4oTLnk1Dn6C24I8-C38oU7KaPQsSnbg3UrNDRLt-xteBjIDJbKJoI-Mf-3bfTr12DTjhPrMQ-kObMT-027OKKOu0R68btjC3Pcsh6KqMhbbKpbA0RrtBRojthF0HPonHjLhjTJ33J; BDUSS=lCVjlETkZBaUVselBBbVZrT3NOV2d0N3dwbVlXTVY0dFNseEV1MW4zYTJNNjljQVFBQUFBJCQAAAAAAAAAAAEAAACoy7tPYnJvdGhlcrjfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALamh1y2podcS3; IKUT=4086; delPer=0; PSINO=1; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=28690_1420_21084_28720_28558_28607_28584_28641_28518_28605; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1552489899,1552705454,1552785613,1552948489; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552948497",
        "Host": "www.ximalaya.com",
        "Pragma": "no-cache",
        # "If-None-Match":"805a101163ded41:0",
        "Referer": "https://www.ximalaya.com/category/",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
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

        conn = pymysql.connect(host='localhost', port=3306, user='root', password='gaozhiwei', database='nlpdata',
                               autocommit=True, charset='utf8')
        cur = conn.cursor()
        url = 'https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category={}&subcategory={}&meta=&sort=0&page=1&perPage=5000'
        sql1 = 'select albumtitle,albumid from ximalayatwo'
        url = "https://www.ximalaya.com/revision/album/getTracksList?albumId={}&pageNum=1"
        cur.execute(sql1)
        scr_data_list = cur.fetchall()
        for i in scr_data_list:
            meta_dict = dict()
            url_cur = url.format(i[1])
            # print(i)
            # print(url_cur)
            meta_dict['albumname']=i[0]
            meta_dict['albumid'] = i[1]
            meta_dict['cursor']= cur
            yield scrapy.Request(url_cur,meta=meta_dict,callback=self.parse_two)

    def parse_two(self,response):
        meta_dict = response.meta
        scr_url = 'https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&sort=-1&pageSize=30'
        json_data = response.body.decode('utf-8')
        json_dict = json.loads(json_data)
        totalsize=json_dict['data']['trackTotalCount']
        meta_dict['totalsize']=totalsize
        num = int(totalsize)//30
        yushu= int(totalsize)%30
        if yushu !=0:
            num= num+1
        count = 0
        for i in range(1,num+1):
            count += 1
            if count > 1:
                break
            meta_dict['page']=i
            cru_url=scr_url.format(meta_dict['albumid'],i)
            # print(cru_url)
            yield scrapy.Request(cru_url,callback=self.parse_there,meta=meta_dict)
    def parse_there(self,response):
        sql1 = 'Insert into ximalayathere(albumid, albumname, totalsize, trackid, trackname, trackplayurl, tracklinkurl, trackanchorid, trackcoverpath,page) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        meta_dict = response.meta
        cur = meta_dict['cursor']
        json_data = response.body.decode('utf-8')
        # with open('/home/gaozhiwei/ximalayaalbumtrackjson/{}.json'.format(meta_dict['albumname']+str(meta_dict['page'])),'w') as f:
        #     f.write(json_data)
        json_dict = json.loads(json_data)
        data_list = json_dict['data']['tracksAudioPlay']
        data_write_list = []
        for i in data_list:
            con_list=[]
            con_list.append(meta_dict['albumid'])
            con_list.append(meta_dict['albumname'])
            con_list.append(meta_dict['totalsize'])
            con_list.append(i['trackId'])
            con_list.append(i['trackName'])
            con_list.append(i['src'])
            con_list.append(i['trackUrl'])
            con_list.append(i['anchorId'])
            con_list.append(i['trackCoverPath'])
            con_list.append(str(meta_dict['page']))
            data_write_list.append(con_list)
        cur.executemany(sql1,data_write_list)

        print(meta_dict)


    # def parse(self, response):
    #     conn = pymysql.connect(host='localhost', port=3306, user='root', password='gaozhiwei', database='nlpdata',
    #                            autocommit=True, charset='utf8')
    #     cur = conn.cursor()
    #     url = 'https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category={}&subcategory={}&meta=&sort=0&page=1&perPage=5000'
    #     sql1 = 'select categorytwoname,categorytherename,categorytherelinkurl from ximalayaone'
    #     cur.execute(sql1)
    #     data_list = cur.fetchall()
    #     num = 0
    #     for i in data_list:
    #         num +=1
    #         meta_dict={}
    #         meta_dict['categoryonename']=i[0]
    #         meta_dict['categorytwoname'] = i[1]
    #         meta_dict['srclinkurl']=i[2]
    #         meta_dict['cursor']=cur
    #         url_data = i[2]
    #         list1 = url_data.split('/')
    #         url1=url.format(list1[1],list1[2])
    #         # print(url1)
    #         # print(meta_dict)
    #         yield scrapy.Request(url1,callback=self.parse_detail,meta=meta_dict)
    #     print(num,'total_num')

    def parse_detail(self,response):
        meta_dict = response.meta
        cur = meta_dict['cursor']
        json_data = response.body.decode('utf-8')
        # print(meta_dict,'meta_dict')
        sql = 'insert into ximalayatwo(categorynameone,categorynametwo,srcurllink,totalsize,albumid,albumtitle,albumcoverpath,albumauthorname,albumuserid,albumlinkurl,albumtrackcount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        file_path_src ='./ximalayaalbum/{}.json'
        file_path= file_path_src.format(meta_dict['categorytwoname'])
        # with open(file_path, 'w') as f:
        #     f.write(json_data)
        json_dict = json.loads(json_data)
        data_list = []
        categorynameone = meta_dict['categoryonename']
        categorynametwo = meta_dict['categorytwoname']
        srcurllink = meta_dict['srclinkurl']
        totalsize = json_dict['data']['total']
        # print(json_dict['data'])
        for i in json_dict['data']['albums']:
            dictone = dict()
            dictone['categorynameone'] = categorynameone
            dictone['categorynametwo'] = categorynametwo
            dictone['srcurllink'] = srcurllink
            dictone['totalsize'] = totalsize
            dictone['albumid'] = i['albumId']
            dictone['title'] = i['title']
            dictone['coverPath'] = i['coverPath']
            dictone['authorName'] = i['anchorName']
            dictone['userid'] = i['uid']
            dictone['linkurl'] = i['link']
            dictone['trackCount'] = i['trackCount']
            data_list.append(dictone)
        num = 0
        for i in data_list:
            mysql_list = []
            mysql_list.append(i['categorynameone'])
            mysql_list.append(i['categorynametwo'])
            mysql_list.append(i['srcurllink'])
            mysql_list.append(i['totalsize'])
            mysql_list.append(i['albumid'])
            mysql_list.append(i['title'])
            mysql_list.append(i['coverPath'])
            mysql_list.append(i['authorName'])
            mysql_list.append(i['userid'])
            mysql_list.append(i['linkurl'])
            mysql_list.append(i['trackCount'])
            cur.execute(sql,mysql_list)
            # print(i)
            num += 1
        print(num,'num')
        # for i in data_list:
        #     print(i)
        # print('dsfasdfasdfasdfasdfasfasdfasdf')








