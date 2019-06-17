from lxml import etree
from scrapy import selector
parser = etree.HTMLParser(encoding="utf-8")
htmlelement = etree.parse("./hhafd.html", parser=parser)
# print(etree.tostring(htmlelement, encoding="utf-8").decode("utf-8"))
# a = selector(htmlelement)
import json
a = htmlelement.xpath("//div[@class='audio_tit1']")
j =0
list1= []
for i in a:
    dic = {}
    j+=1
    url =i.xpath("./div/a/@data-src")
    title =i.xpath("./dl/dt/a/text()")
    date =i.xpath("./dl/dd/text()")
    dic['url']=url[0]
    dic['title']=title[0]
    dic['date']=date[0]
    list1.append(dic)
json_data = json.dumps(list1,ensure_ascii=False)
with open('./caixindata.json','w') as f:
    f.write(json_data)
