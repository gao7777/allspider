
import json,re


result_list = []

with open("/home/gaozhiwei/Desktop/bee_video/detail.json") as f:
    # json_data = f.readline(3)
    num = 0
    for line in f:
        num +=1
        # print(line.strip())
        # print(re.search("Top", line.strip()))
        # if num>1000000:
        #     break
        data = json.loads(line.strip())
        # cur_dict = {}
        # cur_dict['chanelid']= data['chnId']
        # cur_dict['chanelname']= data['chnName']
        # cur_dict['categoryname']= data['cateName']
        # cur_dict['name']= data['name']
        # print(cur_dict['chanelname'])
        if data['chnName'] == "综艺":
            # print(data['chnName'])

            result_list.append(data)
print(len(result_list))
with open("/home/gaozhiwei/Desktop/mifenzongyi.json",'w') as f:
    f.write(json.dumps(result_list,ensure_ascii=False,indent=3))
print(len(result_list))
# for i in result_list:
#     print(i)

total_size = {}
# def main():
#     with open("/home/gaozhiwei/Desktop/mifenfilter.json",'r') as f:
#         # f.write(json.dumps(result_list,ensure_ascii=False,indent=1))
#         json_data = f.read()
#     data_list = json.loads(json_data)
#     print(len(data_list))
#     name_set = set()
#     for i in data_list:
#         name = i['name']
#         channel_name = i['chanelname'].strip()
#         if total_size.get(channel_name):
#             total_size[channel_name] = total_size[channel_name]+1
#         else:
#             total_size[channel_name] = 1
#
#         # if channel_name in ["电视剧","电影","综艺","动漫","少儿"]:
#         #     print(channel_name)
#         #     name_set.add(name)
#     print(len(name_set))
#     print(total_size)
#     totalnum = total_size.values()
#     zong_size = 0
#     for i in totalnum:
#         zong_size +=i
#     print(zong_size)




# if __name__ == '__main__':
#     main()