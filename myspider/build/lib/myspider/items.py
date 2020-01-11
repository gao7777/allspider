# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_1 = scrapy.Field()
    detail = scrapy.Field()


class XimaItem(scrapy.Item):
    url_1 = scrapy.Field()
    name = scrapy.Field()
    url_2 = scrapy.Field()
    comment = scrapy.Field()
class ZhidaoItem(scrapy.Item):
    question = scrapy.Field()


class XiaopingItem(scrapy.Item):
    name = scrapy.Field()
    url=scrapy.Field()
    zuopin= scrapy.Field()

class Kuwo(scrapy.Item):
    song = scrapy.Field()
    singer = scrapy.Field()
    url = scrapy.Field()

class DoubanItem(scrapy.Item):
    move_title = scrapy.Field()
    move_detail_url = scrapy.Field()
    yuyan = scrapy.Field()
    yanyuan = scrapy.Field()
    diqu = scrapy.Field()
    leixing = scrapy.Field()
    daoyan = scrapy.Field()
    bianju = scrapy.Field()
class Kuwoall(scrapy.Item):
    category_one = scrapy.Field()
    category_two = scrapy.Field()
    url_1 = scrapy.Field()
    song_title = scrapy.Field()
    album_name = scrapy.Field()
    singer_name = scrapy.Field()
    url_3 = scrapy.Field()
    geci = scrapy.Field()
    url_2 = scrapy.Field()
class GushiciItem(scrapy.Item):

    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
