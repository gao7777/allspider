import json
import re


def main():
    with open("/home/gaozhiwei/Desktop/ximalayashierwang.json") as f:
        json_data = f.read()
    data = json.loads(json_data)
    data_list = data['dict']
    num =0
    first_round = []
    for i in data_list:
        title = i['minorType']
        value_list = i['value']

        for value in value_list:
            if len(value) <2:
                # print(i)
                break
                # num +=1
                # print(i)
        else:
            if re.search(":", title):
                title = re.sub(":", "：", title)
            i['value'].append(title)
            i['value']= list(set(i['value']))
            first_round.append(i)

    print(len(first_round))
    total_num = len(first_round)/10000
    str_total_num = str(total_num)
    if re.search(".",str_total_num):
        total_num= total_num+1
    total_num = int(total_num)
    total_num = 1
    for i in range(total_num):
        path = "/home/gaozhiwei/Desktop/ximalayashierwang%d.json"%(i)
        cur_list = first_round[i*10000:(i+1)*10000]
        cur_list= first_round
        cur_dict = {}
        cur_dict['dict'] = cur_list
        # print(cur_list[0])
        # print(len(cur_list))
        # print(i,'iiiiiiii')
        with open(path,'w') as f:
            f.write(json.dumps(cur_dict,ensure_ascii=False,indent=1))





if __name__ == '__main__':
    main()