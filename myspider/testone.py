# import re,json,pymysql
#
# conn = pymysql.connect(host='localhost', user='root', password="gaozhiwei",
#                  database='nlpdata', port=3306, unix_socket=None,
#                  charset='utf8',autocommit=True)
# cur = conn.cursor()
# sql = 'insert into beeviedeo(title) values (%s)'
# sql1= 'select title from beeviedeo'
# with open('/home/gaozhiwei/Desktop/beeVideo_movie_title.json','r') as f:
#     json_data = f.read()
# dict_data = json.loads(json_data)
# values_list = dict_data['dict'][0]['value']
# num = 0
# values_list= list(set(values_list))
# for i in values_list:
#     num +=1
#     # cur.execute(sql,i)
#     if len(i) <=4:
#         print(i)
# print(num)
# data_list = cur.execute(sql1)
# data_list = cur.fetchall()
# value_list = []
# for i in data_list:
#     value_list.append(i[0])
# cur_dict = dict()
# cur_dict['dict']=[]
# cur1_dict = {}
# cur1_dict['majorType'] = 'video'
# cur1_dict['value'] = value_list
# cur_dict['dict'].append(cur1_dict)
# json_beedata = json.dumps(cur_dict,ensure_ascii=False,indent=3)
# with open('/home/gaozhiwei/Desktop/beevideo.json','w') as f:
#     f.write(json_beedata)
#

# import re,json,pymysql
# conn = pymysql.connect(host='localhost', user='root', password="gaozhiwei",
#                  database='nlpdata', port=3306, unix_socket=None,
#                  charset='utf8',autocommit=True)
# cur = conn.cursor()
# cur1 = conn.cursor()
# sql= 'select id,data from record where id>%s and id <%s '
# sql1 = 'select id,merchant_id,client_id,dialog_id,ver,query,data,cost,timestamp,device_id from record where id = %s'
# sql2 = 'insert into record_chat(id,merchant_id,client_id,dialog_id,ver,query,data,cost,timestamp,device_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#
# num = 0
# jishu = 0
# while True:
#     cur_sql = sql%(str(num),str(num+100000))
#     cur.execute(cur_sql)
#     data_list = cur.fetchall()
#     for i in data_list:
#         data = i[1]
#         one = re.search('chat',data)
#         if one:
#             id = i[0]
#             cur1.execute(sql1,id)
#             cur1_data_list = list(cur1.fetchall()[0])
#             print(cur1_data_list)
#             cur1.execute(sql2,cur1_data_list)
#             # print(i[0])
#             # print(one.group())
#             # print(data)
#     if data_list == ():
#         break
#     num =num +100000
#     jishu+=1
# print(jishu)

# for i in data_list:
#     print(i)
# import re,json
# with open('/home/gaozhiwei/Desktop/ximalayadiyiban.json','r') as f:
#     source_data_json = f.read()
# source_data_dict = json.loads(source_data_json)
# print(source_data_dict)
# dict_data = source_data_dict['dict']
# num  = 0
# while True:
#     if num >= len(dict_data):
#         break
#     cur_dict = {}
#     cur_dict['dict'] = []
#     for i in range(num,num+50000):
#         if i ==None:
#             break
#         try:
#             cur_dict['dict'].append(dict_data[i])
#         except Exception as e:
#             print(e)
#             break
#     with open('/home/gaozhiwei/Desktop/ximalayayidiban/%d.json'%num,'w') as f:
#         f.write(json.dumps(cur_dict,ensure_ascii=False,indent=1))
#     num = num +50000
# import json,re
# with open('/home/gaozhiwei/Desktop/kuwozuixin.json') as f:
#     data = f.read()
# num =0
# data = json.loads(data)
# for i in data['dict']:
#     num+=1
#     print(i)
# print(num)
# str1 = 'dfsFFF说法 是否接受对方'
# str2 = str1.lower()
# print(str2)
# import json
#
# with open("/home/gaozhiwei/Desktop/ximalayadiyiban/150000.json",'r') as f:
#     data = f.read()
#
# dict_data = json.loads(data)
# data_list = dict_data['dict']
# for index,i in enumerate(data_list):
#     cur_list = i['value']
#     for j in cur_list:
#         if len(j)==1:
#             pass
#         else:
#             max_len = 0
#             max_str = ''
#             for k in cur_list:
#                 if len(k)>=max_len:
#                     max_len=len(k)
#                     max_str = k
#     data_list[index]['value']=[]
#     data_list[index]['value'].append(max_str.upper())
#
#
#
# final_dict = {}
# final_dict['dict']=data_list
# with open('/home/gaozhiwei/Desktop/ximalayadiyiban/chilihou150000.json','w') as f:
#     f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))
# import re
# str = "的唐诗，并邀请了多为6~8岁的孩子来诵读唐诗，用充满稚气、节奏感强的童0-9sui声记在心中。我们还采用了三种朗读模式--听唐诗、读唐诗、背唐"
# if re.search("[0-9年]~[0-9年]", str):
#     list = re.findall("[0-9年][~|-][0-9年]", str)
#     for i in list:
#         cur_str = re.sub("[~|-]","至",i)
#         str = re.sub(i,cur_str,str)
#         print(str)
#     print(list)

# from zhongyinwenchuli import To_chinese4
#
# str = "089"
# data = To_chinese4(int(str))
# print(data)

# import json
# with open("/home/gaozhiwei/Desktop/migutingshuzongziyuan.json") as f:
#     json_data = f.read()
# data = json.loads(json_data)
# list = data['dict']
# final_data = {}
# final_data['dict']=[]
# for i in list:
#     cur_dict = {}
#     cur_dict['majorType']='migu_read_title'
#     cur_dict['minorType']=
#     cur_dict['value']=[]
#     print(i)
# import json
#
# with open("/home/gaozhiwei/Desktop/migutingshu.json") as f:
#     json_src_data = f.read()
#
#
#
# data = json.loads(json_src_data)
# valus_list = data['dict']
# cont_list = []
# for i in valus_list:
#     cur_dict = i
#     cur_value_list = i['value']
#     cur_value_list.append(i['minorType'])
#     cur_dict['value']=list(set(cur_value_list))
#     cont_list.append(cur_dict)
#
# for i in cont_list:
#     print(i)
#
#
# data['dict']= cont_list
#
#
# with open("/home/gaozhiwei/Desktop/migutingshudisanban.json",'w') as f:
#     f.write(json.dumps(data,ensure_ascii=False,indent=1))



# import json,os,time
#
#
#
# # path= "/home/gaozhiwei/Desktop/poetry/"
# #
# # dict = {}
# # dict['dict'] = []
# # for i,j,k in os.walk(path):
# #     print(i)
# #     for l in k:
# #         print(i+l)
# #         with open(i+l) as f:
# #             data = f.read()
# #             data = json.loads(data)
# #             for kk in data:
# #                 print(kk)
# #                 dict['dict'].append(kk)
# #
# # print(len(dict['dict']))
# # with open('/home/gaozhiwei/Desktop/quntangshi.json','w') as f:
# #
# #     f.write(json.dumps(dict,ensure_ascii=False,indent=1))
#
# import re
#
#
# path = "/home/gaozhiwei/Desktop/"
#
# with open(path+"tangshisanbaishou.json",'r') as f:
#     tangs = f.read()
# with open(path+"quantangshi.json",'r') as f:
#     quants = f.read()
#
# ts_list = json.loads(tangs)['dict']
# qt_list = json.loads(quants)['dict']
#
# start = time.time()
# final_dict = {}
# final_dict['dict']=[]
# for i in ts_list:
#     cur_title = i['title']
#     if re.search("/",cur_title):
#         cur_title=re.sub(r"/.+",'',cur_title)
#     cur_title = re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", '', cur_title)
#     if re.search('其[一二三四五六七八九十]',cur_title):
#         cur_str = re.search('其[一二三四五六七八九十]',cur_title).group()
#         cur_title = re.sub("其[一二三四五六七八九十]",cur_str[1],cur_title)
#         # print(cur_title)
#         # print(i)
#     cur_author=i['author'][2:]
#     cur_list = []
#     cur_list.append(i)
#     print(cur_title,cur_author)
#     print(i)
#     for j in qt_list:
#         try:
#             cur_j_title = j['title']
#             cur_j_title = re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", '', cur_j_title)
#             cur_j_author = j['author']
#             # print(cur_j_title,cur_j_author)
#             if cur_title ==cur_j_title and cur_author == cur_j_author:
#                 cur_list.append(j)
#
#             # print(cur_j_author,cur_j_title)
#         except Exception as e:
#             pass
#             # print(j,e)
#             # print('*'*10)
#             # print(e)
#             # print(cur_list)
#     final_dict['dict'].append(cur_list)
#     # print(final_dict['dict'])
# end = time.time()
# with open('/home/gaozhiwei/Desktop/zongffff22.json','w') as f:
#     f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))
# print(end - start,"end",end)
import json

import pymysql


def main():
    conn = pymysql.connect(host="localhost",port=3306,database = "nlpdata",user='root',passwd="gaozhiwei")
    cursor = conn.cursor()
    sql = "select albumtitle from ximalayatwo"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    data_set = set()
    for i in data_list:
        title = i[0]
        data_set.add(title)

    with open("/home/gaozhiwei/Desktop/ximalayaremen.json") as f:
        jsondata = f.read()
    re_data_list = json.loads(jsondata)
    remen_set = set()
    for i in re_data_list['dict']:
        # print(i['minorType'])
        remen_set.add(i['minorType'])
    num = 0
    donthave = []
    for i in remen_set:
        title = i
        if title in data_set:
            num +=1
        else:
            donthave.append(title)
            print(title)

    with open('/home/gaozhiwei/Desktop/ximaremenqushi.json','w') as f:
        f.write(json.dumps(donthave,ensure_ascii=False,indent=1))



    print(len(remen_set))
    print(num)
    print(len(donthave))

def maintest():
    a = 00000000
    b = 12
    c = a+b
    print(str(c).zfill(8))


if __name__ == '__main__':
    # main()
    maintest()
