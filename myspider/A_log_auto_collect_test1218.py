import datetime
import json
import os
import re
import time
import pytz
from ftplib import FTP,FTP_TLS

import pymysql


def log_filter():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql_insert_hugo_log = "insert into hugo_log_new(user_id, device_id,dialogue_id,user_device_id,ip,merchant_id,domain,query,artist,title, album, type, engine,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_insert_userid = "insert into babel_recommender_system.user(user_id) values (%s);"
    sql_insert_useraction = "insert into user_action_new(dialogue_id, user_id, song, action_type, log_date, song_id) VALUES (%s,%s,%s,%s,%s,%s)"
    sql_insert_musiccollection = "insert into babel_recommender_system.music_collection_new(user_id, song, orider_times) VALUES (%s,%s,%s)"
    sql_update_musiccollection = "update music_collection set babel_recommender_system.music_info.order_times = '%s' where id = %s"
    # update_timestamp_sql = "update hugo_log set hugo_log.timestamp = '%s' where id =%s"
    sql_select_user_id = "select user_id from babel_recommender_system.user;"
    sql_select_song_list = "select raw_song,song_id from babel_recommender_system.music;"
    sql_select_music_collention = 'select song from music_collection'
    song_title_total_map = dict()
    song_title_total_map_xinzeng_title = set()
    userid_total_set = set()
    musiccollect_insert_sql_list = list()
    musiccollect_update_sql_list = list()
    user_insert_sql_list = list()
    user_action__insert_sql_list = list()
    cursor_k8s.execute(sql_select_song_list)
    song_list = cursor_k8s.fetchall()
    for i in song_list:
        raw_song = i[0]
        song_id = i[1]
        if raw_song not in song_title_total_map.keys():
            song_title_total_map[raw_song] = song_id
    cursor_k8s.execute(sql_select_user_id)
    userid_list  = cursor_k8s.fetchall()
    for i in userid_list:
        cur_userid = i[0]
        userid_total_set.add(cur_userid)
    cursor_k8s.execute(sql_select_music_collention)
    song_collection_list = cursor_k8s.fetchall()
    for i in song_collection_list:
        cur_collect_song= i[0]
        song_title_total_map_xinzeng_title.add(cur_collect_song)
    final_insert_hugolog_list = list()
    base_hugo_path = '/home/gaozhiwei/hugoserverlog/'
    filenames = os.listdir(base_hugo_path)
    # log_list = list()
    print('sss')
    with open("/home/gaozhiwei/hugo-server1218.log") as f:
        log_list = f.readlines()
    # for i in log_lines:
    #     print(i)

    num = 0
    dialogId_set = set()
    deviceId_set = set()
    device_test_list = [
        "bookOfFamily_test",
        "playcontrol_test",
        "videosearch_test",
        "home_switch_test",
        "dictionary_test",
        "photoalbum_test",
        "calculator_test",
        "microphone_test",
        "yangguang_test",
        "migu_read_test",
        "bjyidong_test",
        "lineLine_test",
        "relation_test",
        "cookbook_test",
        "ximalaya_test",
        "shengyin_test",
        "babybus_test",
        "address_test",
        "variety_test",
        "cartoon_test",
        "badcase_test",
        "huangli_test",
        "zipCode_test",
        "workout_test",
        "synonym_test",
        "collect_test",
        "control_test",
        "garbage_test",
        "weather_test",
        "camera_test",
        "serial_test",
        "koudai_test",
        "common_test",
        "speaker0920",
        "yidong_test",
        "volume_test",
        "power_test",
        "movie_test",
        "music_test",
        "huilv_test",
        "alarm_test",
        "wangle2233",
        "audio_test",
        "phone_test",
        "wunuo_test",
        "stock_test",
        "deviceId1",
        "news_test",
        "lrts_test",
        "chat_test",
        "joke_test",
        "poem_test",
        "time_test",
        "home_test",
        "TV_test",
        "fm_test",
        "wangle",
        "monitor.bcloud.zabbix-server",
        "hugov3bcloud.zabbix-server"
    ]
    parameter_set = set()
    for log in log_list:
        # print(log.strip())
        record_src = re.search('record (.*)', log.strip())
        if record_src is not None:
            record = record_src.group(1)
            record_dict = json.loads(record)
            # print(record_dict)
            # record_query = record_dict['query']
            userid = record_dict.get('userId')
            ip = record_dict.get('ip')
            # dialogId = record_dict.get('dialogId')
            merchantId = record_dict.get('merchantId')
            deviceId = record_dict.get("deviceId")
            if deviceId is not None and deviceId not in device_test_list and re.match("monitor.bcloud|hugov3bcloud",
                                                                                      deviceId) is None:
                deviceId_set.add(deviceId)
                if userid is not None:
                    record_result = record_dict['result']
                    dialogId = record_dict['dialogId']
                    # dialogId_set.add(dialogId)
                    for cur_record_dict in record_result:
                        # print(cur_record_dict['selected'])
                        if cur_record_dict['selected'] == True:
                            # print(cur_record_dict['domain'])
                            # print(cur_record_dict)
                            cur_record_data = cur_record_dict['data']
                            # print(cur_record_dict.keys())
                            cur_data_dict = json.loads(cur_record_data)
                            fin_engine = cur_record_dict.get('engine', None)
                            fin_query = cur_record_dict['query']
                            fin_source = cur_record_dict['source']
                            fin_domain = cur_record_dict['domain']
                            parameters = cur_data_dict.get('parameters')
                            answer = cur_data_dict.get("answer")
                            if fin_domain == "music":
                                log_timestamp = re.match("\[(.*?)\]", log.strip()).group(1)
                                cur_timestamp = datetime.datetime.strptime(log_timestamp, "%Y-%m-%d %H:%M:%S,%f")
                                local_timestamp = int(time.mktime(
                                    cur_timestamp.timetuple()) * 1000.0 + cur_timestamp.microsecond / 1000.0)
                                cur_insert_timestamp = str(local_timestamp)
                                # print(cur_insert_timestamp)
                                num += 1
                                music_userid = userid
                                music_parameters = parameters
                                music_answer = answer
                                music_deviceId = deviceId
                                music_ip = ip
                                music_dialogId = dialogId
                                music_merchantId = merchantId
                                music_engine = fin_engine
                                music_fin_source = fin_source
                                music_query = fin_query
                                music_domain = fin_domain
                                for i in parameters.keys():
                                    parameter_set.add(i)
                                music_type = music_parameters.get("tags", None)
                                music_album = music_parameters.get("album", None)
                                music_title = music_parameters.get("title", None)
                                if music_title is not None:
                                    music_title = json.dumps(music_title, ensure_ascii=False)
                                music_artist = music_parameters.get("artist", None)
                                if music_artist is not None:
                                    music_artist = json.dumps(music_artist, ensure_ascii=False)
                                cur_list = list()
                                cur_list.append(music_userid)
                                cur_list.append(music_deviceId)
                                cur_list.append(music_dialogId)
                                cur_list.append(music_deviceId)
                                cur_list.append(music_ip)
                                cur_list.append(music_merchantId)
                                cur_list.append(music_domain)
                                cur_list.append(music_query)
                                cur_list.append(music_artist)
                                cur_list.append(music_title)
                                cur_list.append(music_album)
                                cur_list.append(music_type)
                                cur_list.append(music_engine)
                                cur_list.append(cur_insert_timestamp)
                                final_insert_hugolog_list.append(cur_list)
                                if music_userid not in userid_total_set:
                                    cur_userid_list = list()
                                    cur_userid_list.append(music_userid)
                                    user_insert_sql_list.append(cur_userid_list)
                                    userid_total_set.add(music_userid)
                                if music_title not in song_title_total_map.keys() and music_title not in song_title_total_map_xinzeng_title:
                                    cur_musiccollect_list = list()
                                    cur_musiccollect_list.append(music_userid)
                                    cur_musiccollect_list.append(music_title)
                                    cur_musiccollect_list.append('1')
                                    musiccollect_insert_sql_list.append(cur_musiccollect_list)
                                    song_title_total_map_xinzeng_title.add(music_title)

                                cur_useraction_list = list()
                                cur_useraction_list.append(music_dialogId)
                                cur_useraction_list.append(music_userid)
                                cur_useraction_list.append(music_title)
                                cur_useraction_list.append("music")
                                cur_useraction_list.append(cur_insert_timestamp)
                                cur_useraction_song_id = song_title_total_map.get(music_title,None)
                                cur_useraction_list.append(cur_useraction_song_id)
                                user_action__insert_sql_list.append(cur_useraction_list)





    # for i in final_insert_hugolog_list:
    #     print(i)
    # for i in userid_total_set:
    #     print(i)
    # for i,j in song_title_total_map.items():
    #     print(i,j)
    # for i in user_insert_sql_list:
    #     print(i)
    # for i in musiccollect_insert_sql_list:
    #     print(i)
    # for i in user_action__insert_sql_list:
    #     print(i)
    cursor_k8s.executemany(sql_insert_hugo_log, final_insert_hugolog_list)
    cursor_k8s.executemany(sql_insert_userid,user_insert_sql_list)
    cursor_k8s.executemany(sql_insert_useraction,user_action__insert_sql_list)
    cursor_k8s.executemany(sql_insert_musiccollection,musiccollect_insert_sql_list)

    conn_k8s.commit()
    # sort_deviceId_set = sorted(deviceId_set,key=lambda i:len(i),reverse=True)
    # for i in sort_deviceId_set:
    #     print(i)
    # print(len(deviceId_set))

    # print(parameter_set)
    # print(num)

def main():
    ftp = FTP()
    FTPIP= "47.94.108.110 "
    FTPPORT= 21
    USERNAME= "ftpuser"
    USERPWD= "kHVFBW53Wz"
    ftp.connect(FTPIP,FTPPORT)
    ftp.login(USERNAME,USERPWD)
    ftp.set_pasv(1)
    welcome = ftp.getwelcome()
    print(welcome,'welcome')
    hugo_path ="/nas/data/babel/logs/nlp-prod/hugo-server/"
    ftp.cwd(hugo_path)
    dir_names = ftp.nlst('/nas/data/babel/logs/nlp-prod/hugo-server/')
    dir_name = dir_names[-1]
    ftp.cwd(dir_name)
    file_names = ftp.nlst()
    # print(file_names)
    # fileHandler=open('/home/gaozhiwei/hugoserverlog/huge.log','wb').write
    # filename = 'hugo-server.log'
    # code = ftp.retrbinary('RETR hugo-server.log' , fileHandler, 10240 )
    # print(file_names)
    pytz.timezone('Asia/Shanghai')
    local_date = datetime.datetime.today().strftime("%Y-%m-%d")
    print(local_date)
    for i in file_names:
        if re.match("hugo-server-"+local_date+".*.log.gz",i):
            cur_file_path = "/home/gaozhiwei/hugoserverlog/"+i
            cur_fileHandler=open(cur_file_path,'wb').write
            code = ftp.retrbinary('RETR %s'%(i) , cur_fileHandler, 10240)
            # print(code)
            # print(i)
    ftp.close()
    log_filter(local_date)

if __name__ == '__main__':
    # main()
    log_filter()