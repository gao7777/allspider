import datetime
import json
import os
import re
import time

import pymysql


def log_filter():
    local_date = (datetime.datetime.today() + datetime.timedelta(-3)).strftime("%Y-%m-%d")
    print(local_date)
    file_path = "/home/gaozhiwei/hugoserverlog/%shugo.log" % (local_date)
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='halo_media', password="3edc#EDC",
                                           database='halo_media_resources')
    cursor_k8s = conn_k8s.cursor()
    media_resources_conn = pymysql.connect(host='k8s-nfs.sai.corp', user='halo_media', password="3edc#EDC",
                                           database='halo_media_resources')
    media_cursor = media_resources_conn.cursor()
    sql_insert_hugo_log = "insert into halo_media_resources.hugo_log(user_id, device_id,dialogue_id,user_device_id,ip,merchant_id,domain,query,artist,title, album, type, engine,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_insert_userid = "insert into halo_media_resources.user(user_id) values (%s);"
    sql_insert_useraction = "insert into halo_media_resources.user_action(dialogue_id, user_id, song, action_type, log_date, song_id) VALUES (%s,%s,%s,%s,%s,%s)"
    sql_insert_musiccollection = "insert into babel_recommender_system.music_collection_new(user_id, song, orider_times) VALUES (%s,%s,%s)"
    sql_update_musiccollection = "update music_collection set babel_recommender_system.music_info.order_times = '%s' where id = %s"
    # update_timestamp_sql = "update hugo_log set hugo_log.timestamp = '%s' where id =%s"
    sql_select_user_id = "select user_id from halo_media_resources.user;"
    sql_select_song_list = "select raw_song,song_id from babel_recommender_system.music;"
    sql_select_music_collention = 'select song from music_collection'
    media_sql_select = "select id,name from halo_media_resources.song;"
    media_cursor.execute(media_sql_select)
    media_data_list = media_cursor.fetchall()
    song_title_total_map = dict()
    media_song_name_map = dict()
    for i in media_data_list:
        # print(i)
        id = i[0]
        name = i[1]
        media_song_name_map[name] = id
    song_title_total_map_xinzeng_title = set()
    userid_total_set = set()
    musiccollect_insert_sql_list = list()
    musiccollect_update_sql_list = list()
    user_insert_sql_list = list()
    user_action__insert_sql_list = list()
    # cursor_k8s.execute(sql_select_song_list)
    # song_list = cursor_k8s.fetchall()
    # song_list = list()
    # for i in song_list:
    #     raw_song = i[0]
    #     song_id = i[1]
    #     if raw_song not in song_title_total_map.keys():
    #         song_title_total_map[raw_song] = song_id
    cursor_k8s.execute(sql_select_user_id)
    userid_list = cursor_k8s.fetchall()
    for i in userid_list:
        cur_userid = i[0]
        userid_total_set.add(cur_userid)
    # cursor_k8s.execute(sql_select_music_collention)
    # song_collection_list = cursor_k8s.fetchall()
    # for i in song_collection_list:
    #     cur_collect_song = i[0]
    #     song_title_total_map_xinzeng_title.add(cur_collect_song)
    final_insert_hugolog_list = list()
    base_hugo_path = '/home/gaozhiwei/hugoserverlog/'
    filenames = os.listdir(base_hugo_path)
    # log_list = list()
    with open(file_path) as f:
        log_list = f.readlines()

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
                                    # print(music_title,'music_title')
                                    # print(song_title_total_map.keys()[0])
                                    cur_musiccollect_list.append('1')
                                    musiccollect_insert_sql_list.append(cur_musiccollect_list)
                                    song_title_total_map_xinzeng_title.add(music_title)

                                cur_useraction_list = list()
                                cur_useraction_list.append(music_dialogId)
                                cur_useraction_list.append(music_userid)
                                if music_title is not None:
                                    try:
                                        cur_song_json_list = json.loads(music_title)
                                        cur_song_str = ','.join(cur_song_json_list)
                                    except:
                                        cur_song_str = None
                                else:
                                    cur_song_str = None
                                cur_useraction_list.append(cur_song_str)
                                cur_useraction_list.append("music")
                                cur_useraction_list.append(cur_insert_timestamp)
                                # song_id deal
                                if music_title is not None:
                                    cur_muedia_music_title = json.loads(music_title)[0]
                                else:
                                    cur_muedia_music_title = None
                                # cur_useraction_song_id = song_title_total_map.get(music_title,None)
                                # print(cur_muedia_music_title,'musictitle')

                                cur_useraction_song_id = media_song_name_map.get(cur_muedia_music_title, None)
                                if cur_useraction_song_id is not None:
                                    cur_useraction_song_id = str(cur_useraction_song_id)
                                # if cur_useraction_song_id is not None:
                                # print(cur_useraction_song_id,'uuuuuuusongid')
                                cur_useraction_list.append(cur_useraction_song_id)
                                user_action__insert_sql_list.append(cur_useraction_list)

    # cursor_k8s.executemany(sql_insert_hugo_log, final_insert_hugolog_list)
    # cursor_k8s.executemany(sql_insert_userid,user_insert_sql_list)
    # cursor_k8s.executemany(sql_insert_useraction,user_action__insert_sql_list)
    # cursor_k8s.executemany(sql_insert_musiccollection,musiccollect_insert_sql_list)
    print("finish")
    #
    # conn_k8s.commit()




def main():
    log_filter()


if __name__ == '__main__':
    main()
    # log_filter()
