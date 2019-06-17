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



def main():
    conn = pymysql.connect(host="localhost", database="nlpdata", user='root', password='gaozhiwei',
                           autocommit=True)
    cursor = conn.cursor()
    sql = "select id,category,title ,url_mp3 from qiankuntingshu"
    sql_update = "update qiankuntingshu set isplay='1' where id={};"
    sql_updateone = "update qiankuntingshu set mp3name={} where id={};"
    cmd =" wget -O  /home/gaozhiwei/Downloads/xiaohua/{} {}"
    f= open("/home/gaozhiwei/Desktop/xiazaiflag.txt",'a')

    cursor.execute(sql)
    data_list = cursor.fetchall()
    # data_list= data_list[265:266]
    for i in data_list:
        name = i[1]+i[2]
        print(i)
        # print(name,i[3])
        url = i[3]
        # print(type(url))
        if url:
            huizhui = url[-4:]
            finalname = name +str(huizhui)
            # print(finalname)
            down_url = cmd.format(finalname,url)
            # print(down_url)
            flag = os.system(down_url)
            # print(flag)
            # print(type(flag))
            if flag ==0:
                cur_updateurl = sql_update.format(i[0])
                cur_updateurlone= sql_updateone.format(json.dumps(finalname,ensure_ascii=False),i[0])
                cursor.execute(cur_updateurl)
                # print(cur_updateurlone)
                cursor.execute(cur_updateurlone)
            f.write(str(flag)+url+'\n')

    f.close()





if __name__ == '__main__':
    main()