# from math import ceil
# allData = 10516136
# dataOfEach = 10000
# batch = ceil(allData / dataOfEach)
# print(batch)
import json
import random
import re
# with open('/home/gaozhiwei/Desktop/search_datasix1.json') as f:
#     for i in f:
#         # print(json.loads(i))
#         print(i)


# list_test =["6172934047989787860", "3754990154023337689", "8832091840866486980"]
# list =["6172934047989787860", "3754990154023337689", "8832091840866486980",'s','fasf','234452345324564']
# for i in list:
#     if i in list_test:
#         print(i)


# str1 = "fasdfsadf(fasf)"
#
#
# try:
#     a = str1.index('(')
#     str1 = str1[:a]
#     print(a)
# except Exception as e:
#     pass
#
# print(str1)
# str1 =",导演:,J·C·尚多尔,编剧:,马克·鲍尔,/,J·C·尚多尔,主演:,本·" \
#       "阿弗莱克,/,查理·汉纳姆,/,佩德罗·帕斯卡,/,奥斯卡·伊萨克,/,亚德里亚·霍纳,/,加内特·赫德兰,/,希拉·凡德,/,雷纳尔多·加列戈斯,森·奎恩,/,卡洛斯·利纳雷斯,类型:,动作,/,犯罪,/,冒险,制片国家/地区:,美国,语言:,英语,/,西班牙语,/,葡萄牙语,上映日期:,2019-03-13(美国),片长:,125分钟,又名:,三重边界(台),/,三重国境,"
# insex = str1.index('地区')
# print(insex)
# str1 =str1[insex:]
# print(str1)
# str1=re.search(':,([\u4e00-\u9fa5]*),',str1)
# print(str1.group(1))
# print(type(str1.group(1)))
# insex = str1.index('语言')
# print(insex)
# str1 =str1[insex:]
# print(str1)
# str1=re.search(':,([\u4e00-\u9fa5]*),',str1)
# print(str1.group(1))
# print(type(str1.group(1)))
# import requests
# url = " http://tpv.daxiangdaili.com/ip/?tid=558847662461809&num=100  "
# response = requests.request('get',url)
# str = response.text
# # print(response.content)
# # print(type(response.text))
# ip_list = str.split('\r\n')
# print(ip_list)

# import re
# import json
# with open('./myspider/kugouhtml/80后专属情歌.html','r+') as f:
#     con = f.read()
#     # print(con)
#     data = re.search('var jsonm = {"stat":200,"musiclist":(.+}])?',con)
#     dict_data= data.group(1)
#     print(dict_data)
#     print(type(dict_data))
#     dict_data= json.loads(dict_data)
#     print(type(dict_data))


# import pathlib
# import os
# # i=pathlib.Path("/home/gaozhiwei/Destop")
# # print(i.is_dir())
# i = os.path.exists("/home/gaozhiwei/Deskop")
# print(i)
# import requests
# DEFAULT_REQUEST_HEADERS ={
# "Accept-Encoding": "identity;q=1, *;q=0",
# "chrome-proxy":"frfr",
# "Range": "bytes=0-",
# "Referer":"http://fm.caixin.com/m/goodmor/",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
#     }
# responsr = requests.get("https://videoapi.caixin.com/vmsRedis/api/getaudio.jsp?aid=25623&cid=15224&ff=.mp3",headers=DEFAULT_REQUEST_HEADERS)
# print(responsr.content)

# list_json =None
# with open("./100data.json",'r') as f:
#     a=f.read()
#     b = json.loads(a)
#     list_json=b
# print(b)
# o=0
# for i in list_json:
#     # print(i)
#     o+=1
# print(o)
#
# import os,re
# list_final = []
# list1= os.listdir('/home/gaozhiwei/Desktop/dd')
# j = 0
# n= 0
# for i in list1:
#     a = re.match('(.+?)15[5|4]',i)
#     file_date=a.group(1)
#     for j in list_json:
#         json_date = j['date']
#         json_date=re.sub('-','',json_date)
#         mid_jsondata=re.match('(\d\d\d\d)(.)(.*)',json_date)
#         if mid_jsondata.group(2)=="0":
#             # print(mid_jsondata.group(1))
#             # print(type(mid_jsondata.group(1)))
#             json_date=mid_jsondata.group(1)+mid_jsondata.group(3)
#         # print(json_date)
#
#         if json_date == file_date:
#             n+=1
#             tem ={}
#             tem['title']=j['title']
#             tem['date']= j['date']
#             tem['filedate'] = file_date
#             list_final.append(tem)
#             # print(json_date)
#             # print(file_date)
#             # print("=" * 10)
#             str_title_original = '/home/gaozhiwei/Desktop/dd/{}'.format(i)
#             str_title="/home/gaozhiwei/Desktop/dd/{}".format(tem['date'])
#             os.rename(str_title_original,str_title)
# list_final_json = json.dumps(list_final,ensure_ascii=False)
#
# with open('./finalzhanghong.json','w') as f:
#     f.write(list_final_json)
# print(list_final)
#
# print(n)
#
# from selenium import webdriver
#
# import time
#
# url = 'https://system.address'
#
#
# def login():
#     '''先定义一个正常登录的方法，获取登录前和登录后的cookie'''
#
#     driver = webdriver.Chrome()
#
#     driver.get(url)
#     driver.maximize_window()
#     cookieBefore = driver.get_cookies()
#     # 打印登录前的cookie
#     print(cookieBefore)
#     time.sleep(2)
#     driver.find_element_by_id("new-username").clear()
#     driver.find_element_by_id("new-username").send_keys("username")
#     driver.implicitly_wait(5)
#     driver.find_element_by_id("new-password").clear()
#     driver.find_element_by_id("new-password").send_keys("password")
#     driver.find_element_by_id('home-right-login').click()
#     driver.implicitly_wait(5)
#     # 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
#     time.sleep(5)
#     print("登录后！")
#     cookiesAfter = driver.get_cookies()
#     print("cookiesAfter:")
#     print(cookiesAfter)
#     # cookie 存放到了list,其中是dict
#     # 对比发现登录后的cookie比登录前多了4个dict。
#     # 如下代码分别是  1、4 、7、 8
#     len1 = len(cookiesAfter)
#     print("len:%d" %len1)
#     cookie1 = cookiesAfter[0]
#     cookie2 = cookiesAfter[3]
#     cookie3 = cookiesAfter[-2]
#     cookie4 = cookiesAfter[-1]
#     print("cookie1:%s" %cookie1)
#     print("cookie2:%s" %cookie2)
#     print("cookie3:%s" %cookie3)
#     print("cookie4:%s" %cookie4)
#     driver.quit()
#     # 将获取的这四个cookie作为参数，传递给，使用cookie登录的函数，如下
#     cookieLogin(cookie1,cookie2,cookie3,cookie4)
# def cookieLogin(cookie1,cookie2,cookie3,cookie4):
#     print("+++++++++++++++++++++++++")
#     print("cookieLogin")
#     print("cookie2:%s" % cookie2)
#     print("cookie4:%s" % cookie4)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     # 清除一下cookie
#     driver.delete_all_cookies()
#     time.sleep(3)
#     driver.get(url)
#     # 打开浏览器后添加访问地址后，添加cookie
#     driver.add_cookie(cookie1)
#     driver.add_cookie(cookie2)
#     driver.add_cookie(cookie3)
#     driver.add_cookie(cookie4)
#     print("cookies")
#     # 打印一下cookie,与上面正常登录的cookie对比一下
#     print(driver.get_cookies())
#     time.sleep(5)
#     # 刷新页面，可以看到已经是登录状态了，至此完成的使用cookie 的登录。
#     driver.refresh()
#     time.sleep(5)
#     driver.quit()
#
#
# if __name__ == "__main__":
#
#     login()
# import re,json
#
# f1= open('./filter(1).txt','r',encoding='utf-8')
# f2= open('./only_title(1).txt','r',encoding='utf-8')
# data_dict = dict()
# data_dict["dict"]=[]
#
# for i in range(5974):
#     cur_dict = dict()
#     cur_dict["majorType"]="question"
#     cur_dict["minorType"]=None
#     cur_dict["value"]=[]
#     data1 = f1.readline()
#     data2 = f2.readline()
#     data1 = re.match('contentName:(.+)',data1)
#     data1= data1.group(1)
#     data2=data2.strip()
#     # print(data2,'data2')
#     data2 = re.search('contentName=(.+)',data2)
#     data2= data2.group(1)
#     cur_dict["minorType"]=data2
#     cur_dict["value"].append(data1)
#     data_dict["dict"].append(cur_dict)
# print(data_dict)
#     # print(data1,data2)
# f1.close()
# f2.close()
# json_data = json.dumps(data_dict,ensure_ascii=False)
# with open('./filter_data.json','w') as f:
#     f.write(json_data)
# import re,json
# from ximalayazhengze import quchubidian,chinese_num
#
# with open('./finalximalaya.json','r') as f:
#     json_data = f.read()
# json_dict = json.loads(json_data)
# dict_list = json_dict['dict']
# data_list =[]
# for i in dict_list:
#     data_list.append(i['minorType'])
# with open('./test.txt','r') as f:
#     hot_list = f.readlines()
# extend_list = []
# num =0
# hot_list=list(set(hot_list))
# for i in hot_list:
#     if i.strip() in data_list:
#         pass
#     else:
#         num +=1
#         # print(i.strip())
#         # print(i.strip())
#         cur_dict = dict()
#         data_str = i.strip()
#         # str.find()
#         cur_dict['resource'] = i.strip()
#         # hhh= re.search('\[.+\]|＜.+＞|\{.+\}|<.+>|【.+】|\(.+\)|《.+》|:.+',data_str)
#         # if hhh:
#         #     print(data_str)
#         #     num+=1
#         data = re.search('\[.+\]', data_str)
#         if data:
#             cur_str = re.search('\[.+\]', data_str)
#             cur_dict['[]'] = cur_str.group()
#             # print(cur_str.group())
#         data = re.search('\{.+\}', data_str)
#         if data:
#             data_str = re.sub('\{.+\}', '', data_str)
#             # print(cur_str)
#         data = re.search('＜.+＞', data_str)
#         if data:
#             data_str = re.sub('＜.+＞', '', data_str)
#             # print(cur_str)
#         data = re.search('<.+>', data_str)
#         if data:
#             cur_str = re.search('<.+>', data_str)
#             cur_dict['<.+>'] = cur_str.group()
#         data = re.search('【.+】', data_str)
#         if data:
#             cur_str = re.search('【.+】', data_str)
#             cur_dict['【】'] = cur_str.group()
#         data = re.search('\(.+\)', data_str)
#         if data:
#             data_str = re.sub('\(.+\)', '', data_str)
#             # cur_dict['【】']=cur_str.group()
#         data = re.search('《.+》', data_str)
#         if data:
#             cur_str = re.search('《.+》', data_str)
#             cur_dict['《》'] = cur_str.group()
#             # cur_dict['【】']=cur_str.group()
#             # print(cur_dict['《》'])
#         data = re.search(' ', data_str)
#         if data:
#             # num+=1
#             # print(data_str)
#             cur_list = data_str.split(' ')
#             cur_dict['spacesplit'] = cur_list
#             # print(cur_list)
#
#         data = re.search(':', data_str)
#         if data:
#             # print(data_str)
#             cur_list = data_str.split(':')
#             cur_dict[':split'] = cur_list
#             # print(cur_list)
#         data = re.search('：', data_str)
#         if data:
#             # print(data_str)
#             cur_list = data_str.split('：')
#             cur_dict['：split'] = cur_list
#             # print(cur_list)
#         # Todo
#         cur_dict['final'] = data_str
#         if cur_dict.keys():
#             extend_list.append(cur_dict)
# extend_listtwo = []
# for i in extend_list:
#     newcur_dict = dict()
#     newcur_dict[i['resource']] = []
#     for j in i.values():
#         if isinstance(j,list):
#             for k in j:
#                 k = quchubidian(k).strip()
#                 # print(j)
#                 k = chinese_num(k)
#                 if k !='':
#                     newcur_dict[i['resource']].append(k)
#         else:
#             j = quchubidian(j).strip()
#             # print(j)
#             j = chinese_num(j)
#             if j != '':
#                 newcur_dict[i['resource']].append(j)
#     extend_listtwo.append(newcur_dict)
# finaldict = {}
# finaldict['dict']=[]
# testnum =0
# for i in extend_listtwo:
#     # print(i)
#     testnum+=1
#     cur_dict = {}
#     cur_dict['majorType'] = 'question'
#     cur_dict['minorType'] = list(i.keys())[0]
#     cur_dict['value'] = []
#     for j in list(i.values())[0]:
#         if j !='':
#             cur_dict['value'].append(j)
#     cur_dict['value']=list(set(cur_dict['value']))
#     finaldict['dict'].append(cur_dict)
# testtestnum = 0
# with open('/home/gaozhiwei/Desktop/shujuqingxifinal.json','r') as f:
#     hh_json = f.read()
# hh_dict = json.loads(hh_json)
#
#
# for i in finaldict['dict']:
#     testtestnum+=1
#     hh_dict['dict'].append(i)
#     print(i)
#
# json_da = json.dumps(hh_dict, ensure_ascii=False)
# print(testnum)
# print(num)
# print(testtestnum)
# with open('./tianjiahou.json','w') as f:
#     f.write(json_da)
# list = ['s','d','dsss']
# for i,j in enumerate(list):
#     print(i)
#     print(j)
# import re
#
# str = " gafg ffg     fadsf发达发 fadsf"
#
# data = re.findall("[a-zA-Z]+[ ]+[a-zA-Z]+",str)
#
# # print(len(data.group()))
# print(len(data))
#
# for i in data:
#     jj=re.sub(' ',"*",i)
#     print(jj)
#     print(i+'ddd')
# def quchubidian(str):
#     # print(str)
#
#     eng_list = re.findall("[a-zA-Z]+[ ]+[a-zA-Z]+",str)
#     if len(eng_list) !=0:
#         for i in eng_list:
#             print(i)
#             zhanwenhoustr = re.sub(' ',"*",i)
#             print(zhanwenhoustr,'zhdsfaf')
#             str=re.sub(i,zhanwenhoustr,str)
#             print(str)
#         if re.search('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a*]',str):
#             str=re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a*]", '', str)
#             print(str)
#         str=re.sub("\*"," ",str)
#     else:
#         if re.search('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]',str):
#             str=re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", '', str)
#     if re.search('丨',str):
#         str = re.sub('丨','',str)
#     return str.upper()
# #
# # def main():
# #     str = "发达散发dddFD    FDFfa 发噶"
# #     # print(str)
# #     res = quchubidian(str)
# #     print(res)
# # if __name__ == '__main__':
# #     main()
#
#
# import json,re
#
#
# with open("/home/gaozhiwei/Desktop/zongffff22.json") as f:
#     json_data = f.read()
#
#
#
# dict_data = json.loads(json_data)
# num =0
# final_dict = {}
# final_dict['dict'] = []
# for i in dict_data['dict']:
#     if len(i) == 2:
#         if re.search("\(.+\)", i[0]['content']):
#             print(i)
#             num += 1
#             final_dict['dict'].append(i)
#
#
# print(num)
#
#
# with open('/home/gaozhiwei/Desktop/duochongbiaoda.json','w') as f:
#     f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))


# import re,json
#
#
# with open("/home/gaozhiwei/Desktop/haixian_0.json",'rb') as f:
#     num =0
#     list11 = []
#     while True:
#         data = f.readline()
#         if data and num<10:
#
#             str_data = data.decode("gbk")
#             print(type(str_data))
#             print(str_data.strip().encode("utf-8"))
#             num +=1
#             list11.append(str_data.strip())
#             # print(data.decode("gbk"))
#         else:
#             with open("./jjj.json",'w') as f:
#                 f.write(json.dumps(list11,ensure_ascii=False,indent=1))
#             break

# print(data.decode("gbk"))


# print(data.decode("gbk"))
# num = 0
# for i in data:
#     num+=1
#     print(i.decode("gbk"))
#
# print(num)
# print(data[0].strip())


import re,json


# with open("/home/gaozhiwei/Desktop/caipubuchong.json") as f:
#     data1 = f.read()
# with open("/home/gaozhiwei/Desktop/caipubuchongdierban.json") as f:
#     data2 = f.read()
#
# data1 = json.loads(data1)
# final_dict = {}
# final_dict['dict']=[]
# num = 0
# for i in data1['dict']:
#     if i['step'] !='':
#         final_dict['dict'].append(i)
# data2 = json.loads(data2)
# for i in data2['dict']:
#     if i['step']!='':
#         final_dict['dict'].append(i)
#
# # final_dict['dict']= list(set(final_dict['dict']))
# print(len(final_dict['dict']))
#
# with open("/home/gaozhiwei/Desktop/finalcaipu596.json") as f:
#
#     final_data= f.read()
#
# with open("/home/gaozhiwei/Desktop/caipu.json") as f:
#
#     total_data = f.read()
#
# he_list = []
# total_data=json.loads(total_data)
# final_data=json.loads(final_data)
# num=0
# for i in total_data:
#     # print(i['content'])
#     # print(type(i['content']))
#     j = json.loads(i['content'])
#     for k in final_data['dict']:
#         print(k)
#         if k['name']==i['key_word']:
#             num +=1
#             j['stepPicture_url']=k['img_list']
#             j['step']=[k['step']]
#             i['content']=json.dumps(j,ensure_ascii=False)
#             he_list.append(i)
# print(len(he_list))
#
#
# with open("/home/gaozhiwei/Desktop/Helist.json",'w') as f:
#     f.write(json.dumps(he_list,ensure_ascii=False,indent=1))
#         # print(type(j))
#         # print(j)
#         # print(j['step'])
#         # print(i['key_word'])
#
# print(num)
import time

from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import threading

def pringstr(str,two):
    try:
        print('start',str)
        dd= 1/0
        a = random.randint(2,5)
        print(a,'aaaaaaa')
        print(threading.enumerate())
        time.sleep(a)
        assert a==2
        print('end',str)
    except Exception as e:
        print(e)
        print("dfsfsf")
def main():
    # str_list = ["a","b","c"]
    str_list = [str(i) for i in range(2)]
    # with  ThreadPoolExecutor(5) as execute:
    execute = ThreadPoolExecutor(max_workers=1)
        # for each in str_list:
        #     execute.submit(pringstr,each,"ffsf")
        #     # execute.map(pringstr,str_list)
        # print("dfsfsfs")
    all_task = [execute.submit(pringstr,i,i) for i in str_list]

    wait(all_task,return_when=ALL_COMPLETED)
    print("finish")
def maintest():
    a = random.randint(10,20)
    print(a)


if __name__ == '__main__':
    main()
    # maintest()








