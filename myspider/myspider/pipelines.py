# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os

import pymongo,pymysql
import time
import pandas as pd
import csv
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        print(spider.name)
        # print(item)
        return item

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
class ZhidaoPipeline(object):
    def process_item(self,item,spider):
        print('llksflzhidao')
        # print(type(item))
        # print('guanfao')
        # print(item)
        list_question= item['question']
        # print(list_question)
        dict_data= {}
        # print(item['question'][0])
        # print(type['question'][0])
        try:
            dict_data[list_question[0]]=list_question[1:]
            data_json = json.dumps(dict_data,ensure_ascii=False)
            with open('/home/gaozhiwei/Desktop/zhidaodata/{}.json'.format(list_question[0]),'w+') as f:
                print('data_jsondddd',data_json)
                f.write(data_json)
        except Exception as e:
            print('shjumeiyou',e)

        # with open('./allzhidaodata.csv','w+') as csvfile:
            # fieldnames = ['question']
            # csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames, delimiter=',')  # csv中默认,分隔单元格，delimiter可以不指定
            # csv_writer.writerow({'name': 'Zarten1', 'age': 1})
            # csv_writer.writerow(item)
            # writer = csv.writer(csvfile)
            # writer.writer.writerows(item['question'])

class XiaopinPipeline(object):
    def process_item(self,item,spider):
        print('start')
        print(item)
        name = item['name']
        zuoping = item['zuopin']
        dict_1 = {}
        dict_1[name]=zuoping

        # data = json.dumps(dict_1)
        # pd.to_csv('./xiaoping.csv',mode='a+')
        # print(dict_1)
        with open('./5xiaopin.txt','a+',encoding='utf-8') as f:
            f.write(str(dict_1)+'\n')
        # print(dict_1,'dfsfsf')
        # with open('./xiaoping1.csv', 'a+', encoding='utf-8') as f:
        #     a = csv.writer(f)
        #     a.writerows(dict_1)

class KuwoPipeline(object):
    def __init__(self):
        self.dict = {}
        self.song_title = set()
    def open_spider(self, spider):
        self.dict['dict'] = []
    def process_item(self,item,spider):
        print(item)
        self.dict['dict'].append(item)
        self.song_title.add(item['song'])
        # with open('./kuwo.json','a+') as f:
        #     item= json.dumps(item,ensure_ascii=False)
        #     f.write(item+',')
    def close_spider(self,spider):
        print('close_spider')
        print(self.dict)
        print(self.song_title)
        # with open('/home/gaozhiwei/Desktop/test.txt','w') as f:
        #     for i in self.song_title:
        #         f.write(i+'\n')
        cur_dict = {}
        cur_dict['dict']=[]
        for i in self.song_title:
            for j in self.dict['dict']:
                if j['song'] == i:
                    cur_dict['dict'].append(j)
                    break
        with open('/home/gaozhiwei/Desktop/kuwozuixin5.29.json','w') as f:
            json_data = json.dumps(cur_dict,ensure_ascii=False,indent=2)
            f.write(json_data)


        # with open('./kuwo666.json','w+') as f:
        #     old_data = f.read()
        #     # print(len(old_data))
        #     # print(old_data,'gagffsfg')
        #     # print(type(old_data))
        #     # print(a)
        #     if old_data:
        #         # print('iii')
        #         old_data = json.loads(old_data)
        #         # print(type(old_data))
        #         # print(old_data)
        #         print(len(old_data))
        #         dict_list = a.extend(old_data)
        #         dict_list=a
        #         print(len(a))
        #     else:
        #         dict_list=a
        #     # print(len(dict_list),'all')
        #     final_data =[dict(t) for t in set([tuple(d.items()) for d in dict_list])]
        #     # print(final_data,'fadfadsffa')
        #     # print(len(final_data),'all')
        #     data_json = json.dumps(final_data,ensure_ascii=False)
        #     f.write(data_json)

class DoubanPipeline(object):
    def __init__(self):
        # self.file = open('./douban.json','a+')
        # self.num = 1
        self.con = pymysql.connect(host="127.0.0.1", user='root', password='gaozhiwei', database='nlpdata',autocommit=True,charset='utf8')
        self.curson = self.con.cursor()
        # self.sql = 'INSERT INTO doubandianying (move_detail_url, movie_title, dayan, bianju, movielanguage, leixing, diqu,yanyuan) values (%s,%s,%s,%s,%s,%s,%s,%s);'
        self.sql = 'INSERT INTO doubandianshiju (move_detail_url, movie_title, dayan, bianju, movielanguage, leixing, diqu,yanyuan) values (%s,%s,%s,%s,%s,%s,%s,%s);'

    def open_spider(self,spider):
        self.num=0
    def process_item(self,item,spider):
        # print(item)
        data_list =[]
        data_list.append(item["move_detail_url"])
        data_list.append(item["move_title"])
        daoyan = item["daoyan"]
        dayanstr = ''
        for i in daoyan:
            dayanstr=dayanstr+i+'/'
        data_list.append(dayanstr)
        bianju=item["bianju"]
        bianjustr = ''
        for i in bianju:
            bianjustr = bianjustr + i + '/'
        data_list.append(bianjustr)
        data_list.append(item["yuyan"])
        leixing=item["leixing"]
        leixingstr = ''
        for i in leixing:
            leixingstr = leixingstr + i + '/'
        data_list.append(leixingstr)
        data_list.append(item["diqu"])
        data_list.append(item["yanyuan"])
        print(data_list)
        # dict_item = dict(item)
        # dict_item_json = json.dumps(dict_item,ensure_ascii=False)
        self.curson.execute(self.sql,tuple(data_list))
        # self.file.write(dict_item_json+',')
    def close_spider(self, spider):  # 在爬虫关闭的时候仅执行一次
        # self.file.close()
        # self.curson.commit()
        print('22222')
        self.con.close()
class KuwoallPipeline(object):
    def __init__(self):
        # self.file = open('./douban.json','a+')
        # self.num = 1
        self.con = pymysql.connect(host="127.0.0.1", user='root', password='gaozhiwei', database='nlpdata',autocommit=True)
        self.curson = self.con.cursor()
        self.sql = 'INSERT INTO kuwodata (category_one,category_two,url_1,song_title,album_name,singer_name,url_3,url_2) values (%s,%s,%s,%s,%s,%s,%s,%s);'
    def open_spider(self,spider):
        self.num=0
    def process_item(self,item,spider):
        print(item)
        data_list =[]
        data_list.append( item["category_one"])
        data_list.append(item["category_two"])
        data_list.append(item["url_1"])
        data_list.append(item["song_title"])
        data_list.append(item["album_name"])
        data_list.append(item["singer_name"])
        data_list.append(item["url_3"])
        # data_list.append(item["geci"])
        data_list.append(item["url_2"])
        self.curson.execute(self.sql,data_list)
    def close_spider(self, spider):  # 在爬虫关闭的时候仅执行一次
        # self.curson.commit()
        self.con.close()

class GushiciPipeline(object):
    def __init__(self):
        self.dict = {}
        self.dict['dict'] = []
        self.f = open('/home/gaozhiwei/Desktop/tanshisanbaishou.json','w')
    def open_spider(self,spider):
        print(spider)
        # dict = {}
        # dict['dict']=[]
    def process_item(self,item,spider):
        print('itempipeline',item)
        self.dict['dict'].append(item)
        # json_data = json.dumps(item,ensure_ascii=False,indent=2)
        # self.f.write(json_data+"\n")
    def close_spider(self,spider):
        json_data = json.dumps(self.dict,ensure_ascii=False,indent=1)
        self.f.write(json_data)
        self.f.close()



class MeishitianxiaPipeline():
    def __init__(self):

        self.final_dict = {}
        self.final_dict['dict'] = []
    def open_spider(self,spider):
        pass
    def process_item(self,item,spider):
        print("dddddddddddd",item)
        self.final_dict['dict'].append(item)
    def close_spider(self,spider):
        with open("/home/gaozhiwei/Desktop/caipubuchongdierban.json",'w') as f:
            f.write(json.dumps(self.final_dict,ensure_ascii=False,indent=1))
class QiiankuntingshuPipeline():
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",database="nlpdata",user='root',password='gaozhiwei',autocommit=True)
        self.cursor=self.conn.cursor()
        self.sql = "insert into qiankuntingshu(category,title,url) values(%s,%s,%s);"

    def open_spider(self,spider):
        pass
    def process_item(self,item,spider):
        category=item['category']
        title=item['title']
        url=item['url']
        cur_list = []
        cur_list.append(category)
        cur_list.append(title)
        cur_list.append(url)
        # print(category,title,url)
        self.cursor.execute(self.sql,cur_list)
    def close_spider(self,spider):
        pass