# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os

import pymongo
import time


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        print(spider.name)
        print(item)

        # return item

class XimaPipeline(object):
    def __init__(self):
        self.f = './test.txt'
        self.file = None
    def open_spider(self,spider):
        self.file = open(self.f, 'a+')

    def process_item(self,item,spider):
        print(spider.name,'spname')
        print(item,'itemmmm')
        # json_item = json.dumps(item)

        self.file.write(str(item)+'\n')
        return item

    def close_spider(self, spider):  # 在爬虫关闭的时候仅执行一次

        self.file.close()

class MongoPipeline(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.mongo_client.test
        self.collection = self.db.agent

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
class FilePipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y%m%d', time.localtime())
        filename = 'test' + now + '.txt'
        with open(filename, 'a', encoding='utf-8') as fp:
            imgname = os.path.basename(item['country'])
            fp.write(imgname + ' ')
            if os.path.exists(imgname):
                pass
            else:
                pass
                # with open(imgname, 'wb') as fp:
                    # response = request.urlopen(item['country'])
                    # fp.write(response.read())
            fp.write(item['agent_ip'] + ' ')
            fp.write(item['agent_port'] + ' ')
            fp.write(item['agent_addr'] + ' ')
            fp.write(item['anonymity'] + ' ')
            fp.write(item['agent_type'] + ' ')
            fp.write(item['survival_time'] + ' ')
            fp.write(item['verify_time'] + '\n\n')
            time.sleep(1)
        return item

class DailiPipeline(object):

    def process_item(self, item, spider):
        now = time.strftime('%Y%m%d', time.localtime())
        filename = 'Daili' + now + '.json'
        with codecs.open(filename, 'a', encoding='utf-8') as fp:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            fp.write(line)
        return item


import csv
class DailiPipeline(object):
    def process_item(self,item,spider):
        with open(r'./zarten.csv', 'a', newline='') as csvfile:
            fieldnames = ['', '']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')  # csv中默认,分隔单元格，delimiter可以不指定
            csv_writer.writeheader()
            csv_writer.writerow({'name': 'Zarten1', 'age': 1})
            csv_writer.writerow({'name': 'Zarten2', 'age': 2})
            csv_writer.writerows()