import json
import re,pymysql
from zhongyinwenchuli import Year_to_chinese,To_chinese4
def quchubidian(str):
    if re.search("[0-9年]~[0-9年]", str):
        list = re.findall("[0-9年][~|-][0-9年]", str)
        for i in list:
            cur_str = re.sub("[~|-]", "至", i)
            str = re.sub(i, cur_str, str)
    if re.search('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]',str):
        str=re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", '', str)
    if re.search('丨',str):
        str = re.sub('丨','',str)
    return str
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

def main():
    with open('/home/gaozhiwei/Desktop/kuwozuixin5.29.json','r') as f:
        data = f.read()
    data = json.loads(data)
    data_list = data['dict']
    cur_dict = {}
    cur_dict['dict'] =[]
    for i in data_list:
        tem_dict = {}
        song_name = i['song']
        song_name = song_name.upper()
        song_name = quchubidian(song_name)
        song_name= chinese_num(song_name)
        singer_name = i['singer']
        singer_name = singer_name.upper()
        tem_dict['song'] = song_name
        tem_dict['singer']=singer_name
        cur_dict['dict'].append(tem_dict)
    with open('/home/gaozhiwei/Desktop/kuwofilter5.29.json','w') as f:
        final_json_data = json.dumps(cur_dict,ensure_ascii=False,indent=1)
        f.write(final_json_data)







if __name__ == '__main__':
    main()
