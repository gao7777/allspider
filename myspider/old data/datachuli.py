#
#
#
#
#
# import pandas as pd
#
#
#
#
#
#
import json
#
#
#
# set_list=set()
# dict_1 = {}
# with open('./5xiaopin.txt','r+') as f:
#     data_list = f.readlines()
#     for i in data_list:
#         set_list.add(i)
#
# with open('./zhefsdfzz.txt','w+') as f:
#     for i in set_list:
#         # print(i)
#         # print(type(i))
#         ddd= eval(i.strip())
#         itemss= ddd.items()
#         itemss = tuple(itemss)
#         print(itemss)
#         dict_1[itemss[0][0]]=itemss[0][1]
#     # print(dict_1.items())
#     with open('./xiaopingz.json','w+') as f:
#         data_json = json.dumps(dict_1,ensure_ascii=False)
#         print(type(data_json))
#         f.write(data_json)
#         # print(ddd.items())
#         # print(type(ddd))
#         # dict_ii = json.dumps(i,ensure_ascii=False)
#         # print(dict_ii)
#         # d = json.loads(dict_ii)
#         # print(d)
#         # print(type(d))
#         # print(dict_ii)
import re
list_1 =['综艺节目','小品','辽宁春晚小品','河南豫剧','二人转','最新相声','开心剧乐部','欢乐喜剧人','热门视频','曲艺大全','春晚小品','微电影','相声大全','民间小调']

with open('./xiaopingz.json','r+') as f:
    data_json = f.read()
    data_json=re.sub('赵本山小品','赵本山',data_json)
    data_json=re.sub('[《|》]+?','',data_json)
    print(data_json)
    data_dict = json.loads(data_json)
    for i in list_1:
        del data_dict[i]
    # print(data_json)
    data_json = json.dumps(data_dict,ensure_ascii=False)
    dict1 = {}
    dict1['name']= list(data_dict.keys())
    dict1_json = json.dumps(dict1,ensure_ascii=False)
    dict2={}
    all_list = []
    j=0
    for i in data_dict.values():
        if i ==None:
            j= j+1
        print(i)
        all_list.extend(i)
    # print(all_list)
    # print(j)
    print(len(all_list))
    all_set= set()
    for i in all_list:
        all_set.add(i)
    print(len(all_set))
    all_list= list(all_set)
    print(all_list)
    j=0
    for i in all_list:
        if i =="":
            all_list.remove(i)

            j=j+1

    print(j)
    dict2['values'] = all_list

    dict2_json = json.dumps(dict2,ensure_ascii=False)

    print(data_json)
    print(dict2_json)
    print(dict1_json)
    with open('/home/gaozhiwei/Desktop/xinping.json','w+') as f:
        f.write(data_json)
    with open('/home/gaozhiwei/Desktop/xinpingname.json', 'w+') as f:
        f.write(dict1_json)
    with open('/home/gaozhiwei/Desktop/xinpingvalue.json','w+') as f:
        f.write(dict2_json)
