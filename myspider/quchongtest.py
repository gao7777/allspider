import pymysql

def main():
    conn = pymysql.connect(host='52.80.70.220',port=3306,user='root',password='gaozhiwei',autocommit=True)
    print('ww')
    cursor = conn.cursor()
    sql = 'select id,trackname,trackplayurl,isplay from nlpdata.ximalayathere_1 where isplay !="0"'
    data_list = cursor.execute(sql)
    data_list= cursor.fetchall()
    trackplayurl_set = set()

    for i in data_list:
        # id = i[0]
        # trackname = i[1]
        trackplayurl= i[2]
        isplay = i[3]
        # print(isplay)
        # print(type(isplay))
        # print(trackplayurl)
        if trackplayurl is not None:
            if trackplayurl not in trackplayurl_set:
                trackplayurl_set.add(trackplayurl)
                # print(isplay)

    print(len(trackplayurl_set))


    # print(len(data_list))




if __name__ == '__main__':
    main()