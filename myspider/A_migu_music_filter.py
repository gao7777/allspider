import json
import os

import pymysql


def main():
    base_path = "/home/gaozhiwei/Desktop/migudata1207alltags1.json"
    title_set = set()
    final_dict = list()
    with open(base_path) as f:
        data_json = f.read()
        data_dict = json.loads(data_json)
        for data in data_dict:
            title = data['title']
            singer = data['singer_name']
            unique_title_singer_str = title+singer
            if unique_title_singer_str not in title_set:
                title_set.add(unique_title_singer_str)
                final_dict.append(data)

            # print(title,singer)
    for i in final_dict:
        print(i)
    with open("/home/gaozhiwei/Desktop/migu1207totaldata.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=2))


def insert_into_music_total():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    sql_insert_into = "insert into music_total(song,singer,album,source) values (%s,%s,%s,%s)"

    with open('/home/gaozhiwei/Desktop/migu1207totaldata.json') as f:
        data = f.read()
    data_list = json.loads(data)
    final_insert_list = list()
    for i in data_list:
        # print(i)
        song_name = i['title']
        singer_name = i['singer_name']
        album_name = i['album_name']
        # print(song_name,singer_name,album_name)
        cur_list = list()
        cur_list.append(song_name)
        cur_list.append(singer_name)
        cur_list.append(album_name)
        cur_list.append("migu")
        final_insert_list.append(cur_list)
    # for i in final_insert_list[200:230]:
    #     print(i)
    cursor_k8s.executemany(sql_insert_into,final_insert_list)
    conn_k8s.commit()

def filter_yuzhou_source():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    sql_insert_into_music_universe = "insert into music_universe( song, album, singer, source, universe_id, pic_url, audio_url) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    with open("/home/gaozhiwei/Desktop/universe-music(1).json") as f:
        json_data = f.read()
    dict_data = json.loads(json_data)
    entity_list = dict_data['entities']
    final_insert_list = list()
    for i in entity_list:
        # print(i)
        album = i['album']
        id = i['id']
        name = i['name']
        pic_url = i['pic_url']
        presenter = i['presenter']
        url = i['url']
        cur_list = list()
        cur_list.append(name)
        cur_list.append(album)
        cur_list.append(presenter)
        cur_list.append("universe_music")
        cur_list.append(id)
        cur_list.append(pic_url)
        cur_list.append(url)
        final_insert_list.append(cur_list)
    # for i in final_insert_list:
    #     print(i)
    cursor_k8s.executemany(sql_insert_into_music_universe,final_insert_list)
    conn_k8s.commit()



    # sql_select_music = "select id, song_id, song, raw_song, singer_id, songwriter_id, album_id, publish_time, composer_id, audio_url, source_id, create_time, update_time, name, gender from babel_recommender_system.music"
def filter_yuzhou_source_two():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()

    sql_insert_into = "insert into music_total(song,singer,album,source) values (%s,%s,%s,%s)"

    with open("/home/gaozhiwei/Desktop/universe-music(1).json") as f:
        json_data = f.read()
    dict_data = json.loads(json_data)
    entity_list = dict_data['entities']
    final_insert_list = list()
    title_singer_set = set()
    for i in entity_list:
        # print(i)
        album = i['album']
        id = i['id']
        name = i['name']
        pic_url = i['pic_url']
        presenter = i['presenter']
        url = i['url']
        title_singer = name+presenter
        if title_singer not in title_singer_set:
            title_singer_set.add(title_singer)
            cur_list = list()
            cur_list.append(name)
            cur_list.append(presenter)
            cur_list.append(album)
            cur_list.append("universe_music")
            final_insert_list.append(cur_list)
    # for i in final_insert_list:
    #     print(i)
    # print(len(final_insert_list))
    cursor_k8s.executemany(sql_insert_into, final_insert_list)
    conn_k8s.commit()


if __name__ == '__main__':
    # main()
    # insert_into_music_total()
    # filter_yuzhou_source()
    filter_yuzhou_source_two()
