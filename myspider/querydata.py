import gc
import json
import time

import pymysql as MySQLdb  # 这里是python3  如果你是python2.x的话，import MySQLdb

# 数据库连接属性
from math import ceil

host = '127.0.0.1'
usr = 'root'
passwd = 'gaozhiwei'
db = 'nlpdata'
def sql_slect(row):
    merchant_id=row[3]
    query = row[1]
    # print(merchant_id)
    data_dict = row[2]
    data_dict = json.loads(data_dict)
    # print(type(data_dict))
    # print(data_dict)
    data_list = data_dict['result']
    rerutn_list = []
    for answer in data_list:
        if answer['code'] == 0:
            if 'domain' in answer:
                if 'data' in answer:
                    # print(answer)
                    domain = answer['domain']
                    data = answer['data']
                    if 'parameters' in data:
                        parameter = data['parameters']
                        if parameter:
                            list = []
                            list.append(query.strip())
                            list.append(json.dumps(parameter, ensure_ascii=False).strip())
                            list.append(domain.strip())
                            list.append(merchant_id.strip())
                            tuple_data = tuple(list)
                            rerutn_list.append(tuple_data)
    # print(rerutn_list)
    return rerutn_list


    # for i in xie_data:
    # print(i)
    # print('dgga')


    # cur.executemany(sql1, xie_data)
    # # conn.commit()
    # # print('xie',xie_data)
    # print('ddd')
    # IDctrl += 1
    # gc.collect()
    # time.sleep(0.5)
def sql_slecttwo(row):
    merchant_id=row[3]
    query = row[1]
    # print(merchant_id)
    data_dict = row[2]
    data_dict = json.loads(data_dict)
    # print(type(data_dict))
    # print(data_dict)
    data_list = data_dict['result']
    rerutn_list = []
    for answer in data_list:
        if answer['code'] == 0:
            if 'domain' in answer:
                if 'data' in answer:
                    # print(answer)
                    domain = answer['domain']
                    data = answer['data']
                    if 'parameters' in data:
                        parameter = data['parameters']
                        if parameter:
                            list = []
                            list.append(query.strip())
                            list.append(json.dumps(parameter, ensure_ascii=False).strip())
                            list.append(domain.strip())
                            list.append(merchant_id.strip())
                            tuple_data = tuple(list)
                            rerutn_list.append(tuple_data)
    # print(rerutn_list)
    return rerutn_list


    # for i in xie_data:
    # print(i)
    # print('dgga')


    # cur.executemany(sql1, xie_data)
    # # conn.commit()
    # # print('xie',xie_data)
    # print('ddd')
    # IDctrl += 1
    # gc.collect()
    # time.sleep(0.5)
# 总共多少数据
allData = 10516136
# 每个批次多少条数据
dataOfEach = 10000
# 批次
batch = ceil(allData / dataOfEach)

# 文件名
global IDctrl
IDctrl = 0

# 连接数据库
conn = MySQLdb.connect(host=host, user=usr, password=passwd, database=db,autocommit=True)
cur = conn.cursor()
# cur1 = conn.cursor()

while IDctrl < batch:
    # 读取数据库
    print(IDctrl)
    # sql = 'SELECT ver,query,data FROM record where ID > '+str(IDctrl*10000) +'and id <='+str(IDctrl*10000+dataOfEach)+';'
    sql = 'SELECT ver,query,data,merchant_id FROM record where id > {} and id <{} and ver=2;'
    # sql = 'SELECT ver,query,data FROM record where ID > 0 and id <10000;'
    # sql1 ='INSERT  INTO search_data (query,parameters,domain) values (%s,%s,%s);'
    sql1 ='INSERT  INTO search_datanine (query,parameters,domain,merchant_id) values (%s,%s,%s,%s);'
    sql2 ='INSERT  INTO search_dataeight (query,parameters,domain,merchant_id) values (%s,%s,%s,%s);'
    merchant_id_list = ["6172934047989787860", "3754990154023337689", "8832091840866486980",]
    print(sql.format(str(IDctrl * 10000), str((IDctrl + 1) * 10000)))
    cur.execute(sql.format(str(IDctrl*10000),str((IDctrl+1)*10000)))
    rows = cur.fetchall()
    xie_data = []
    xie_data1 = []
    for row in rows:
        merchant_id = row[3]
        # print(type(merchant_id))
        if merchant_id not in merchant_id_list:
            return_list = sql_slect(row)
            xie_data.extend(return_list)
        else:
            return_list = sql_slecttwo(row)
            xie_data1.extend(return_list)

        # query = row[1]
        # print(merchant_id)
        # data_dict = row[2]
        # data_dict = json.loads(data_dict)
        # # print(type(data_dict))
        # # print(data_dict)
        # data_list = data_dict['result']
        # for answer in data_list:
        #     if answer['code']==0:
        #         if 'domain' in answer:
        #             if 'data' in answer:
        #             # print(answer)
        #                 domain = answer['domain']
        #                 data = answer['data']
        #                 if 'parameters' in data:
        #                     parameter = data['parameters']
        #                     if parameter:
        #                         list = []
        #                         list.append(query.strip())
        #                         list.append(json.dumps(parameter,ensure_ascii=False).strip())
        #                         list.append(domain.strip())
        #                         tuple_data = tuple(list)
        #                         # print(parameter,'parameter')

    # for i in xie_data1:
    #     print(i)
    #     print('dgga')
    cur.executemany(sql1,xie_data)
    cur.executemany(sql2,xie_data1)
    # conn.commit()
    # print('xie',xie_data)
    print('ddd')
    IDctrl += 1
    gc.collect()
    time.sleep(0.5)


# 关闭数据库连接
# f.close()
conn.close()