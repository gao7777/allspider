import json,pymysql

def main():
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='gaozhiwei',database='nlpdata',autocommit=True,charset='utf8')
    cur = conn.cursor()
    # sql = 'insert into ximalayaone(categoryoneid,categoryonename,categorytwoid,categorytwoname,categorytwopicpath,categorytwolinkurl,categorythereid,categorytherename,categorytherelinkurl,categorytheremetaid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # sql = 'insert into ximalayatwo(categorynameone,categorynametwo,srcurllink,totalsize,albumid,albumtitle,albumcoverpath,albumauthorname,albumuserid,albumlinkurl,albumtrackcount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql1 = 'select categoryonename,categorytwoname,categorytherelinkurl from ximalayaone'
    cur.execute(sql1)
    data_list=cur.fetchall()
    for i in data_list:
        url = i[2]
        list1= url.split('/')
        print(list1[1],list1[2])
        print(i)

    with open('./myspider/ximalayaliuxingcategoryalbums.json','r') as f:
        json_data = f.read()
    json_dict = json.loads(json_data)
    data_list = []
    categorynameone='yinyue'
    categorynametwo = 'liuxing'
    srcurllink='/yinyue/liuxing/'
    totalsize = json_dict['data']['total']
    # print(json_dict['data'])
    for i in json_dict['data']['albums']:
        dictone = dict()
        dictone['categorynameone']=categorynameone
        dictone['categorynametwo']=categorynametwo
        dictone['srcurllink']=srcurllink
        dictone['totalsize']=totalsize
        dictone['albumid']=i['albumId']
        dictone['title']=i['title']
        dictone['coverPath']=i['coverPath']
        dictone['authorName']=i['anchorName']
        dictone['userid']=i['uid']
        dictone['linkurl']=i['link']
        dictone['trackCount']=i['trackCount']
        data_list.append(dictone)
    num=0
    for i in data_list:
        mysql_list=[]
        mysql_list.append(i['categorynameone'])
        mysql_list.append(i['categorynametwo'])
        mysql_list.append(i['srcurllink'])
        mysql_list.append(i['totalsize'])
        mysql_list.append(i['albumid'])
        mysql_list.append(i['title'])
        mysql_list.append(i['coverPath'])
        mysql_list.append(i['authorName'])
        mysql_list.append(i['userid'])
        mysql_list.append(i['linkurl'])
        mysql_list.append(i['trackCount'])
        # cur.execute(sql,mysql_list)
        # print(i)
        num+=1
    print(num)


    # for i in json_dict['data']:
    #     dictone = dict()
    #     dictone['categoryoneid'] = i['id']
    #     dictone['categoryonename'] = i['name']
    #     for j in i['categories']:
    #         dicttwo={}
    #         for key,value in dictone.items():
    #             dicttwo[key] = value
    #         dicttwo['categorytwoid']=j['id']
    #         dicttwo['categorytwoname']=j['displayName']
    #         dicttwo['categorytwopicpath']=j['picPath']
    #         dicttwo['categorytwolinkurl']=j['link']
    #         for k in j['subcategories']:
    #             dictthere = {}
    #             for key,value in dicttwo.items():
    #                 dictthere[key]=value
    #             dictthere['categorythereid'] = k['id']
    #             dictthere['categorytherename'] = k['displayValue']
    #             dictthere['categorytherelinkurl'] = k['link']
    #             dictthere['categorytheremetaid'] = k['metadataId']
    #             data_list.append(dictthere)

    # num = 0
    # for i in data_list:
    #     data_tuple_list = list()
    #     data_tuple_list.append(i['categoryoneid'])
    #     data_tuple_list.append(i['categoryonename'])
    #     data_tuple_list.append(i['categorytwoid'])
    #     data_tuple_list.append(i['categorytwoname'])
    #     data_tuple_list.append(i['categorytwopicpath'])
    #     data_tuple_list.append(i['categorytwolinkurl'])
    #     data_tuple_list.append(i['categorythereid'])
    #     data_tuple_list.append(i['categorytherename'])
    #     data_tuple_list.append(i['categorytherelinkurl'])
    #     data_tuple_list.append(i['categorytheremetaid'])
    #     # cur.execute(sql,data_tuple_list,)
    #     num+=1
    #     print(i)

if __name__ == '__main__':
    main()
