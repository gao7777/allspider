import json
import re

import pandas as pd
import pymysql

num_mapgewei={
    "0":"零",
    "1":"一",
    "2":"二",
    "3":"三",
    "4":"四",
    "5":"五",
    "6":"六",
    "7":"七",
    "8":"八",
    "9":"九"
}
def Year_to_chinesenew(num):
    str_num = num
    re_str =""
    # print(str_num)
    for i in str_num:
        i=str(int(i))
        re_str+=num_mapgewei[i]
    return re_str
def chinese_num(str_data):
    num_list = re.findall("\d+", str_data)
    if num_list != []:
        # print(num_list)
        for i in num_list:
            # print(i)
            # print(b,'1')
            if len(i) >= 1:
                # print(i)
                zw_str = Year_to_chinesenew(i)
                # print(zw_str)
                str_data = re.sub(i, zw_str, str_data,count=1)
                # print(b)
            # else:
            #     # print(b)
            #     zw_str = To_chinese4(int(i))
            #     str_data = re.sub(i, zw_str, str_data,count=1)
            #     # print(b,'===xiyuu44')
            #     # print(num_list)
        # print(str_data)
    return str_data
def main():
    category_dict = {
        '1':"可回收垃圾",
        '2':"有害垃圾",
        '3':"湿垃圾",
        '4':"干垃圾"
    }
    zhongwen_dict= {
        'dry_garbage':'干垃圾',
        'wet_garbage':'湿垃圾',
        'recyclable':'可回收垃圾',
        'harmful_waste':'有害垃圾'
    }
    yingwenchiuli_dict = {
        '干垃圾': 'dry_garbage',
        '湿垃圾': 'wet_garbage',
        '可回收垃圾': 'recyclable',
        '有害垃圾': 'harmful_waste'
    }
    data_list = []
    with open("/home/gaozhiwei/Desktop/garbage.txt") as f:
        txt_data= f.readlines()
    for i in txt_data:
        # print(i)
        cur_str = i.strip()
        cur_str= re.sub(r"{\t}*"," ",cur_str)
        cur_data_list = cur_str.split("\t")
        # print(cur_data_list)
        cur_dict = dict()
        cur_dict[cur_data_list[0]]=cur_data_list[1]
        # cur_dict[cur_data_list[1]]
        data_list.append(cur_dict)
    # for i in data_list:
    #     print(i,'ddddd')
    df=pd.read_csv("/home/gaozhiwei/Desktop/product.csv")
    data= df.head(100000)
    data_dict = df.to_dict()
    # print(data_dict)
    name = data_dict['name']
    sortId = data_dict['sortId']
    # print(sortId)
    # print(name)
    # print(data)
    for i in name:
        # print(name[i])
        # print(sortId[i])
        cur_dict = dict()
        category = category_dict[str(sortId[i])]
        cur_dict[name[i]]=category
        data_list.append(cur_dict)
    # for i in data_list:
    #     print(i)

    dftwo=pd.read_csv("/home/gaozhiwei/Desktop/trash_info.csv")
    data_dict_two= dftwo.to_dict()
    # print(data_dict_two)
    keys1= data_dict_two['1号电池']
    keys2 = data_dict_two['有害垃圾']
    for i in keys1:
        # print(keys1[i])
        name = keys1[i]
        category= keys2[i]
        # print(keys2[i])
        cur_dict=dict()
        if category=='可回收物':
            category="可回收垃圾"
        if category in ['可回收垃圾','有害垃圾','湿垃圾','干垃圾']:
            cur_dict[name]=category
            # print(cur_dict)
            data_list.append(cur_dict)


    # conn = pymysql.connect(host='word-segment2.sai.corp', user='root', password="root",
    #              database='skill_data', port=3306,charset='utf8')
    # cursor = conn.cursor()
    # # sql = 'select * from t_commond_skillgarbage'
    # sql = "select * from t_commond_skill t where t.domain = 'garbage';"
    # cursor.execute(sql)
    # sql_data_list = cursor.fetchall()
    # for i in sql_data_list:
    #     print(i)
    #     name = i[2]
    #     category= i[4]
    #     category= json.loads(category)
    #     print(category,'categoryyyyyy')
    #     # for j in category:
    #         # print(j)
    #     cur_dict = dict()
    #     cur_dict[name]= category[0]
    #     # print(cur_dict)
    #     data_list.append(cur_dict)
    # print(len(data_list))

    quchong_set = set()
    final_list = list()
    chongfushuju= list()
    for i in data_list:
        # print(i.keys())
        cur_keys = i.keys()
        # print(cur_keys)
        for j in cur_keys:
            # print(j)
            src_j = j
            j= j.upper()
            j= chinese_num(j)
            if j not in quchong_set:
                quchong_set.add(j)
                cur_dict= dict()
                cur_dict[j]= i[src_j]
                final_list.append(cur_dict)
            else:
                # print(i,'kkkkkkk')
                cur_dict=dict()
                cur_dict[j]=i[src_j]
                for k in final_list:
                    if list(k.keys())[0]==j:
                        key1 = k[j]
                        key2 = i[src_j]
                        if key1 in zhongwen_dict.keys():
                            key1 = zhongwen_dict[key1]
                        if key2 in zhongwen_dict.keys():
                            key2 = zhongwen_dict[key2]
                        if key1 != key2:
                            # print(j)
                            cur_diff_dict= dict()
                            cur_diff_dict[j]=[key1,key2]
                            print(cur_diff_dict)
                            chongfushuju.append(cur_diff_dict)
                            # print(j,key1,key2,'llll')

                # print(cur_dict)
        # print(type(i.keys()))
    print(len(quchong_set))
    print(len(final_list))
    print(len(data_list))
    # for i in final_list:
    #     print(i,'fffffff')

    # with open('/home/gaozhiwei/Desktop/lajifenleinew810.json','w') as f:
    #     f.write(json.dumps(final_list,ensure_ascii=False,indent=2))
    with open('/home/gaozhiwei/Desktop/lajidiff.json', 'w') as f:
        f.write(json.dumps(chongfushuju,ensure_ascii=False,indent=2))



if __name__ == '__main__':
    main()