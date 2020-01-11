# -*- coding: utf-8 -*-
import json
from scrapy.selector import Selector
import pymysql
import scrapy
import pandas as pd



num = 0


class XimaSpider(scrapy.Spider):
    name = 'migusinger'
    allowed_domains = ['migu.cn']
    start_urls = []
    custom_settings = {
        "DOWNLOAD_DELAY" :1,
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

    def start_requests(self):
        import string
        base_url = "http://music.migu.cn/v3/music/artist?tagId=2&type={type}&firstLetter={firstletter}&page=1"
        for i in string.ascii_uppercase[:3]:
            for j in string.ascii_uppercase[:26]:
                cur_url = base_url.format(type=i, firstletter=j)
                yield scrapy.Request(cur_url,callback=self.parse, dont_filter=True)
    def parse(self,response):
        request_url = response.url
        response = Selector(response)
        base_url = "http://music.migu.cn"
        singer_list = response.xpath("//div[@id='J_ArtistList']/div[@class='thumbnail']/a/@href").getall()
        if len(singer_list)!=0:
            for i in singer_list:
                # print(i)
                song_first_page = base_url+i+'/song'
                yield scrapy.Request(url=song_first_page,callback=self.parseone)
        next_page = response.xpath("//div[@class='views-pagination']/a[@class='pagination-item']/@href").getall()
        self.total_url.add(request_url)
        if len(next_page)!=0:
            for i in next_page:
                # print(i,'cur_url;lkfdsajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjlkjfdsa;;;;;;;;;;;;;;')
                cur_url = base_url+i
                if cur_url not in self.total_url:
                    self.total_url.add(cur_url)
                    yield scrapy.Request(url=cur_url,callback=self.parse)

    def parseone(self,response):

        # meta=response.meta
        response = Selector(response)
        song_list = response.xpath("//div[@class='songlist-body']/div[@class='row J_CopySong']")
        base_url = "http://music.migu.cn"
        if len(song_list)!=0:
            for i in song_list:
                href = i.xpath("./div[@class='song-name J_SongName']/a[@class='song-name-txt']/@href").get()
                cur_url = base_url+href
                yield scrapy.Request(cur_url,callback=self.parsetwo)


    def parsetwo(self,response):
        request_url = response.url
        response = Selector(response)
        song_name = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/h2[@class='info_title']/text()").get()
        song_singer = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_singer']/a/text()").get()
        song_tag_list = response.xpath("//div[@class='container songinfoCon']/div[@class='info_contain']/div[@class='info_about']/p[@class='about_blog']/span/span[@class='songtag']/text()").getall()
        song_tag_str = '/'.join(song_tag_list)
        song_lyric = response.xpath("string(//div[@class='lyric']/div[@class='info-contain lyr-contain'])").get()
        # print(request_url,song_name,song_singer,song_tag_str,song_lyric)
        pipe_dict = dict()
        pipe_dict['song_name']=song_name
        pipe_dict['song_singer']=song_singer
        pipe_dict['song_tag_str']=song_tag_str
        pipe_dict['song_lyric']=song_lyric
        pipe_dict['request_url']=request_url
        yield pipe_dict























