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
