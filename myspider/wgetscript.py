import json

import pymysql,os



# # cmd =" wget -O  /home/gaozhiwei/Downloads/fssfs.m4a http://audio.xmcdn.com/group26/M06/9A/5B/wKgJRlkDPAOybtpvAAsj_M3hkRg791.m4a"
# cmd =" ffplay http://audio.xmcdn.com/group26/M06/9A/5B/wKgJRlkDPAOybtpvAAsj_M3hkRg791.m4a"
# # keyicmd = "wget -O  /home/gaozhiwei/Downloads/keyi.m4a http://audio.xmcdn.com/group28/M01/5A/23/wKgJSFlElDezulHLAAwsTV9X1n4593.m4a"
# keyicmd = "ffplay http://audio.xmcdn.com/group28/M01/5A/23/wKgJSFlElDezulHLAAwsTV9X1n4593.m4a"
# aaa = os.system(cmd)
# print(aaa)
#
# bbb = os.system(keyicmd)
# print(bbb)
#
# aaa = os.popen(cmd)
# print(aaa)
#
# bbb = os.popen(keyicmd)
# print(bbb)



# def main():
#     conn = pymysql.connect(host="localhost", database="nlpdata", user='root', password='gaozhiwei',
#                            autocommit=True)
#     cursor = conn.cursor()
#     sql = "select id,category,title ,url_mp3 from qiankuntingshu"
#     sql_update = "update qiankuntingshu set isplay='1' where id={};"
#     sql_updateone = "update qiankuntingshu set mp3name={} where id={};"
#     cmd =" wget -O  /home/gaozhiwei/Downloads/xiaohua/{} {}"
#     f= open("/home/gaozhiwei/Desktop/xiazaiflag.txt",'a')
#
#     cursor.execute(sql)
#     data_list = cursor.fetchall()
#     # data_list= data_list[265:266]
#     for i in data_list:
#         name = i[1]+i[2]
#         print(i)
#         # print(name,i[3])
#         url = i[3]
#         # print(type(url))
#         if url:
#             huizhui = url[-4:]
#             finalname = name +str(huizhui)
#             # print(finalname)
#             down_url = cmd.format(finalname,url)
#             # print(down_url)
#             flag = os.system(down_url)
#             # print(flag)
#             # print(type(flag))
#             if flag ==0:
#                 cur_updateurl = sql_update.format(i[0])
#                 cur_updateurlone= sql_updateone.format(json.dumps(finalname,ensure_ascii=False),i[0])
#                 cursor.execute(cur_updateurl)
#                 # print(cur_updateurlone)
#                 cursor.execute(cur_updateurlone)
#             f.write(str(flag)+url+'\n')
#
#     f.close()


def set_mp3name():
    pass


def main():
    conn = pymysql.connect(host="localhost", database="nlpdata", user='root', password='gaozhiwei',
                           autocommit=True)
    cursor = conn.cursor()
    quchongsql = 'select trackplayurl from nlpdata.ximalayathere_1'
    cursor.execute(quchongsql)
    data_list = cursor.fetchall()
    data_set = set(data_list)
    print(len(data_set))
    for i in range(10):
        print(data_set[i])
    # print(len(data_list))
    # tuple1 = ((1),("11"),("111","111"))
    # tuple12= ((1),("11"),("111",'111'))
    # set_test = set()
    # set_test.add(tuple1)
    # set_test.add(tuple12)
    # print(set_test)
    # sql_update = "update qiankuntingshu set isplay='1' where id={};"
    # sql_updateone = "update qiankuntingshu set mp3name={} where id={};"
    # cmd = " wget -O  /home/gaozhiwei/Downloads/xiaohua/{} {}"
    cmd = " wget -O  /home/gaozhiwei/Desktop/ximalayamp3test/{} {}"
    # f = open("/home/gaozhiwei/Desktop/ximalayamp3test.txt", 'a')

    # cursor.execute(sql)
    # data_list = cursor.fetchall()
    # data_set = set()
    # num = 0
    # for i in data_list:
    #     url = i[0]
    #     if url != None:
    #         num+=1
    #         if url not in data_set:
    #             data_set.add(url)
    #         else:
    #             print(url)
    # print(len(data_set))
    # print(num)
    # print(num - len(data_set))
    # url= "https://fdfs.xmcdn.com/group45/M00/B5/29/wKgKlFuUbzLCqxjvAGRcZs7xLXk420.m4a"
    # flag = os.system(cmd.format("test1",url))
    # print(type(flag))
    # print(flag)
    # for i in data_list:
    #     name = i[1] + i[2]
    #     print(i)
    #     # print(name,i[3])
    #     url = i[3]
    #     # print(type(url))
    #     if url:
    #         huizhui = url[-4:]
    #         finalname = name + str(huizhui)
    #         # print(finalname)
    #         down_url = cmd.format(finalname, url)
    #         # print(down_url)
    #         flag = os.system(down_url)
    #         # print(flag)
    #         # print(type(flag))
    #         if flag == 0:
    #             cur_updateurl = sql_update.format(i[0])
    #             cur_updateurlone = sql_updateone.format(json.dumps(finalname, ensure_ascii=False), i[0])
    #             cursor.execute(cur_updateurl)
    #             # print(cur_updateurlone)
    #             cursor.execute(cur_updateurlone)
    #         f.write(str(flag) + url + '\n')

    # f.close()

def maintest():
    tuple_test = (1,"d","fsf")
    print(*tuple_test)
    list_test = ['1',2,"fsfsf"]
    print(*list_test)

if __name__ == '__main__':
    # main()
    maintest()