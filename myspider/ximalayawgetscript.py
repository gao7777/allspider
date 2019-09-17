
import json

import pymysql,os
from concurrent.futures import ThreadPoolExecutor, wait
import threading
from DBUtils.PooledDB import PooledDB


def get_mp3(id,albumid,trackid,trackurl,pooldb):
    huizhui = trackurl[-4:]
    cmd = " wget -t 2 --timeout=15 -O  /home/gaozhiwei/Desktop/ximalayamp3test/{} {}"
    updata_sql1 ='update nlpdata.ximalayathere_1 set isplay="1",mp3name={} where id = {}'
    updata_sql2 ='update nlpdata.ximalayathere_1 set isplay="2",mp3name={} where id = {}'
    updata_sql3 ='update nlpdata.ximalayathere_1 set isplay="3",mp3name={} where id = {}'
    mp3name= albumid+'+'+trackid+huizhui
    try:

        flag = os.system(cmd.format(mp3name,trackurl))
        # lock.acquire(timeout=2)
        if flag ==0:
            conn = pooldb.connection()
            cursor = conn.cursor()
            cursor.execute(updata_sql1.format(json.dumps(mp3name),id))
            cursor.close()
            conn.close()
        else:
            conn = pooldb.connection()
            cursor = conn.cursor()
            cursor.execute(updata_sql2.format(json.dumps(mp3name),id))
            cursor.close()
            conn.close()
    except Exception as e:
        print(e,'e'*1000)
        conn = pooldb.connection()
        cursor = conn.cursor()
        cursor.execute(updata_sql3.format(json.dumps(mp3name), id))
        cursor.close()
        conn.close()


def main():
    db_config = {
        "host":"localhost",
        "database":"nlpdata",
        'user':'root',
        'password':"gaozhiwei",
        "autocommit":True,
        "charset":"utf8"
    }
    pooldb = PooledDB(creator=pymysql,maxconnections=30,mincached=5,**db_config)
    conn_main = pooldb.connection()
    cursor_main = conn_main.cursor()
    select_sql = 'select id,albumid,trackid,trackplayurl from nlpdata.ximalayathere_1 xima where xima.id >1200 and id<1400 and xima.trackplayurl is not null'
    cursor_main.execute(select_sql)
    data_list = cursor_main.fetchall()
    # print(len(data_list))
    executer = ThreadPoolExecutor(max_workers=30)

    task_list = [executer.submit(get_mp3,*i,pooldb) for i in data_list]
    wait(task_list)
    cursor_main.close()
    conn_main.close()



if __name__ == '__main__':
    main()