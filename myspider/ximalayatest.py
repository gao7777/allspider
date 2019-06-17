



import json
import re,pymysql
from zhongyinwenchuli import Year_to_chinese,To_chinese4
def quchubidian(str):
    # print(str)

    eng_list = re.findall("[a-zA-Z]+[ ]+[a-zA-Z]+",str)
    if len(eng_list) !=0:
        for i in eng_list:
            zhanwenhoustr = re.sub(' ',"*",i)
            str=re.sub(i,zhanwenhoustr,str)
        if re.search('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a*]',str):
            str=re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a*]", '', str)
        str=re.sub("\*"," ",str)
    else:
        if re.search('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]',str):
            str=re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", '', str)
    if re.search('丨',str):
        str = re.sub('丨','',str)
    return str.upper()
def chinese_num(str_data):
    num_list = re.findall("\d+", str_data)
    if num_list != []:
        for i in num_list:
            # print(i)
            # print(b,'1')
            if len(i) == 4:
                # print(i)
                zw_str = Year_to_chinese(int(i))
                # print(zw_str)
                str_data = re.sub(i, zw_str, str_data)
                # print(b)
            else:
                # print(b)
                zw_str = To_chinese4(int(i))
                str_data = re.sub(i, zw_str, str_data)
                # print(b,'===xiyuu44')
                # print(num_list)
    return str_data
def ximalayachuli(data_str):
    cur_dict={}
    data = re.search('\[.+\]', data_str)
    if data:
        cur_str = re.search('\[.+\]', data_str)
        cur_dict['[]'] = cur_str.group()
        # print(cur_str.group())
    data = re.search('\{.+\}', data_str)
    if data:
        data_str = re.sub('\{.+\}', '', data_str)
        # print(cur_str)
    data = re.search('＜.+＞', data_str)
    if data:
        data_str = re.sub('＜.+＞', '', data_str)
        # print(cur_str)
    data = re.search('<.+>', data_str)
    if data:
        cur_str = re.search('<.+>', data_str)
        cur_dict['<.+>'] = cur_str.group()
        # print(cur_str.group())
    # data = re.search('丨', data_str)
    # if data:
    #     data_str = re.sub('丨','',data_str)
    data = re.search('【.+】', data_str)
    if data:
        cur_str = re.search('【.+】', data_str)
        cur_dict['【】'] = cur_str.group()
    data = re.search('\(.+\)', data_str)
    if data:
        data_str = re.sub('\(.+\)', '', data_str)
        # cur_dict['【】']=cur_str.group()
    data = re.search('（.+）', data_str)
    if data:
        data_str = re.sub('（.+）', '', data_str)
        # cur_dict['【】']=cur_str.group()
    data = re.search('《.+》', data_str)
    if data:
        cur_str = re.search('《.+》', data_str)
        cur_dict['《》'] = cur_str.group()
        # cur_dict['【】']=cur_str.group()
        # print(cur_dict['《》'])
    data = re.search(' ', data_str)
    if data:
        # num+=1
        # print(data_str)
        cur_list = data_str.split(' ')
        cur_dict['spacesplit'] = cur_list
        # print(cur_list)

    data = re.search(':', data_str)
    if data:
        # print(data_str)
        cur_list = data_str.split(':')
        cur_dict[':split'] = cur_list
        # print(cur_list)
    data = re.search('：', data_str)
    if data:
        # print(data_str)
        cur_list = data_str.split('：')
        cur_dict['：split'] = cur_list
        # print(cur_list)
    # Todo
    cur_dict['final'] = data_str
    cur_final_list = []
    for i in cur_dict.values():
        if isinstance(i,list):
            for j in i:
                j=quchubidian(j)
                j=chinese_num(j)
                if j!='':
                    cur_final_list.append(j.upper())
        else:
            i = quchubidian(i).strip()
            i = chinese_num(i)
            if i !='':
                cur_final_list.append(i.upper())
    return cur_final_list
with open('./ximalayaremen.txt','r') as f:
    datalist = f.readlines()


i = len(datalist)
print(i)
datalist = list(set(datalist))
j = len(datalist)
print(j)
for i in datalist:
    i = ximalayachuli(i.strip())
    # print(i)
finalxima_dict = {}
finalxima_dict['dict'] =[]
for i in datalist:
    cur_dict = {}
    cur_dict['majorType'] = 'question'
    cur_dict['minorType'] = i.strip()
    res_list = ximalayachuli(i.strip())
    cur_dict['value'] = list(set(res_list))
    finalxima_dict['dict'].append(cur_dict)
print(len(finalxima_dict['dict']))
with open('/home/gaozhiwei/Desktop/hhhhsfs.json','w') as f:
    f.write(json.dumps(finalxima_dict,ensure_ascii=False,indent=1))



