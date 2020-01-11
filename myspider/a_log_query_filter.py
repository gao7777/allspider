import json
import os
import re

import pymysql


def main():
    file_name_lists = os.listdir("/home/gaozhiwei/Desktop/1119/")
    num = 0
    rule_num = 0
    final_dict = list()
    engine_set = set()
    total_num = 0
    cur_situo_chat_list = list()
    # for file_name in file_name_lists:
    # print(file_name)
    base_path = "/home/gaozhiwei/Desktop/hugolog122711.log"
    # with open('/home/gaozhiwei/Desktop/1119/%s' % file_name) as f:
    with open(base_path) as f:
        log_list = f.readlines()
        for log in log_list:
            log = log.strip()
            # print(log)
            log_timestamp = re.match("\[(.*?)\]", log).group(1)
            print(log_timestamp)
            # num +=1
            query = re.search('query=(.*?),', log).group(1)
            clientId = re.search('clientId=(.*?),', log).group(1)
            engine = re.search('engine":"(.*?)"', log)
            domain = re.search('"domain":"(.*?)"', log)
            # print(query)
            # print(clientId)
            # print(source)
            if domain is not None:
                # num +=1
                # print(domain.group(1))
                record = re.search('record (.*)', log).group(1)
                record_dict = json.loads(record)
                # print(record_dict)
                record_query = record_dict['query']
                record_result = record_dict['result']
                for cur_record_dict in record_result:
                    # print(cur_record_dict['selected'])
                    if cur_record_dict['selected'] == True:
                        # print(cur_record_dict['domain'])
                        # print(cur_record_dict)
                        cur_record_data = cur_record_dict['data']
                        cur_data_dict = json.loads(cur_record_data)
                        fin_engine = cur_record_dict.get('engine', None)
                        fin_query = cur_record_dict['query']
                        fin_source = cur_record_dict['source']
                        fin_domain = cur_record_dict['domain']
                        # print(cur_data_dict)
                        fin_answer = cur_data_dict['answer']
                        # print(fin_engine,fin_query,fin_source,fin_domain,fin_answer)
                        cur_dict = dict()
                        cur_dict['query'] = fin_query
                        cur_dict['source'] = fin_source
                        # if fin_source =="situo" and fin_domain=='chat':
                        #     cur_1206_situo_map = dict()
                        #     cur_1206_situo_map['query'] = fin_query
                        #     cur_1206_situo_map['source'] = fin_source
                        #     cur_1206_situo_map['answer'] = fin_answer
                        #     cur_1206_situo_map['data'] = cur_record_dict
                        #     cur_situo_chat_list.append(cur_1206_situo_map)
                        # num +=1
                        # print(fin_engine,fin_query,fin_source,fin_domain,fin_answer)
                        # print(cur_record_dict)
                        cur_dict['domain'] = fin_domain
                        cur_dict['engine'] = fin_engine
                        engine_set.add(fin_engine)
                        final_dict.append(cur_dict)
                        total_num += 1
                        if fin_engine != None:
                            # num +=1
                            if fin_engine == "saiV2Rule":
                                rule_num += 1

    # print(num)
    # print(rule_num)
    print(total_num)
    # print(engine_set)
    with open('/home/gaozhiwei/Desktop/qalogfiltre1227.json', 'w') as f:
        f.write(json.dumps(final_dict, indent=1, ensure_ascii=False))
    # with open("/home/gaozhiwei/Desktop/1206situo.json",'w') as f:
    #     f.write(json.dumps(cur_situo_chat_list,ensure_ascii=False,indent=2))


def sql_insertinto():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    media_resources_conn = pymysql.connect(host='k8s-nfs.sai.corp', user='halo_media', password="3edc#EDC",
                                           database='halo_media_resources')
    media_cursor = media_resources_conn.cursor()
    # sql_insert_hugo_log = "insert into hugo_log_new(user_id, device_id,dialogue_id,user_device_id,ip,merchant_id,domain,query,artist,title, album, type, engine,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # sql_insert_userid = "insert into babel_recommender_system.user(user_id) values (%s);"
    # sql_insert_useraction = "insert into user_action_new(dialogue_id, user_id, song, action_type, log_date, song_id) VALUES (%s,%s,%s,%s,%s,%s)"
    # sql_insert_musiccollection = "insert into babel_recommender_system.music_collection_new(user_id, song, orider_times) VALUES (%s,%s,%s)"
    # sql_update_musiccollection = "update music_collection set babel_recommender_system.music_info.order_times = '%s' where id = %s"
    # # update_timestamp_sql = "update hugo_log set hugo_log.timestamp = '%s' where id =%s"
    # sql_select_user_id = "select user_id from babel_recommender_system.user;"
    # sql_select_song_list = "select raw_song,song_id from babel_recommender_system.music;"
    # sql_select_music_collention = 'select song from music_collection'
    # media_sql_select = "select id,name from halo_media_resources.song;"

    #
    # sql_select_old_hugo = "select  user_id, client_id, device_id, dialogue_id, user_device_id, dialog_info, ip, merchant_id, timestamp, domain, query, region, artist, title, album, type, engine, play_time from hugo_log_new"
    # sql_insert_new_hugo = "insert into halo_media_resources.hugo_log(user_id, client_id, device_id, dialogue_id, user_device_id, dialog_info, ip, merchant_id, timestamp, domain, query, region, artist, title, album, type, engine, play_time)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # cursor_k8s.execute(sql_select_old_hugo)
    # data_list = cursor_k8s.fetchall()
    # media_cursor.executemany(sql_insert_new_hugo,data_list)
    # media_resources_conn.commit()

    # sql_select_old_user = "select  user_id, gender, stage from babel_recommender_system.user;"
    # sql_insert_new_user = "insert into halo_media_resources.user(user_id, gender, stage) VALUES (%s,%s,%s)"
    # cursor_k8s.execute(sql_select_old_user)
    # data_list = cursor_k8s.fetchall()
    # media_cursor.executemany(sql_insert_new_user,data_list)
    # media_resources_conn.commit

    sql_select_old_useraction = "select dialogue_id, user_id, song, action_times, action_type, log_date, song_id from user_action_new"
    sql_insertinto_new_useraction = "insert into halo_media_resources.user_action(dialogue_id, user_id, song, action_times, action_type, log_date, song_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor_k8s.execute(sql_select_old_useraction)
    data_list = cursor_k8s.fetchall()
    final_insert_data_list = list()
    for cur_list in data_list:
        cur_insert_list = list()
        cur_insert_list.append(cur_list[0])
        cur_insert_list.append(cur_list[1])
        cur_song_json = cur_list[2]
        # print(cur_song_json)
        if cur_song_json is not None:
            try:
                cur_song_json_list = json.loads(cur_song_json)
                cur_song_str = ','.join(cur_song_json_list)
            except:
                cur_song_str = None

        else:
            cur_song_str = None

        cur_insert_list.append(cur_song_str)
        cur_insert_list.append(cur_list[3])
        cur_insert_list.append(cur_list[4])
        cur_insert_list.append(cur_list[5])
        cur_insert_list.append(cur_list[6])

        final_insert_data_list.append(cur_insert_list)
    media_cursor.executemany(sql_insertinto_new_useraction,final_insert_data_list)
    media_resources_conn.commit()


def A_test():
    test_list = ['a', 'b']
    cur_str = ','.join(test_list)
    print(cur_str)


if __name__ == '__main__':
    main()
    # sql_insertinto()
    # A_test()
