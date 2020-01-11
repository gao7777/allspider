import datetime
import json
import re
import time

import pymysql
import requests


def main():

    with open('/home/gaozhiwei/Desktop/heimingdan.txt') as f:
        heimingdan_list = f.readlines()
    heimingdan_list = [i.strip() for i in heimingdan_list]
    for i in heimingdan_list:
        print(i)
    final_dict = {
    "dicts": [
        {
            "type": "audio",
            "source_name": "宇宙有声",
            "values": [

            ]
        }
    ]
    }
    title_set = set()
    # print(final_dict['dicts'][0]['values'])
    list_dir_path  = "/home/gaozhiwei/Desktop/信源"
    import os,json,re
    file_name_list = os.listdir(list_dir_path)
    # print(file_name_list)
    final_dict = dict()
    for i in file_name_list:
        with open(list_dir_path+'/'+i,'r') as f:
            json_data = f.read()
            dict_data = json.loads(json_data)

            # print(type(dict_data))
            for key in dict_data.keys():
                final_dict[key] = dict_data[key]
            final_dict['values']=list()
            value_list = dict_data['values']
            for body in value_list:
                # print(body)
                author = body['author']
                title = body['title']
                if author not in heimingdan_list and title not in heimingdan_list:
                    if title not in title_set:
                        title_set.add(title)
                        # del body['tags']
                        final_dict['values'].append(body)
    fianl_final_dict = dict()
    fianl_final_dict['dicts']=list()
    fianl_final_dict['dicts'].append(final_dict)



    print(final_dict)
    # print(len(final_dict['dicts'][0]['values']))
    # print(len(title_set))


    with open("/home/gaozhiwei/Desktop/yuzhouaudio1106.json",'w') as file:
        file.write(json.dumps(fianl_final_dict,ensure_ascii=False,indent=1))
def logtest():

    with open("/home/gaozhiwei/Desktop/fffffff.txt") as f:
        data_list = f.readlines()
    # print(data_list)
    final_list = list()
    for i in data_list:
        str_list = i.strip().split(',')
        userid = str_list[2]
        query = str_list[3]
        cur_dict = dict()
        cur_dict['query'] = query
        cur_dict['userid'] = userid
        final_list.append(cur_dict)
        # res=requests.post(url='http://localhost:8888/log/store/',data=cur_dict)
        # print(res.content)
    final_dict = dict()
    final_dict['dicts']=final_list[:1000]
    final_json = json.dumps(final_dict,ensure_ascii=False,indent=1)
    print(final_json)
    with open('/home/gaozhiwei/Desktop/ssssss.json','w') as f:
        f.write(final_json)

def xinyuan_oprea():
    with open('/home/gaozhiwei/Desktop/nlp-universe-opera.json') as f:
        json_data = f.read()
    dict_data = json.loads(json_data)
    final_dict = {
        "dicts": [
            {
                "type": "audio",
                "source_name": "宇宙有声",
                "values": [

                ]
            }
        ]
    }
    title_set = set()
    values = dict_data['values']
    for value in values:

        if value['title'] not in title_set:
            title_set.add(value['title'])
            final_dict['dicts'][0]['values'].append(value)
    print(final_dict)

    with open('/home/gaozhiwei/Desktop/xinyuan_opera.json','w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))


def xinyuan_fenghuangfm():
    with open('/home/gaozhiwei/Desktop/nlp-fenghuangfm.json') as f:
        json_data = f.read()
    dict_data = json.loads(json_data)
    final_dict = {
        "dicts": [
            {
                "type": "audio",
                "source_name": "凤凰故事",
                "values": [

                ]
            }
        ]
    }
    title_set = set()
    values = dict_data['values']
    for value in values:
        if value['title'] not in title_set:
            title  = value['title']
            title_set.add(value['title'])
            # print(title)
            filter_title = re.sub("（.*[）|)].*",'',title)
            # print(filter_title)
            value['title'] = filter_title
            final_dict['dicts'][0]['values'].append(value)
    print(final_dict)

    with open('/home/gaozhiwei/Desktop/xinyuan_fenghuang.json','w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))


def test_ttt():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    insert_into_music_qianqian = "insert into music_taihemusic_new(song, album, singer, source, tags) VALUES (%s,%s,%s,%s,%s)"
    title_singer_set = set()

    with open("/home/gaozhiwei/Desktop/taihe1218.json") as f:
        json_data =f.read()
    final_dict = dict()
    json_data = json.loads(json_data)
    key_set = set()
    for i in json_data:
        # print(i)
        key = i.keys()
        tag = list(i.keys())[0]
        # print(tag)
        for j in i[tag] :
            title = j['title']
            singer= j['singer']
            album = j['album']
            if title is not None:
                if singer is not None:
                    cur_str = title+singer
                else:
                    cur_str = title
                if cur_str not in title_singer_set:
                    title_singer_set.add(cur_str)
                    tem_dict = dict()
                    tem_dict['title'] = title
                    tem_dict['singer'] =singer
                    tem_dict['album'] = album
                    tem_dict['tags'] = set()
                    tem_dict['tags'].add(tag)
                    final_dict[cur_str] = tem_dict
                else:
                    print(tag)
                    final_dict[cur_str]['tags'].add(tag)
        # print(list(key)[0])
        key_set.add(list(key)[0])
    # print(key_set)
    # print(len(key_set))
    # print(final_dict)
    num =0
    final_insert_into_qianqianyinyue = list()
    for a,b in final_dict.items():
        num +=1
        # print(b)
        title = b['title']
        singer = b['singer']
        album = b['album']
        tag_str = ','.join(list(b['tags']))
        # print(title,singer,album,tag_str)
        cur_list = list()
        cur_list.append(title)
        cur_list.append(album)
        cur_list.append(singer)
        cur_list.append('taihe')
        cur_list.append(tag_str)
        final_insert_into_qianqianyinyue.append(cur_list)
    for i in final_insert_into_qianqianyinyue:
        print(i)
    print(len(final_insert_into_qianqianyinyue))
    cursor_k8s.executemany(insert_into_music_qianqian,final_insert_into_qianqianyinyue)
    conn_k8s.commit()

def test_timestamp():
    log = """[2019-12-17 15:42:17,362][INFO ][defaultEventExecutor-2-1] com.sai.semantic.SemanticProgressiveListener - {botId=BT1574939130659144438, clientId=null, deviceId=b90dbe0e20e387c7bb9e74686c51d1f2, dialogId=6e384a3a-b9d0-4fa4-b5b4-9bc2d119ad91, dialogInfo=null, ip=121.69.129.34, merchantId=47, query=我要听周杰伦的告白气球, region=null, userDeviceId=null, userId=anonymous_23cde382adbc477aae9e2a8437bca8cc} [SaveJob] record {"cost":416,"ip":"121.69.129.34","query":"我要听周杰伦的告白气球","dialogId":"6e384a3a-b9d0-4fa4-b5b4-9bc2d119ad91","deviceId":"b90dbe0e20e387c7bb9e74686c51d1f2","userId":"anonymous_23cde382adbc477aae9e2a8437bca8cc","result":[{"code":400,"latency":254,"source":"platform_ruyi","message":"ok","startTime":1576568536950,"intentComplete":false,"selected":false},{"code":0,"data":"{\"audio_list\":[{\"artist\":\"周杰伦\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/34YBAFdskzmAUMlOADSMOxgm3l4714.mp3\",\"title\":\"告白气球\"},{\"artist\":\"周杰伦\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/4e15c71567a68a417b0f6225a62db007.mp3\",\"title\":\"安静\"},{\"artist\":\"周杰伦\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/3f18806af4eeb8682c6d24c1c86b6dd3.mp3\",\"title\":\"屋顶\"},{\"artist\":\"周杰伦\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/LZQEAFguky2AU7OFAEHk-4CpoG8440.mp3\",\"title\":\"晴天\"},{\"artist\":\"周杰伦\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/rYYBAFUBVceAQsKQADn6ct4sfQo314.mp3\",\"title\":\"青花瓷\"},{\"artist\":\"罗大佑\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/d9fd511c700ad75d9d5aca09d872810b.mp3\",\"title\":\"沧海一声笑\"},{\"artist\":\"林志炫\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/b3241e713f26c82c9f18bd0b6a9832fd.mp3\",\"title\":\"你的样子\"},{\"artist\":\"李宗盛\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/8cb08cb1598d182e215fe1f0a5e3af5c.mp3\",\"title\":\"鬼迷心窍\"},{\"artist\":\"李宗盛\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/79663ff2c3341c79687970ea7b4b6f7a.mp3\",\"title\":\"当爱已成往事\"},{\"artist\":\"王菲\",\"album\":\"\",\"audio_url\":\"http://static.soundai.cn:23080/music/v1/41e0db24fb49080764c965412f636f0e.mp3\",\"title\":\"浮躁\"}],\"answer\":\"为您播放周杰伦的告白气球\",\"tts_url\":\"http://tts.soundai.cn/tts/v1/synthesize?encoding=base64&text=5Li65oKo5pKt5pS-5ZGo5p2w5Lym55qE5ZGK55m95rCU55CD\",\"parameters\":{\"artist\":[\"周杰伦\"],\"title\":[\"告白气球\"]}}","query":"我要听周杰伦的告白气球","latency":403,"source":"saiV2","message":"","engine":"saiV2Rule","domain":"music","startTime":1576568536949,"intentComplete":false,"selected":true}],"merchantId":"47","botId":"BT1574939130659144438"}
[2019-12-17 15:42:18,902][INFO ][defaultEventExecutor-2-1] com.sai.semantic.SemanticProgressiveListener - {botId=BT1576051103480588454, clientId=null, deviceId=fac6ecc8beaf71b690fc1543281a9e54, dialogId=6fd83dc6-ae12-4b8b-a3a7-66491c217907, dialogInfo=null, ip=119.137.53.27, merchantId=47, query=音量调到二十, region=null, userDeviceId=null, userId=1a5ee3047c68c1283dab0822a6e0b99a} [SaveJob] record {"cost":176,"ip":"119.137.53.27","query":"音量调到二十","dialogId":"6fd83dc6-ae12-4b8b-a3a7-66491c217907","deviceId":"fac6ecc8beaf71b690fc1543281a9e54","userId":"1a5ee3047c68c1283dab0822a6e0b99a","result":[{"code":200,"data":"{\"answer\":\"好的，为您调节音量到20\",\"tts_url\":\"http://tts.soundai.cn/tts/v1/synthesize?encoding=base64&text=5aW955qE77yM5Li65oKo6LCD6IqC6Z-z6YeP5YiwMjA=\",\"parameters\":{\"operation\":\"SET\",\"value\":20}}","query":"音量调到二十","latency":151,"source":"saiV2","message":"ok","engine":"saiV2Rule","domain":"volume","startTime":1576568538729,"intentComplete":false,"selected":true},{"code":400,"latency":171,"source":"platform_ruyi","message":"ok","startTime":1576568538730,"intentComplete":false,"selected":false}],"merchantId":"47","botId":"BT1576051103480588454"}
"""
    log_timestamp = re.match("\[(.*?)\]", log.strip()).group(1)
    print(log_timestamp)
    cur_timestamp = datetime.datetime.strptime(log_timestamp, "%Y-%m-%d %H:%M:%S,%f")
    print(cur_timestamp)
    print(cur_timestamp.timetuple())
    i = cur_timestamp.timetuple()
    print(time.mktime(i))
    print(cur_timestamp.microsecond)
    local_timestamp = int(time.mktime(
        cur_timestamp.timetuple()) * 1000.0 + cur_timestamp.microsecond / 1000.0)
    cur_insert_timestamp = str(local_timestamp)
    print(cur_insert_timestamp)

def taihe_zhenghe():
    conn_k8s = pymysql.connect(host='k8s-nfs.sai.corp', user='recommender', password="recommender",
                               database='babel_recommender_system')
    cursor_k8s = conn_k8s.cursor()
    sql_select_taihenew = "select * from music_taihemusic_new;"
    sql_select_old_taihe = "select * from music_taihemusic where album like '%.》'"
    update_sql_taihe_music = "update babel_recommender_system.music_taihemusic set album='%s'  where id =%s;"
    cursor_k8s.execute(sql_select_taihenew)
    taihe_new_table = cursor_k8s.fetchall()
    all_new_data_map = dict()
    for i in taihe_new_table:
        song = i[1]
        album = i[2]
        singer = i[3]
        if singer is not None:
            cur_key = song+singer
        else:
            cur_key= song
        if cur_key not in all_new_data_map.keys():
            all_new_data_map[cur_key] = album
    cursor_k8s.execute(sql_select_old_taihe)
    old_taihe_data = cursor_k8s.fetchall()
    num =0
    for i in old_taihe_data:
        # print(i)
        id = i[0]
        song = i[1]
        album = i[2]
        singer = i[3]
        if singer is not None:
            cur_key = song + singer
        else:
            cur_key = song
        if cur_key not in all_new_data_map.keys():
            print(cur_key)
            num+=1
        else:
            new_album = all_new_data_map[cur_key]
            # print(new_album)
            try:
                new_album = re.sub("'", "\\\'", new_album)
                new_album = re.sub('"', '\\\"', new_album)
                cursor_k8s.execute(update_sql_taihe_music%(new_album,id))
            except Exception as e:
                print(e)
                print(update_sql_taihe_music%(new_album,id))
    print(num)
    conn_k8s.commit()
    time.localtime()











if __name__ == '__main__':
    # main()
    # logtest()
    # xinyuan_oprea()
    # xinyuan_fenghuangfm()
    # test_ttt()
    # test_timestamp()
    taihe_zhenghe()

