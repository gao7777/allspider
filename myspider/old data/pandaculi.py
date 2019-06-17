import re
from urllib.request import quote,unquote
from urllib.parse import quote,unquote,urlencode
import pandas as pd


# with open('./allzhidaodata.csv','r+') as f:
#     a =f.readlines()
#     print(len(a))
#     j= 0
#     f_a = open('./url_list.txt','a+')
#     for i in a[1:]:
#         # print(len(i))
#         # j=j+1
#         # b=re.sub(r'\d+,','',i)
#         # c =re.sub(r'[_,-,].+','',b)
#         c =re.sub(r'[^\u4E00-\u9FA5|a-z|A-Z]','',i)
#         print(c)
#         # c=c.encode('utf-8')
#         # print(j)
#         add = quote(c,encoding='gbk',)
#         print(add)
#
#         url = 'https://zhidao.baidu.com/search?word={}&ie=gbk&site=-1&sites=0&date=0&pn=10'.format(add)+'\n'
#         f_a.write(url)
#         print(url)
test_one = '%E7%83%AD%E9%97%A8'
a = unquote(test_one)
print(a)
b = quote(a)
print(b)