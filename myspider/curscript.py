import json

# var = {"code":0,"msg":"ok",
#        "result":{
#            "_text":"冥想音乐",
#             "msg_id":"3a2b5a30-5984-4c63-8123-cf7996734d5f",
#            "intents":[
#                {"parameters":
#                     {"soundid":"37730296;37730297;13102995;13102998,9594998,9594996,9594994,10264556,10264213,10264211,10264209,10263749,10263064,10263593,10263594,10263733,10263347,10265132,12686512,10264671,199,9529804,9529819,10395078,2892133,9874061,2900953,288214","any":"","service":"meditation music"},
#                 "action":"sys.action.xmly/random/soundid",
#                 "name":"唤醒v1",
#                 "result":
#                     {"id":"xmly:sound:10264671","html_link":"http://www.ximalaya.com/sound/10264671","source":"喜马拉雅","source_link":"http://www.ximalaya.com/","sound_id":"10264671","title":"雨中的空旷森林，别样的美","media_url":"http://audio.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmuaghP1vABSy9Dqr0SM199.m4a","cover_url":"http://imagev2.xmcdn.com/group10/M04/BF/A1/wKgDZ1ZkR9ShaKqvAAP_W9aJeJ4253.jpg!op_type=3&columns=100&rows=100","mp3_audio_url":"http://fdfs.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmujyVthgAAo6rzSjU2I871.mp3","album":"仿佛在仙境.....","album_id":"3260407","type":"sound",
#                      "tracks":{"id":10264671,"kind":"track","category_id":2,"track_title":"雨中的空旷森林，别样的美","track_tags":"3D奇妙体验馆","track_intro":"仙境啊~~~~","cover_url_small":"http://imagev2.xmcdn.com/group10/M04/BF/A1/wKgDZ1ZkR9ShaKqvAAP_W9aJeJ4253.jpg!op_type=3&columns=100&rows=100","cover_url_middle":"http://imagev2.xmcdn.com/group10/M04/BF/A1/wKgDZ1ZkR9ShaKqvAAP_W9aJeJ4253.jpg!op_type=3&columns=180&rows=180","cover_url_large":"http://imagev2.xmcdn.com/group10/M04/BF/A1/wKgDZ1ZkR9ShaKqvAAP_W9aJeJ4253.jpg!op_type=3&columns=640&rows=640",
#                                "announcer":{"id":1014416,"kind":"user","nickname":"Timmy_Mao","avatar_url":"http://fdfs.xmcdn.com/group6/M02/C3/57/wKgDhFUTO7Kgdw91AACC-gTuZoA032_web_large.jpg","is_verified":"true","anchor_grade":9},
#                                "duration":167,"play_count":64596,"favorite_count":235,"comment_count":37,"can_download":"true","order_num":2,
#                                "subordinated_album":{"id":3260407,"album_title":"仿佛在仙境.....",
#                                                                                                                                                                    "cover_url_small":"http://fdfs.xmcdn.com/group11/M07/B6/AE/wKgDa1ZkQDOhiSDtAAMtuiFQWZk787_mobile_small.jpg",
#                                                                                                                                                                    "cover_url_middle":"http://fdfs.xmcdn.com/group11/M07/B6/AE/wKgDa1ZkQDOhiSDtAAMtuiFQWZk787_mobile_meduim.jpg",
#                                                                                                                                                                    "cover_url_large":"http://fdfs.xmcdn.com/group11/M07/B6/AE/wKgDa1ZkQDOhiSDtAAMtuiFQWZk787_mobile_large.jpg"},"source":2,"updated_at":1473142776000,"created_at":1448450954000,"is_paid":"false","is_free":"false","is_trailer":"false","has_sample":"false","sample_duration":0,"play_url_32":"http://fdfs.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmujyVthgAAo6rzSjU2I871.mp3","play_size_32":670383,"play_url_64":"http://fdfs.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmunAFr1fABR0PGQg6VQ546.mp3","play_size_64":1340476,"play_url_24_m4a":"http://audio.xmcdn.com/group12/M05/A9/B6/wKgDXFZVmubD_vpVAAfpogfuC6k264.m4a","play_size_24_m4a":518562,"play_url_64_m4a":"http://audio.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmuaghP1vABSy9Dqr0SM199.m4a","play_size_64_m4a":1356532,"play_size_amr":0,"download_url":"http://download.xmcdn.com/group12/M05/A9/B6/wKgDXFZVmubRqxz4AAqcQVXqRQc304.aac","download_size":695361,"contain_video":"false","download_count":0},"current_order_num":2,"match_rule":"suggest","track_list":[{"track_title":"Garden of happiness II (mitNaturgeräuschen)-Largo","album_title":"沁人心脾的冥想音乐","cover_url":"http://imagev2.xmcdn.com/group26/M08/8B/9C/wKgJRlkVF92AcIqgABKxNpPcMXo129.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group26/M02/8B/82/wKgJRlkVFiDhBZN_ADfsD6tteyA640.m4a","announcer":"睡前音乐台","track_id":37730296,"order_num":0,"album_id":"8079478"},
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"track_title":"The singing garden-Largo","album_title":"沁人心脾的冥想音乐","cover_url":"http://imagev2.xmcdn.com/group26/M08/8B/9C/wKgJRlkVF92AcIqgABKxNpPcMXo129.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group26/M02/8B/83/wKgJRlkVFizDl9vGADXMvTNWvmM154.m4a","announcer":"睡前音乐台","track_id":37730297,"order_num":1,"album_id":"8079478"},{"track_title":"Streamside Songbirds","album_title":"穿过风穿过森林穿过大自然","cover_url":"http://imagev2.xmcdn.com/group16/M08/90/0B/wKgDalYybVuguTiPAAG6JVqCiPU397.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group14/M02/8F/F7/wKgDZFYybZ3Byqg5ALRtvxO6yFQ585.m4a","announcer":"声音百科","track_id":9594998,"order_num":0,"album_id":"3123474"},{"track_title":"Pleasant Beach","album_title":"穿过风穿过森林穿过大自然","cover_url":"http://imagev2.xmcdn.com/group16/M08/90/0B/wKgDalYybVuguTiPAAG6JVqCiPU397.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group12/M00/8F/70/wKgDXFYybZDQ0fyjAJDrYq3ozKQ698.m4a","announcer":"声音百科","track_id":9594996,"order_num":1,"album_id":"3123474"},{"track_title":"Gentle Rain","album_title":"穿过风穿过森林穿过大自然","cover_url":"http://imagev2.xmcdn.com/group16/M08/90/0B/wKgDalYybVuguTiPAAG6JVqCiPU397.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group14/M02/90/38/wKgDY1YybZXiC3a8ACH4KhMuwvQ779.m4a","announcer":"声音百科","track_id":9594994,"order_num":2,"album_id":"3123474"},{"track_title":"雷雨","album_title":"戴着耳机听雨声","cover_url":"http://imagev2.xmcdn.com/group7/M00/C5/B6/wKgDWlZk4PDi6I_WAABMhw1nmUI562.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group11/M0B/B6/1C/wKgDbVZVmb_A_qw9AEoYRgYLSn0373.m4a","announcer":"呀呀呀土豆","track_id":10264556,"order_num":6,"album_id":"3260371"},{"track_title":"辽阔的水流","album_title":"水声也能如此悦耳","cover_url":"http://imagev2.xmcdn.com/group11/M00/B6/75/wKgDa1ZkJKviFqO4AAHA6G2OM6I113.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group9/M00/AA/32/wKgDZlZVl_Xx-iFWAAfOrSDpGJM881.m4a","announcer":"Timmy_Mao","track_id":10264213,"order_num":0,"album_id":"3260235"},{"track_title":"小溪","album_title":"水声也能如此悦耳","cover_url":"http://imagev2.xmcdn.com/group7/M0A/C4/CD/wKgDX1ZkJUSRCdUaAARYpRccIHk997.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group7/M04/AA/D0/wKgDX1ZVl1_y3gUMABRCUlk94_8025.m4a","announcer":"Timmy_Mao","track_id":10264211,"order_num":2,"album_id":"3260235"},{"track_title":"潺潺流动的小溪","album_title":"水声也能如此悦耳","cover_url":"http://imagev2.xmcdn.com/group11/M02/CF/8E/wKgDbVZkLNzRqwjDAACd93krJsc712.jpg!op_type=3&columns=100&rows=100","media_url":"http://audio.xmcdn.com/group14/M01/AA/9B/wKgDZFZVliLhS8heAAfjilnzzks946.m4a","announcer":"Timmy_Mao","track_id":10264209,"order_num":3,"album_id":"3260235"},{"track_title":"旋转的潮流","album_title":"送你一片海","cover_url":"http://imagev2.xmcdn.com/group10/M06/C3/62/wKgDaVZk8QLjhHaHAAGY80enlt8241.jpg!op_type=3&columns=100&rows=100","media_url":"http://aod.tx.xmcdn.com/group9/M07/AA/2A/wKgDZlZVkjfjau_NAGDZs6Ehpvw713.m4a","announcer":"亲爱的小鬼","track_id":10263749,"order_num":3,"album_id":"3260197"}],"text":"安然地冥想音乐帮你摆脱心念的滋扰，下雨声、鸟叫声、海浪声和流水声，随你点播"},"outputs":[{"type":"wechat.music","property":{"title":"雨中的空旷森林，别样的美","description":"仿佛在仙境.....","music_url":"http://audio.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmuaghP1vABSy9Dqr0SM199.m4a"}},{"type":"dialog","property":{"text":"安然地冥想音乐帮你摆脱心念的滋扰，下雨声、鸟叫声、海浪声和流水声，随你点播","emotion":"calm"}},{"type":"voice","property":{"name":"1","voice_url":"http://audio.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmuaghP1vABSy9Dqr0SM199.m4a"}}],"score":"1.0","scoreColor":"c4","is_match":1,"skill_id":"5e3b22a9-9137-4df3-a92d-d64e96f913b3","id":"dadc8038-5833-428b-abd6-13538f5e444c"}],"meta_process_milliseconds":178}}
#
#
#
# result = var['result']
# intents = result['intents']
# parameters = intents[0]
# print(parameters)
# print(len(parameters))
# print(type(parameters))
# print(parameters.keys())
# parameters1 = parameters['parameters']
# action = parameters['action']
# name = parameters['name']
# result = parameters['result']
# # print("result"+result)
# # print("action",action)
# # print("parameters",parameters1)
# # print("name",name)
# output = parameters['outputs']
# # print("output",output)
# for i,j in parameters.items():
#     print(i,j)
# print("="*20)
# for i,j in result.items():
#     print(i,j)
# print("="*30)
# for i,j in output[0].items():
#     print("ddfsfs")
#     print(i,j)
#
# tracks = result['tracks']
# print("=="*20)
# print(type(tracks))
# for i,j in tracks.items():
#     print(i,j)
#
# var = [{'type': 'wechat.music', 'property': {'title': '雨中的空旷森林，别样的美', 'description': '仿佛在仙境.....', 'music_url': 'http://audio.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmuaghP1vABSy9Dqr0SM199.m4a'}}, {'type': 'dialog', 'property': {'text': '安然地冥想音乐帮你摆脱心念的滋扰，下雨声、鸟叫声、海浪声和流水声，随你点播', 'emotion': 'calm'}}, {'type': 'voice', 'property': {'name': '1', 'voice_url': 'http://audio.xmcdn.com/group12/M0B/A9/E1/wKgDW1ZVmuaghP1vABSy9Dqr0SM199.m4a'}}]
# print(len(var))
#
# final_list = []
#
# for i in var:
#     print(i.items())
#     print(i)
#     final_list.append(i)
#
#
# with open("/home/gaozhiwei/Desktop/mingxiangyinyue.json","w") as f:
#     f.write(json.dumps(final_list,ensure_ascii=False,indent=1))


import requests



# headers = {
#     "Content-Type":"application/json",
#     "Postman-Token":"64e5a7eb-4b36-4b40-880d-6d8679d50350",
#     "cache-control":"no-cache"
# }
# url = "http://api.ruyi.ai/ruyi-api/v1/message"
# data = {
# 	"app_key":"3b01b176-5135-45d4-a2cb-52d22fdeacef",
# 	"q": "猫叫声",
# 	"user_id":"test123",
# 	"context": {
# 	"ip":"61.50.105.110"
#     }}
# # response = requests.post(url,headers=headers,data=data)
# # print(response)
# # print(response.content)
#
import os

from urllib.parse import quote,unquote



animal_list = ['猫头鹰','狗','喜鹊','蚊子','斑马','小羊','鸭子','燕子','老虎','霸王龙','犀牛','恐龙','猫','马','猪','猴子','刺猬','奶牛','青蛙','狼','猫咪','兔子','八哥','鸟','老牛','鸡','狮子','三角龙','布谷鸟','蝙蝠','驴','杜鹃','虫子','蜥蜴','老鼠','母鸡','牛','大象','熊猫','鸟儿','蝴蝶','猫猫','小猫','金鱼','鲨鱼','海豚','鳄鱼','百灵鸟','河马','小鸡','孔雀','东北虎','鲸鱼','蛇','乌鸦','鹅','公鸡','雷龙','龙','老鹰','企鹅','羊','鹦鹉','麻雀','凤凰','骆驼','苍龙','熊','灰狼','斑鸠','蟋蟀','蜜蜂','喵喵','鸟类','蛐蛐','苍蝇','狗狗','毛驴','蚂蚁']
#
command = "curl -X POST  'http://api.ruyi.ai/ruyi-api/v1/message' -H 'Content-Type: application/json'   -H 'Postman-Token: 64e5a7eb-4b36-4b40-880d-6d8679d50350'   -H 'cache-control: no-cache'   -d {}"

data = {
"app_key":"3b01b176-5135-45d4-a2cb-52d22fdeacef",
"q": "猫叫声",
"user_id":"test123",
"context":{"ip":"61.50.105.110"}}

# print(json.dumps(data,ensure_ascii=False))
# jsondata = json.dumps(data,ensure_ascii=False)
#
# answer_list = []
# for i in animal_list:
#     data['q']=i+'叫声'
#     response = os.popen(command.format("\'" + str(data) + "\'"))
#     cur_str = response.read()
#     answer_list.append(cur_str)
#     # print(type(cur_str))
#     # print(cur_str)
#
#
# # var ={"code":0,"msg":"ok","result":{"_text":"斑马","msg_id":"d8a5435d-0b0f-435a-a394-eec3a26056ff","intents":[{"parameters":{"answer":"斑马，是现存的奇蹄目马科马属3种兽类的通称。因身上有起保护作用的斑纹而得名。没有任何动物比斑马的皮毛更与众不同。斑马周身的条纹和人类的指纹一样——没有任何两头完全相同。斑马为非洲特产。非洲东部、中部和南部产平原斑马，由腿至蹄具条纹或腿部无条纹。东非还产一种格式斑马，体格最大，耳长（约30厘米）而宽，全身条纹窄而密，因而又名细纹斑马。南非洲产山斑马，与其它两种斑马不同的是，它有一对象驴似的大长耳朵。除腹部外，全身密布较宽的黑条纹，雄体喉部有垂肉。斑马是草食性动物。除了草之外，灌木、树枝、树叶甚至树皮也是它们的食物。适应能力较强的消化系统，令斑马可以在低营养条件下生存，比其他草食性动物优胜。斑马对非洲疾病的抗病力比马强，但斑马始终未能被驯化成家畜，也没有能和马进行杂交。","service":"baike"},"action":"dialog","name":"通用百科知识FAQ","result":{"text":"斑马，是现存的奇蹄目马科马属3种兽类的通称。因身上有起保护作用的斑纹而得名。没有任何动物比斑马的皮毛更与众不同。斑马周身的条纹和人类的指纹一样——没有任何两头完全相同。斑马为非洲特产。非洲东部、中部和南部产平原斑马，由腿至蹄具条纹或腿部无条纹。东非还产一种格式斑马，体格最大，耳长（约30厘米）而宽，全身条纹窄而密，因而又名细纹斑马。南非洲产山斑马，与其它两种斑马不同的是，它有一对象驴似的大长耳朵。除腹部外，全身密布较宽的黑条纹，雄体喉部有垂肉。斑马是草食性动物。除了草之外，灌木、树枝、树叶甚至树皮也是它们的食物。适应能力较强的消化系统，令斑马可以在低营养条件下生存，比其他草食性动物优胜。斑马对非洲疾病的抗病力比马强，但斑马始终未能被驯化成家畜，也没有能和马进行杂交。","type":"dialog"},"outputs":[{"type":"wechat.text","property":{"text":"斑马，是现存的奇蹄目马科马属3种兽类的通称。因身上有起保护作用的斑纹而得名。没有任何动物比斑马的皮毛更与众不同。斑马周身的条纹和人类的指纹一样——没有任何两头完全相同。斑马为非洲特产。非洲东部、中部和南部产平原斑马，由腿至蹄具条纹或腿部无条纹。东非还产一种格式斑马，体格最大，耳长（约30厘米）而宽，全身条纹窄而密，因而又名细纹斑马。南非洲产山斑马，与其它两种斑马不同的是，它有一对象驴似的大长耳朵。除腹部外，全身密布较宽的黑条纹，雄体喉部有垂肉。斑马是草食性动物。除了草之外，灌木、树枝、树叶甚至树皮也是它们的食物。适应能力较强的消化系统，令斑马可以在低营养条件下生存，比其他草食性动物优胜。斑马对非洲疾病的抗病力比马强，但斑马始终未能被驯化成家畜，也没有能和马进行杂交。"}},{"type":"dialog","property":{"text":"斑马，是现存的奇蹄目马科马属3种兽类的通称。因身上有起保护作用的斑纹而得名。没有任何动物比斑马的皮毛更与众不同。斑马周身的条纹和人类的指纹一样——没有任何两头完全相同。斑马为非洲特产。非洲东部、中部和南部产平原斑马，由腿至蹄具条纹或腿部无条纹。东非还产一种格式斑马，体格最大，耳长（约30厘米）而宽，全身条纹窄而密，因而又名细纹斑马。南非洲产山斑马，与其它两种斑马不同的是，它有一对象驴似的大长耳朵。除腹部外，全身密布较宽的黑条纹，雄体喉部有垂肉。斑马是草食性动物。除了草之外，灌木、树枝、树叶甚至树皮也是它们的食物。适应能力较强的消化系统，令斑马可以在低营养条件下生存，比其他草食性动物优胜。斑马对非洲疾病的抗病力比马强，但斑马始终未能被驯化成家畜，也没有能和马进行杂交。","emotion":"positive"}}],"score":"1.0","scoreColor":"c4","is_match":1,"skill_id":"f4f28d81-b4bd-4cb7-989e-05a0dbc1f804","id":"ca502ea5-3292-4a6d-9874-1dea2806092a"}],"meta_process_milliseconds":623}}
# with open("/home/gaozhiwei/Desktop/answerlist.json",'w') as f:
#     f.write(json.dumps(answer_list,ensure_ascii=False,indent=1))




import json,os

with open("/home/gaozhiwei/Desktop/answerlist.json") as f:
    json_data = f.read()


data = json.loads(json_data)

dataone = data[1]
dataone = json.loads(dataone)
for i,j in dataone.items():
    print(i,j)
num =0
intents = dataone['result']['intents']
for i in intents:
    print(i)

# print(outputs)


wgetcommand= "wget -O /home/gaozhiwei/Desktop/animalvoice/{}  {}"
animal_mp3_name_list = []
for i in data:
    try:
        i = json.loads(i)
        intents = i['result']['intents']
        for j in intents:
            outputs = j['outputs']
            for k in outputs:
                property = k['property']
                if property.get('voice_url') or property.get('music_url'):
                    if property.get('voice_url'):
                        voice_url = property.get("voice_url")
                        voice_url= unquote(voice_url)
                        print(voice_url)
                        index = voice_url.rfind('/')
                        if index!=-1:
                            cur_title = voice_url[index+1:]
                            animal_mp3_name_list.append(cur_title)
                            # os.system(wgetcommand.format(cur_title,voice_url))
                            # print(cur_title)
                    if property.get('music_url'):
                        music_url = property.get('music_url')
                        # print(music_url)
                        index = music_url.rfind('/')
                        if index != -1:
                            cur_title = "music_url"+music_url[index+1:]
                            # os.system(wgetcommand.format(cur_title,music_url))
                            # print(cur_title)


                    num +=1


    except Exception as e:
        print(e)
        print(i)


print(num)
print(len(animal_list))
import re
queshi_list = []
for i in animal_list:
    for j in animal_mp3_name_list:
        if re.search(i,j):
            print(i,j)
            break

    else:
        queshi_list.append(i)



for i in queshi_list:
    print(i)