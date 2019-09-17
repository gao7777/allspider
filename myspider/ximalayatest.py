import json
import re,pymysql

def main():
    conn = pymysql.connect(host='52.80.70.220', port=3306, user='root', password='gaozhiwei', database='nlpdata',
                           autocommit=True, charset='utf8')
    cursor = conn.cursor()
    # sql_two = "select albumid from ximalayatwo_1 "
    sql = " insert into nlpdata.ximalayaremen select * from nlpdata.ximalayathere_1 where albumid={}"
    with open("/home/gaozhiwei/Desktop/ximalayaremen.json") as f:
        json_data = f.read()
    data_list = json.loads(json_data)['dict']
    data_set = set()
    for i in data_list:
        cur_list = []
        cur_list.append(i['album_url'])
        cur_list.append(i['album_title'])
        cur_list.append(i['album_id'])
        data_set.add(tuple(cur_list))
    print(len(data_set))
    print(len(data_list))
    album_id_set= set()
    for i in data_set:
        album_id_set.add(i[2])
    for i in album_id_set:
        try:
            cursor.execute(sql.format(i))
            print(i)
        except Exception as e:
            print(e)
            print("false album_id",i)
    # db_config = {
    #     "host": "52.80.70.220",
    #     "database":"nlpdata",
    #     'user':'root',
    #     'password':"gaozhiwei",
    #     "autocommit":True,
    #     "charset": "utf8"
    # }
    # pooldb = PooledDB(creator=pymysql, maxconnections=11, mincached=5, **db_config)
    # executer = ThreadPoolExecutor(max_workers=10)
    # task_list = [executer.submit(sql_excuter,i,pooldb) for i in album_id_set]
    # wait(task_list)



if __name__ == '__main__':
    main()



