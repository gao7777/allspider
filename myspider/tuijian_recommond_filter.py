import json
import math
import os
import re
import time

import pymysql
from datetime import datetime


def main():
    string_8_id_src = "00000000"
    conn_music = pymysql.connect(host='music.sai.corp', user='root', password="root",
                                 database='saimusic')
    conn_local = pymysql.connect(host='localhost', user='root', password='gaozhiwei', database='recommondsystem')
    cursor_local = conn_local.cursor()
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    cursor_music = conn_music.cursor()
    sql_music_singer = 'select * from saimusic.singer'
    sql_music_tag = 'select * from saimusic.tag'
    sql_music_song = 'select id,name, singer_id, source_id, play_time, link, path, create_time, update_time from saimusic.song'
    sql_k8s_singer_insert = "insert into babel_recommender_system.singer(singer_id,name,gender) values (%s,%s,%s)"
    sql_k8s_song_insert = "insert into babel_recommender_system.music(raw_song, publish_time, audio_url, source_id,create_time,update_time,singer_id,album) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_k8s_tag_insert = "insert into babel_recommender_system.tag(name) values (%s)"
    sql_k8s_song = "select id,source_id from babel_recommender_system.music "
    sql_local_music = 'select id,song_id, song, singer_id, source_id, play_time, create_time, update_time, album, publish_time, netease_source_id from recommondsystem.music'
    sql_local_musicinfo = 'select id,song_id, hot_comment_number, comment_number from recommondsystem.music_info'
    sql_insert_k8s_musicinfo = "insert into babel_recommender_system.music_info(song_id, hot_commont_number, commont_number) values (%s,%s,%s)"
    sql_music_song_tag = "select song_id,tag_id from saimusic.song_tag"
    sql_insert_k8s_song_tag = "insert into babel_recommender_system.song_tag(song_id, tag_id) VALUES (%s,%s)"
    sql_select_k8s_song_album = "select distinct album from babel_recommender_system.music"
    sql_insert_k8s_album = "insert into album(name) VALUES (%s)"
    sql_update_k8s_music = "update music set babel_recommender_system.music.song_id = '{}' where id = {}"
    sql_select_musci_k8s = "select id,raw_song from babel_recommender_system.music"

    # singer 处理
    # cursor_music.execute(sql_music_singer)
    # data_list = cursor_music.fetchall()
    # insert_singer_list = list()
    # test_set = set()
    # for data in data_list:
    #     id = data[0]
    #     string_id = str(id).zfill(8)
    #     cur_gender = str(data[2])
    #     cur_list = list()
    #     cur_list.append(string_id)
    #     cur_list.append(str(data[1]))
    #     cur_list.append(cur_gender)
    #     insert_singer_list.append(tuple(cur_list))
    #     # print(cur_list)
    # cursor_k8s.executemany(sql_k8s_singer_insert,insert_singer_list)
    # conn_k8s.commit()
    # tag 处理
    # cursor_music.execute(sql_music_tag)
    # tag_list = cursor_music.fetchall()
    # insert_tag_list = list()
    # for i in tag_list:
    #     insert_tag_list.append([i[1]])
    # print(insert_tag_list)
    # cursor_k8s.executemany(sql_k8s_tag_insert,insert_tag_list)
    # conn_k8s.commit()
    # song 处理
    # cursor_local.execute(sql_local_music)
    # local_music_data_list=cursor_local.fetchall()
    # cursor_local.execute(sql_local_musicinfo)
    # local_music_info_data_list = cursor_local.fetchall()
    # cursor_music.execute(sql_music_song)
    # music_song_data_list = cursor_music.fetchall()
    # # for i in music_song_data_list[:2]:
    # #     print(i)
    # # for i in local_music_data_list[:2]:
    # #     print(i)
    # # for i in local_music_info_data_list[:2]:
    # #     print(i)
    # music_song_map = dict()
    # for num  in range(len(music_song_data_list)):
    #
    #     music_source_id = music_song_data_list[num][3]
    #     # local_song_source_id = local_music_data_list[num][4]
    #     if music_source_id not in music_song_map.keys():
    #         music_song_map[music_source_id] = num
    #     else:
    #         pass
    #         # print(music_source_id)
    # insert_k8s_song_list = list()
    # for local_song in local_music_data_list:
    #     local_song_source_id = local_song[4]
    #     if local_song_source_id  in music_song_map.keys():
    #         cur_list = list()
    #         music_song = music_song_data_list[music_song_map[local_song_source_id]]
    #         cur_list.append(music_song[1])
    #         pulish_time = local_song[9]
    #         if pulish_time is not  None:
    #             pulish_time = pulish_time.strftime("%Y-%m-%d %H:%M:%S")
    #         cur_list.append(pulish_time)
    #         cur_list.append(music_song[5])
    #         cur_list.append(music_song[3])
    #         cur_list.append(local_song[6].strftime("%Y-%m-%d %H:%M:%S"))
    #         cur_list.append(local_song[7].strftime("%Y-%m-%d %H:%M:%S"))
    #         cur_list.append(str(music_song[2]).zfill(8))
    #         cur_list.append(local_song[8])
    #         insert_k8s_song_list.append(cur_list)
    #         # print(cur_list)
    #         # print(local_song)
    #         # print(music_song_data_list[music_song_map[local_song_source_id]])
    # cursor_k8s.executemany(sql_k8s_song_insert,insert_k8s_song_list)
    # conn_k8s.commit()
    # print(insert_k8s_song_list[:1])
    # music info 处理
    # cursor_local.execute(sql_local_music)
    # music_local_data_list = cursor_local.fetchall()
    # musicinfo_local_data_list = cursor_local.execute(sql_local_musicinfo)
    # musicinfo_local_data_list = cursor_local.fetchall()
    # cursor_k8s.execute(sql_k8s_song)
    # k8s_song_data_list = cursor_k8s.fetchall()
    # k8s_musci_sourceid_map = dict()
    # for i in k8s_song_data_list:
    #     source_id = i[1]
    #     # print(source_id)
    #     if source_id not in k8s_musci_sourceid_map.keys():
    #         k8s_musci_sourceid_map[source_id]= i[0]
    #     # print(source_id)
    # local_map = dict()
    # for i in music_local_data_list:
    #     song_id = i[1]
    #     source_id = i[4]
    #
    #     if song_id not in local_map.keys():
    #         local_map[song_id] = source_id
    #
    #         # print(song_id,source_id)
    # # print(local_map)
    # insert_k8s_music_info = list()
    # count =0
    # final_insert_k8s_musicinfo_list = list()
    # for i in musicinfo_local_data_list:
    #     song_id = i[1]
    #     hot_comment_number = i[2]
    #     comment_number = i[3]
    #     # print(hot_comment_number,comment_number)
    #     # print(i)
    #     cur_source_id = str(local_map[song_id])
    #
    #     if cur_source_id not in k8s_musci_sourceid_map.keys():
    #         print(cur_source_id)
    #         count+=1
    #     cur_list = list()
    #
    #     # print(k8s_musci_sourceid_map)
    #     cur_k8s_song_id = k8s_musci_sourceid_map[cur_source_id]
    #     cur_list.append(str(cur_k8s_song_id).zfill(8))
    #     cur_list.append(str(hot_comment_number))
    #     cur_list.append(str(comment_number))
    #     final_insert_k8s_musicinfo_list.append(cur_list)
    #     # print(song_id,cur_source_id,cur_k8s_song_id)
    # for i in final_insert_k8s_musicinfo_list:
    #     if len(i) <3:
    #         print(i)
    #     if '' in i :
    #         print(i)
    # cursor_k8s.executemany(sql_insert_k8s_musicinfo,final_insert_k8s_musicinfo_list)
    # conn_k8s.commit()
    # song_tag
    # cursor_music.execute(sql_music_song_tag)
    # song_tag_list = cursor_music.fetchall()
    # insert_k8s_song_tag_list = list()
    # for i in song_tag_list:
    #     song_id = i[0]
    #     tag_id = i[1]
    #     cur_list = list()
    #     cur_list.append(str(song_id).zfill(8))
    #     cur_list.append(str(tag_id))
    #     insert_k8s_song_tag_list.append(cur_list)
    #     # print(cur_list)
    #     # print(song_id)
    #     # print(type(song_id))
    #     if song_id >320904:
    #         print(i)
    # cursor_k8s.executemany(sql_insert_k8s_song_tag,insert_k8s_song_tag_list)
    # conn_k8s.commit()
    # album 数据
    # cursor_k8s.execute(sql_select_k8s_song_album)
    # album_list = cursor_k8s.fetchall()
    # final_list = list()
    # for i in album_list:
    #     name = i[0]
    #     if name is not None and name !='':
    #         cur_list = list()
    #         cur_list.append(name)
    #         final_list.append(cur_list)
    #     # print(i)
    #
    # cursor_k8s.executemany(sql_insert_k8s_album,final_list)
    # conn_k8s.commit()
    # music song_id 处理
    # cursor_k8s.execute(sql_select_musci_k8s)
    # data_list = cursor_k8s.fetchall()
    # for i in data_list:
    #     print(i)
    #     id = i[0]
    #     song_id = str(id).zfill(8)
    #     print(song_id)
    #     # print(sql_update_k8s_music.format(song_id, id))
    #     # print()
    #     cursor_k8s.execute(sql_update_k8s_music.format(song_id,id))
    # conn_k8s.commit()


def log_filter():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql_insert_hugo_log = "insert into hugo_log(user_id, device_id,dialogue_id,user_device_id,ip,merchant_id,domain,query,artist,title, album, type, engine,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # update_timestamp_sql = "update hugo_log set hugo_log.timestamp = '%s' where id =%s"
    final_insert_hugolog_list = list()
    base_path1 = "/home/gaozhiwei/Desktop/hugo-log/hugo-log/log/filtersavelog.log"
    base_path2 = "/home/gaozhiwei/Desktop/logsavejob.log"
    base_path3 = "/home/gaozhiwei/Desktop/logsavejob1.log"
    log_list = list()
    with open(base_path1, 'r') as f:
        log_list_path1 = f.readlines()
    with open(base_path2, 'r') as f:
        log_list_path2 = f.readlines()
    with open(base_path3, 'r') as f:
        log_list_path3 = f.readlines()
    log_list.extend(log_list_path1)
    log_list.extend(log_list_path2)
    log_list.extend(log_list_path3)

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
                                cur_timestamp = datetime.strptime(log_timestamp, "%Y-%m-%d %H:%M:%S,%f")

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
                                # cur_list.append()

                                # if music_title is not None and len(music_title) >1:
                                #     print(music_title,music_engine,music_query,'title')
                                # if music_artist is not None and len(music_artist) >1:
                                #     print(music_artist,music_engine,music_query,'artist')
                                # if music_album is not None:
                                #     print(music_album,'album',music_engine,music_query)

                                # parameter_set.add(lambda i:for i in parameters.keys())
                                # print(music_query,music_answer,music_parameters,music_userid)
    # for i in final_insert_hugolog_list:
    #     print(i)
    cursor_k8s.executemany(sql_insert_hugo_log, final_insert_hugolog_list)
    conn_k8s.commit()
    # sort_deviceId_set = sorted(deviceId_set,key=lambda i:len(i),reverse=True)
    # for i in sort_deviceId_set:
    #     print(i)
    # print(len(deviceId_set))
    print(parameter_set)
    print(num)


def userid_deal():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql = 'select distinct user_id from hugo_log_old'
    # sql_select_userid = "select user_id,dialogue_id,title,domain from hugo_log where title is not null"
    # sql_insert_into_user_action = "insert into user_action(user_id,dialogue_id,song_id,action_type) values (%s,%s,%s,%s)"

    # cursor_k8s.execute(sql)
    # data_list = cursor_k8s.fetchall()
    # sql_insert = "insert into user(user_id) values (%s)"
    # for i in data_list:
    #     print(i)
    # print(len(data_list))
    # cursor_k8s.executemany(sql_insert,data_list)
    # conn_k8s.commit()
    # cursor_k8s.execute(sql_select_userid)
    # data_list = cursor_k8s.fetchall()
    # cursor_k8s.executemany(sql_insert_into_user_action,data_list)
    # conn_k8s.commit()
    # for i in data_list:
    #     print(i)


def hugologtable_filter():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    sql_log_hugo = "select title,user_id from hugo_log_old where title is not null "
    sql_music_select = "select raw_song,song_id from babel_recommender_system.music where raw_song='%s'"
    sql_insert_into_music_collection = "insert into music_collection(song, user_id, orider_times) values (%s,%s,%s)"

    cursor_k8s.execute(sql_log_hugo)
    log_list = cursor_k8s.fetchall()
    num = 0
    title_set = set()
    music_collection_dict = dict()
    for i in log_list:
        # print(i)
        userid = i[1]
        title_list = json.loads(i[0])
        for title in title_list:
            # print(title)
            cursor_k8s.execute(sql_music_select % (title))
            cur_data_list = cursor_k8s.fetchall()
            if len(cur_data_list) > 0:
                # print(cur_data_list)
                for data in cur_data_list:
                    # print(data)
                    if len(data) == 0:
                        pass
                        # print(title)
                        # print(data)
            else:
                # print(title)
                title_set.add(title)
                # num +=1
                if title not in music_collection_dict.keys():
                    music_collection_dict[title] = dict()
                    music_collection_dict[title][userid] = 1
                else:
                    if userid not in music_collection_dict[title].keys():
                        music_collection_dict[title][userid] = 1
                    else:
                        music_collection_dict[title][userid] += 1

    # print(music_collection_dict)
    # print(music_collection_dict.keys())
    # print(num)
    # print(title_set)
    final_insert_music_collection_list = list()
    for title, title_dict in music_collection_dict.items():
        for userid, order_times in title_dict.items():
            cur_list = list()
            cur_list.append(title)
            cur_list.append(userid)
            cur_list.append(order_times)
            final_insert_music_collection_list.append(cur_list)
    for i in final_insert_music_collection_list:
        print(i)
    cursor_k8s.executemany(sql_insert_into_music_collection, final_insert_music_collection_list)
    conn_k8s.commit()


def user_action_update():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql = "select id,song,user_id,dialogue_id from user_action"
    sql_update_user_action = "update user_action set babel_recommender_system.user_action.song_id = '%s' where id =%s"
    insertinto_user_action = "insert into user_action(song,user_id,dialogue_id,song_id) values (%s,%s,%s,%s)"
    sql_select_title = "select song_id,raw_song from babel_recommender_system.music where raw_song='%s'"
    delete_user_action = "delete from user_action where id = %s"

    cursor_k8s.execute(sql)

    data_list = cursor_k8s.fetchall()
    for i in data_list:
        id = i[0]
        song_list = json.loads(i[1])
        userid = i[2]
        if len(song_list) == 1:
            song_title = song_list[0]
            cursor_k8s.execute(sql_select_title % (song_title))
            data = cursor_k8s.fetchall()
            if len(data) > 0:
                songid = data[0][0]
                print(songid)
                cursor_k8s.execute(sql_update_user_action % (songid, id))
        else:
            cur_insert_into_user_action = list()
            for song_i in song_list:
                cursor_k8s.execute(sql_select_title % (song_i))
                data = cursor_k8s.fetchall()
                if len(data) > 0:
                    songid = data[0][0]
                else:
                    songid = None
                cur_insertinto = list(i[1:])
                cur_insertinto.append(songid)
                cur_insert_into_user_action.append(cur_insertinto)
            print(cur_insert_into_user_action)
            cursor_k8s.executemany(insertinto_user_action, cur_insert_into_user_action)
            cursor_k8s.execute(delete_user_action % (id))
    conn_k8s.commit()


def animal_filter():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql = "select id, raw_song, singer_id, album, audio_url from babel_recommender_system.music"
    sql_select_singer = "select name,singer_id from babel_recommender_system.singer "
    cursor_k8s.execute(sql)
    data_list = cursor_k8s.fetchall()
    cursor_k8s.execute(sql_select_singer)
    singer_list = cursor_k8s.fetchall()
    singer_map = dict()
    for i in singer_list:
        name = i[0]
        singer_id = i[1]
        if singer_id not in singer_map.keys():
            singer_map[singer_id] = name
    cur_map = dict()
    for i in data_list:
        raw_song = i[1]
        singer_id = i[2]
        # print(singer_id)
        singer = singer_map[singer_id]
        if raw_song not in cur_map.keys():
            cur_map[raw_song] = list()
            cur_data = list(i)
            cur_data.append(singer)
            cur_map[raw_song].append(cur_data)
        else:
            cur_data = list(i)
            cur_data.append(singer)
            cur_map[raw_song].append(cur_data)
    final_map = dict()
    for i, j in cur_map.items():
        if i not in final_map.keys() and len(j) > 1:
            final_map[i] = j
    with open("/home/gaozhiwei/Desktop/recommond_music.json", 'w') as f:
        f.write(json.dumps(final_map, ensure_ascii=False, indent=1))


def album_update():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    select_data_sql = "select id,name from album"
    select_data_sql_music_album = "select id,album from babel_recommender_system.music"
    # update_sql_albumid = "update album set album_id = '%s' where id =%s"
    update_sql_music_album = "update babel_recommender_system.music set album_id = '%s' where id =%s"
    select_data_album_id = "select album_id from album where name='%s'"
    cursor_k8s.execute(select_data_sql_music_album)
    data_list = cursor_k8s.fetchall()
    for i in data_list:
        id = i[0]
        album = i[1]
        print(id, album)
        if album is not None:
            try:
                album = re.sub("'", "\\\'", album)
                album = re.sub('"', '\\\"', album)
                cursor_k8s.execute(select_data_album_id % (album))
                tem_object = cursor_k8s.fetchall()
                album_id = tem_object[0][0]
                cursor_k8s.execute(update_sql_music_album % (album_id, id))
                print(tem_object)
                print(album_id)
            except Exception as e:
                print(e)
                print(album)
                print("fdsaaaaaaaaaaa")
                break
    #     cursor_k8s.execute(update_sql_albumid%(album_id,id))
    conn_k8s.commit()


def user_action_timestamp():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()


def musice_total_filter():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()


    select_sql_music_total = "select id, song, album, singer from music_total where song='%s' and singer='%s' and source='migu';"
    select_sql_music_total_all = "select id, song, album, singer,source from music_total;"

    update_sql_music_album = "update babel_recommender_system.music_total set tags = '%s', pub_date='%s',zuoci='%s',zuoqu='%s',lyric='%s'  where id =%s"

    # file_path = "/home/gaozhiwei/Desktop/1212fileter.log"
    # src_file_path = "/home/gaozhiwei/Desktop/migu1207totaldata.json"
    # json_file_path = "/home/gaozhiwei/Desktop/migudata1209detail12121.json"
    json_file_path = "/home/gaozhiwei/Desktop/migudata1218detail.json"

    # with open(src_file_path) as f:
    #     src_json_data = f.read()
    with open(json_file_path) as f:
        detail_json = f.read()
    # src_dict_data = json.loads(src_json_data)
    # for i in src_dict_data:
    #     print(i)
    dict_data = json.loads(detail_json)
    print(len(dict_data))
    cursor_k8s.execute(select_sql_music_total)
    # data_list = cursor_k8s.fetchall()
    # for i in data_list:
    #     print(i)
    num =0
    for i in dict_data:
        src = i.get('src', None)
        song_tag = i.get('song_tag_str', None)
        song_lyric = i.get('song_lyric', None)
        zuoci = i.get('zuoci', None)
        zuoqu = i.get('zuoqu', None)
        pub_data = i.get('pub_data', None)
        if src is not None:
            src_title = src['title']
            if src_title is not None:
                src_title = re.sub("'", "\\\'", src_title)
                src_title = re.sub('"', '\\\"', src_title)
            src_singer_name = src['singer_name']
            if src_singer_name is not None:
                src_singer_name = re.sub("'", "\\\'", src_singer_name)
                src_singer_name = re.sub('"', '\\\"', src_singer_name)
            src_album_name = src['album_name']
            if src_album_name is not None:
                src_album_name = re.sub("'", "\\\'", src_album_name)
                src_album_name = re.sub('"', '\\\"', src_album_name)
            # print(src_title,src_singer_name)
            # print(select_sql_music_total%(src_title,src_singer_name))
            try:
                cursor_k8s.execute(select_sql_music_total % (src_title, src_singer_name))
                # num += 1
                data_list = cursor_k8s.fetchall()
                # print(data_list)
                if len(data_list) != 0:
                    for cur_music_total in data_list:
                        cur_id = cur_music_total[0]
                        if zuoci is not None:
                            cur_zuoci = re.match("作词：(.*)",zuoci).group(1)
                        if zuoqu is not None:
                            cur_zuoqu = re.match("作曲：(.*)",zuoqu).group(1)
                        if song_tag is not None:
                            cur_tag = re.sub("/",',',song_tag)
                        # print(cur_zuoci,cur_zuoqu,cur_tag,pub_data,'============'*20,song_lyric)
                        if song_lyric is not None:
                            cur_song_lyric = re.sub("'", "\\\'", song_lyric)
                            cur_song_lyric = re.sub('"', '\\\"', cur_song_lyric)
                        cursor_k8s.execute(update_sql_music_album%(cur_tag,pub_data,cur_zuoci,cur_zuoqu,cur_song_lyric,cur_id))
                        # print(update_sql_music_album % (cur_tag, pub_data, cur_zuoci, cur_zuoqu, cur_song_lyric, cur_id))
                        num +=1
            except Exception as e:
                print(e,'baocuo***************************************')
                print(src_title, src_singer_name)
    # print(len(dict_data))
    print(num)
    conn_k8s.commit()
def log_str_filter():
    json_file_path = "/home/gaozhiwei/Desktop/migu1207totaldata.json"
    with open(json_file_path) as f:
        data_json = f.read()
    all_total_data = json.loads(data_json)
    title_singer_map = dict()
    file_url_key_map = dict()
    for i in all_total_data:
        # print(i)
        file_title = i['title']
        file_singer = i['singer_name']
        file_url = i['url']
        cur_file_singer_title  = file_title+file_singer
        title_singer_map[cur_file_singer_title] = file_url
        file_url_key_map[file_url] = i
    print(len(title_singer_map))
    dict_data = json.loads(data_json)
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    select_sql_music_total = "select id, song, album, singer from music_total where song='%s' and singer='%s' and source='migu';"
    select_sql_music_total_all = "select id, song, album, singer,source from music_total ;"

    update_sql_music_album = "update babel_recommender_system.music_total set tags = '%s', pub_date='%s',zuoci='%s',zuoqu='%s',lyric='%s'  where id =%s;"
    file_path = "/home/gaozhiwei/Desktop/1212fileter.log"
    file_path = "/home/gaozhiwei/Desktop/1212fileter.log"
    with open(file_path) as f:
        str_list = f.readlines()
    num = 0
    for i in str_list:
        # print(i)
        # if re.match()
        if re.match("itemmmmmmmmmmmm (\{.*\})",i):
            dict_data = re.match("itemmmmmmmmmmmm (\{.*\})",i).group(1)
            # print(dict_data)
            # dict_data = re.sub("'",'"',dict_data)
            if re.search("'song_tag_str': '(.*?)'",dict_data):
                song_tags =  re.search("'song_tag_str': '(.*?)'",dict_data).group(1).strip()
            elif re.search("'song_tag_str': \"(.*?)\"",dict_data):
                song_tags =  re.search("'song_tag_str': \"(.*?)\"",dict_data).group(1).strip()
            if re.search("'song_lyric': '(.*?)'",dict_data):
                song_lyric =  re.search("'song_lyric': '(.*?)'",dict_data).group(1).strip()
            elif re.search("'song_lyric': \"(.*?)\"",dict_data):
                song_lyric= re.search("'song_lyric': \"(.*?)\"",dict_data).group(1).strip()
            # else:
            #     song_lyric= None
            if  re.search("'pub_data': '(.*?)'",dict_data):
                pub_data =  re.search("'pub_data': '(.*?)'",dict_data).group(1).strip()
            else:
                pub_data= None
            if re.search("'zuoci': '(.*?)'",dict_data):
                zuoci  =  re.search("'zuoci': '(.*?)'",dict_data).group(1).strip()
            else:
                zuoci =None
            if re.search("'zuoqu': '(.*?)'",dict_data):
                zuoqu =  re.search("'zuoqu': '(.*?)'",dict_data).group(1).strip()
            else:
                zuoqu = None
            if  re.search("'title': '(.*?)'",dict_data):
                title =  re.search("'title': '(.*?)'",dict_data).group(1)
            elif  re.search("'title': \"(.*?)\"",dict_data):
                title = re.search("'title': \"(.*?)\"",dict_data).group(1)
            # else:
            #     title = None
            if re.search("'singer_name': '(.*?)'",dict_data):
                singer_name =  re.search("'singer_name': '(.*?)'",dict_data).group(1)
            elif re.search("'singer_name': \"(.*?)\"",dict_data):
                singer_name= re.search("'singer_name': \"(.*?)\"",dict_data).group(1)
            # else:
            #     singer_name =None
            if re.search("'album_name': '(.*?)'",dict_data):
                album_name =  re.search("'album_name': '(.*?)'",dict_data).group(1)
            # else:
            #     album_name = None
            # 1214 处理数据里丢失的数据
            cur_singer_title = title+ singer_name
            if cur_singer_title in title_singer_map.keys():
                title_singer_map.pop(cur_singer_title)
                # all_total_data

            if song_tags !='' and song_tags is not None and '\\' not in title and '\\' not in singer_name:
                # num +=1
                # print(song_tags,singer_name,title,pub_data,zuoci,zuoqu)
                try:
                    if title is not None:
                        title = re.sub("'", "\\\'", title)
                        title = re.sub('"', '\\\"', title)
                        # title = re.sub('\\', '\\', title)
                    if singer_name is not None:
                        singer_name = re.sub("'", "\\\'", singer_name)
                        singer_name = re.sub('"', '\\\"', singer_name)

                    # cursor_k8s.execute(select_sql_music_total % (title, singer_name))
                    data_list = cursor_k8s.fetchall()
                    # print(data_list)
                    if len(data_list) != 0:
                        for cur_music_total in data_list:
                            cur_id = cur_music_total[0]
                            if zuoci is not None and zuoci[-1] == '\\':
                                zuoci = zuoci[:-1]
                            if zuoqu is not None and zuoqu[-1] == '\\':
                                zuoqu = zuoqu[:-1]
                            if song_tags is not None:
                                cur_tag = re.sub("/", ',', song_tags)
                            # print(cur_zuoci,cur_zuoqu,cur_tag,pub_data,'============'*20,song_lyric)
                            if song_lyric is not None:
                                cur_song_lyric = re.sub("'", "\\\'", song_lyric)
                                cur_song_lyric = re.sub('"', '\\\"', cur_song_lyric)
                                if cur_song_lyric[-1] =='\\':
                                    cur_song_lyric= cur_song_lyric[:-1]
                                # cur_song_lyric = re.sub("\","\\",)
                            # print(update_sql_music_album % (cur_tag, pub_data, cur_zuoci, cur_zuoqu, cur_id))
                            # if cur_zuoci is not None:
                            #     if '\\'  in cur_zuoci:
                            #         cur_zuoci = re.sub("\\\\",'',cur_zuoci)
                            # if cur_zuoqu is not  None:
                            #     if '\\' in cur_zuoqu:
                            #         cur_zuoqu = re.sub("\\\\",'',cur_zuoqu)
                            if zuoci is not None:
                                cur_zuoci = re.match("作词：(.*)", zuoci).group(1)
                            if zuoqu is not None:
                                cur_zuoqu = re.match("作曲：(.*)", zuoqu).group(1)
                            # try:
                            #     cursor_k8s.execute(update_sql_music_album % (cur_tag, pub_data, cur_zuoci, cur_zuoqu, cur_song_lyric,cur_id))
                            #     num+=1
                            #     # conn_k8s.commit()
                            # except Exception as e:
                            #     # num +=1
                            #     print(e)
                            #     print("updatechuruole *****************")
                            #     print(update_sql_music_album% (cur_tag, pub_data, zuoci, zuoqu, cur_id))

                            # conn_k8s.commit()
                #             # print(update_sql_music_album % (cur_tag, pub_data, cur_zuoci, cur_zuoqu, cur_song_lyric, cur_id))


                except Exception as e:
                    pass
                    # num +=1
                    # print(title)
                    # print(singer_name)
                    # print(select_sql_music_total % (title, singer_name))
                    # print(update_sql_music_album % (cur_tag, pub_data, zuoci, zuoqu, cur_song_lyric, cur_id))
                    # print(dict_data)
                    # raise e
            # print(song_tags,pub_data,zuoci,zuoqu,title,singer_name,album_name)
            # try:
            #     cur_dict = json.loads(dict_data)
            #     print(cur_dict)
            # except:
            #     num +=1
            #     # print(cur_dict)
    # conn_k8s.commit()
    print(len(title_singer_map.keys()))
    final_filter_filemap = list()
    for k,v in title_singer_map.items():
        # print(k,v)
        # print(v)
        if v in file_url_key_map.keys():
            final_filter_filemap.append(file_url_key_map[v])
    for i in final_filter_filemap:
        print(i)
    # print(title_singer_map)
    print(len(final_filter_filemap))
    print(num)
    with open("/home/gaozhiwei/Desktop/migu1214totaldata.json",'w') as f:
        f.write(json.dumps(final_filter_filemap,ensure_ascii=False,indent=1))


def migu_youwentishuju():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql_select_sql = "select id,song,singer,tags,pub_date from music_total where tags is null and source='migu'"
    json_file_path = "/home/gaozhiwei/Desktop/migu1207totaldata.json"

    with open(json_file_path) as f:
        data_json = f.read()
    dict_data = json.loads(data_json)
    cursor_k8s.execute(sql_select_sql)
    data_list = cursor_k8s.fetchall()
    for i in data_list:
        print(i)


def log_songid_filter():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    media_resources_conn = pymysql.connect(host='k8s-nfs.sai.corp', user='halo_media', password="3edc#EDC",
                               database='halo_media_resources')
    media_cursor = media_resources_conn.cursor()


    media_sql_select = "select id,name from halo_media_resources.song;"
    k8s_sql_select_log_useraction = "select id,song from user_action_new;"
    k8s_update_sql_useraction_new = "update user_action_new set song_id='%s' where id = %s"
    # print(media_cursor)
    media_cursor.execute(media_sql_select)
    media_data_list = media_cursor.fetchall()
    cursor_k8s.execute(k8s_sql_select_log_useraction)
    k8s_useraction_list = cursor_k8s.fetchall()
    media_song_name_map = dict()

    # for i in k8s_useraction_list:
    #     print(i)
    num =0
    for i in media_data_list:
        # print(i)
        id = i[0]
        name = i[1]
        media_song_name_map[name] = id
    for i in k8s_useraction_list:
        song = i[1]
        id = i[0]
        if song is not None:
            # print(song)
            song = json.loads(song)
            song = song[0]
            # print(song)
            cur_music_id = media_song_name_map.get(song,None)
            if cur_music_id is not None:
                # print(cur_music_id,song)
                # print(cur_music_id)
                cursor_k8s.execute(k8s_update_sql_useraction_new%(str(cur_music_id),id))

                num +=1


    print(num)
    conn_k8s.commit()
    # print(len(k8s_useraction_list))














if __name__ == '__main__':
    # main()
    # log_filter()
    # userid_deal()
    # hugologtable_filter()
    # user_action_update()
    # animal_filter()
    # album_update()
    # musice_total_filter()
    # log_str_filter()
    # migu_youwentishuju()
    log_songid_filter()
