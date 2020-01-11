import json
import os
import re

from kuwozhengzescript import quchubidian,chinese_num
from zhongyinwenchuli import To_chinese4
import pymysql


def main():
    conn = pymysql.connect(host='qa2.sai.corp',user='semantic_r',password='semantic_resources',database='semantic_resources')
    cur = conn.cursor()
    sql = 'select id,major,minor,value  from dict_music union  select id,major,minor,value  from dict_audio union  select id,major,minor,value from dict_news union  select id,major,minor,value from dict_video;'
    cur.execute(sql)
    data_list = cur.fetchall()
    sql_set = set()
    sql_dict = dict()
    all_data_set = set()
    all_data_dict = dict()
    # dictionary_txt = open('/home/gaozhiwei/Desktop/字典重复的数据.txt','w')
    sql_txt = open('/home/gaozhiwei/Desktop/信源导入的和媒资库重复的数据','w')
    for data in data_list:
        if data[3] not in sql_set:
            sql_set.add(data[3])
            sql_dict[data[3]]=data
        else:
            pass
            # print(data[2])
    path = '/home/gaozhiwei/Desktop/nlpmoshi/semantic-resources/dictionaries'
    for os_path,dirname,files in os.walk(path):
        for filename in files:
            with open(os.path.join(os_path,filename)) as f:
                json_data = f.read()
            # print(filename)
            dict_data = json.loads(json_data)
            cur_dict = dict_data['dict']
            for one_dict in cur_dict:
                values = one_dict['value']
                for two_values in values:
                    # print(two_values)
                    if two_values in sql_set:
                        # print(two_values)
                        # print(one_dict['majorType'])
                        # print(cur_dict)
                        print(two_values,filename)
                        print(sql_dict[two_values])
                        print('='*10)
                        sql_txt.write(two_values+'\r\n'+filename+'\r\n'+json.dumps(sql_dict[two_values],ensure_ascii=False)+'\r\n'+'='*20+'\r\n')
                        # if two_values not in all_data_set:
                        #     all_data_set.add(two_values)
                        #     all_data_dict[two_values]= filename
                        # else:
                        #     # dictionary_txt.write(two_values+filename+'\r\n'+all_data_dict[two_values]+'\r\n'+'='*30+'\r\n')
                        #     print(two_values,filename)
                        #     print(all_data_dict[two_values])
                        #     print('='*30)

    # dictionary_txt.close()
    sql_txt.close()


def xima():
    path = '/home/gaozhiwei/Desktop/nlpmoshi/semantic-resources/dictionaries'
    src_values = set()
    new_set = set()
    final_dict = dict()

    final_dict['dict']=list()
    with open('/home/gaozhiwei/Desktop/ximalayazuixin.txt') as f:
        new_data_list = f.readlines()


    for os_path,dirname,files in os.walk(path):
        for filename in files:
            if re.match('ximalaya',filename):
                # print(filename)
                with open(os.path.join(os_path,filename)) as f:
                    json_data = f.read()

                # # print(filename)
                dict_data = json.loads(json_data)
                cur_dict = dict_data['dict']
                for one_dict in cur_dict:
                    values = one_dict['value']
                    for two_values in values:
                        src_values.add(two_values)
                        # print(two_values)
    for i in new_data_list:
        i= i.strip()
        if i not in src_values and len(i)>=2:
            new_set.add(i)
            print(i)
            filter = quchubidian(i)
            filter = chinese_num(filter)
            print(filter)
            cur_dict=dict()
            cur_dict['majorType']='ximalaya_title'
            cur_dict['minorType']=i
            cur_dict['value']= list()
            if i !=filter:
                cur_dict['value'].append(i)
                cur_dict['value'].append(filter)
            else:
                cur_dict['value'].append(i)
            final_dict['dict'].append(cur_dict)
    with open('/home/gaozhiwei/Desktop/ximaxinzeng.json','w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))
    print(final_dict)

    print(len(new_set))






if __name__ == '__main__':
    # main()
    xima()