import csv
import json
import re
import jieba
import pandas as pd
_MAPPING = (
u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九')
_P0 = (u'', u'十', u'百', u'千',u'万')
_S4 = 10 ** 5
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
def Chuling(str1):
    if str1[-1] =='零':
        str1=str1[:-1]
    # re.sub()
    return str1
def Year_to_chinese(num):
    # print(num)
    str =''
    lst1=[]
    # print(lst1)
    while num>10:
        # print(num%10)
        lst1.append(num % 10)
        num = num//10
    lst1.append(num)
    lst1.reverse()
    # print(lst1)
    for i,j in enumerate(lst1):
        str+= _MAPPING[j]
    if re.search("十",str):
        str = re.sub("十","一零",str)
    return str
def Year_to_chinesenew(num):
    str_num = num
    re_str =""
    # print(str_num)
    for i in str_num:
        i=str(int(i))
        re_str+=num_mapgewei[i]
    return re_str

def To_chinese4(num):
    # print(num,'hhhh')
    # assert (0 <= num and num < _S4)
    if not 0<=num and num <_S4:
        return ''
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num // 10
        lst.append(num)
        c = len(lst)  # 位数
        result = ''
        # print(lst)
        try:
            for idx, val in enumerate(lst):
                val = int(val)
                if val != 0:
                    result += _P0[idx] + _MAPPING[val]
                    # print(type(lst[idx - 1]))
                    # print(lst[idx + 1])
                    if idx < c - 1 and lst[idx + 1] == 0:
                        # print(type(lst[idx+1]))
                        # print(lst[idx+1])
                        result += u'零'
                else:
                    pass
                    # result+="零"
            return result[::-1]
        except Exception as e:
            return ''


def quchubidian(str):
    # print(str)

    eng_list = re.findall("[a-zA-Z]+[ ]+[a-zA-Z]+",str)
    if len(eng_list) !=0:
        for i in eng_list:
            # print(i)
            zhanwenhoustr = re.sub(' ',"*",i)
            # print(zhanwenhoustr,'zhdsfaf')
            str=re.sub(i,zhanwenhoustr,str)
            # print(str)
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
    if re.search("℃",str_data):
        list = re.findall("℃", str_data)
        for i in list:
            cur_str = re.sub("℃", "度", i)
            str_data = re.sub(i, cur_str, str_data)
    if re.search("[0-9年][~|-][0-9年]", str_data):
        list = re.findall("[0-9年][~|-][0-9年]", str_data)
        for i in list:
            cur_str = re.sub("[~|-]", "至", i)
            str_data = re.sub(i, cur_str, str_data)
    if re.search("[\d]+[.|.][\d]+",str_data):
        list = re.findall("[\d]+[.|.][\d]+",str_data)
        for i in  list:
            cur_str = re.sub("[.|.]","点",i)
            str_data= re.sub(i,cur_str,str_data)
    if re.search(r"[\d]+[/][\d]+",str_data):
        cur=re.search(r"([\d]+)[/]([\d]+)",str_data)
        str_data=re.sub("[\d]+[/][\d]+",cur.group(2)+"/"+cur.group(1),str_data)
        list = re.findall(r"[\d]+[/][\d]+",str_data)
        for i in  list:
            cur_str = re.sub(r"/","分之",i)
            str_data= re.sub(i,cur_str,str_data)
    num_list = re.findall("\d+", str_data)
    if num_list != []:
        for i in num_list:
            # print(i)
            # print(b,'1')
            if len(i) >= 4:
                # print(i)
                zw_str = Year_to_chinesenew(i)
                # print(zw_str)
                str_data = re.sub(i, zw_str, str_data,count=1)
                # print(b)
            else:
                # print(b)
                zw_str = To_chinese4(int(i))
                str_data = re.sub(i, zw_str, str_data,count=1)
                # print(b,'===xiyuu44')
                # print(num_list)
    return str_data





def migutitle(titlename_list):

    # with open("/home/gaozhiwei/Desktop/authorname_sort_uniq.txt") as f:
    #     json_data = f.readlines()
    # with open("/home/gaozhiwei/Desktop/contentname_sort_uniq.txt") as f:
    #     json_data = f.readlines()
    #
    # for i in json_data:
    #     print(i.strip())
    #
    # dict = json.loads(json_data)['dict']
    # value_list = dict[0]['value']
    final_list = []
    titlename_list = list(set(titlename_list))
    for i in titlename_list:
        i = i.strip()
        source=i
        src_i = i
        i = chinese_num(i)
        i= quchubidian(i)
        if re.search(":",src_i):
            src_i=re.sub(":","：",src_i)
        cur_list = []
        cur_list.append(src_i)
        cur_list.append(i)
        cur_final_list = list(set(cur_list))
        cur_dict={}
        cur_dict['majorType']="migu_read_title"
        cur_dict['minorType']=source
        cur_dict['value']=cur_final_list
        final_list.append(cur_dict)


    for i in final_list:
        print(i)

    final_dict = {}
    final_dict['dict']= []
    final_dict['dict']=final_list
    # final_dict_cur ={}
    # final_dict_cur['majorType'] = "migu_read_author"
    # final_dict_cur['value']= final_list
    # final_dict['dict'].append(final_dict_cur)
    with open("/home/gaozhiwei/Desktop/contentname_sort_uniq629.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))
def miguauthor(author_list):
    author_list= list(set(author_list))
    final_list = []
    for i in author_list:
        cur_list = []
        cur_list.append(i)
        i = chinese_num(i)
        i = quchubidian(i)
        cur_list.append(i)
        cur_list= list(set(cur_list))
        for j in cur_list:
            final_list.append(j)
    final_dict = {}
    final_dict['dict']=[]
    f_dict = {}
    f_dict['majorType'] = "migu_read_author"
    f_dict['value']= final_list
    final_dict['dict'].append(f_dict)
    with open("/home/gaozhiwei/Desktop/authorname_sort_uniq629.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))

def maintest():
    list1 = ['s','f']
    for num in range(3):
        for i in list1:
            if i =='s':
                print(i)
                break

        else:
            print(i+'else')
            print("else")


def mainximalaya():
    with open("/home/gaozhiwei/Desktop/ximalayadiyiban.json",'r') as f:
        json_data = f.read()
    with open("/home/gaozhiwei/Desktop/ximalayaremen.json",'r') as f:
        remen_data = f.read()
    remen_data= json.loads(remen_data)
    remen_data= remen_data['dict']
    data = json.loads(json_data)
    data = data['dict']
    remen_list = []
    title_list  = []
    for i in data:
        title_list.append(i['minorType'])
    for i in remen_data:
        title_list.append(i['minorType'])
        remen_list.append(i['minorType'])
    print(len(title_list))
    print(len(list(set(title_list))))
    title_list= list(set(title_list))
    final_dict ={}
    final_dict['dict'] = []

    for i in title_list:
        for j in remen_data:
            if j['minorType'] == i:
                final_dict['dict'].append(j)
                break
        else:
            cur_dict = {}
            cur_dict['majorType']='question'
            cur_dict['minorType']=i
            value = chinese_num(i)
            value = quchubidian(value)
            cur_dict['value']= [value]
            final_dict['dict'].append(cur_dict)

    print(len(final_dict['dict']))

    with open("/home/gaozhiwei/Desktop/ximalayazhenghe.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))


def migutingshu():
    with open("/home/gaozhiwei/Desktop/apiSearch.txt") as f:
        data = f.readlines()

    title_name= []
    author_name = []
    for i in data:
        i = i.strip()
        if re.match("contentName=(.*)",i):
            contentname = re.match("contentName=(.*)",i).group(1)
            if contentname!= "" and contentname!= None:
                title_name.append(contentname)
        if re.match("author=(.*)",i):
            authorname = re.match("author=(.*)",i).group(1)
            if authorname != "" and authorname!= None:
                author_name.append(authorname)

    miguauthor(author_name)
    migutitle(title_name)


def mainximalayacsv():
    # with open("/home/gaozhiwei/Desktop/ximalaya.csv",encoding='utf-8') as csv_file:
    #     data= csv.reader(csv_file)
    #     print(data)
    #     num = 0
    #     for i in data:
    #         if num >10:
    #             break
    #         else:
    #             num +=1
    #         print(i)
    df = pd.read_csv("/home/gaozhiwei/Desktop/ximalaya.csv")
    df_dict = df.to_dict(orient='list')
    zhuanji_list = df_dict['专辑名称']
    with open("/home/gaozhiwei/Desktop/butong.json") as f:
        chongfu_json = f.read()
    shierwang_list = json.loads(chongfu_json)
    zhuanji_list = shierwang_list
    zhuanji_list = list(set(zhuanji_list))
    print(len(zhuanji_list),'zong')
    final_dict = {}
    final_dict['dict'] = []
    handle_list = []
    for i in zhuanji_list:
        i = str(i)
        try:
            i = i.strip()
        except Exception as e:
            print(i)
        if i =="" or None:
            pass
        else:
            cur_dict = {}
            cur_dict['majorType']="question"
            cur_dict['minorType'] = i
            cur_dict['value'] = []
            handle_i = chinese_num(i)
            handle_i= quchubidian(handle_i)
            handle_list.append(handle_i)
            # cur_dict['value'].append(i)
            cur_dict['value'].append(handle_i)
            cur_dict['value']= list(set(cur_dict['value']))
            final_dict['dict'].append(cur_dict)

    # handle_list_set = set(handle_list)
    # for i in handle_list_set:
    #     count = 0
    #     for j in handle_list:
    #         if i ==j:
    #             count +=1
    #     if count !=1:
    #         print(i,count)
    final_set = set()
    final_dict_roundone = []
    chongfu_list = []
    for i in final_dict['dict']:
        cur_value_list =i['value']
        for value in cur_value_list:
            if value not in final_set:
                final_set.add(value)
                final_dict_roundone.append(i)
            else:
                chongfu_list.append(i)
                print(i)
    print(len(chongfu_list))
    final_dict['dict'] = final_dict_roundone
    print(len(final_dict_roundone))
    final_final_dict_list = []
    for i in final_dict['dict']:
        i['value'].append(i['minorType'])
        i['value'] = list(set(i['value']))
        final_final_dict_list.append(i)
    final_dict['dict'] = final_final_dict_list






    with  open("/home/gaozhiwei/Desktop/ximalayashierwang.json",'w') as f:
        f.write(json.dumps(final_dict,indent=1,ensure_ascii=False))







if __name__ == '__main__':
    # main()
    # maintest()
    # mainximalaya()
    migutingshu()
    # mainximalayacsv()