import json
import os

from zhengzescriptzuixn import *
def maincollectdata():
    with open("/home/gaozhiwei/Desktop/mifenzongyi.json") as f:
        json_data = f.read()
    filter_data_list = list()
    dict_data_list = json.loads(json_data)
    for i in dict_data_list:
        cur_dict = dict()
        cur_dict['moviename'] = i['name']
        cur_dict['movieyear'] = i['year']
        cur_dict['moviecateName'] = i['cateName']
        cur_dict['movieareaName'] = i['areaName']
        cur_dict['moviedirectors'] = []
        if i.get('directors'):
            for director in i['directors']:
                cur_dict['moviedirectors'].append(director['name'])
        cur_dict['movieperformers'] = []
        if i.get('performers'):
            for performer in i['performers']:
                cur_dict['movieperformers'].append(performer['name'])
        cur_dict['movieannotation'] = i['annotation']
        cur_dict['moviean_id'] = i['_id']
        cur_dict['movieanmergedId'] = i['mergedId']
        filter_data_list.append(cur_dict)
    with open("/home/gaozhiwei/Desktop/mifengzongyiwholedata.json",'w') as f:
        f.write(json.dumps(filter_data_list,ensure_ascii=False,indent=3))

def main():
    with open("/home/gaozhiwei/Desktop/mifengzongyiwholedata.json") as f:
        json_data = f.read()
    src_data_list = json.loads(json_data)
    final_dict = {}
    final_dict['dict'] = []
    movietitle_list = []
    for i in src_data_list:
        movie_title = i['moviename']
        movietitle_list.append(movie_title)
    movietitle_list = list(set(movietitle_list))
    for i in movietitle_list:
        cur_dict = {}
        movie_title = i
        cur_dict['majorType'] = "mifeng_movietitle"
        cur_dict['minorType'] = movie_title
        cur_dict['value'] = []
        handle_i = chinese_num(movie_title)
        handle_i = quchubidian(handle_i)
        # cur_dict['value'].append(i)
        cur_dict['value'].append(handle_i)
        cur_dict['value'] = list(set(cur_dict['value']))
        final_dict['dict'].append(cur_dict)
    with open("/home/gaozhiwei/Desktop/mifengzongyititle.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))

def resourceset():
    with open("/home/gaozhiwei/Desktop/beeVideo_serial_title.json") as f:
        json_data = f.read()
    with open("/home/gaozhiwei/Desktop/mifengdianshijutitle.json") as f:
        mifeng_data = f.read()
    with open("/home/gaozhiwei/Desktop/serial_title.json") as f:
        json_data2 = f.read()
    data2 = json.loads(json_data2)

    mifeng_data= json.loads(mifeng_data)
    # print(mifeng_data)
    data = json.loads(json_data)
    # print(data)
    source_data = data['dict'][0]['value']
    new_data =[i['value'][0] for i in mifeng_data['dict']]
    print(len(source_data))
    # print(new_data)
    # print(len(new_data))
    data2title_list = data2['dict'][0]['value']
    source_data.extend(new_data)
    print(len(source_data))
    print(len(data2title_list))
    source_data.extend(data2title_list)
    print(len(source_data))
    firlter_set = list(set(source_data))
    print(firlter_set)
    print(len(firlter_set))
    for i in firlter_set:
        if len(i) <2:
            print(i)
            firlter_set.remove(i)
    print(len(firlter_set))


    print(type(firlter_set))


    final_dict = dict()
    final_dict['dict']=[]
    cur_dict = dict()
    cur_dict['majorType']='serial_title'
    cur_dict['value']=firlter_set

    final_dict['dict'].append(cur_dict)
    with open('/home/gaozhiwei/Desktop/serial_title717.json','w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=3))

def moviefirter():
    file_name_list = os.listdir("/home/gaozhiwei/Desktop/moviequchongshuju")
    totla_title_list = []
    for i in file_name_list:
        dir_front = "/home/gaozhiwei/Desktop/moviequchongshuju/"
        with open(dir_front+i,'r') as f:
            json_data = f.read()
        title_list = json.loads(json_data)['dict'][0]['value']
        print(len(title_list))
        totla_title_list.extend(title_list)
    print(len(totla_title_list))

    with open('/home/gaozhiwei/Desktop/mifengmovietitle.json') as f:
        json_data= f.read()
    new_data = json.loads(json_data)
    new_data_list = [i['value'][0]for i in new_data['dict']]
    print(new_data_list)
    totla_title_list.extend(new_data_list)
    print(len(totla_title_list))
    totla_title_list= list(set(totla_title_list))
    print(len(totla_title_list))
    for i in totla_title_list:
        if len(i)<2:
            print(i)
    if len(totla_title_list) >20000:
        page = len(totla_title_list)//20000
        yushu = len(totla_title_list)%20000
        if yushu !=0:
            page=page+1
        for i in range(page):
            cur_total_list = totla_title_list[i*20000:(i+1)*20000]
            final_data = dict()
            final_data['dict'] = []
            cur_dict = dict()
            cur_dict['majorType'] = "movie_title"
            cur_dict['value'] = cur_total_list
            final_data['dict'] = cur_dict
            # with open('/home/gaozhiwei/Desktop/movie_title{}717.json'.format(i),'w') as f:
            #     f.write(json.dumps(final_data,ensure_ascii=False,indent=3))
        # print(page,yushu)
    else:
        final_data = dict()
        final_data['dict']=[]
        cur_dict = dict()
        cur_dict['majorType']="movie_title"
        cur_dict['value']=totla_title_list
        final_data['dict']=totla_title_list
        with open('/home/gaozhiwei/Desktop/movie_title717.json','w') as f:
            f.write(json.dumps(final_data,ensure_ascii=False,indent=3))
def variatyfirlter():
    file_name_list = os.listdir("/home/gaozhiwei/Desktop/zongyiquchongshuju")
    totla_title_list = []
    for i in file_name_list:
        dir_front = "/home/gaozhiwei/Desktop/zongyiquchongshuju/"
        with open(dir_front + i, 'r') as f:
            json_data = f.read()
        title_list = json.loads(json_data)['dict'][0]['value']
        print(len(title_list))
        totla_title_list.extend(title_list)
    print(len(totla_title_list))
    with open('/home/gaozhiwei/Desktop/mifengzongyititle.json') as f:
        json_data = f.read()
    new_data = json.loads(json_data)
    new_data_list = [i['value'][0] for i in new_data['dict']]
    print(new_data_list)
    totla_title_list.extend(new_data_list)
    print(len(totla_title_list))
    totla_title_list = list(set(totla_title_list))
    print(len(totla_title_list))
    if len(totla_title_list) > 20000:
        page = len(totla_title_list) // 20000
        yushu = len(totla_title_list) % 20000
        if yushu != 0:
            page = page + 1
        for i in range(page):
            cur_total_list = totla_title_list[i * 20000:(i + 1) * 20000]
            final_data = dict()
            final_data['dict'] = []
            cur_dict = dict()
            cur_dict['majorType'] = "movie_title"
            cur_dict['value'] = cur_total_list
            final_data['dict'] = cur_dict
            print(final_data)
            with open('/home/gaozhiwei/Desktop/varity_title{}717.json'.format(i), 'w') as f:
                f.write(json.dumps(final_data, ensure_ascii=False, indent=3))
        print(page,yushu)
    else:
        final_data = dict()
        final_data['dict'] = []
        cur_dict = dict()
        cur_dict['majorType'] = "variety_title"
        cur_dict['value'] = totla_title_list
        final_data['dict'] = cur_dict
        print('else')
        print(final_data)
        with open('/home/gaozhiwei/Desktop/varity_title717.json', 'w') as f:
            f.write(json.dumps(final_data, ensure_ascii=False, indent=3))
def shaoerfirlter():
    with open('/home/gaozhiwei/Desktop/mifengshaoertitle.json') as f:
        json_data = f.read()
    data= json.loads(json_data)
    final_data= {}
    final_data['dict'] = []
    values_list = [i['value'][0] for i in data['dict']]
    print(values_list)
    print(len(values_list))
    print(len(set(values_list)))
    values_list= list(set(values_list))
    for i in values_list:
        if len(i)<2:
            print(i)
    cur_dict = dict()
    cur_dict['majorType']= "children_title"
    cur_dict['value'] = values_list
    final_data['dict']= cur_dict
    with open("/home/gaozhiwei/Desktop/children_title717.json",'w') as f:
        f.write(json.dumps(final_data,ensure_ascii=False,indent=3))

if __name__ == '__main__':

    # maincollectdata()
    # main()
    # resourceset()
    moviefirter()
    # variatyfirlter()
    # shaoerfirlter()