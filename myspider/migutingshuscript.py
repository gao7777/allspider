import re,json,os
from kuwozhengzescript import quchubidian,chinese_num
from zhongyinwenchuli import To_chinese4
num = 0
max = 0
max_name = ""
def zhangjiezhuanhuan(str_data):
    num_list = re.findall("\d+", str_data)
    if num_list != []:
        for i in num_list:
            zw_str = To_chinese4(int(i))
            str_data = re.sub(i, zw_str, str_data)
            # print(b,'===xiyuu44')
            # print(num_list)
    return str_data
def zhanjie_handle(contentid):
    # print(contentid)
    filname = "/home/gaozhiwei/Desktop/migu/data/contents/Content%s.txt"
    flag = os.path.exists(filname%(contentid))
    # if flag==1:
        # print(filname%(contentid))
    with open(filname%(contentid),'r') as f:
        data_list = f.readlines()
    global max
    global max_name
    if len(data_list) > max:
        max = len(data_list)
        max_name = filname%(contentid)
    final_list = []
    for i in data_list:
        # print(i.strip())
        source = i
        cur_str = "\d+#\d+#(.*)"
        # print(cur_str)
        if re.search(cur_str,i.strip()):
            i = re.match(cur_str,i.strip())
            i=i.group(1)
            i = quchubidian(i.strip())
            i = zhangjiezhuanhuan(i)
            # if len(i)<5:
            #     global num
            #     num +=1
            #     print(i)
            #     print(source.strip())

            # print(i)
            final_list.append(i)
        # print(final_list)
    return final_list
    # pass


def main():
    with open("/home/gaozhiwei/Desktop/migu/data/apiSearch.txt") as f:
        list = f.readlines()

    dict_list = []
    dict_list1=[]
    for i in range(0,len(list)):
        if list[i].strip() =="###":
            cur_dict = {}
            # cur_dict1= {}
            index=re.match("[a-zA-Z]+=(.*)",list[i+1].strip()).group(1)
            contentId=re.match("[a-zA-Z]+=(.*)",list[i+2].strip()).group(1)
            contentName=re.match("[a-zA-Z]+=(.*)",list[i+3].strip()).group(1)
            source_contentName = contentName
            author=re.match("[a-zA-Z]+=(.*)",list[i+4].strip()).group(1)
            readerName=re.match("[a-zA-Z]+=(.*)",list[i+5].strip()).group(1)
            shortrecommend=re.match("[a-zA-Z]+=(.*)",list[i+6].strip()).group(1)
            longrecommend=re.match("[a-zA-Z]+=(.*)",list[i+7].strip()).group(1)
            cur_dict['index']=index
            cur_dict['contentId']=contentId
            contentName = quchubidian(contentName)
            contentName = chinese_num(contentName)
            cur_dict['contentName']=contentName.upper()
            author = quchubidian(author)
            author = chinese_num(author)
            cur_dict['author']=author.upper()
            readerName = quchubidian(readerName)
            readerName = chinese_num(readerName)
            cur_dict['readerName']=readerName.upper()
            shortrecommend = quchubidian(shortrecommend)
            shortrecommend = chinese_num(shortrecommend)
            cur_dict['shortrecommend']=shortrecommend.upper()
            longrecommend = quchubidian(longrecommend)
            longrecommend = chinese_num(longrecommend)
            cur_dict['longrecommend']=longrecommend.upper()
            zhangjie_list=zhanjie_handle(contentId)
            cur_dict['chapter'] = zhangjie_list
            # cur_dict1['majorType'] = 'migu_read_title'
            # cur_dict1['minorType'] =source_contentName
            # cur_dict1['value'] = []
            # cur_dict1['value'].append(contentName.upper())
            # dict_list1.append(cur_dict1)
            dict_list.append(cur_dict)

        # print(type(i))
        # print(list[i].strip())

    # print(list)
    # for i in dict_list:
    #     print(i)
    final_dict = {}
    final_dict['dict'] = dict_list
    with open("/home/gaozhiwei/Desktop/hhhdddfss.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))




if __name__ == '__main__':
    main()
    print(max,max_name)
    print(num)