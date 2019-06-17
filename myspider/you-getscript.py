import os,pymysql
con = pymysql.connect(host='192.168.44.136',port=3306,user='root',password = 'gaozhiwei',database='nlpdata',autocommit=True)
cur = con.cursor()
# sql='select song_title,url_3,id from kuwodata where id>40000 and id<50000'
sql='select song_title,isplay,id from kuwodata where id>0 and id<50000'
sql1 ='update kuwodata set isplay=0 where id=%s'
sql2 ='update kuwodata set isplay=1 where id=%s'
str = "/home/gaozhiwei/kuwomusic/{}.mp3"
data = cur.execute(sql)
data_one = cur.fetchall()
j=0
for i in data_one:
    str1 = str.format(i[0])
    if os.path.exists(str1):
        cur.execute(sql2,i[2])
        j+=1
    else:
        cur.execute(sql1,i[2])
print(j)
# for i in data_one:
#     os_commeng = "you-get -O %s -o '/home/gaozhiwei/kuwomusic' %s"%(str(i[0]),str(i[1]))
#     a= os.system(os_commeng)
#     if a !=0:
#         cur.execute(sql1, i[2])
#         j +=1
#     print(a)
con.close()

# for i in range(10):
#     os_commeng = "you-get -O %s -o '/home/gaozhiwei/kuwomusic' 'http://www.kuwo.cn/yinyue/3381156/'"%(i)
#     a= os.system(os_commeng)

