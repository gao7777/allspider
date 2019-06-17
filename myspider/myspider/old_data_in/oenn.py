import json

list_json = [{"label_id": [0, 11, 12], "image_id": "01dbd060b48994cd8a1aca1f1ebe7cf4febcdeb5.jpg"},
{"label_id": [1, 11, 12], "image_id": "022efb13db1719182cd6868cda18c4da46cae862.jpg"},
{"label_id": [2, 11, 12], "image_id": "03c31c963a11bc8684b4ac6016368365eaa01c30.jpg"},
{"label_id": [3, 11, 12], "image_id": "11389364c084cacc011f6134ac5862735a188fd7.jpg"}]



# with open('./url_list.txt','r') as f:
#     # data_jaon = json.dumps(list_json)
#     # print(type(data_jaon))
#     # f.write(data_jaon)
#     a = f.readline()
#     print(a)
# fa_file = open('./head100url_list.txt','w+')
# def re_url():
#     url_list = []
#     print('uuudsl')
#     i= 0
#     fa_file = open('./head100url_list.txt', 'w+')
#     with open('./url_list.txt','r') as f:
#         while True:
#             line = f.readline()
#             print(line)
#             if line:
#                 i= i+1
#                 fa_file.write(line)
#                 url_list.append(line.strip())
#                 if i == 100:
#                     break
#                 # url_list=line
#             else:
#                 break
#                 # return url_list
#     print(url_list)
#     fa_file.close()
#     print(i)
# re_url()

def re_url():
    url_list = []
    print('uuudsl')
    with open('./head100url_list.txt','r') as f:
        print('ds',f)
        while True:
            line = f.readline()
            if line:
                print(line)
                url_list.append(line.strip())
            else:
                return url_list

re_url()