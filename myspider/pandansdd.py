import json
import re
import ijson
import pandas as pd

# A=json.load('~/Desktop/shuju/search.train.json')
# a=open('/home/gaozhiwei/Desktop/shuju/search.train.json')
# questions = ijson.parse(a)
# for i in questions:
#     print(i[2])

# dataframe = pd.read_csv('./zhidao天为什么是蓝色的呢？.csv',)
# dataframe = pd.read_json('/home/gaozhiwei/Desktop/shuju/search.train.json',)
list1 = []
with open('/home/gaozhiwei/Desktop/shuju/search.train.json','r') as f:
    while True:
        a = f.read(1000000)
        if a:
            list = re.findall(r'title": "(.*?)", "paragraphs"',a)
            for i in list:
                if i is None or i!="":
                    print(i)
                    list1.append(i)
            # list1.extend(list)
        else:
            break

    a =pd.DataFrame(list1)
    a.to_csv('./allzhidaodata.csv')

    # print(list1)
    # print(type(json.loads(a)))



    # print(f.read(2))
# dataframe.read(1000)
# a=dataframe['question']
# a.to_csv('./teeef.csv')
