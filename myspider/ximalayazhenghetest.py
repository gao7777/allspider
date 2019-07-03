import json,re

def main():
    with open('/home/gaozhiwei/Desktop/ximalayashiwang0.json') as f:
        shiwang_json = f.read()
    with open("/home/gaozhiwei/Desktop/ximalayashierwang0.json") as f:
        shiqiwang_json = f.read()

    with open("./ximalayadelete",'r') as f:
        delete_list = f.readlines()
    delete_list1 = []
    for i in delete_list:
        delete_list1.append(i.strip())
    heping_list = []
    shiqiwang_data = json.loads(shiqiwang_json)
    shiwang_data = json.loads(shiwang_json)
    shiqiwang_title_list = []
    for i in shiqiwang_data['dict']:
        title = i['minorType']
        # print(title)
        shiqiwang_title_list.append(title)
        if title not in delete_list1:
            heping_list.append(i)

    print(len(shiqiwang_title_list))
    print(len(set(shiqiwang_title_list)))
    shiwang_title_list = []
    for i in shiwang_data['dict']:
        title = i['minorType']
        shiwang_title_list.append(title)
        heping_list.append(i)
    print(len(shiwang_title_list))
    print(len(set(shiwang_title_list)))
    print(len(heping_list))
    num = 0
    shiqiwang_title_list_set = set(shiqiwang_title_list)
    shiwang_title_list_set = set(shiwang_title_list)
    butong_list=[]
    # for i in shiqiwang_title_list_set:
    #     if i in shiwang_title_list_set:
    #         num +=1
    #         print(i)
    #         butong_list.append(i)
    #
    # print(num)
    final_dict = {}
    final_dict['dict'] = heping_list
    with open("/home/gaozhiwei/Desktop/hebing.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))

    # with open("/home/gaozhiwei/Desktop/butong.json",'w') as f:
    #     f.write(json.dumps(butong_list,ensure_ascii=False,indent=1))

def final_handle():
    with open('/home/gaozhiwei/Desktop/hebing2.json') as f:
        json_data = f.read()
    with open("./ximalayadelete",'r') as f:
        delete_list = f.readlines()
    delete_list1 = [i.strip() for i in delete_list]
    data = json.loads(json_data)
    data_list = data['dict']
    final_list = []
    num =0
    for i in data_list:
        values = i['value']
        values = list(set(values))
        cur_list = []
        # if len(values) == 3:
        #     num +=1
        #     print(i)
        for value in values:
            if value in delete_list1:
                print(i)
                num +=1
                break
        else:
            final_list.append(i)
    print(len(final_list))
    print(len(data_list))
    print(num)
    num_set = 0
    final_list11= []
    final_set = set()
    for i in final_list:
        values = i['value']
        for j in values:
            if j not in final_set:
                final_set.add(j)
                # final_list11.append(i)
            else:
                num_set+=1
                print(i)
                break
        else:
            final_list11.append(i)
    final_list = final_list11
    total_num = len(final_list)
    print(total_num)
    print(type(total_num))
    range_num = total_num/5000
    if re.search(".",str(range_num)):
        range_num+=1
    range_num = int(range_num)
    for i in range(range_num):
        path = "/home/gaozhiwei/Desktop/ximalayazhenghe/ximalaya_title%d.json"%(i)
        cur_list = final_list[i * 5000:(i+1) * 5000]
        cur_dict = {}
        cur_dict['dict'] = cur_list
        with open(path, 'w') as f:
            f.write(json.dumps(cur_dict, ensure_ascii=False, indent=1))

    print(num_set)









    data['dict'] = final_list


    # with open('/home/gaozhiwei/Desktop/hebing3.json','w') as f:
    #     f.write(json.dumps(data,ensure_ascii=False,indent=1))




if __name__ == '__main__':
    # main()
    final_handle()
