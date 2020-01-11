# -*- coding: utf-8 -*-
import json
import re

from scrapy.selector import Selector
import pymysql
import scrapy
import pandas as pd




num =0
num1 =0

class XimaSpider(scrapy.Spider):
    name = 'migutag'
    allowed_domains = ['migu.cn']
    start_urls = []
    custom_settings = {
        "DOWNLOAD_DELAY" :0.2,
        'DEFAULT_REQUEST_HEADERS' : {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "music.migu.cn",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    },
        "ITEM_PIPELINES": {
            'myspider.pipelines.MyspiderPipeline': 500,
            'myspider.pipelines.MiguMusicSingerPipeline': 508,
        }
    }
    total_url = set()

    # def start_requests(self):
    #     import string
    #     base_url = "http://music.migu.cn/v3/music/artist?tagId={tag}&type={type}&firstLetter={firstletter}&page=1"
    #     for tag in string.digits[1:4]:
    #         for i in string.ascii_uppercase[:3]:
    #             for j in string.ascii_uppercase[:26]:
    #                 cur_url = base_url.format(tag=tag,type=i, firstletter=j)
    #                 yield scrapy.Request(cur_url,callback=self.parse, dont_filter=True)
    def start_requests(self):
        with open("/home/gaozhiwei/Desktop/migu1214totaldata.json") as f:
        # with open("/home/sound/1209spidersmigu/migu1207totaldata.json") as f:
            data_json = f.read()
        dict_data = json.loads(data_json)
        # print(len(dict_data))
        for i in dict_data:
            # print(i)
            url = i['url']
            cur_url = "http://music.migu.cn"+url

        # print(num)
            yield scrapy.Request(cur_url,callback=self.parse,meta=i)
    # def parse(self,response):
    #     request_url = response.url
    #     response = Selector(response)
    #     base_url = "http://music.migu.cn"
    #     singer_list = response.xpath("//div[@id='J_ArtistList']/div[@class='thumbnail']/a/@href").getall()
    #     if len(singer_list)!=0:
    #         for i in singer_list:
    #             # print(i)
    #             song_first_page = base_url+i+'/song'
    #             print(song_first_page)
    #             yield scrapy.Request(url=song_first_page,callback=self.parsemiddle)
    #     next_page = response.xpath("//div[@class='views-pagination']/a[@class='pagination-item']/@href").getall()
    #
    #     self.total_url.add(request_url)
    #     if len(next_page)!=0:
    #         for i in next_page:
    #             print(i,'cur_url;lkfdsajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjlkjfdsa;;;;;;;;;;;;;;')
    #             cur_url = base_url+i
    #             if cur_url not in self.total_url:
    #                 self.total_url.add(cur_url)
    #                 yield scrapy.Request(url=cur_url,callback=self.parse)
    #
    # def parsemiddle(self,response):
    #     request_url = response.url
    #     response = Selector(response)
    #     max_page= response.xpath("//div[@class='views-pagination']/a[@class='pagination-item'][last()]/text()").get()
    #     print(max_page,'fdsaaaaaaaaaaaaaa')
    #     if max_page is not None:
    #         for i in range(1,int(max_page)+1):
    #             cur_url = request_url+'?page=%s'%(str(i))
    #             print(cur_url)
    #             yield scrapy.Request(url=cur_url,callback=self.parseone)
    #     else:
    #         yield scrapy.Request(url=request_url,callback=self.parseone)
    #
    #
    #
    # def parseone(self,response):
    #
    #     # meta=response.meta
    #     response = Selector(response)
    #     song_list = response.xpath("//div[@class='songlist-body']/div[@class='row J_CopySong']")
    #     base_url = "http://music.migu.cn"
    #     if len(song_list)!=0:
    #         for i in song_list:
    #             cur_dict =dict()
    #             href = i.xpath("./div[@class='song-name J_SongName']/a[@class='song-name-txt']/@href").get()
    #             song_name = i.xpath("./div[@class='song-name J_SongName']/a[@class='song-name-txt']/text()").get()
    #             # singer_name = i.xpath("./div[@class='song-singers J_SongSingers']/a/text()").get()
    #             singer_name = i.xpath("string(./div[@class='song-singers J_SongSingers'])").get()
    #             album_name = i.xpath("./div[@class='song-belongs']/a/text()").get()
    #             singer_name = re.sub("\s",'',singer_name)
    #             # print(singer_name)
    #             # print("="*20)
    #             cur_dict['title'] = song_name
    #             cur_dict['singer_name'] = singer_name
    #             cur_dict['album_name'] = album_name
    #             cur_dict['url'] = href
    #             # print(cur_dict)
    #             yield cur_dict
    #
    #     # next_page =response.xpath("")
    #             # cur_url = base_url+href
    #             # yield scrapy.Request(cur_url,callback=self.parsetwo)
    def parse(self,response):
        meta = response.meta
        request_url = response.url
        response = Selector(response)
        song_name = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/h2[@class='info_title']/text()").get()
        song_singer = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_singer']/a/text()").get()
        song_tag_list = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_about']/p[@class='about_blog']/span/span[@class='songtag']/text()").getall()
        song_zuoci = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_about']/p[1]/span/text()").get()
        song_zuoqu = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_about']/p[2]/span/text()").get()
        song_album_url = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_about']/p[3]/span/a/@href").get()
        song_album = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_about']/p[3]/span/a/text()").get()
        song_tag_str = '/'.join(song_tag_list)
        song_lyric = response.xpath("string(//div[@class='lyric']/div[@class='info-contain lyr-contain'])").get()
        # print(request_url,song_name,song_singer,song_tag_str,song_lyric)
        pipe_dict = dict()
        pipe_dict['song_name']=song_name
        pipe_dict['song_singer']=song_singer
        pipe_dict['song_tag_str']=song_tag_str
        pipe_dict['song_lyric']=song_lyric
        pipe_dict['request_url']=request_url
        pipe_dict['src'] = meta
        pipe_dict['zuoci'] = song_zuoci
        pipe_dict['zuoqu'] = song_zuoqu
        pipe_dict['album_url'] = song_album_url
        pipe_dict['album_name'] = song_album
        base_url = "http://music.migu.cn"
        # print(pipe_dict)
        cur_url = base_url+song_album_url
        yield scrapy.Request(url=cur_url,callback=self.parseone,meta=pipe_dict)


    def parseone(self,response):
        meta = response.meta
        response = Selector(response)
        pub_data = response.xpath("//div[@class='pub-date']/text()").get()
        meta['pub_data'] = pub_data
        # print(meta)
        yield meta























