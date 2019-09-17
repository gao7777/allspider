import json
import re

from zhengzescriptzuixn import *
def main():
    with open("/home/gaozhiwei/Desktop/Resource.json") as f:
        data = f.readlines()
    final_list = []
    final_list2=[]
    for i in data:
        # print(i)
        cur_dict = i.strip()
        if re.search('"programName":"(.*?)—熊猫天天讲故事"',cur_dict):
            j = re.search('"programName":"(.*?)—熊猫天天讲故事"',cur_dict)
            category_last= j.group(1)
            # print(category_last)
            title = re.search('"title":"(.*?)"',cur_dict)
            title = title.group(1)
            # print(title)
            tags = re.search('"tags":"(.*?)"',cur_dict)
            tags = tags.group(1)
            # print(tags)
            tags_list = tags.split(" ")
            # print(tags_list)
            dict_cur = dict()
            dict_cur['title']= title
            dict_cur['category_last'] = category_last
            dict_cur['tags']= tags_list
            final_list.append(dict_cur)
    for i in final_list:
        # print(i)
        title= i['title']
        if re.search("（微信版）",title):
            # print(title)
            cur_title = re.sub("（微信版）","",title)
            title= cur_title
        if re.search("—",title):
            cur_title = re.sub(".*—?",'',title)
            title = cur_title
        if re.search("【平台】",title):
            cur_title = re.sub("【平台】",'',title)
            title = cur_title
        if re.search("【熊猫天天的好朋友】",title):
            cur_title = re.sub("【熊猫天天的好朋友】",'',title)
            title = cur_title
        i['title']= title.strip()
        if title!='':
            final_list2.append(i)
    # print(len(final_list))
    tags_final_list = list()
    category_last_set = set()
    title_set = set()
    for i in final_list2:
        print(i)
        title= i['title']
        title_set.add(title)
        cur_category_last = i['category_last']
        if cur_category_last!='':
            category_last_set.add(i['category_last'])
        tags_final_list= tags_final_list+i['tags']

    tags_final_set = set(tags_final_list)
    tags_final_set.remove('')
    print(len(final_list2))
    print(len(final_list))
    print(len(title_set))
    print(tags_final_set)
    print(category_last_set)

    final_json_dict = dict()
    final_json_dict['dict']= []
    cur_final_json_dict = dict()
    cur_final_json_dict['majorType']="pandas_categorytwo"
    cur_final_json_dict['value']=list(category_last_set)
    # for i in title_set:
    #     # print(i)
    #     i = chinese_num(i)
    #     i = quchubidian(i)
    #     cur_final_json_dict['value'].append(i)
    print(cur_final_json_dict)
    final_json_dict['dict'].append(cur_final_json_dict)

    with open("/home/gaozhiwei/Desktop/pandasstorycategorytwo.json",'w') as f:
        f.write(json.dumps(final_json_dict,ensure_ascii=False,indent=2))

def test_method():
    import math
    str = None
    tmp_list = list()
    # tmp_list.append(str,'default')
    print(2004/400)
    print(math.floor(2004/400))
    print([['s']*100])
    print(tmp_list)


if __name__ == '__main__':
    # main()
    test_method()