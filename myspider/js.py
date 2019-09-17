import random
import string
import time
import requests,hashlib
from zhengzescriptzuixn import *
"""
APP_ID=soundAI000000001
APP_SECRET=5WYU1VQasIfYtek1AzHKtZg8ccALWRxp
TIMESTAMP=$(date +%s)
SIGN_TYPE=sha1
SIGNATURE=$(echo -n "${APP_ID}${APP_SECRET}${TIMESTAMP}" | openssl dgst -$SIGN_TYPE -hex | cut -d' ' -f2)
NONCE=$(openssl rand -base64 12)
"""
def main():
    # a=2
    # b = a>>1
    # print(b)
    # c = a&b
    # print(c)
    nowtime = time.time()
    print(nowtime)
    nowtime= str(nowtime).split(".")[0]
    nowtime = int(nowtime)
    print(nowtime)
    print(type(nowtime))
    # '1564804322653'.split('.')
    # 1564804656896
    # 1564805263
    rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(28))
    print(rand_str)
    appsecret = "5WYU1VQasIfYtek1AzHKtZg8ccALWRxp"
    signature= 'soundAI0000000015WYU1VQasIfYtek1AzHKtZg8ccALWRxp%d'%(nowtime)
    signature=hashlib.sha1(signature.encode())
    print(signature)
    post_url = "http://open.idaddy.cn/api/v3/cat/list"
    parameter  = dict()
    parameter['app_id']="soundAI000000001"
    parameter['device_id']=1111
    parameter['timestamp']=nowtime
    parameter['nonce']=rand_str
    parameter['signature']=signature
    parameter['sign_type']='sha1'
    parameter['cat_ids']=[]

    # parameter['sign_type']='sha1'
    # response = requests.post(post_url,data=parameter)
    # print(response)
    # print(response.text)
#     print('\u540d\u8457')
#     print({"data":{"cats":[{"id":6707,"name":"\u513f\u6b4c","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/qx7houcn.png","age_scope":"-1-8","parent":0},{"id":6708,"name":"\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/vfj0epki.png","age_scope":"1+","parent":0},{"id":6948,"name":"\u97f3\u4e50","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/fk36owk7.png","age_scope":"0+","parent":0},{"id":7156,"name":"\u82f1\u8bed","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/9rlfhx3f.png","age_scope":"1+","parent":0},{"id":7716,"name":"\u56fd\u5b66","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/9y0vcvet.png","age_scope":"0+","parent":0},{"id":16815,"name":"\u79d1\u666e","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/9ez08ldk.png","age_scope":"3+","parent":0},{"id":17164,"name":"\u540d\u8457","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/4ajjhpe0.png","age_scope":"5+","parent":0},{"id":17176,"name":"\u80ce\u6559","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/aetyh99o.png","age_scope":"-1-1","parent":0},{"id":17466,"name":"\u7ed8\u672c","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/e3f42br0.png","age_scope":"1-8","parent":0},{"id":19205,"name":"\u5386\u53f2","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/c90txxr7.png","age_scope":"4+","parent":0}]},"retcode":0})
#     print({"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0}]},"retcode":0})
#     print({"data":{"works":[{"id":"ADIGM1A1DTw","name":"\u767d\u96ea\u516c\u4e3b\uff08\u5349\u5349\u963f\u59e8\uff09","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/7d0xe5rv.jpg","status":4,"cats":[{"id":"6709","name":"\u7761\u524d\u6545\u4e8b"},{"id":"11549","name":"\u5973\u5b69\u6545\u4e8b"},{"id":"12029","name":"\u7ecf\u5178\u7ae5\u8bdd"}],"audios":[{"id":"ADcGMFA3DTNRYA","name":"\u767d\u96ea\u516c\u4e3b\uff08\u5349\u5349\u963f\u59e8\uff09\u7b2c1\u96c6","type":0,"play_url":"","status":0},{"id":"ADcGMFAxDT1RZQ","name":"\u767d\u96ea\u516c\u4e3b\uff08\u5349\u5349\u963f\u59e8\uff09\u7b2c2\u96c6","type":0,"play_url":"","status":0},{"id":"ADcGMFA8DTZRYQ","name":"\u767d\u96ea\u516c\u4e3b\uff08\u5349\u5349\u963f\u59e8\uff09\u7b2c3\u96c6","type":0,"play_url":"","status":0},{"id":"ADcGMFA8DTZRbg","name":"\u767d\u96ea\u516c\u4e3b\uff08\u5349\u5349\u963f\u59e8\uff09\u7b2c4\u96c6","type":0,"play_url":"","status":0},{"id":"ADcGMFA9DTRRZg","name":"\u767d\u96ea\u516c\u4e3b\uff08\u5349\u5349\u963f\u59e8\uff09\u7b2c5\u96c6","type":0,"play_url":"","status":0}]}]},"retcode":0})
#     idlist= [6707,6708,6948,7156,7716,16815,17164,17176,17466,19205]
    idlist = [6707, 6708, 6948, 7156, 7716, 16815, 17164, 17176, 17466, 19205]
#     print({"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0}]},"retcode":0})
#     print({"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0}]},"retcode":0})
#     print({"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0},{"id":"ADEGP1A8DTM","name":"\u6c49\u58f0\u7248\u897f\u6e38\u8bb0","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/qkjne5cb.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u540d\u8457,\u767e\u542c\u4e0d\u538c\u7684\u897f\u6e38\u8bb0","tags":"\u53e4\u5178,\u7ecf\u5178,\u5b59\u609f\u7a7a,\u56db\u5927\u540d\u8457,\u5927\u5723","performer":"\u53e3\u888b\u6545\u4e8b \u897f\u6e38\u6c49\u8bed\u4e50\u56ed\u56e2\u961f","author":"\u897f\u6e38\u6c49\u8bed\u4e50\u56ed\u56e2\u961f","age_from":3,"age_to":10,"comment":"","description":"\u897f\u6e38\u8bb0\u4e2d\u7684\u7cbe\u5f69\u3001\u7ecf\u5178\u7684\u6545\u4e8b\uff0c\u4f18\u7f8e\u7684\u80cc\u666f\u97f3\u4e50\uff0c\u7ed8\u58f0\u7ed8\u8272\u7684\u914d\u97f3\uff0c\u8ba9\u5c0f\u670b\u53cb\u4eec\u6109\u5feb\u5730\u5b66\u4e60\u7ecf\u5178\u3002","rank":305,"score":8.4,"status":0}]},"retcode":0})
#     print({"data":{"works":[{"id":"ADwGMlAw","name":"\u6050\u9f99\u4e3a\u4ec0\u4e48\u4f1a\u6d88\u5931\u5462\uff1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/xggq6p7h.jpg","tariff":0,"price":0,"terms":"\u6050\u9f99\u6545\u4e8b\u5927\u5408\u96c6,\u79d1\u666e\u6545\u4e8b,\u81ea\u7136\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e,\u6050\u9f99","performer":"\u53e3\u888b\u6545\u4e8b \u73b0\u4ee3\u6559\u80b2\u51fa\u7248\u793e","author":"\u73b0\u4ee3\u6559\u80b2\u51fa\u7248\u793e","age_from":3,"age_to":8,"comment":"","description":"\u5c0f\u5144\u59b9\u4fe9\u5bf9\u4e8e\u6050\u9f99\u7684\u6d88\u5931\u539f\u56e0\u975e\u5e38\u597d\u5947\uff0c\u4e8e\u662f\u7238\u7238\u4eca\u665a\u7684\u7761\u524d\u6545\u4e8b\uff0c\u5c31\u662f\u7ed9\u4ed6\u4fe9\u8bb2\u79d1\u5b66\u5bb6\u4eec\u5206\u6790\u7684\u51e0\u4e2a\u53ef\u80fd\u7684\u6050\u9f99\u6d88\u5931\u539f\u56e0\u3002\u5c0f\u670b\u53cb\u4eec\uff0c\u4f60\u4eec\u548c\u8fd9\u5bf9\u5c0f\u5144\u59b9\u4fe9\u4e00\u6837\u5bf9\u6050\u9f99\u611f\u5174\u8da3\u5417\uff1f\u5feb\u6765\u542c\u4ed6\u4eec\u7684\u7238\u7238\u8bb2\u6050\u9f99\u6545\u4e8b\u5427\uff01","rank":245,"score":7.9,"status":0},{"id":"ADwGMlAx","name":"\u5c0f\u6050\u9f99\u662f\u4ece\u4ec0\u4e48\u5730\u65b9\u6765\u7684\uff1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/6zevcjjo.jpg","tariff":0,"price":0,"terms":"\u6050\u9f99\u6545\u4e8b\u5927\u5408\u96c6,\u79d1\u666e\u6545\u4e8b,\u81ea\u7136\u77e5\u8bc6","tags":"\u79d1\u666e,\u6050\u9f99,\u535a\u7269\u9986","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":2,"age_to":7,"comment":"","description":"\u5c0f\u6050\u9f99\u662f\u4ece\u54ea\u91cc\u6765\u7684\u5462\uff1f\u6050\u9f99\u7684\u751f\u6d3b\u72b6\u6001\u53c8\u662f\u600e\u4e48\u6837\u7684\u5462\uff1f\u8fd9\u4e2a\u79d1\u666e\u513f\u7ae5\u6545\u4e8b\u4f1a\u544a\u8bc9\u4f60\u7b54\u6848\u3002","rank":243,"score":8.5,"status":0},{"id":"ADwGMVA9","name":"\u7231\u8fea\u751f\u548c\u7535\u706f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/s1020d49.jpg","tariff":0,"price":0,"terms":"\u540d\u4eba\u6545\u4e8b,\u79d1\u5b66\u77e5\u8bc6","tags":"\u79d1\u5b66\u53d1\u660e,\u7231\u8fea\u751f,\u7535\u706f","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":4,"age_to":8,"comment":"","description":"","rank":183,"score":9,"status":4},{"id":"ADAGNVAxDTM","name":"\u4e5d\u4e5d\u4e58\u6cd5\u53e3\u8bc0","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/b9q8jjaw.jpg","tariff":0,"price":0,"terms":"\u79d1\u5b66\u77e5\u8bc6","tags":"","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":10,"comment":"","description":"\u300a\u4e5d\u4e5d\u4e58\u6cd5\u6b4c\u8bc0\u300b\uff0c\u53c8\u5e38\u79f0\u4e3a\u201c\u5c0f\u4e5d\u4e5d\u201d\u3002\u5b66\u751f\u5b66\u7684\u201c\u5c0f\u4e5d\u4e5d\u201d\u53e3\u8bc0\uff0c\u662f\u4ece\u201c\u4e00\u4e00\u5f97\u4e00\u201d\u5f00\u59cb\uff0c\u5230\u201c\u4e5d\u4e5d\u516b\u5341\u4e00\u201d\u6b62\uff0c\u800c\u5728\u53e4\u4ee3\uff0c\u5374\u662f\u5012\u8fc7\u6765\uff0c\u4ece\u201c\u4e5d\u4e5d\u516b\u5341\u4e00\u201d\u8d77\uff0c\u5230\u201c\u4e00\u4e00\u5982\u4e00\u201d\u6b62\u3002\u56e0\u4e3a\u53e3\u8bc0\u5f00\u5934\u4e24\u4e2a\u5b57\u662f\u201c\u4e5d\u4e5d\u201d\uff0c\u6240\u4ee5\uff0c\u4eba\u4eec\u5c31\u628a\u5b83\u7b80\u79f0\u4e3a\u201c\u4e5d\u4e5d\u201d\u3002","rank":250,"score":7.8,"status":0},{"id":"ADAGM1A2DTE","name":"\u4eba\u7c7b\u8840\u578b\u7684\u53d1\u73b0","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/70tm3nun.jpg","tariff":0,"price":0,"terms":"\u751f\u6d3b\u5e38\u8bc6,\u767e\u79d1\u5168\u4e66,\u767e\u79d1\u77e5\u8bc6,\u79d1\u666e\u6545\u4e8b","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e\u6545\u4e8b,\u5065\u5eb7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":18,"comment":"","description":"\u8840\u578b\u88ab\u79f0\u4e3a100\u4e2a\u4f1f\u5927\u53d1\u660e\u4e4b\u4e00\uff0c\u56e0\u4e3a\u5b83\u5bf9\u8f93\u8840\u5177\u6709\u91cd\u8981\u610f\u4e49\uff0c\u4e0d\u76f8\u5bb9\u7684\u8840\u578b\u8f93\u8840\u53ef\u80fd\u5bfc\u81f4\u6eb6\u8840\u53cd\u5e94\u7684\u53d1\u751f\uff0c\u9020\u6210\u6eb6\u8840\u6027\u8d2b\u8840\u3001\u80be\u8870\u7aed\u3001\u4f11\u514b\u4ee5\u81f3\u6b7b\u4ea1\u3002","rank":254,"score":7.9,"status":0},{"id":"ADAGMVA3DTY","name":"\u690d\u6811\u8282\u7684\u7531\u6765","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/9msxp9dv.jpg","tariff":0,"price":0,"terms":"\u79d1\u666e\u6545\u4e8b,\u8e0f\u6625\u90ca\u6e38\u4e13\u8f91,\u767e\u79d1\u5168\u4e66,\u767e\u79d1\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e\u6545\u4e8b,\u6c11\u4fd7\u6545\u4e8b","performer":"\u53e3\u888b\u6545\u4e8b","author":"","age_from":3,"age_to":12,"comment":"","description":"\u5c0f\u670b\u53cb\u4eec\u90fd\u77e5\u90533\u670812\u65e5\u662f\u4e2d\u56fd\u7684\u690d\u6811\u8282\uff0c\u53ef\u662f\u4f60\u4eec\u77e5\u9053\u690d\u6811\u8282\u4e3a\u4ec0\u4e48\u8981\u5b9a\u57283\u670812\u65e5\u5417\uff1f\u5b83\u548c\u54ea\u4e00\u4f4d\u5386\u53f2\u540d\u4eba\u6709\u5173\uff1f\u60f3\u77e5\u9053\u7684\u5c31\u6765\u542c\u6545\u4e8b\u5427~","rank":253,"score":9.1,"status":0},{"id":"ADMGMlAzDT0","name":"\u591a\u7eb3\u5b66\u767e\u79d1 1","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/rtbgctd5.jpg","tariff":0,"price":0,"terms":"\u767e\u79d1\u77e5\u8bc6,\u79d1\u5b66\u542f\u8499","tags":"\u6d77\u6d0b,\u52a8\u7269,\u8ba4\u8bc6\u81ea\u6211,\u767e\u79d1,\u591a\u7eb3","performer":"\u53e3\u888b\u6545\u4e8b \u591a\u7eb3","author":"\u591a\u7eb3","age_from":1,"age_to":8,"comment":"","description":"\u591a\u7eb3\u5b66\u767e\u79d1\u7cfb\u5217\uff0c\u5305\u542b\u5e2e\u5b9d\u5b9d\u8ba4\u8bc6\u81ea\u6211\u3001\u6d77\u91cc\u7684\u79d8\u5bc6\u3001\u53ef\u7231\u7684\u52a8\u7269\u4e16\u754c\u4e09\u5927\u90e8\u5206\u3002","rank":183,"score":9.9,"status":4},{"id":"ADIGMlAyDTY","name":"\u8be5\u5403\u996d\u4e86","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/6up0mwg4.jpg","tariff":0,"price":0,"terms":"\u751f\u6d3b\u6210\u957f,\u81ea\u7136\u77e5\u8bc6","tags":"\u98df\u7269\u94fe,\u8718\u86db,\u732b,\u5b9d\u8d1d\u5f00\u5fc3,\u7ed8\u672c","performer":"\u53e3\u888b\u6545\u4e8b \u5409\u7f8e\u5e7c\u6559\u96c6\u56e2","author":"[\u82f1]\u6731\u6069.\u83ab\u8389","age_from":2,"age_to":7,"comment":"\u628a\u539f\u672c\u67af\u71e5\u4e4f\u5473\u7684\u79d1\u666e\u77e5\u8bc6\u878d\u5165\u5230\u4e86\u6709\u8da3\u7684\u6545\u4e8b\u4e2d\uff0c\u8ba9\u5b69\u5b50\u77e5\u9053\u4e86\u8718\u86db\u5403\u82cd\u8747\u3001\u5c0f\u9e1f\u5403\u8718\u86db\u3001\u5c0f\u732b\u5403\u5c0f\u9e1f\u7684\u81ea\u7136\u89c4\u5f8b\u2026\u2026\u540c\u65f6\uff0c\u53e3\u871c\u8179\u5251\u7684\u8718\u86db\uff0c\u61a8\u50bb\u7684\u5c0f\u9e1f\uff0c\u81ea\u4ee5\u4e3a\u662f\u7684\u5c0f\u732b\u7b49\u5404\u79cd\u89d2\u8272\u7684\u5f62\u8c61\u90fd\u6829\u6829\u5982\u751f\uff0c\u8ba9\u5b69\u5b50\u5bf9\u6545\u4e8b\u548c\u4e3b\u9898\u4eba\u7269\u7684\u7406\u89e3\u66f4\u4e3a\u900f\u5f7b\u3002","description":"\u5403\u996d\u7684\u65f6\u95f4\u5230\u4e86\u2026\u2026\u732b\u54aa\u9965\u997f\u5730\u770b\u7740\u5c0f\u9e1f\uff1b\u5c0f\u9e1f\u9965\u997f\u5730\u76ef\u7740\u8718\u86db\uff1b\u8718\u86db\u4e5f\u540c\u6837\u9965\u997f\u7684\u6ce8\u89c6\u7740\u82cd\u8747\u3002\u6700\u540e\uff0c\u7a76\u7adf\u6709\u6ca1\u6709\u4eba\u6ca6\u4e3a\u4e86\u522b\u4eba\u9910\u684c\u4e0a\u7684\u7f8e\u98df\u5462\u2026\u2026","rank":182,"score":5.2,"status":4},{"id":"ADIGPlA1DTQ","name":"\u591a\u7eb3\u767e\u79d1\u7ed8\u672c\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/xgs0bhnx.jpg","tariff":0,"price":0,"terms":"\u513f\u7ae5\u9605\u8bfb\u4ece\u542c\u5f00\u59cb,\u767e\u79d1\u77e5\u8bc6,\u79d1\u5b66\u542f\u8499","tags":"\u767e\u79d1,\u591a\u7eb3,\u8eab\u4f53,\u52a8\u7269,\u8ba4\u77e5","performer":"\u53e3\u888b\u6545\u4e8b \u591a\u7eb3","author":"\u591a\u7eb3","age_from":3,"age_to":10,"comment":"","description":"\u591a\u7eb3\u5b66\u767e\u79d1\u7cfb\u5217\uff0c\u5305\u542b\u5e2e\u5b9d\u5b9d\u8ba4\u8bc6\u81ea\u6211\u3001\u6d77\u91cc\u7684\u79d8\u5bc6\u3001\u53ef\u7231\u7684\u52a8\u7269\u4e16\u754c\u4e09\u5927\u90e8\u5206\u3002","rank":328,"score":8.6,"status":0},{"id":"ADwGMVA2DT0","name":"\u718a\u7238\u7238\u7684\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48 1","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/9qojo9ur.jpg","tariff":0,"price":0,"terms":"\u767e\u79d1\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u718a\u7238\u7238,\u79d1\u666e\u77e5\u8bc6,\u65e5\u5e38\u77e5\u8bc6,\u81ea\u7136\u77e5\u8bc6","performer":"\u53e3\u888b\u6545\u4e8b \u718a\u7238\u7238","author":"\u718a\u7238\u7238","age_from":3,"age_to":12,"comment":"","description":"\u300a\u718a\u7238\u7238\u7684\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48\u300b\u7cfb\u5217\uff0c\u662f\u56fd\u5185\u9996\u521b\u7684\u4e92\u52a8\u95ee\u7b54\u7c7b\u667a\u6167\u542f\u8499\u8282\u76ee\u3002\r\n\u8ba9\u5b69\u5b50\u8d8a\u542c\u8d8a\u7231\u95ee\uff0c\u8d8a\u95ee\u8d8a\u806a\u660e\u3002\u6765\u81ea\u5b69\u5b50\u771f\u5b9e\u63d0\u95ee\uff0c\u539f\u521b\u4e92\u52a8\u95ee\u7b54\u6545\u4e8b\u3002\r\n3-12\u5c81\uff0c\u5f53\u5b69\u5b50\u95ee\u51fa\u7b2c\u4e00\u4e2a\u4e3a\u4ec0\u4e48\uff0c\u597d\u5947\u5fc3\u5f00\u59cb\u840c\u82bd\u3002\u5982\u679c\u5bb6\u957f\u6ca1\u80fd\u6b63\u786e\u5730\u5f15\u5bfc\u548c\u57f9\u517b\uff0c\u90a3\u5b69\u5b50\u7684\u597d\u5947\u5fc3\u5c06\u6e10\u6e10\u6cef\u706d\uff0c\u8f93\u5728\u8d77\u8dd1\u7ebf\u4e0a\u3002\r\n\u4e00\u4e2a\u62e5\u6709\u597d\u5947\u5fc3\u7684\u4eba\uff0c\u5c31\u50cf\u62e5\u6709\u6e90\u6e90\u4e0d\u65ad\u7684\u80fd\u91cf\u53bb\u5c1d\u8bd5\u3001\u63a2\u7d22\u548c\u5b66\u4e60\u3002\u67d0\u79cd\u7a0b\u5ea6\u4e0a\u8bf4\uff0c\u597d\u5947\u5fc3\u624d\u662f\u4e00\u4e2a\u4eba\u6700\u5927\u7684\u7ade\u4e89\u529b\u3002\r\n\u597d\u5947\u5fc3\u6539\u53d8\u4e16\u754c\uff0c\u8ba9\u6211\u4eec\u4ee5\u4fdd\u62a4\u597d\u5947\u5fc3\u7684\u65b9\u5f0f\u6765\u6539\u53d8\u4e16\u754c\u3002","rank":209,"score":9.2,"status":4},{"id":"ADwGMVA3DTU","name":"\u718a\u7238\u7238\u7684\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e482","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/p3avdi67.jpg","tariff":0,"price":0,"terms":"\u767e\u79d1\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u718a\u7238\u7238,\u79d1\u666e\u77e5\u8bc6,\u65e5\u5e38\u77e5\u8bc6,\u81ea\u7136\u77e5\u8bc6","performer":"\u53e3\u888b\u6545\u4e8b \u718a\u7238\u7238","author":"\u718a\u7238\u7238","age_from":3,"age_to":12,"comment":"","description":"\u300a\u718a\u7238\u7238\u7684\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48\u300b\u7cfb\u5217\uff0c\u662f\u56fd\u5185\u9996\u521b\u7684\u4e92\u52a8\u95ee\u7b54\u7c7b\u667a\u6167\u542f\u8499\u8282\u76ee\u3002\r\n\u8ba9\u5b69\u5b50\u8d8a\u542c\u8d8a\u7231\u95ee\uff0c\u8d8a\u95ee\u8d8a\u806a\u660e\u3002\u6765\u81ea\u5b69\u5b50\u771f\u5b9e\u63d0\u95ee\uff0c\u539f\u521b\u4e92\u52a8\u95ee\u7b54\u6545\u4e8b\u3002\r\n3-12\u5c81\uff0c\u5f53\u5b69\u5b50\u95ee\u51fa\u7b2c\u4e00\u4e2a\u4e3a\u4ec0\u4e48\uff0c\u597d\u5947\u5fc3\u5f00\u59cb\u840c\u82bd\u3002\u5982\u679c\u5bb6\u957f\u6ca1\u80fd\u6b63\u786e\u5730\u5f15\u5bfc\u548c\u57f9\u517b\uff0c\u90a3\u5b69\u5b50\u7684\u597d\u5947\u5fc3\u5c06\u6e10\u6e10\u6cef\u706d\uff0c\u8f93\u5728\u8d77\u8dd1\u7ebf\u4e0a\u3002\r\n\u4e00\u4e2a\u62e5\u6709\u597d\u5947\u5fc3\u7684\u4eba\uff0c\u5c31\u50cf\u62e5\u6709\u6e90\u6e90\u4e0d\u65ad\u7684\u80fd\u91cf\u53bb\u5c1d\u8bd5\u3001\u63a2\u7d22\u548c\u5b66\u4e60\u3002\u67d0\u79cd\u7a0b\u5ea6\u4e0a\u8bf4\uff0c\u597d\u5947\u5fc3\u624d\u662f\u4e00\u4e2a\u4eba\u6700\u5927\u7684\u7ade\u4e89\u529b\u3002\r\n\u597d\u5947\u5fc3\u6539\u53d8\u4e16\u754c\uff0c\u8ba9\u6211\u4eec\u4ee5\u4fdd\u62a4\u597d\u5947\u5fc3\u7684\u65b9\u5f0f\u6765\u6539\u53d8\u4e16\u754c\u3002","rank":199,"score":9,"status":4}]},"retcode":0})
# # {"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0}]},"retcode":0}
#
#     list_data= {"data":{"cats":[{"id":6707,"name":"\u513f\u6b4c","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/qx7houcn.png","age_scope":"-1-8","parent":0},{"id":6708,"name":"\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/vfj0epki.png","age_scope":"1+","parent":0},{"id":6948,"name":"\u97f3\u4e50","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/fk36owk7.png","age_scope":"0+","parent":0},{"id":7156,"name":"\u82f1\u8bed","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/9rlfhx3f.png","age_scope":"1+","parent":0},{"id":7716,"name":"\u56fd\u5b66","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/9y0vcvet.png","age_scope":"0+","parent":0},{"id":16815,"name":"\u79d1\u666e","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/9ez08ldk.png","age_scope":"3+","parent":0},{"id":17164,"name":"\u540d\u8457","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/4ajjhpe0.png","age_scope":"5+","parent":0},{"id":17176,"name":"\u80ce\u6559","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/aetyh99o.png","age_scope":"-1-1","parent":0},{"id":17466,"name":"\u7ed8\u672c","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/e3f42br0.png","age_scope":"1-8","parent":0},{"id":19205,"name":"\u5386\u53f2","icon":"http:\/\/img.ilisten.idaddy.cn\/f\/h\/9\/c90txxr7.png","age_scope":"4+","parent":0}]},"retcode":0}
#     cats= list_data['data']['cats']
#     cats_id = []
#     for i in cats:
#         print(i['id'])
#         cats_id.append(i['id'])
#     print(cats_id)
#     aaaa={"data":{"works":[{"id":"ADQGMw","name":"\u667a\u6597\u5927\u7070\u72fc","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/4uvppsw4.jpg","tariff":0,"price":0,"terms":"\u52a8\u7269\u6545\u4e8b,\u7537\u5b69\u6545\u4e8b","tags":"\u513f\u7ae5\u6545\u4e8b,\u5927\u7070\u72fc","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":6,"comment":"","description":"\u8fd9\u4e2a\u7ae5\u8bdd\u6545\u4e8b\u8bb2\u8ff0\u7684\u662f\u5c0f\u767d\u5154\u3001\u7b28\u7b28\u718a\u548c\u6dd8\u6c14\u72d7\u7b49\u5c0f\u52a8\u7269\u4eec\u667a\u6597\u5927\u7070\u72fc\u4ece\u800c\u8131\u9669\u7684\u6545\u4e8b\uff0c\u6559\u5bfc\u5c0f\u670b\u53cb\u4eec\u9047\u5230\u574f\u4eba\u65f6\u8981\u591a\u52a8\u8111\u7b4b\uff0c\u505a\u673a\u667a\u52c7\u6562\u7684\u597d\u5b69\u5b50\u3002","rank":259,"score":9.3,"status":0},{"id":"ADQGMQ","name":"\u771f\u5047\u5c0f\u767d\u5154","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/yryqbjn4.jpg","tariff":0,"price":0,"terms":"\u52a8\u7269\u6545\u4e8b,2013\u5e74\u5ea6\u7cbe\u9009\u96c6","tags":"\u5c0f\u767d\u5154,\u52a8\u7269\u6545\u4e8b","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":6,"comment":"","description":"\u5c0f\u72d0\u72f8\u5ac9\u5992\u5f53\u7ecf\u7406\u7684\u5c0f\u767d\u5154\u4fbf\u53d8\u8eab\u6210\u5c0f\u767d\u5154\u7684\u6a21\u6837\uff0c\u5c31\u8fde\u718a\u6cd5\u5b98\u90fd\u5224\u65ad\u4e0d\u51fa\u8c01\u662f\u771f\u7684\uff0c\u8c01\u662f\u5047\u7684\u3002\u6700\u540e\u53eb\u6765\u4e86\u5154\u5988\u5988\u3002\u5979\u80fd\u8ba4\u51fa\u6765\u8c01\u662f\u81ea\u5df1\u7684\u5b69\u5b50\u5417\uff1f","rank":249,"score":8.8,"status":0},{"id":"ADQGP1A1","name":"\u8d1d\u591a\u82ac\u2014\u81f4\u7231\u4e3d\u4e1d","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/ku6t9vr0.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac,\u81f4\u7231\u4e3d\u4e1d","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":1,"comment":"","description":"\u300a\u732e\u7ed9\u7231\u4e3d\u4e1d\u300b\uff08f\u00fcr Elise\uff09\u662f\u8d1d\u591a\u82ac\u521b\u4f5c\u7684\u4e00\u9996\u5176\u94a2\u7434\u5c0f\u54c1\u3002\u8d1d\u591a\u82ac\u662f\u96c6\u897f\u65b9\u53e4\u5178\u6d3e\u4e4b\u5927\u6210\uff0c\u5f00\u6d6a\u6f2b\u4e50\u6d3e\u4e4b\u5148\u6cb3\u7684\u4f1f\u5927\u4f5c\u66f2\u5bb6\u3002\u4eba\u4eec\u90fd\u6bd4\u8f83\u719f\u6089\u4ed6\u7684\u4ea4\u54cd\u66f2\u3001\u534f\u594f\u66f2\u3001\u5ba4\u5185\u4e50\u548c\u6b4c\u5267\u7b49\u5927\u578b\u4f5c\u54c1\uff0c\u4f46\u662f\uff0c\u4ed6\u7684\u4e3a\u6570\u4e0d\u591a\u7684\u5668\u4e50\u5c0f\u54c1\uff0c\u4e5f\u540c\u6837\u7ed9\u4eba\u7559\u4e0b\u4e86\u6df1\u523b\u7684\u5370\u8c61\u3002\u94a2\u7434\u5c0f\u54c1\u300a\u732e\u7ed9\u7231\u4e3d\u4e1d\u300b\u5c31\u662f\u5176\u4e2d\u6bd4\u8f83\u8457\u540d\u7684\u4e00\u9996\u3002\u4f46\u4e50\u8c31\u53d1\u73b0\u4e8e1867\u5e74\uff0c\u56e0\u6b64\u8d1d\u591a\u82ac\u751f\u524d\u5e76\u672a\u53d1\u8868\u3002","rank":199,"score":8.9,"status":0},{"id":"ADQGP1A2","name":"\u6b22\u4e50\u9882","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/3ws8i9cv.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50,\u8d77\u5e8a\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac,\u6b22\u4e50\u9882,\u97f3\u4e50\u542f\u8499","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u6b22\u4e50\u9882\u300b\uff0c\u53c8\u79f0\u300a\u5feb\u4e50\u9882\u300b\uff08\u5fb7\u8bed\u4e3aAn die Freude\uff09\uff0c\u662f\u57281785\u5e74\u7531\u5fb7\u56fd\u8bd7\u4eba\u5e2d\u52d2\u6240\u5199\u7684\u8bd7\u6b4c\u3002\u8d1d\u591a\u82ac\u4e3a\u4e4b\u8c31\u66f2\uff0c\u6210\u4e3a\u4ed6\u7684\u7b2c\u4e5d\u4ea4\u54cd\u66f2\u7b2c\u56db\u4e50\u7ae0\u7684\u4e3b\u8981\u90e8\u4efd\uff0c\u5305\u542b\u56db\u72ec\u7acb\u58f0\u90e8\u3001\u5408\u5531\u3001\u4e50\u56e2\u3002\u800c\u8fd9\u7531\u8d1d\u591a\u82ac\u6240\u8c31\u66f2\u7684\u97f3\u4e50\uff08\u4e0d\u5305\u542b\u6587\u5b57\uff09\u6210\u4e3a\u4e86\u73b0\u4eca\u6b27\u6d32\u8054\u76df\u7684\u76df\u6b4c\u3002\u6b22\u4e50\u9882\uff0c\u73b0\u5728\u6700\u5e38\u63d0\u8d77\u7684\u662f\u8d1d\u591a\u82ac\u7684\u97f3\u4e50\u4f5c\u54c1\u3001\u5e2d\u52d2\u7684\u8bd7\u6b4c\u3001\u80e1\u98ce\u957f\u8bd7\u300a\u65f6\u95f4\u5f00\u59cb\u4e86\u300b\u4e2d\u7684\u7b2c\u4e00\u4e50\u7ae0\u548c\u4e00\u90e8\u79d1\u5e7b\u5c0f\u8bf4\u540d\u5b57\uff0c\u5c24\u5176\u662f\u524d\u4e24\u8005\uff0c\u66f4\u4e3a\u4eba\u4eec\u719f\u77e5\u3002","rank":245,"score":9,"status":0},{"id":"ADQGP1Ax","name":"\u5c0f\u661f\u661f\u53d8\u594f\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/rueimdd3.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u83ab\u624e\u7279,\u5c0f\u661f\u661f","performer":"\u53e3\u888b\u6545\u4e8b \u83ab\u624e\u7279","author":"\u83ab\u624e\u7279","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u5c0f\u661f\u661f\u53d8\u594f\u66f2\u300b\u662f\u83ab\u624e\u7279\u7684\u4f5c\u54c1\uff0c\u662f\u4e00\u9996\u810d\u7099\u4eba\u53e3\u7684\u540d\u66f2\uff0c\u539f\u9898\u4e3a\u201c \u554a\uff01\u5988\u5988\uff0c\u6211\u8981\u544a\u8bc9\u4f60\u201d\u7684\u5341\u4e8c\u6bb5\u53d8\u594f\u66f2\u3002\u6b64\u66f2\u662f1778\u5e74\u521d\u590f\uff0c\u83ab\u624e\u7279\u505c\u7559\u5df4\u9ece\u65f6\uff0c\u4e3a\u4e00\u4f4d\u5973\u5f1f\u5b50\u800c\u4f5c\u7684\u3002\u97f3\u4e50\u4e3b\u9898\u51fa\u81ea\u4e00\u9996\u53e4\u8001\u7684\u6b27\u6d32\u6c11\u8c23\uff0c\u6709\u597d\u51e0\u4e2a\u56fd\u5bb6\u7528\u4e0d\u540c\u7684\u8bed\u8a00\u6b4c\u5531\u8fc7\u3002\u5728\u6211\u4eec\u4e2d\u56fd\u5c31\u6709\u90a3\u9996\u201c \u4e00\u95ea\u4e00\u95ea\u4eae\u6676\u6676\uff0c\u6ee1\u5929\u90fd\u662f\u5c0f\u661f\u661f\u201d\u3002\u8fd9\u4e2a\u4e3b\u9898\u7684\u8282\u594f\u4e0e\u65cb\u5f8b\u5355\u7eaf\u8d28\u6734\uff0c\u83ab\u624e\u7279\u4e3a\u5b83\u914d\u4e0a\u5341\u4e8c\u6bb5\u53ef\u7231\u53c8\u5bcc\u6709\u9b45\u529b\u7684\u53d8\u594f\uff0c\u4e50\u58f0\u4e00\u76f4\u81ea\u7136\u800c\u6109\u5feb\u7684\u6d41\u6dcc\u7740\u3002","rank":187,"score":9.2,"status":0},{"id":"ADQGPlA0","name":"\u73a9\u5177\u5175\u8fdb\u884c\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/768h5b2w.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u83ab\u624e\u7279,\u73a9\u5177\u5175","performer":"\u53e3\u888b\u6545\u4e8b \u83ab\u624e\u7279","author":"\u83ab\u624e\u7279","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\u53c8\u79f0\u300a\u73a9\u5177\u5175\u7684\u6e38\u884c\u300b\u3002\u5168\u66f2\u5171\u957f\u56db\u5206\u949f\u3002\u7531\u5fb7\u56fd\u4f5c\u66f2\u5bb6\u83b1\u6602\u00b7\u8036\u585e\u5c14\uff081871\u2014\u20141942\uff09\u4f5c\u4e8e 1901\u5e74\u524d\u540e\uff0c\u7ba1\u5f26\u4e50\u66f2\u3002\u83b1\u6602\u00b7\u8036\u585e\u5c14\u5199\u7684\u8fd9\u9996\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\u662f\u6d41\u884c\u6700\u5e7f\u7684\u4e00\u9996\u3002\u4ee5\u73a9\u5177\u5175\u4e3a\u9898\u6750\u7684\u513f\u7ae5\u6b4c\u66f2\uff0c\u83b1\u6602\u00b7\u8036\u585e\u5c14\u751f\u4e8e1871\u5e74\u3002\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\u636e\u8bf4\u662f\u4f5c\u66f2\u5bb6\u56de\u5fc6\u8d77\u5c0f\u65f6\u5019\u505a\u7684\u4e00\u4e2a\u751c\u871c\u7684\u68a6\uff0c\u7528\u68a6\u5883\u91cc\u7684\u6545\u4e8b\u5199\u6210\u3002\u5185\u5bb9\u662f\u8fd9\u6837\u7684\uff1a\u665a\u4e0a\uff0c\u5c0f\u4e3b\u4eba\u7761\u89c9\u4e86\uff0c\u73a9\u5177\u5175\u4eec\u4e00\u4e2a\u4e2a\u4ece\u73a9\u5177\u7bb1\u91cc\u5077\u5077\u722c\u4e86\u51fa\u6765\u3002\u4ed6\u4eec\u5148\u6392\u5217\u6210\u6574\u9f50\u7684\u961f\u4f0d\u6e38\u884c\uff0c\u540e\u6765\u53c8\u6253\u95f9\u5b09\u800d\u3002\u6b63\u5f53\u5929\u521a\u8499\u4eae\u7684\u65f6\u5019\uff0c\u5c0f\u4e3b\u4eba\u9192\u4e86\uff0c\u73a9\u5177\u5175\u4eec\u60ca\u614c\u7684\u9003\u56de\u73a9\u5177\u7bb1\u5b50\u91cc\u3002\u5c0f\u4e3b\u4eba\u8d77\u5e8a\uff0c\u6253\u5f00\u7bb1\u5b50\u4e00\u770b\uff0c\u73a9\u5177\u4eec\u4e1c\u5012\u897f\u6b6a\u5730\u8eba\u5728\u91cc\u9762\u3002\u5475\uff01\u539f\u6765\u521a\u624d\u662f\u4e00\u573a\u7f8e\u4e3d\u7684\u68a6\u3002 \u8fd9\u9996\u4e50\u66f2\u5bf9\u5b69\u5b50\u6765\u8bf4\uff0c\u662f\u57f9\u517b\u6b23\u8d4f\u97f3\u4e50\u5174\u8da3\u7684\u6700\u597d\u65b9\u5f0f\u4e4b\u4e00\uff0c\u5b69\u5b50\u4eec\u5728\u542c\u97f3\u4e50\u8fc7\u7a0b\u4e2d\u83b7\u5f97\u5feb\u4e50\uff0c\u5524\u8d77\u4ed6\u4eec\u5bf9\u97f3\u4e50\u7684\u70ed\u7231\u3002\u901a\u8fc7\u6b23\u8d4f\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\uff0c\u8ba9\u5b69\u5b50\u4eec\u4f53\u4f1a\u96c4\u58ee\u6709\u529b\u800c\u53c8\u6b22\u5feb\u6d3b\u6cfc\u7684\u97f3\u4e50\u60c5\u7eea\uff0c\u6fc0\u53d1\u4ed6\u4eec\u8046\u542c\u97f3\u4e50\u7684\u60c5\u7eea\u3002\u5728\u8fd9\u6837\u7684\u5b66\u4e60\u4e2d\uff0c\u4f7f\u97f3\u4e50\u5145\u6ee1\u4e86\u751f\u547d\u7684\u6d3b\u529b\uff0c\u6563\u53d1\u7740\u6d53\u6d53\u7684\u4eba\u6587\u6c14\u606f\u3002\u5bf9\u4e8e\u5e74\u957f\u8005\u6765\u8bf4\uff0c\u8046\u542c\u8fd9\u9996\u97f3\u4e50\u4e5f\u662f\u540c\u6837\u611f\u53d7\u5230\u827a\u672f\u7684\u718f\u9676\uff0c\u91cd\u56de\u5230\u9752\u5c11\u5e74\u65f6\u4ee3\u7684\u751f\u547d\u6d3b\u529b\u3002","rank":184,"score":7.8,"status":0},{"id":"ADcGNlA2","name":"\u8212\u4f2f\u7279\u2014\u5706\u821e\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/k1affvzb.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8212\u4f2f\u7279","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u8212\u4f2f\u7279","age_from":-1,"age_to":16,"comment":"","description":"\u5f17\u6717\u8328\u00b7\u8212\u4f2f\u7279\uff08Franz Seraphicus Peter Schubert\uff0c1797\u5e741\u670831\u65e5\uff0d1828\u5e7411\u670819\u65e5\uff09\u662f\u5965\u5730\u5229\u4f5c\u66f2\u5bb6\uff0c\u4ed6\u662f\u65e9\u671f\u6d6a\u6f2b\u4e3b\u4e49\u97f3\u4e50\u7684\u4ee3\u8868\u4eba\u7269\uff0c\u4e5f\u88ab\u8ba4\u4e3a\u662f\u53e4\u5178\u4e3b\u4e49\u97f3\u4e50\u7684\u6700\u540e\u4e00\u4f4d\u5de8\u5320\u3002","rank":184,"score":9.6,"status":0},{"id":"ADcGNlAw","name":"ABC Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/78qt3tk9.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,2013\u5e74\u5ea6\u7cbe\u9009\u96c6,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,ABC\u6b4c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":2,"age_to":6,"comment":"","description":"\u53c8\u79f0\u82f1\u6587\u5b57\u6bcd\u6b4c\u6216ABC\u6b4c\uff0c\u662f\u4e16\u754c\u4e0a\u591a\u4e2a\u91c7\u7528\u62c9\u4e01\u5b57\u6bcd\u4f5c\u4e66\u5199\u6587\u5b57\u7684\u56fd\u5bb6\u6240\u901a\u7528\u5b66\u4e60\u5b57\u6bcd\u65f6\u7ecf\u5e38\u5531\u7684\u6b4c\uff0c\u6b4c\u8bcd\u5f88\u7b80\u5355\uff0c\u5c31\u662f26\u4e2a\u82f1\u6587\u5b57\u6bcd\u6309\u987a\u5e8f\u5531\u51fa\u6765\u3002","rank":240,"score":8.6,"status":0},{"id":"ADcGNlAz","name":"Apple Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/6olw552q.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u82f9\u679c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"Apple round, Apple red. \r\nApple juicy, Apple sweet. \r\nApple Apple I love you.\r\nApple sweet I love to eat","rank":238,"score":9.4,"status":0},{"id":"ADcGNlA9","name":"Are You Sleeping","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/uwuk5mi6.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u7761\u89c9,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":0,"age_to":6,"comment":"","description":"\u53e3\u888b\u6545\u4e8b\u662f\u4e2d\u56fd\u77e5\u540d\u7684\u513f\u7ae5\u7cbe\u54c1\u5185\u5bb9\u5e73\u53f0\uff0c\u7531\u5de5\u7a0b\u5e08\u7238\u7238\u8363\u8a89\u51fa\u54c1\u3002\u53e3\u888b\u6545\u4e8b\u81f4\u529b\u4e8e\u4e3a0-12\u5c81\u5b69\u5b50\u63d0\u4f9b\u4f18\u8d28\u7684\u6709\u58f0\u5185\u5bb9\u670d\u52a1\uff0c\u6ee1\u8db3\u5bb6\u957f\u8bb2\u6545\u4e8b\/\u5b9d\u8d1d\u542c\u6545\u4e8b\u7684\u9700\u6c42\u3002\u542c\u513f\u7ae5\u6587\u5b66\u3001\u513f\u6b4c\u7ae5\u8c23\u3001\u7ecf\u5178\u7ae5\u8bdd\u3001\u56fd\u5b66\u542f\u8499\u2026\u2026\u5c31\u7528\u53e3\u888b\u6545\u4e8b\uff01\u53e3\u888b\u6545\u4e8b\uff0c\u5b69\u5b50\u60f3\u542c\u7684\u8fd9\u91cc\u90fd\u6709\uff01","rank":243,"score":8.2,"status":0}]},"retcode":0}
#     print(aaaa)
    a6707= {"data":{"works":[{"id":"ADcGNlAw","name":"ABC Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/78qt3tk9.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,2013\u5e74\u5ea6\u7cbe\u9009\u96c6,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,ABC\u6b4c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":2,"age_to":6,"comment":"","description":"\u53c8\u79f0\u82f1\u6587\u5b57\u6bcd\u6b4c\u6216ABC\u6b4c\uff0c\u662f\u4e16\u754c\u4e0a\u591a\u4e2a\u91c7\u7528\u62c9\u4e01\u5b57\u6bcd\u4f5c\u4e66\u5199\u6587\u5b57\u7684\u56fd\u5bb6\u6240\u901a\u7528\u5b66\u4e60\u5b57\u6bcd\u65f6\u7ecf\u5e38\u5531\u7684\u6b4c\uff0c\u6b4c\u8bcd\u5f88\u7b80\u5355\uff0c\u5c31\u662f26\u4e2a\u82f1\u6587\u5b57\u6bcd\u6309\u987a\u5e8f\u5531\u51fa\u6765\u3002","rank":240,"score":8.6,"status":0},{"id":"ADcGNlAz","name":"Apple Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/6olw552q.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u82f9\u679c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"Apple round, Apple red. \r\nApple juicy, Apple sweet. \r\nApple Apple I love you.\r\nApple sweet I love to eat","rank":238,"score":9.4,"status":0},{"id":"ADcGNlA9","name":"Are You Sleeping","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/uwuk5mi6.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u7761\u89c9,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":0,"age_to":6,"comment":"","description":"\u53e3\u888b\u6545\u4e8b\u662f\u4e2d\u56fd\u77e5\u540d\u7684\u513f\u7ae5\u7cbe\u54c1\u5185\u5bb9\u5e73\u53f0\uff0c\u7531\u5de5\u7a0b\u5e08\u7238\u7238\u8363\u8a89\u51fa\u54c1\u3002\u53e3\u888b\u6545\u4e8b\u81f4\u529b\u4e8e\u4e3a0-12\u5c81\u5b69\u5b50\u63d0\u4f9b\u4f18\u8d28\u7684\u6709\u58f0\u5185\u5bb9\u670d\u52a1\uff0c\u6ee1\u8db3\u5bb6\u957f\u8bb2\u6545\u4e8b\/\u5b9d\u8d1d\u542c\u6545\u4e8b\u7684\u9700\u6c42\u3002\u542c\u513f\u7ae5\u6587\u5b66\u3001\u513f\u6b4c\u7ae5\u8c23\u3001\u7ecf\u5178\u7ae5\u8bdd\u3001\u56fd\u5b66\u542f\u8499\u2026\u2026\u5c31\u7528\u53e3\u888b\u6545\u4e8b\uff01\u53e3\u888b\u6545\u4e8b\uff0c\u5b69\u5b50\u60f3\u542c\u7684\u8fd9\u91cc\u90fd\u6709\uff01","rank":243,"score":8.2,"status":0},{"id":"ADcGNVA0","name":"Do Re Mi","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/6syrladh.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":4,"comment":"","description":"\u300aDo Re Mi\u300b\u662f\u5965\u65af\u5361\u7ecf\u5178\u7535\u5f71\u300aThe Sound of Music\u300b\uff08\u97f3\u4e50\u4e4b\u58f0\uff09\u7684\u4e3b\u9898\u66f2\u4e4b\u4e00\uff0c\u4e5f\u662f\u8457\u540d\u7684\u97f3\u4e50\u542f\u8499\u6b4c\u3002\u662f\u4e3b\u4eba\u516cMaria\uff08\u739b\u5229\u4e9a\uff09\u6559\u6388\u7ed9\u4e03\u4e2a\u5b69\u5b50\u4eec\u7684\u7b2c\u4e00\u9996\u6b4c\uff0c\u540c\u65f6\u4e5f\u6253\u5f00\u4e86\u5b69\u5b50\u4eec\u5728\u519b\u4e8b\u5bb6\u5ead\u7981\u9522\u591a\u5e74\u7684\u6d6a\u6f2b\u548c\u60f3\u8c61\u3002","rank":242,"score":8.8,"status":0},{"id":"ADcGNVA3","name":"Edelweiss","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/axy8eeg3.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u96ea\u7ed2\u82b1","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":16,"comment":"","description":"\u5965\u65af\u5361\u7ecf\u5178\u7535\u5f71\u300a\u97f3\u4e50\u4e4b\u58f0\u300b\u63d2\u66f2\u4e4b\u4e00\uff0cEdelweiss\uff08\u96ea\u7ed2\u82b1\uff09\u751f\u957f\u5728\u745e\u58eb\u963f\u5c14\u5351\u65af\u5c71\u8109\u4e00\u5e26\u3002\u8fd9\u79cd\u82b1\u5728\u963f\u5c14\u5351\u65af\u5c71\u8109\u4e2d\u901a\u5e38\u751f\u957f\u5728\u6d77\u62d41700\u7c73\u4ee5\u4e0a\u7684\u5730\u65b9\uff0c\u7531\u4e8e\u5b83\u53ea\u751f\u957f\u5728\u975e\u5e38\u5c11\u6709\u7684\u5ca9\u77f3\u5730\u8868\u4e0a\uff0c\u56e0\u800c\u6781\u4e3a\u7a00\u5c11 \uff0c\u96ea\u7ed2\u82b1\u662f\u745e\u58eb\u7684\u56fd\u82b1\u8c61\u5f81\u7740\u52c7\u6562\uff0c\u96ea\u7ed2\u82b1\u751f\u957f\u5728\u73af\u5883\u8270\u82e6\u7684\u9ad8\u5c71\u4e0a\uff0c\u5e38\u4eba\u96be\u4ee5\u5f97\u89c1\u5176\u7f8e\u4e3d\u5bb9\u989c\uff0c\u6240\u4ee5\u89c1\u8fc7\u96ea\u7ed2\u82b1\u7684\u4eba\u90fd\u662f\u82f1\u96c4\u3002","rank":183,"score":9,"status":0},{"id":"ADcGNVAx","name":"Good Morning To You","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/5etfvolu.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587","performer":"\u53e3\u888b\u6545\u4e8b Twins","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u8fd9\u9996\u82f1\u6587\u513f\u6b4c\u8282\u594f\u9c9c\u660e\uff0c\u7405\u7405\u4e0a\u53e3\uff0c\u6613\u5ff5\u6613\u8bb0\u6613\u4f20\u3002\u5728\u541f\u5531\u4e2d\uff0c\u4f18\u7f8e\u7684\u65cb\u5f8b\u3001\u548c\u8c10\u7684\u8282\u594f\u3001\u771f\u631a\u7684\u60c5\u611f\u53ef\u4ee5\u7ed9\u513f\u7ae5\u4ee5\u7f8e\u7684\u4eab\u53d7\u548c\u60c5\u611f\u718f\u9676\u3002","rank":245,"score":8.7,"status":0},{"id":"ADcGNVAy","name":"Good Night","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/kglrmgdc.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u665a\u5b89,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"\u300aGood Night\u300b\u662f\u4e00\u9996\u82f1\u6587\u665a\u5b89\u66f2\uff0c\u900f\u8fc7\u8f7b\u76c8\u4e0e\u7ef5\u5bc6\u7684\u7535\u5b50\u97f3\u6548\u4e0e\u751c\u7f8e\u7684\u7ae5\u58f0\u62fc\u51d1\u51fa\u4e00\u7247\u8f7b\u76c8\u4e0e\u67d4\u548c\u7684\u753b\u9762\uff0c\u662f\u4f34\u5b9d\u5b9d\u5165\u7761\u7684\u4f73\u66f2\uff0c\u540c\u65f6\u8fd9\u4e5f\u662f\u4e00\u9996\u5f88\u597d\u7684\u82f1\u8bed\u542f\u8499\u513f\u6b4c\u3002","rank":238,"score":8.2,"status":0},{"id":"ADcGNVA8","name":"Happy Birthday","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/lavns6gr.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u751f\u65e5\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"\u8fd9\u662f\u4e00\u9996\u5927\u5bb6\u90fd\u8033\u719f\u80fd\u8be6\u7684\u4e00\u9996\u6b4c\u66f2\u3002\u6211\u4eec\u8fc7\u751f\u65e5\u7684\u65f6\u5019\uff0c\u90fd\u4f1a\u5531\u4e00\u9996\u300a\u751f\u65e5\u5feb\u4e50\u300b\u3002\u539f\u521b\u4f5c\u8005\u662f\u7f8e\u56fd\u7684\u5e0c\u5c14\u59d0\u59b9\u3002\u8fd9\u9996\u6b4c\u53ef\u4ee5\u8bf4\u662f\u4e16\u754c\u4e0a\u6700\u6d41\u884c\u7684\u8868\u8fbe\u751f\u65e5\u795d\u798f\u7684\u6b4c\u66f2\u4e86\u3002","rank":184,"score":9.6,"status":0},{"id":"ADcGNVA9","name":"Hello Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/o3tj3l2q.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u6253\u62db\u547c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":4,"comment":"","description":"\u53e3\u888b\u6545\u4e8b\u662f\u4e2d\u56fd\u77e5\u540d\u7684\u513f\u7ae5\u7cbe\u54c1\u5185\u5bb9\u5e73\u53f0\uff0c\u7531\u5de5\u7a0b\u5e08\u7238\u7238\u8363\u8a89\u51fa\u54c1\u3002\u53e3\u888b\u6545\u4e8b\u81f4\u529b\u4e8e\u4e3a0-12\u5c81\u5b69\u5b50\u63d0\u4f9b\u4f18\u8d28\u7684\u6709\u58f0\u5185\u5bb9\u670d\u52a1\uff0c\u6ee1\u8db3\u5bb6\u957f\u8bb2\u6545\u4e8b\/\u5b9d\u8d1d\u542c\u6545\u4e8b\u7684\u9700\u6c42\u3002\u542c\u513f\u7ae5\u6587\u5b66\u3001\u513f\u6b4c\u7ae5\u8c23\u3001\u7ecf\u5178\u7ae5\u8bdd\u3001\u56fd\u5b66\u542f\u8499\u2026\u2026\u5c31\u7528\u53e3\u888b\u6545\u4e8b\uff01\u53e3\u888b\u6545\u4e8b\uff0c\u5b69\u5b50\u60f3\u542c\u7684\u8fd9\u91cc\u90fd\u6709\uff01","rank":183,"score":9,"status":0},{"id":"ADcGNFA0","name":"\u82f1\u8bed\u542f\u8499\u7cbe\u9009\u5355\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/bk12lxmg.jpg","tariff":0,"price":0,"terms":"\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033,\u82f1\u8bed\u513f\u6b4c","tags":"\u513f\u6b4c,\u5feb\u4e50,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":6,"comment":"","description":"\u8fd9\u9996\u62c9\u8131\u7ef4\u4e9a\u513f\u6b4c\u5e76\u6ca1\u6709\u4e13\u95e8\u7684\u4f5c\u66f2\u4eba\uff0c\u800c\u662f\u6539\u7f16\u81ea\u4fc4\u56fd\u8457\u540d\u97f3\u4e50\u5bb6\u675c\u90a3\u8036\u592b\u65af\u57fa\u7684\u4f5c\u54c1\u300aMolodejnaya\u300b\u4e2d\u7684\u65cb\u5f8b\uff0c\u81f3\u4e8e\u8bcd\u4f5c\u66f4\u662f\u65e0\u4ece\u8003\u5bdf\uff0c\u56e0\u5176\u7b80\u5355\u987a\u7545\u7684\u65cb\u5f8b\uff0c\u8fc5\u901f\u7ea2\u904d\u5168\u7403\uff0c\u88ab\u65e0\u6570\u4eba\u5f15\u7528\u521b\u4f5c\u3002\u5f53\u7136\uff0c\u5176\u7b80\u6d01\u6b22\u5feb\u800c\u53c8\u6781\u5177\u8282\u594f\u611f\u7684\u7279\u70b9\u4e5f\u80fd\u5f88\u5bb9\u6613\u88ab\u5c0f\u670b\u53cb\u8ddf\u5531\u8d77\u6765\u3002","rank":190,"score":9,"status":0}]},"retcode":0}
    # print(a6707)

    a6708={"data":{"works":[{"id":"ADQGMw","name":"\u667a\u6597\u5927\u7070\u72fc","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/4uvppsw4.jpg","tariff":0,"price":0,"terms":"\u52a8\u7269\u6545\u4e8b,\u7537\u5b69\u6545\u4e8b","tags":"\u513f\u7ae5\u6545\u4e8b,\u5927\u7070\u72fc","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":6,"comment":"","description":"\u8fd9\u4e2a\u7ae5\u8bdd\u6545\u4e8b\u8bb2\u8ff0\u7684\u662f\u5c0f\u767d\u5154\u3001\u7b28\u7b28\u718a\u548c\u6dd8\u6c14\u72d7\u7b49\u5c0f\u52a8\u7269\u4eec\u667a\u6597\u5927\u7070\u72fc\u4ece\u800c\u8131\u9669\u7684\u6545\u4e8b\uff0c\u6559\u5bfc\u5c0f\u670b\u53cb\u4eec\u9047\u5230\u574f\u4eba\u65f6\u8981\u591a\u52a8\u8111\u7b4b\uff0c\u505a\u673a\u667a\u52c7\u6562\u7684\u597d\u5b69\u5b50\u3002","rank":259,"score":9.3,"status":0},{"id":"ADQGMQ","name":"\u771f\u5047\u5c0f\u767d\u5154","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/yryqbjn4.jpg","tariff":0,"price":0,"terms":"\u52a8\u7269\u6545\u4e8b,2013\u5e74\u5ea6\u7cbe\u9009\u96c6","tags":"\u5c0f\u767d\u5154,\u52a8\u7269\u6545\u4e8b","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":6,"comment":"","description":"\u5c0f\u72d0\u72f8\u5ac9\u5992\u5f53\u7ecf\u7406\u7684\u5c0f\u767d\u5154\u4fbf\u53d8\u8eab\u6210\u5c0f\u767d\u5154\u7684\u6a21\u6837\uff0c\u5c31\u8fde\u718a\u6cd5\u5b98\u90fd\u5224\u65ad\u4e0d\u51fa\u8c01\u662f\u771f\u7684\uff0c\u8c01\u662f\u5047\u7684\u3002\u6700\u540e\u53eb\u6765\u4e86\u5154\u5988\u5988\u3002\u5979\u80fd\u8ba4\u51fa\u6765\u8c01\u662f\u81ea\u5df1\u7684\u5b69\u5b50\u5417\uff1f","rank":249,"score":8.8,"status":0},{"id":"AD0GPlAy","name":"\u5988\u5988\u751f\u6c14\u4e86","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/ywp84sp0.jpg","tariff":0,"price":0,"terms":"\u751f\u6d3b\u6545\u4e8b","tags":"\u513f\u7ae5\u6545\u4e8b,\u5988\u5988,\u751f\u6c14","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":6,"comment":"","description":"\u5c31\u5feb\u5230\u5c0f\u5e03\u53ee\u7684\u751f\u65e5\u4e86\uff0c\u4ed6\u60f3\u8981\u7238\u7238\u3001\u5988\u5988\u7ed9\u4ed6\u4e70\u4e0a\u6b21\u5728\u5546\u573a\u91cc\u770b\u89c1\u7684\u90a3\u53ea\u7535\u52a8\u72d7\u3002\u7238\u7238\u3001\u5988\u5988\u4f1a\u7b54\u5e94\u4ed6\u5417\uff1f\u8fd9\u5219\u5c0f\u6545\u4e8b\u57f9\u517b\u5b69\u5b50\u4e0d\u4e71\u8981\u4e1c\u897f\u7684\u597d\u4e60\u60ef\u3002\u8bf7\u5988\u5988\u533a\u522b\u5bf9\u5f85\u5b69\u5b50\u7684\u8981\u6c42\uff0c\u4e0d\u8981\u4e00\u5473\u8fc1\u5c31\u81ea\u5df1\u7684\u5b69\u5b50\uff0c\u8fc7\u5206\u6eba\u7231\u5b69\u5b50\u5bf9\u5b69\u5b50\u5fc3\u7406\u5065\u5eb7\u6210\u957f\u6709\u5bb3\u800c\u65e0\u76ca\u3002","rank":257,"score":7.7,"status":0},{"id":"ADwGMlAw","name":"\u6050\u9f99\u4e3a\u4ec0\u4e48\u4f1a\u6d88\u5931\u5462\uff1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/xggq6p7h.jpg","tariff":0,"price":0,"terms":"\u6050\u9f99\u6545\u4e8b\u5927\u5408\u96c6,\u79d1\u666e\u6545\u4e8b,\u81ea\u7136\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e,\u6050\u9f99","performer":"\u53e3\u888b\u6545\u4e8b \u73b0\u4ee3\u6559\u80b2\u51fa\u7248\u793e","author":"\u73b0\u4ee3\u6559\u80b2\u51fa\u7248\u793e","age_from":3,"age_to":8,"comment":"","description":"\u5c0f\u5144\u59b9\u4fe9\u5bf9\u4e8e\u6050\u9f99\u7684\u6d88\u5931\u539f\u56e0\u975e\u5e38\u597d\u5947\uff0c\u4e8e\u662f\u7238\u7238\u4eca\u665a\u7684\u7761\u524d\u6545\u4e8b\uff0c\u5c31\u662f\u7ed9\u4ed6\u4fe9\u8bb2\u79d1\u5b66\u5bb6\u4eec\u5206\u6790\u7684\u51e0\u4e2a\u53ef\u80fd\u7684\u6050\u9f99\u6d88\u5931\u539f\u56e0\u3002\u5c0f\u670b\u53cb\u4eec\uff0c\u4f60\u4eec\u548c\u8fd9\u5bf9\u5c0f\u5144\u59b9\u4fe9\u4e00\u6837\u5bf9\u6050\u9f99\u611f\u5174\u8da3\u5417\uff1f\u5feb\u6765\u542c\u4ed6\u4eec\u7684\u7238\u7238\u8bb2\u6050\u9f99\u6545\u4e8b\u5427\uff01","rank":245,"score":7.9,"status":0},{"id":"ADwGMlAx","name":"\u5c0f\u6050\u9f99\u662f\u4ece\u4ec0\u4e48\u5730\u65b9\u6765\u7684\uff1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/6zevcjjo.jpg","tariff":0,"price":0,"terms":"\u6050\u9f99\u6545\u4e8b\u5927\u5408\u96c6,\u79d1\u666e\u6545\u4e8b,\u81ea\u7136\u77e5\u8bc6","tags":"\u79d1\u666e,\u6050\u9f99,\u535a\u7269\u9986","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":2,"age_to":7,"comment":"","description":"\u5c0f\u6050\u9f99\u662f\u4ece\u54ea\u91cc\u6765\u7684\u5462\uff1f\u6050\u9f99\u7684\u751f\u6d3b\u72b6\u6001\u53c8\u662f\u600e\u4e48\u6837\u7684\u5462\uff1f\u8fd9\u4e2a\u79d1\u666e\u513f\u7ae5\u6545\u4e8b\u4f1a\u544a\u8bc9\u4f60\u7b54\u6848\u3002","rank":243,"score":8.5,"status":0},{"id":"ADwGMVA9","name":"\u7231\u8fea\u751f\u548c\u7535\u706f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/s1020d49.jpg","tariff":0,"price":0,"terms":"\u540d\u4eba\u6545\u4e8b,\u79d1\u5b66\u77e5\u8bc6","tags":"\u79d1\u5b66\u53d1\u660e,\u7231\u8fea\u751f,\u7535\u706f","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":4,"age_to":8,"comment":"","description":"","rank":183,"score":9,"status":4},{"id":"ADQGN1A9DTI","name":"\u4e0d\u7231\u7761\u89c9\u7684\u5c0f\u7334\u5b50","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/9ow5gusy.jpg","tariff":0,"price":0,"terms":"2013\u5e74\u5ea6\u7cbe\u9009\u96c6,\u513f\u7ae5\u9605\u8bfb\u4ece\u542c\u5f00\u59cb,\u6545\u4e8b\u65c5\u884c\u8bb0,\u7761\u524d\u6545\u4e8b","tags":"\u7334\u5b50,\u52a8\u7269,\u513f\u7ae5\u6545\u4e8b,\u4e0d\u7231\u7761\u89c9","performer":"\u53e3\u888b\u6545\u4e8b \u9c7c\u6dfc\u6dfc","author":"\u6e21\u6e21\u9e1f","age_from":-1,"age_to":5,"comment":"\u4e3b\u64ad\u9c7c\u6dfc\u6dfc\u771f\u60c5\u6f14\u7ece\u7684\u539f\u521b\u7cbe\u54c1\u6545\u4e8b\uff0c\u6b22\u8fce\u5173\u6ce8\u6211\u4eec\u540e\u7eed\u7684\u5176\u4ed6\u539f\u521b\u6545\u4e8b","description":"\u8fd9\u662f\u4e00\u5219\u7ed9\u4e0d\u7231\u7761\u89c9\u7684\u5c0f\u670b\u53cb\u7684\u6545\u4e8b\uff0c\u5982\u679c\u4f60\u603b\u662f\u4e3a\u4e86\u8ba9\u5b69\u5b50\u65e9\u4e9b\u5165\u7761\u4f24\u900f\u4e86\u8111\u7b4b\uff0c\u90a3\u5c31\u8d76\u7d27\u8ba9\u5b69\u5b50\u542c\u542c\u8fd9\u4e2a\u5145\u6ee1\u60f3\u8c61\u529b\u7684\u5b89\u9759\u6545\u4e8b\u5427\uff01","rank":337,"score":9,"status":0},{"id":"ADQGNlA0DTw","name":"\u51b0\u96ea\u5973\u738b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/iiq0dh1c.jpg","tariff":0,"price":0,"terms":"\u51b0\u96ea\u5973\u738b,\u5973\u5b69\u6545\u4e8b,\u7ecf\u5178\u7ae5\u8bdd","tags":"\u5916\u56fd\u7ecf\u5178,\u5973\u5b69\u6545\u4e8b","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u5b89\u5f92\u751f","age_from":3,"age_to":18,"comment":"","description":"\u300a\u96ea\u5973\u738b\u300b\u662f\u5b89\u5f92\u751f\u7ae5\u8bdd\u4f5c\u54c1\u4e2d\u6700\u7ecf\u5178\u7684\u4f5c\u54c1\u4e4b\u4e00\u3002\u7ae5\u8bdd\u4e2d\u8bb2\u8ff0\u4e86\u51b7\u9177\u65e0\u60c5\u7684\u767d\u96ea\u7687\u540e\u5c06\u4e00\u7247\u73bb\u7483\u788e\u7247\u6ce8\u5165\u5c0f\u7537\u5b69\u52a0\u4f0a\u7684\u5185\u5fc3\uff0c\u4ece\u800c\u4f7f\u4ed6\u53d8\u5f97\u548c\u767d\u96ea\u7687\u540e\u4e00\u6837\u51b7\u9177\u65e0\u60c5\u3002\u53e6\u4e00\u4e2a\u5c0f\u5973\u5b69\u683c\u5c14\u8fbe\u662f\u52a0\u4f0a\u7684\u597d\u670b\u53cb\uff0c\u683c\u5c14\u8fbe\u8981\u53bb\u5bfb\u627e\u767d\u96ea\u7687\u540e\u5e76\u89e3\u9664\u52a0\u4f0a\u8eab\u4e0a\u7684\u8bc5\u5492\u3002","rank":293,"score":8.4,"status":0},{"id":"ADQGNlAxDTc","name":"\u5c0f\u732b\u5237\u7259","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/ls3olcl9.jpg","tariff":0,"price":0,"terms":"\u751f\u6d3b\u6545\u4e8b","tags":"\u513f\u7ae5\u6545\u4e8b,\u5237\u7259","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":6,"comment":"","description":"\u5c0f\u732b\u4ece\u732a\u5927\u4f2f\u7684\u7259\u5237\u5e97\u4e70\u4e86\u4e00\u652f\u7259\u5237\u56de\u5bb6\u5237\u7259\uff0c\u5b83\u56de\u5230\u5bb6\u5c31\u5f00\u59cb\u5237\u7259\uff0c\u53ef\u7259\u5374\u51fa\u4e86\u8840\uff0c\u8fd9\u5230\u5e95\u662f\u600e\u4e48\u56de\u4e8b\u5462\uff1f\u8fd9\u4e2a\u5c0f\u6545\u4e8b\u65e8\u5728\u6307\u5bfc\u5b69\u5b50\u6b63\u786e\u5730\u5237\u7259\u3002","rank":241,"score":9.2,"status":0},{"id":"ADQGNVAyDTY","name":"\u72fc\u6765\u4e86\uff08\u5973\u58f0\u7248\uff09","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/vwrvdvwy.jpg","tariff":0,"price":0,"terms":"\u7537\u5b69\u6545\u4e8b,\u7761\u524d\u6545\u4e8b","tags":"\u5bd3\u8a00\u6545\u4e8b,\u8bf4\u8c0e,\u653e\u7f8a\u5a03","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":0,"age_to":6,"comment":"","description":"\u300a\u72fc\u6765\u4e86\u300b\u662f\u4f34\u968f\u5b69\u5b50\u7761\u89c9\u7684\u4e00\u4e2a\u6795\u8fb9\u5bd3\u8a00\u6545\u4e8b\uff0c\u6545\u4e8b\u867d\u7136\u7b80\u5355\uff0c\u4f46\u5bcc\u6709\u6559\u80b2\u610f\u4e49\u3002\u662f\u6c11\u95f4\u53e3\u53e3\u76f8\u4f20\u4e0b\u6765\u7684\uff0c\u6559\u80b2\u5b69\u5b50\u8981\u8bda\u5b9e\uff0c\u4e0d\u8981\u6492\u8c0e\u3002","rank":290,"score":8.7,"status":0}]},"retcode":0}
    # print(a6708)
    a6948 ={"data":{"works":[{"id":"ADQGP1A1","name":"\u8d1d\u591a\u82ac\u2014\u81f4\u7231\u4e3d\u4e1d","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/ku6t9vr0.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac,\u81f4\u7231\u4e3d\u4e1d","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":1,"comment":"","description":"\u300a\u732e\u7ed9\u7231\u4e3d\u4e1d\u300b\uff08f\u00fcr Elise\uff09\u662f\u8d1d\u591a\u82ac\u521b\u4f5c\u7684\u4e00\u9996\u5176\u94a2\u7434\u5c0f\u54c1\u3002\u8d1d\u591a\u82ac\u662f\u96c6\u897f\u65b9\u53e4\u5178\u6d3e\u4e4b\u5927\u6210\uff0c\u5f00\u6d6a\u6f2b\u4e50\u6d3e\u4e4b\u5148\u6cb3\u7684\u4f1f\u5927\u4f5c\u66f2\u5bb6\u3002\u4eba\u4eec\u90fd\u6bd4\u8f83\u719f\u6089\u4ed6\u7684\u4ea4\u54cd\u66f2\u3001\u534f\u594f\u66f2\u3001\u5ba4\u5185\u4e50\u548c\u6b4c\u5267\u7b49\u5927\u578b\u4f5c\u54c1\uff0c\u4f46\u662f\uff0c\u4ed6\u7684\u4e3a\u6570\u4e0d\u591a\u7684\u5668\u4e50\u5c0f\u54c1\uff0c\u4e5f\u540c\u6837\u7ed9\u4eba\u7559\u4e0b\u4e86\u6df1\u523b\u7684\u5370\u8c61\u3002\u94a2\u7434\u5c0f\u54c1\u300a\u732e\u7ed9\u7231\u4e3d\u4e1d\u300b\u5c31\u662f\u5176\u4e2d\u6bd4\u8f83\u8457\u540d\u7684\u4e00\u9996\u3002\u4f46\u4e50\u8c31\u53d1\u73b0\u4e8e1867\u5e74\uff0c\u56e0\u6b64\u8d1d\u591a\u82ac\u751f\u524d\u5e76\u672a\u53d1\u8868\u3002","rank":199,"score":8.9,"status":0},{"id":"ADQGP1A2","name":"\u6b22\u4e50\u9882","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/3ws8i9cv.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50,\u8d77\u5e8a\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac,\u6b22\u4e50\u9882,\u97f3\u4e50\u542f\u8499","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u6b22\u4e50\u9882\u300b\uff0c\u53c8\u79f0\u300a\u5feb\u4e50\u9882\u300b\uff08\u5fb7\u8bed\u4e3aAn die Freude\uff09\uff0c\u662f\u57281785\u5e74\u7531\u5fb7\u56fd\u8bd7\u4eba\u5e2d\u52d2\u6240\u5199\u7684\u8bd7\u6b4c\u3002\u8d1d\u591a\u82ac\u4e3a\u4e4b\u8c31\u66f2\uff0c\u6210\u4e3a\u4ed6\u7684\u7b2c\u4e5d\u4ea4\u54cd\u66f2\u7b2c\u56db\u4e50\u7ae0\u7684\u4e3b\u8981\u90e8\u4efd\uff0c\u5305\u542b\u56db\u72ec\u7acb\u58f0\u90e8\u3001\u5408\u5531\u3001\u4e50\u56e2\u3002\u800c\u8fd9\u7531\u8d1d\u591a\u82ac\u6240\u8c31\u66f2\u7684\u97f3\u4e50\uff08\u4e0d\u5305\u542b\u6587\u5b57\uff09\u6210\u4e3a\u4e86\u73b0\u4eca\u6b27\u6d32\u8054\u76df\u7684\u76df\u6b4c\u3002\u6b22\u4e50\u9882\uff0c\u73b0\u5728\u6700\u5e38\u63d0\u8d77\u7684\u662f\u8d1d\u591a\u82ac\u7684\u97f3\u4e50\u4f5c\u54c1\u3001\u5e2d\u52d2\u7684\u8bd7\u6b4c\u3001\u80e1\u98ce\u957f\u8bd7\u300a\u65f6\u95f4\u5f00\u59cb\u4e86\u300b\u4e2d\u7684\u7b2c\u4e00\u4e50\u7ae0\u548c\u4e00\u90e8\u79d1\u5e7b\u5c0f\u8bf4\u540d\u5b57\uff0c\u5c24\u5176\u662f\u524d\u4e24\u8005\uff0c\u66f4\u4e3a\u4eba\u4eec\u719f\u77e5\u3002","rank":245,"score":9,"status":0},{"id":"ADQGP1Ax","name":"\u5c0f\u661f\u661f\u53d8\u594f\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/rueimdd3.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u83ab\u624e\u7279,\u5c0f\u661f\u661f","performer":"\u53e3\u888b\u6545\u4e8b \u83ab\u624e\u7279","author":"\u83ab\u624e\u7279","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u5c0f\u661f\u661f\u53d8\u594f\u66f2\u300b\u662f\u83ab\u624e\u7279\u7684\u4f5c\u54c1\uff0c\u662f\u4e00\u9996\u810d\u7099\u4eba\u53e3\u7684\u540d\u66f2\uff0c\u539f\u9898\u4e3a\u201c \u554a\uff01\u5988\u5988\uff0c\u6211\u8981\u544a\u8bc9\u4f60\u201d\u7684\u5341\u4e8c\u6bb5\u53d8\u594f\u66f2\u3002\u6b64\u66f2\u662f1778\u5e74\u521d\u590f\uff0c\u83ab\u624e\u7279\u505c\u7559\u5df4\u9ece\u65f6\uff0c\u4e3a\u4e00\u4f4d\u5973\u5f1f\u5b50\u800c\u4f5c\u7684\u3002\u97f3\u4e50\u4e3b\u9898\u51fa\u81ea\u4e00\u9996\u53e4\u8001\u7684\u6b27\u6d32\u6c11\u8c23\uff0c\u6709\u597d\u51e0\u4e2a\u56fd\u5bb6\u7528\u4e0d\u540c\u7684\u8bed\u8a00\u6b4c\u5531\u8fc7\u3002\u5728\u6211\u4eec\u4e2d\u56fd\u5c31\u6709\u90a3\u9996\u201c \u4e00\u95ea\u4e00\u95ea\u4eae\u6676\u6676\uff0c\u6ee1\u5929\u90fd\u662f\u5c0f\u661f\u661f\u201d\u3002\u8fd9\u4e2a\u4e3b\u9898\u7684\u8282\u594f\u4e0e\u65cb\u5f8b\u5355\u7eaf\u8d28\u6734\uff0c\u83ab\u624e\u7279\u4e3a\u5b83\u914d\u4e0a\u5341\u4e8c\u6bb5\u53ef\u7231\u53c8\u5bcc\u6709\u9b45\u529b\u7684\u53d8\u594f\uff0c\u4e50\u58f0\u4e00\u76f4\u81ea\u7136\u800c\u6109\u5feb\u7684\u6d41\u6dcc\u7740\u3002","rank":187,"score":9.2,"status":0},{"id":"ADQGPlA0","name":"\u73a9\u5177\u5175\u8fdb\u884c\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/768h5b2w.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u83ab\u624e\u7279,\u73a9\u5177\u5175","performer":"\u53e3\u888b\u6545\u4e8b \u83ab\u624e\u7279","author":"\u83ab\u624e\u7279","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\u53c8\u79f0\u300a\u73a9\u5177\u5175\u7684\u6e38\u884c\u300b\u3002\u5168\u66f2\u5171\u957f\u56db\u5206\u949f\u3002\u7531\u5fb7\u56fd\u4f5c\u66f2\u5bb6\u83b1\u6602\u00b7\u8036\u585e\u5c14\uff081871\u2014\u20141942\uff09\u4f5c\u4e8e 1901\u5e74\u524d\u540e\uff0c\u7ba1\u5f26\u4e50\u66f2\u3002\u83b1\u6602\u00b7\u8036\u585e\u5c14\u5199\u7684\u8fd9\u9996\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\u662f\u6d41\u884c\u6700\u5e7f\u7684\u4e00\u9996\u3002\u4ee5\u73a9\u5177\u5175\u4e3a\u9898\u6750\u7684\u513f\u7ae5\u6b4c\u66f2\uff0c\u83b1\u6602\u00b7\u8036\u585e\u5c14\u751f\u4e8e1871\u5e74\u3002\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\u636e\u8bf4\u662f\u4f5c\u66f2\u5bb6\u56de\u5fc6\u8d77\u5c0f\u65f6\u5019\u505a\u7684\u4e00\u4e2a\u751c\u871c\u7684\u68a6\uff0c\u7528\u68a6\u5883\u91cc\u7684\u6545\u4e8b\u5199\u6210\u3002\u5185\u5bb9\u662f\u8fd9\u6837\u7684\uff1a\u665a\u4e0a\uff0c\u5c0f\u4e3b\u4eba\u7761\u89c9\u4e86\uff0c\u73a9\u5177\u5175\u4eec\u4e00\u4e2a\u4e2a\u4ece\u73a9\u5177\u7bb1\u91cc\u5077\u5077\u722c\u4e86\u51fa\u6765\u3002\u4ed6\u4eec\u5148\u6392\u5217\u6210\u6574\u9f50\u7684\u961f\u4f0d\u6e38\u884c\uff0c\u540e\u6765\u53c8\u6253\u95f9\u5b09\u800d\u3002\u6b63\u5f53\u5929\u521a\u8499\u4eae\u7684\u65f6\u5019\uff0c\u5c0f\u4e3b\u4eba\u9192\u4e86\uff0c\u73a9\u5177\u5175\u4eec\u60ca\u614c\u7684\u9003\u56de\u73a9\u5177\u7bb1\u5b50\u91cc\u3002\u5c0f\u4e3b\u4eba\u8d77\u5e8a\uff0c\u6253\u5f00\u7bb1\u5b50\u4e00\u770b\uff0c\u73a9\u5177\u4eec\u4e1c\u5012\u897f\u6b6a\u5730\u8eba\u5728\u91cc\u9762\u3002\u5475\uff01\u539f\u6765\u521a\u624d\u662f\u4e00\u573a\u7f8e\u4e3d\u7684\u68a6\u3002 \u8fd9\u9996\u4e50\u66f2\u5bf9\u5b69\u5b50\u6765\u8bf4\uff0c\u662f\u57f9\u517b\u6b23\u8d4f\u97f3\u4e50\u5174\u8da3\u7684\u6700\u597d\u65b9\u5f0f\u4e4b\u4e00\uff0c\u5b69\u5b50\u4eec\u5728\u542c\u97f3\u4e50\u8fc7\u7a0b\u4e2d\u83b7\u5f97\u5feb\u4e50\uff0c\u5524\u8d77\u4ed6\u4eec\u5bf9\u97f3\u4e50\u7684\u70ed\u7231\u3002\u901a\u8fc7\u6b23\u8d4f\u300a\u73a9\u5177\u5175\u8fdb\u884c\u66f2\u300b\uff0c\u8ba9\u5b69\u5b50\u4eec\u4f53\u4f1a\u96c4\u58ee\u6709\u529b\u800c\u53c8\u6b22\u5feb\u6d3b\u6cfc\u7684\u97f3\u4e50\u60c5\u7eea\uff0c\u6fc0\u53d1\u4ed6\u4eec\u8046\u542c\u97f3\u4e50\u7684\u60c5\u7eea\u3002\u5728\u8fd9\u6837\u7684\u5b66\u4e60\u4e2d\uff0c\u4f7f\u97f3\u4e50\u5145\u6ee1\u4e86\u751f\u547d\u7684\u6d3b\u529b\uff0c\u6563\u53d1\u7740\u6d53\u6d53\u7684\u4eba\u6587\u6c14\u606f\u3002\u5bf9\u4e8e\u5e74\u957f\u8005\u6765\u8bf4\uff0c\u8046\u542c\u8fd9\u9996\u97f3\u4e50\u4e5f\u662f\u540c\u6837\u611f\u53d7\u5230\u827a\u672f\u7684\u718f\u9676\uff0c\u91cd\u56de\u5230\u9752\u5c11\u5e74\u65f6\u4ee3\u7684\u751f\u547d\u6d3b\u529b\u3002","rank":184,"score":7.8,"status":0},{"id":"ADcGNlA2","name":"\u8212\u4f2f\u7279\u2014\u5706\u821e\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/k1affvzb.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8212\u4f2f\u7279","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u8212\u4f2f\u7279","age_from":-1,"age_to":16,"comment":"","description":"\u5f17\u6717\u8328\u00b7\u8212\u4f2f\u7279\uff08Franz Seraphicus Peter Schubert\uff0c1797\u5e741\u670831\u65e5\uff0d1828\u5e7411\u670819\u65e5\uff09\u662f\u5965\u5730\u5229\u4f5c\u66f2\u5bb6\uff0c\u4ed6\u662f\u65e9\u671f\u6d6a\u6f2b\u4e3b\u4e49\u97f3\u4e50\u7684\u4ee3\u8868\u4eba\u7269\uff0c\u4e5f\u88ab\u8ba4\u4e3a\u662f\u53e4\u5178\u4e3b\u4e49\u97f3\u4e50\u7684\u6700\u540e\u4e00\u4f4d\u5de8\u5320\u3002","rank":184,"score":9.6,"status":0},{"id":"ADcGM1Az","name":"\u591c\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/fyy7fltk.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8096\u90a6","performer":"\u53e3\u888b\u6545\u4e8b \u8096\u90a6","author":"\u8096\u90a6","age_from":-1,"age_to":16,"comment":"","description":"\u591c\u66f2\u662f\u8096\u90a6\u81ea\u5df1\u521b\u65b0\u7684\u4e00\u79cd\u94a2\u7434\u72ec\u594f\u4f53\u88c1\uff0c\u5b83\u5177\u6709\u51b2\u6de1\u5e73\u548c\uff0c\u5bc2\u9759\u5e7d\u6f9c\u7684\u7279\u70b9\uff0c\u8f7b\u7f13\u4e2d\u5076\u5c14\u900f\u7740\u90a3\u4e48\u4e00\u70b9\u70b9\u6c89\u601d\u3002","rank":185,"score":9.6,"status":0},{"id":"ADcGM1A8","name":"\u6708\u5149","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/705lafcd.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac","performer":"\u53e3\u888b\u6545\u4e8b \u8d1d\u591a\u82ac","author":"\u8d1d\u591a\u82ac","age_from":-1,"age_to":16,"comment":"","description":"\u8d1d\u591a\u82ac\u7684\u8fd9\u4e2a\u66f2\u5b50\u4f5c\u4e8e\u4e00\u516bO\u4e00\u5e74\uff0c\u5f53\u65f6\u4ed6\u6b63\u548c\u6731\u4e3d\u6cd5\u5854\u00b7\u8d35\u6070\u5c14\u7b2c\uff081784\u20141856\uff09\u76f8\u7231\uff0c\u8fd9\u4e2a\u66f2\u5b50\u662f\u732e\u7ed9\u5979\u7684\u3002\u5173\u4e8e\u8fd9\u9996\u66f2\u5b50\uff0c\u5c0f\u5b66\u8bed\u6587\u8bfe\u672c\u4e0a\u8fd8\u6d41\u4f20\u7740\u8d1d\u591a\u82ac\u4e0e\u4e00\u5bf9\u5144\u59b9\u4fe9\u7684\u7f8e\u4e3d\u4f20\u8bf4\u3002","rank":248,"score":9.3,"status":0},{"id":"ADcGM1A9","name":"\u5c0f\u72d7\u5706\u821e\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/bekdgh9l.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8096\u90a6","performer":"\u53e3\u888b\u6545\u4e8b \u8096\u90a6","author":"\u8096\u90a6","age_from":-1,"age_to":16,"comment":"","description":"\u4f20\u8bf4\u8096\u90a6\u7684\u60c5\u4eba\u4e54\u6cbb\u00b7\u6851\u5582\u517b\u7740\u4e00\u6761\u5c0f\u72d7\uff0c\u8fd9\u6761\u5c0f\u72d7\u6709\u8ffd\u9010\u81ea\u5df1\u5c3e\u5df4\u56e2\u56e2\u8f6c\u7684\u201c\u5174\u8da3\u201d\u3002\u8096\u90a6\u4f9d\u7167\u4e54\u6cbb\u00b7\u6851\u7684\u8981\u6c42\uff0c\u628a\u201c\u5c0f\u72d7\u6253\u8f6c\u201d\u7684\u60c5\u666f\u8868\u73b0\u5728\u97f3\u4e50\u4e0a\uff0c\u4f5c\u6210\u4e86\u8fd9\u9996\u4e50\u66f2\u3002","rank":184,"score":9.7,"status":0},{"id":"ADcGMlA0","name":"\u5929\u9e45\u6e56","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/ypm6cijj.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,\u5668\u4e50\u6b23\u8d4f,\u94a2\u7434\u66f2","tags":"\u53e4\u5178\u97f3\u4e50,\u94a2\u7434,\u5929\u9e45\u6e56","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u67f4\u53ef\u592b\u65af","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u5929\u9e45\u6e56\u300b\u662f\u67f4\u53ef\u592b\u65af\u57fa\u6700\u8457\u540d\u7684\u4ee3\u8868\u4f5c\u4e4b\u4e00\uff0c\u539f\u4e3a\u67f4\u79d1\u592b\u65af\u57fa\u4e8e1875\u5e74-1876\u5e74\u95f4\u4e3a\u83ab\u65af\u79d1\u5e1d\u56fd\u6b4c\u5267\u9662\u6240\u4f5c\u7684\u82ad\u857e\u821e\u5267\uff0c\u4e8e1877\u5e742\u670820\u65e5\u5728\u83ab\u65af\u79d1\u5927\u5267\u9662\u9996\u6f14\uff0c\u4e4b\u540e\u4f5c\u66f2\u5bb6\u5c06\u539f\u4f5c\u6539\u7f16\u6210\u4e86\u5728\u97f3\u4e50\u4f1a\u4e0a\u6f14\u594f\u7684\u300a\u5929\u9e45\u6e56\u300b\u7ec4\u66f2\uff0c\u7ec4\u66f2\u51fa\u7248\u4e8e1900\u5e7411\u6708\u3002\u800c\u6574\u90e8\u82ad\u857e\u7684\u4f5c\u54c1\u7f16\u53f7\u4e3aOP.20\u3002\u5929\u9e45\u6e56\u662f\u4e16\u754c\u4e0a\u6700\u51fa\u540d\u7684\u82ad\u857e\u821e\u5267\uff0c\u4e5f\u662f\u6240\u6709\u53e4\u5178\u82ad\u857e\u821e\u56e2\u7684\u4fdd\u7559\u5267\u76ee\u3002","rank":258,"score":9,"status":0},{"id":"ADcGMlA1","name":"\u67f4\u53ef\u592b\u65af\u57fa\u2014\u80e1\u6843\u5939\u5b50\u8fdb\u884c\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/kpb0dbcj.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,2014\u5e74\u5ea6\u7cbe\u9009\u5408\u8f91","tags":"\u53e4\u5178\u97f3\u4e50","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u67f4\u53ef\u592b\u65af\u57fa\u7f16\u5199\u7684\u4e00\u4e2a\u82ad\u857e\u821e\u5267\u3002\u6839\u636e\u970d\u592b\u66fc\u7684\u4e00\u90e8\u53eb\u4f5c\u300a\u80e1\u6843\u5939\u5b50\u4e0e\u8001\u9f20\u738b\u300b\u7684\u6545\u4e8b\u6539\u7f16\u3002\u821e\u5267\u7684\u97f3\u4e50\u5145\u6ee1\u4e86\u5355\u7eaf\u800c\u795e\u79d8\u7684\u795e\u8bdd\u8272\u5f69\uff0c\u5177\u6709\u5f3a\u70c8\u7684\u513f\u7ae5\u97f3\u4e50\u7279\u8272\u3002\u201c\u5723\u8bde\u8282\uff0c\u5973\u5b69\u739b\u4e3d\u5f97\u5230\u4e00\u53ea\u80e1\u6843\u5939\u5b50\u3002\u591c\u665a\uff0c\u5979\u68a6\u89c1\u8fd9\u80e1\u6843\u5939\u5b50\u53d8\u6210\u4e86\u4e00\u4f4d\u738b\u5b50\uff0c\u9886\u7740\u5979\u7684\u4e00\u7fa4\u73a9\u5177\u540c\u8001\u9f20\u5175\u4f5c\u6218\u3002\u540e\u6765\u53c8\u628a\u5979\u5e26\u5230\u679c\u9171\u5c71\uff0c\u53d7\u5230\u7cd6\u679c\u4ed9\u5b50\u7684\u6b22\u8fce\uff0c\u4eab\u53d7\u4e86\u4e00\u6b21\u73a9\u5177\u3001\u821e\u8e48\u548c\u76db\u5bb4\u7684\u5feb\u4e50\u3002\u201d","rank":240,"score":8.3,"status":0}]},"retcode":0}
    # print(a6948)

    a7156={"data":{"works":[{"id":"ADcGNlAw","name":"ABC Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/78qt3tk9.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,2013\u5e74\u5ea6\u7cbe\u9009\u96c6,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,ABC\u6b4c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":2,"age_to":6,"comment":"","description":"\u53c8\u79f0\u82f1\u6587\u5b57\u6bcd\u6b4c\u6216ABC\u6b4c\uff0c\u662f\u4e16\u754c\u4e0a\u591a\u4e2a\u91c7\u7528\u62c9\u4e01\u5b57\u6bcd\u4f5c\u4e66\u5199\u6587\u5b57\u7684\u56fd\u5bb6\u6240\u901a\u7528\u5b66\u4e60\u5b57\u6bcd\u65f6\u7ecf\u5e38\u5531\u7684\u6b4c\uff0c\u6b4c\u8bcd\u5f88\u7b80\u5355\uff0c\u5c31\u662f26\u4e2a\u82f1\u6587\u5b57\u6bcd\u6309\u987a\u5e8f\u5531\u51fa\u6765\u3002","rank":240,"score":8.6,"status":0},{"id":"ADcGNlAz","name":"Apple Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/6olw552q.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u82f9\u679c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"Apple round, Apple red. \r\nApple juicy, Apple sweet. \r\nApple Apple I love you.\r\nApple sweet I love to eat","rank":238,"score":9.4,"status":0},{"id":"ADcGNlA9","name":"Are You Sleeping","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/uwuk5mi6.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u7761\u89c9,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":0,"age_to":6,"comment":"","description":"\u53e3\u888b\u6545\u4e8b\u662f\u4e2d\u56fd\u77e5\u540d\u7684\u513f\u7ae5\u7cbe\u54c1\u5185\u5bb9\u5e73\u53f0\uff0c\u7531\u5de5\u7a0b\u5e08\u7238\u7238\u8363\u8a89\u51fa\u54c1\u3002\u53e3\u888b\u6545\u4e8b\u81f4\u529b\u4e8e\u4e3a0-12\u5c81\u5b69\u5b50\u63d0\u4f9b\u4f18\u8d28\u7684\u6709\u58f0\u5185\u5bb9\u670d\u52a1\uff0c\u6ee1\u8db3\u5bb6\u957f\u8bb2\u6545\u4e8b\/\u5b9d\u8d1d\u542c\u6545\u4e8b\u7684\u9700\u6c42\u3002\u542c\u513f\u7ae5\u6587\u5b66\u3001\u513f\u6b4c\u7ae5\u8c23\u3001\u7ecf\u5178\u7ae5\u8bdd\u3001\u56fd\u5b66\u542f\u8499\u2026\u2026\u5c31\u7528\u53e3\u888b\u6545\u4e8b\uff01\u53e3\u888b\u6545\u4e8b\uff0c\u5b69\u5b50\u60f3\u542c\u7684\u8fd9\u91cc\u90fd\u6709\uff01","rank":243,"score":8.2,"status":0},{"id":"ADcGNVA0","name":"Do Re Mi","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/6syrladh.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":4,"comment":"","description":"\u300aDo Re Mi\u300b\u662f\u5965\u65af\u5361\u7ecf\u5178\u7535\u5f71\u300aThe Sound of Music\u300b\uff08\u97f3\u4e50\u4e4b\u58f0\uff09\u7684\u4e3b\u9898\u66f2\u4e4b\u4e00\uff0c\u4e5f\u662f\u8457\u540d\u7684\u97f3\u4e50\u542f\u8499\u6b4c\u3002\u662f\u4e3b\u4eba\u516cMaria\uff08\u739b\u5229\u4e9a\uff09\u6559\u6388\u7ed9\u4e03\u4e2a\u5b69\u5b50\u4eec\u7684\u7b2c\u4e00\u9996\u6b4c\uff0c\u540c\u65f6\u4e5f\u6253\u5f00\u4e86\u5b69\u5b50\u4eec\u5728\u519b\u4e8b\u5bb6\u5ead\u7981\u9522\u591a\u5e74\u7684\u6d6a\u6f2b\u548c\u60f3\u8c61\u3002","rank":242,"score":8.8,"status":0},{"id":"ADcGNVA3","name":"Edelweiss","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/axy8eeg3.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u96ea\u7ed2\u82b1","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":16,"comment":"","description":"\u5965\u65af\u5361\u7ecf\u5178\u7535\u5f71\u300a\u97f3\u4e50\u4e4b\u58f0\u300b\u63d2\u66f2\u4e4b\u4e00\uff0cEdelweiss\uff08\u96ea\u7ed2\u82b1\uff09\u751f\u957f\u5728\u745e\u58eb\u963f\u5c14\u5351\u65af\u5c71\u8109\u4e00\u5e26\u3002\u8fd9\u79cd\u82b1\u5728\u963f\u5c14\u5351\u65af\u5c71\u8109\u4e2d\u901a\u5e38\u751f\u957f\u5728\u6d77\u62d41700\u7c73\u4ee5\u4e0a\u7684\u5730\u65b9\uff0c\u7531\u4e8e\u5b83\u53ea\u751f\u957f\u5728\u975e\u5e38\u5c11\u6709\u7684\u5ca9\u77f3\u5730\u8868\u4e0a\uff0c\u56e0\u800c\u6781\u4e3a\u7a00\u5c11 \uff0c\u96ea\u7ed2\u82b1\u662f\u745e\u58eb\u7684\u56fd\u82b1\u8c61\u5f81\u7740\u52c7\u6562\uff0c\u96ea\u7ed2\u82b1\u751f\u957f\u5728\u73af\u5883\u8270\u82e6\u7684\u9ad8\u5c71\u4e0a\uff0c\u5e38\u4eba\u96be\u4ee5\u5f97\u89c1\u5176\u7f8e\u4e3d\u5bb9\u989c\uff0c\u6240\u4ee5\u89c1\u8fc7\u96ea\u7ed2\u82b1\u7684\u4eba\u90fd\u662f\u82f1\u96c4\u3002","rank":183,"score":9,"status":0},{"id":"ADcGNVAx","name":"Good Morning To You","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/5etfvolu.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587","performer":"\u53e3\u888b\u6545\u4e8b Twins","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u8fd9\u9996\u82f1\u6587\u513f\u6b4c\u8282\u594f\u9c9c\u660e\uff0c\u7405\u7405\u4e0a\u53e3\uff0c\u6613\u5ff5\u6613\u8bb0\u6613\u4f20\u3002\u5728\u541f\u5531\u4e2d\uff0c\u4f18\u7f8e\u7684\u65cb\u5f8b\u3001\u548c\u8c10\u7684\u8282\u594f\u3001\u771f\u631a\u7684\u60c5\u611f\u53ef\u4ee5\u7ed9\u513f\u7ae5\u4ee5\u7f8e\u7684\u4eab\u53d7\u548c\u60c5\u611f\u718f\u9676\u3002","rank":245,"score":8.7,"status":0},{"id":"ADcGNVAy","name":"Good Night","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/kglrmgdc.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u665a\u5b89,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"\u300aGood Night\u300b\u662f\u4e00\u9996\u82f1\u6587\u665a\u5b89\u66f2\uff0c\u900f\u8fc7\u8f7b\u76c8\u4e0e\u7ef5\u5bc6\u7684\u7535\u5b50\u97f3\u6548\u4e0e\u751c\u7f8e\u7684\u7ae5\u58f0\u62fc\u51d1\u51fa\u4e00\u7247\u8f7b\u76c8\u4e0e\u67d4\u548c\u7684\u753b\u9762\uff0c\u662f\u4f34\u5b9d\u5b9d\u5165\u7761\u7684\u4f73\u66f2\uff0c\u540c\u65f6\u8fd9\u4e5f\u662f\u4e00\u9996\u5f88\u597d\u7684\u82f1\u8bed\u542f\u8499\u513f\u6b4c\u3002","rank":238,"score":8.2,"status":0},{"id":"ADcGNVA8","name":"Happy Birthday","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/lavns6gr.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u751f\u65e5\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":6,"comment":"","description":"\u8fd9\u662f\u4e00\u9996\u5927\u5bb6\u90fd\u8033\u719f\u80fd\u8be6\u7684\u4e00\u9996\u6b4c\u66f2\u3002\u6211\u4eec\u8fc7\u751f\u65e5\u7684\u65f6\u5019\uff0c\u90fd\u4f1a\u5531\u4e00\u9996\u300a\u751f\u65e5\u5feb\u4e50\u300b\u3002\u539f\u521b\u4f5c\u8005\u662f\u7f8e\u56fd\u7684\u5e0c\u5c14\u59d0\u59b9\u3002\u8fd9\u9996\u6b4c\u53ef\u4ee5\u8bf4\u662f\u4e16\u754c\u4e0a\u6700\u6d41\u884c\u7684\u8868\u8fbe\u751f\u65e5\u795d\u798f\u7684\u6b4c\u66f2\u4e86\u3002","rank":184,"score":9.6,"status":0},{"id":"ADcGNVA9","name":"Hello Song","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/o3tj3l2q.jpg","tariff":0,"price":0,"terms":"\u82f1\u8bed\u513f\u6b4c,\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033","tags":"\u513f\u6b4c,\u82f1\u6587,\u6253\u62db\u547c,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":4,"comment":"","description":"\u53e3\u888b\u6545\u4e8b\u662f\u4e2d\u56fd\u77e5\u540d\u7684\u513f\u7ae5\u7cbe\u54c1\u5185\u5bb9\u5e73\u53f0\uff0c\u7531\u5de5\u7a0b\u5e08\u7238\u7238\u8363\u8a89\u51fa\u54c1\u3002\u53e3\u888b\u6545\u4e8b\u81f4\u529b\u4e8e\u4e3a0-12\u5c81\u5b69\u5b50\u63d0\u4f9b\u4f18\u8d28\u7684\u6709\u58f0\u5185\u5bb9\u670d\u52a1\uff0c\u6ee1\u8db3\u5bb6\u957f\u8bb2\u6545\u4e8b\/\u5b9d\u8d1d\u542c\u6545\u4e8b\u7684\u9700\u6c42\u3002\u542c\u513f\u7ae5\u6587\u5b66\u3001\u513f\u6b4c\u7ae5\u8c23\u3001\u7ecf\u5178\u7ae5\u8bdd\u3001\u56fd\u5b66\u542f\u8499\u2026\u2026\u5c31\u7528\u53e3\u888b\u6545\u4e8b\uff01\u53e3\u888b\u6545\u4e8b\uff0c\u5b69\u5b50\u60f3\u542c\u7684\u8fd9\u91cc\u90fd\u6709\uff01","rank":183,"score":9,"status":0},{"id":"ADcGNFA0","name":"\u82f1\u8bed\u542f\u8499\u7cbe\u9009\u5355\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/bk12lxmg.jpg","tariff":0,"price":0,"terms":"\u78e8\u8033\u6735\u82f1\u6587,\u82f1\u6587\u78e8\u8033,\u82f1\u8bed\u513f\u6b4c","tags":"\u513f\u6b4c,\u5feb\u4e50,\u82f1\u6587,\u82f1\u6587\u513f\u6b4c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":6,"comment":"","description":"\u8fd9\u9996\u62c9\u8131\u7ef4\u4e9a\u513f\u6b4c\u5e76\u6ca1\u6709\u4e13\u95e8\u7684\u4f5c\u66f2\u4eba\uff0c\u800c\u662f\u6539\u7f16\u81ea\u4fc4\u56fd\u8457\u540d\u97f3\u4e50\u5bb6\u675c\u90a3\u8036\u592b\u65af\u57fa\u7684\u4f5c\u54c1\u300aMolodejnaya\u300b\u4e2d\u7684\u65cb\u5f8b\uff0c\u81f3\u4e8e\u8bcd\u4f5c\u66f4\u662f\u65e0\u4ece\u8003\u5bdf\uff0c\u56e0\u5176\u7b80\u5355\u987a\u7545\u7684\u65cb\u5f8b\uff0c\u8fc5\u901f\u7ea2\u904d\u5168\u7403\uff0c\u88ab\u65e0\u6570\u4eba\u5f15\u7528\u521b\u4f5c\u3002\u5f53\u7136\uff0c\u5176\u7b80\u6d01\u6b22\u5feb\u800c\u53c8\u6781\u5177\u8282\u594f\u611f\u7684\u7279\u70b9\u4e5f\u80fd\u5f88\u5bb9\u6613\u88ab\u5c0f\u670b\u53cb\u8ddf\u5531\u8d77\u6765\u3002","rank":190,"score":9,"status":0}]},"retcode":0}
    # print(a7156)

    a7716 = {"data":{"works":[{"id":"ADAGN1Aw","name":"\u79cb\u5915","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/8zrs8ohz.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u675c\u7267,\u5c0f\u5b66\u751f,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u675c\u7267","age_from":-1,"age_to":18,"comment":"","description":"\u300a\u79cb\u5915\u300b\u662f\u665a\u5510\u8457\u540d\u8bd7\u4eba\u675c\u7267\u6240\u4f5c\u7684\u4e00\u9996\u810d\u7099\u4eba\u53e3\u7684\u4e03\u8a00\u7edd\u53e5\uff0c\u8fd9\u9996\u8bd7\u5199\u4e00\u4e2a\u5931\u610f\u5bab\u5973\u7684\u5b64\u72ec\u751f\u6d3b\u548c\u51c4\u51c9\u5fc3\u60c5\u3002","rank":185,"score":7.8,"status":0},{"id":"ADAGN1Ay","name":"\u4e5d\u6708\u4e5d\u65e5\u5fc6\u5c71\u4e1c\u5144\u5f1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/a7nul5gj.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u738b\u7ef4,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u738b\u7ef4","age_from":4,"age_to":16,"comment":"","description":"\u5510\u4ee3\u8bd7\u4eba\u738b\u7ef4\u56e0\u8eab\u5728\u5f02\u4e61\uff0c\u91cd\u9633\u8282\u601d\u5ff5\u5bb6\u4e61\u7684\u4eb2\u4eba\u800c\u5199\u4e0b\u7684\u4e00\u9996\u4e03\u8a00\u7edd\u53e5\u3002\u8be5\u8bd7\u4ee5\u76f4\u6292\u601d\u4e61\u4e4b\u60c5\u8d77\u7b14\uff0c\u800c\u540e\u7b14\u5cf0\u4e00\u8f6c\uff0c\u5c06\u601d\u7eea\u62c9\u5411\u6545\u4e61\u7684\u4eb2\u4eba\uff0c\u9065\u60f3\u4eb2\u4eba\u6309\u91cd\u9633\u7684\u98ce\u4fd7\u800c\u767b\u9ad8\u65f6\uff0c\u4e5f\u5728\u60f3\u5ff5\u8bd7\u4eba\u81ea\u5df1\u3002\u8bd7\u610f\u53cd\u590d\u8df3\u8dc3\uff0c\u542b\u84c4\u6df1\u6c89\uff0c\u65e2\u6734\u7d20\u81ea\u7136\uff0c\u53c8\u66f2\u6298\u6709\u81f4\u3002\u8bd7\u4e2d\u7684\u201c\u6bcf\u9022\u4f73\u8282\u500d\u601d\u4eb2\u201d\u662f\u5343\u767e\u5e74\u6765\u5e7f\u4e3a\u6d41\u4f20\u7684\u540d\u53e5\uff0c\u6253\u52a8\u4e86\u65e0\u6570\u6e38\u5b50\u79bb\u4eba\u7684\u601d\u4e61\u4e4b\u5fc3\u3002","rank":193,"score":8,"status":0},{"id":"ADAGN1A8","name":"\u51fa\u585e","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/rob5ddyy.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u738b\u660c\u9f84,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u738b\u660c\u9f84","age_from":5,"age_to":16,"comment":"","description":"\u300a\u51fa\u585e\u300b\uff0c\u662f\u8fb9\u585e\u8bd7\u7684\u8457\u540d\u9898\u76ee\u3002\u4e3b\u8981\u4ee5\u63cf\u5199\u8fb9\u7586\u7684\u519b\u65c5\u751f\u6d3b\u4e0e\u519b\u4e8b\u884c\u52a8\u4e3a\u4e3b\u3002\u6709\u4e00\u5b9a\u7684\u4e3b\u89c2\u6c11\u65cf\u610f\u8bc6\uff0c\u56e0\u4e0e\u5176\u6240\u5904\u5386\u53f2\u65f6\u671f\u53ca\u751f\u5b58\u73af\u5883\u6709\u5173\u3002\u95f4\u63a5\u7684\u8868\u8fbe\u4e86\u6218\u4e89\u7684\u6b8b\u9177\u548c\u5bf9\u548c\u5e73\u751f\u6d3b\u7684\u5411\u5f80\u3002","rank":193,"score":9.1,"status":0},{"id":"ADAGNlA1","name":"\u767b\u9e73\u96c0\u697c\uff08\u7ae5\u58f0\uff09","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/1tbsrygx.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u5510\u8bd7,\u738b\u4e4b\u6da3","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u738b\u4e4b\u6da3","age_from":0,"age_to":6,"comment":"","description":"\u300a\u767b\u9e73\u96c0\u697c\u300b\uff0c\u5510\u8bd7\u540d\uff0c\u4e3a\u9898\u548f\u5c71\u897f\u7701\u6c38\u6d4e\u5e02\u9e73\u96c0\u697c\uff08\u53c8\u540d\u9e73\u9e4a\u697c\uff09\u7684\u7bc7\u7ae0\u3002\u7531\u4e8e\u9e73\u96c0\u697c\u697c\u4f53\u58ee\u89c2\uff0c\u7ed3\u6784\u5947\u7279\uff0c\u6c14\u52bf\u96c4\u4f1f\uff0c\u52a0\u4e4b\u533a\u4f4d\u4f18\u8d8a\uff0c\u98ce\u666f\u79c0\u4e3d\uff0c\u5386\u4ee3\u6587\u4eba\u96c5\u58eb\u3001\u9a9a\u4eba\u58a8\u5ba2\uff0c\u591a\u6765\u767b\u697c\u89c2\u77bb\u3001\u653e\u6b4c\u6292\u6000\uff0c\u5e76\u7559\u4e0b\u8bb8\u591a\u5c45\u9ad8\u4e34\u4e0b\uff0c\u96c4\u89c2\u5927\u6cb3\u7684\u4e0d\u673d\u7bc7\u7ae0\u3002","rank":187,"score":9.3,"status":0},{"id":"ADAGNlA2","name":"\u67ab\u6865\u591c\u6cca","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/svt8q69i.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u5f20\u7ee7,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u5f20\u7ee7","age_from":4,"age_to":16,"comment":"","description":"\u5510\u4ee3\u8457\u540d\u8bd7\u4eba\u5f20\u7ee7\u9014\u7ecf\u5bd2\u5c71\u5bfa\u65f6\uff0c\u5199\u4e86\u5343\u53e4\u540d\u7bc7\u300a\u67ab\u6865\u591c\u6cca\u300b\u3002\u81ea\u4ece\u5f20\u7ee7\u7684\u300a\u67ab\u6865\u591c\u6cca\u300b\u95ee\u4e16\u540e\uff0c\u5bd2\u5c71\u5bfa\u56e0\u6b64\u5c31\u540d\u626c\u5929\u4e0b\uff0c\u6210\u4e3a\u5343\u53e4\u7684\u6e38\u89c8\u80dc\u5730\uff0c\u5c31\u662f\u5728\u65e5\u672c\u4e5f\u662f\u5bb6\u55bb\u6237\u6653\u3002\u4e0d\u4f46\u6211\u56fd\u5386\u4ee3\u5404\u79cd\u5510\u8bd7\u9009\u672c\u548c\u522b\u96c6\u5c06\u5f20\u7ee7\u7684\u300a\u67ab\u6865\u591c\u6cca\u300b\u9009\u5165\uff0c\u8fde\u65e5\u672c\u7684\u5c0f\u5b66\u8bfe\u672c\u4e5f\u8f7d\u6709\u6b64\u8bd7\uff0c\u53ef\u89c1\u8bd7\u540d\u4e4b\u76db\u3002","rank":185,"score":9.9,"status":0},{"id":"ADAGNlA3","name":"\u9759\u591c\u601d","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/bpx9mwdq.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u674e\u767d,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u674e\u767d","age_from":0,"age_to":7,"comment":"","description":"\u300a\u9759\u591c\u601d\u300b\u662f\u4f1f\u5927\u8bd7\u4eba\u674e\u767d\u7684\u4f5c\u54c1\uff0c\u8868\u8fbe\u7684\u662f\u601d\u4e61\u4e4b\u60c5\u3002\u8fd9\u9996\u8bd7\u867d\u7136\u53ea\u6709\u533a\u533a\u4e8c\u5341\u4e2a\u5b57\uff0c\u4f46\u5c31\u6d41\u4f20\u7684\u5e7f\u6cdb\u7a0b\u5ea6\u6765\u8bf4\uff0c\u8fd8\u6ca1\u6709\u4e00\u7bc7\u4f5c\u54c1\u53ef\u4ee5\u4e0e\u4e4b\u6bd4\u80a9\uff0c\u5b83\u51e0\u4e4e\u662f\u5168\u4e16\u754c\u534e\u4eba\u8033\u719f\u80fd\u8be6\u7684\u4e00\u9996\u540d\u7bc7\u3002","rank":240,"score":7.8,"status":0},{"id":"ADAGNlAw","name":"\u548f\u67f3","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/jpxo3u60.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u8d3a\u77e5\u7ae0,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u8d3a\u77e5\u7ae0","age_from":0,"age_to":7,"comment":"","description":"\u8fd9\u9996\u548f\u7269\u8bd7\u5199\u7684\u662f\u65e9\u6625\u4e8c\u6708\u7684\u6768\u67f3\u3002\u8bd7\u4e2d\u501f\u67f3\u6811\u6b4c\u548f\u6625\u98ce\uff0c\u628a\u6625\u98ce\u6bd4\u4f5c\u526a\u5200\uff0c\u8bf4\u5979\u662f\u7f8e\u7684\u521b\u9020\u8005\uff0c\u8d5e\u7f8e\u5979\u88c1\u51fa\u4e86\u6625\u5929\uff01","rank":240,"score":8.8,"status":0},{"id":"ADAGNlAx","name":"\u585e\u4e0b\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/jl8gq549.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u5362\u7eb6,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u5362\u7eb6","age_from":4,"age_to":7,"comment":"","description":"\u8fd9\u662f\u5362\u7eb6\u300a\u585e\u4e0b\u66f2\u300b\u7ec4\u8bd7\u4e2d\u7684\u7b2c\u4e09\u9996\u3002\u5362\u7eb6\u66fe\u4efb\u5e55\u5e9c\u4e2d\u7684\u5143\u5e05\u5224\u5b98\uff0c\u5bf9\u884c\u4f0d\u751f\u6d3b\u6709\u4f53\u9a8c\uff0c\u63cf\u5199\u6b64\u7c7b\u751f\u6d3b\u7684\u8bd7\u6bd4\u8f83\u5145\u5b9e\uff0c\u98ce\u683c\u96c4\u52b2\u3002\u8fd9\u9996\u8bd7\u5199\u5c06\u519b\u96ea\u591c\u51c6\u5907\u7387\u5175\u8ffd\u654c\u7684\u58ee\u4e3e\uff0c\u6c14\u6982\u8c6a\u8fc8\u3002","rank":193,"score":7.4,"status":0},{"id":"ADAGNlAz","name":"\u6ec1\u5dde\u897f\u6da7","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/vooma53a.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u97e6\u5e94\u7269,\u5c0f\u5b66\u751f,\u53e4\u8bd7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u97e6\u5e94\u7269","age_from":6,"age_to":16,"comment":"","description":"\u662f\u4e00\u9996\u8457\u540d\u7684\u5c71\u6c34\u8bd7\uff0c\u662f\u5510\u4ee3\u8bd7\u4eba\u97e6\u5e94\u7269\u6700\u8d1f\u76db\u540d\u7684\u5199\u666f\u4f73\u4f5c\u3002\u4f5c\u8005\u4efb\u6ec1\u5dde\u524c\u53f2\u65f6\uff0c\u6e38\u89c8\u81f3\u6ec1\u5dde\u897f\u6da7\uff0c\u5199\u4e0b\u4e86\u8fd9\u9996\u8bd7\u60c5\u6d53\u90c1\u7684\u5c0f\u8bd7\u3002\u8bd7\u91cc\u5199\u7684\u867d\u7136\u662f\u5e73\u5e38\u7684\u666f\u7269\uff0c\u4f46\u7ecf\u8bd7\u4eba\u7684\u70b9\u67d3\uff0c\u5374\u6210\u4e86\u4e00\u5e45\u610f\u5883\u5e7d\u6df1\u7684\u6709\u97f5\u4e4b\u753b\u3002","rank":185,"score":7,"status":0},{"id":"ADAGNlA9","name":"\u66ae\u6c5f\u541f\uff08\u7ae5\u58f0\uff09","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/2bbcqmyc.jpg","tariff":0,"price":0,"terms":"\u53e4\u8bd7\u7cbe\u9009,\u8bd7\u8bcd\u5531\u8bfb","tags":"\u5510\u8bd7,\u767d\u5c45\u6613","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u767d\u5c45\u6613","age_from":0,"age_to":6,"comment":"","description":"\u5510\u671d\u8bd7\u4eba\u767d\u5c45\u6613\u521b\u4f5c\u7684\u4e00\u9996\u4e03\u7edd\uff0c\u5927\u7ea6\u662f822\u5e74\u767d\u5c45\u6613\u5728\u8d74\u676d\u5dde\u4efb\u523a\u53f2\u7684\u9014\u4e2d\u5199\u7684\u3002\u5f53\u65f6\u671d\u5ef7\u653f\u6cbb\u660f\u6697\uff0c\u725b\u674e\u515a\u4e89\u6fc0\u70c8\uff0c\u8bd7\u4eba\u54c1\u5c3d\u4e86\u671d\u5b98\u7684\u6ecb\u5473\uff0c\u81ea\u6c42\u5916\u4efb\u3002\u8be5\u8bd7\u4ece\u4fa7\u9762\u53cd\u6620\u51fa\u4e86\u4f5c\u8005\u79bb\u5f00\u671d\u5ef7\u540e\u8f7b\u677e\u7545\u5feb\u7684\u5fc3\u60c5\u3002","rank":186,"score":9.6,"status":0}]},"retcode":0}

    a16815 ={"data":{"works":[{"id":"ADwGMlAw","name":"\u6050\u9f99\u4e3a\u4ec0\u4e48\u4f1a\u6d88\u5931\u5462\uff1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/xggq6p7h.jpg","tariff":0,"price":0,"terms":"\u6050\u9f99\u6545\u4e8b\u5927\u5408\u96c6,\u79d1\u666e\u6545\u4e8b,\u81ea\u7136\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e,\u6050\u9f99","performer":"\u53e3\u888b\u6545\u4e8b \u73b0\u4ee3\u6559\u80b2\u51fa\u7248\u793e","author":"\u73b0\u4ee3\u6559\u80b2\u51fa\u7248\u793e","age_from":3,"age_to":8,"comment":"","description":"\u5c0f\u5144\u59b9\u4fe9\u5bf9\u4e8e\u6050\u9f99\u7684\u6d88\u5931\u539f\u56e0\u975e\u5e38\u597d\u5947\uff0c\u4e8e\u662f\u7238\u7238\u4eca\u665a\u7684\u7761\u524d\u6545\u4e8b\uff0c\u5c31\u662f\u7ed9\u4ed6\u4fe9\u8bb2\u79d1\u5b66\u5bb6\u4eec\u5206\u6790\u7684\u51e0\u4e2a\u53ef\u80fd\u7684\u6050\u9f99\u6d88\u5931\u539f\u56e0\u3002\u5c0f\u670b\u53cb\u4eec\uff0c\u4f60\u4eec\u548c\u8fd9\u5bf9\u5c0f\u5144\u59b9\u4fe9\u4e00\u6837\u5bf9\u6050\u9f99\u611f\u5174\u8da3\u5417\uff1f\u5feb\u6765\u542c\u4ed6\u4eec\u7684\u7238\u7238\u8bb2\u6050\u9f99\u6545\u4e8b\u5427\uff01","rank":245,"score":7.9,"status":0},{"id":"ADwGMlAx","name":"\u5c0f\u6050\u9f99\u662f\u4ece\u4ec0\u4e48\u5730\u65b9\u6765\u7684\uff1f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/6zevcjjo.jpg","tariff":0,"price":0,"terms":"\u6050\u9f99\u6545\u4e8b\u5927\u5408\u96c6,\u79d1\u666e\u6545\u4e8b,\u81ea\u7136\u77e5\u8bc6","tags":"\u79d1\u666e,\u6050\u9f99,\u535a\u7269\u9986","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":2,"age_to":7,"comment":"","description":"\u5c0f\u6050\u9f99\u662f\u4ece\u54ea\u91cc\u6765\u7684\u5462\uff1f\u6050\u9f99\u7684\u751f\u6d3b\u72b6\u6001\u53c8\u662f\u600e\u4e48\u6837\u7684\u5462\uff1f\u8fd9\u4e2a\u79d1\u666e\u513f\u7ae5\u6545\u4e8b\u4f1a\u544a\u8bc9\u4f60\u7b54\u6848\u3002","rank":243,"score":8.5,"status":0},{"id":"ADwGMVA9","name":"\u7231\u8fea\u751f\u548c\u7535\u706f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/s1020d49.jpg","tariff":0,"price":0,"terms":"\u540d\u4eba\u6545\u4e8b,\u79d1\u5b66\u77e5\u8bc6","tags":"\u79d1\u5b66\u53d1\u660e,\u7231\u8fea\u751f,\u7535\u706f","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":4,"age_to":8,"comment":"","description":"","rank":183,"score":9,"status":4},{"id":"ADAGNVAxDTM","name":"\u4e5d\u4e5d\u4e58\u6cd5\u53e3\u8bc0","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/b9q8jjaw.jpg","tariff":0,"price":0,"terms":"\u79d1\u5b66\u77e5\u8bc6","tags":"","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":10,"comment":"","description":"\u300a\u4e5d\u4e5d\u4e58\u6cd5\u6b4c\u8bc0\u300b\uff0c\u53c8\u5e38\u79f0\u4e3a\u201c\u5c0f\u4e5d\u4e5d\u201d\u3002\u5b66\u751f\u5b66\u7684\u201c\u5c0f\u4e5d\u4e5d\u201d\u53e3\u8bc0\uff0c\u662f\u4ece\u201c\u4e00\u4e00\u5f97\u4e00\u201d\u5f00\u59cb\uff0c\u5230\u201c\u4e5d\u4e5d\u516b\u5341\u4e00\u201d\u6b62\uff0c\u800c\u5728\u53e4\u4ee3\uff0c\u5374\u662f\u5012\u8fc7\u6765\uff0c\u4ece\u201c\u4e5d\u4e5d\u516b\u5341\u4e00\u201d\u8d77\uff0c\u5230\u201c\u4e00\u4e00\u5982\u4e00\u201d\u6b62\u3002\u56e0\u4e3a\u53e3\u8bc0\u5f00\u5934\u4e24\u4e2a\u5b57\u662f\u201c\u4e5d\u4e5d\u201d\uff0c\u6240\u4ee5\uff0c\u4eba\u4eec\u5c31\u628a\u5b83\u7b80\u79f0\u4e3a\u201c\u4e5d\u4e5d\u201d\u3002","rank":250,"score":7.8,"status":0},{"id":"ADAGM1A2DTE","name":"\u4eba\u7c7b\u8840\u578b\u7684\u53d1\u73b0","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/70tm3nun.jpg","tariff":0,"price":0,"terms":"\u751f\u6d3b\u5e38\u8bc6,\u767e\u79d1\u5168\u4e66,\u767e\u79d1\u77e5\u8bc6,\u79d1\u666e\u6545\u4e8b","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e\u6545\u4e8b,\u5065\u5eb7","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":3,"age_to":18,"comment":"","description":"\u8840\u578b\u88ab\u79f0\u4e3a100\u4e2a\u4f1f\u5927\u53d1\u660e\u4e4b\u4e00\uff0c\u56e0\u4e3a\u5b83\u5bf9\u8f93\u8840\u5177\u6709\u91cd\u8981\u610f\u4e49\uff0c\u4e0d\u76f8\u5bb9\u7684\u8840\u578b\u8f93\u8840\u53ef\u80fd\u5bfc\u81f4\u6eb6\u8840\u53cd\u5e94\u7684\u53d1\u751f\uff0c\u9020\u6210\u6eb6\u8840\u6027\u8d2b\u8840\u3001\u80be\u8870\u7aed\u3001\u4f11\u514b\u4ee5\u81f3\u6b7b\u4ea1\u3002","rank":254,"score":7.9,"status":0},{"id":"ADAGMVA3DTY","name":"\u690d\u6811\u8282\u7684\u7531\u6765","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/9msxp9dv.jpg","tariff":0,"price":0,"terms":"\u79d1\u666e\u6545\u4e8b,\u8e0f\u6625\u90ca\u6e38\u4e13\u8f91,\u767e\u79d1\u5168\u4e66,\u767e\u79d1\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u79d1\u666e\u6545\u4e8b,\u6c11\u4fd7\u6545\u4e8b","performer":"\u53e3\u888b\u6545\u4e8b","author":"","age_from":3,"age_to":12,"comment":"","description":"\u5c0f\u670b\u53cb\u4eec\u90fd\u77e5\u90533\u670812\u65e5\u662f\u4e2d\u56fd\u7684\u690d\u6811\u8282\uff0c\u53ef\u662f\u4f60\u4eec\u77e5\u9053\u690d\u6811\u8282\u4e3a\u4ec0\u4e48\u8981\u5b9a\u57283\u670812\u65e5\u5417\uff1f\u5b83\u548c\u54ea\u4e00\u4f4d\u5386\u53f2\u540d\u4eba\u6709\u5173\uff1f\u60f3\u77e5\u9053\u7684\u5c31\u6765\u542c\u6545\u4e8b\u5427~","rank":253,"score":9.1,"status":0},{"id":"ADMGMlAzDT0","name":"\u591a\u7eb3\u5b66\u767e\u79d1 1","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/rtbgctd5.jpg","tariff":0,"price":0,"terms":"\u767e\u79d1\u77e5\u8bc6,\u79d1\u5b66\u542f\u8499","tags":"\u6d77\u6d0b,\u52a8\u7269,\u8ba4\u8bc6\u81ea\u6211,\u767e\u79d1,\u591a\u7eb3","performer":"\u53e3\u888b\u6545\u4e8b \u591a\u7eb3","author":"\u591a\u7eb3","age_from":1,"age_to":8,"comment":"","description":"\u591a\u7eb3\u5b66\u767e\u79d1\u7cfb\u5217\uff0c\u5305\u542b\u5e2e\u5b9d\u5b9d\u8ba4\u8bc6\u81ea\u6211\u3001\u6d77\u91cc\u7684\u79d8\u5bc6\u3001\u53ef\u7231\u7684\u52a8\u7269\u4e16\u754c\u4e09\u5927\u90e8\u5206\u3002","rank":183,"score":9.9,"status":4},{"id":"ADIGMlAyDTY","name":"\u8be5\u5403\u996d\u4e86","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/6up0mwg4.jpg","tariff":0,"price":0,"terms":"\u751f\u6d3b\u6210\u957f,\u81ea\u7136\u77e5\u8bc6","tags":"\u98df\u7269\u94fe,\u8718\u86db,\u732b,\u5b9d\u8d1d\u5f00\u5fc3,\u7ed8\u672c","performer":"\u53e3\u888b\u6545\u4e8b \u5409\u7f8e\u5e7c\u6559\u96c6\u56e2","author":"[\u82f1]\u6731\u6069.\u83ab\u8389","age_from":2,"age_to":7,"comment":"\u628a\u539f\u672c\u67af\u71e5\u4e4f\u5473\u7684\u79d1\u666e\u77e5\u8bc6\u878d\u5165\u5230\u4e86\u6709\u8da3\u7684\u6545\u4e8b\u4e2d\uff0c\u8ba9\u5b69\u5b50\u77e5\u9053\u4e86\u8718\u86db\u5403\u82cd\u8747\u3001\u5c0f\u9e1f\u5403\u8718\u86db\u3001\u5c0f\u732b\u5403\u5c0f\u9e1f\u7684\u81ea\u7136\u89c4\u5f8b\u2026\u2026\u540c\u65f6\uff0c\u53e3\u871c\u8179\u5251\u7684\u8718\u86db\uff0c\u61a8\u50bb\u7684\u5c0f\u9e1f\uff0c\u81ea\u4ee5\u4e3a\u662f\u7684\u5c0f\u732b\u7b49\u5404\u79cd\u89d2\u8272\u7684\u5f62\u8c61\u90fd\u6829\u6829\u5982\u751f\uff0c\u8ba9\u5b69\u5b50\u5bf9\u6545\u4e8b\u548c\u4e3b\u9898\u4eba\u7269\u7684\u7406\u89e3\u66f4\u4e3a\u900f\u5f7b\u3002","description":"\u5403\u996d\u7684\u65f6\u95f4\u5230\u4e86\u2026\u2026\u732b\u54aa\u9965\u997f\u5730\u770b\u7740\u5c0f\u9e1f\uff1b\u5c0f\u9e1f\u9965\u997f\u5730\u76ef\u7740\u8718\u86db\uff1b\u8718\u86db\u4e5f\u540c\u6837\u9965\u997f\u7684\u6ce8\u89c6\u7740\u82cd\u8747\u3002\u6700\u540e\uff0c\u7a76\u7adf\u6709\u6ca1\u6709\u4eba\u6ca6\u4e3a\u4e86\u522b\u4eba\u9910\u684c\u4e0a\u7684\u7f8e\u98df\u5462\u2026\u2026","rank":182,"score":5.2,"status":4},{"id":"ADIGPlA1DTQ","name":"\u591a\u7eb3\u767e\u79d1\u7ed8\u672c\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/xgs0bhnx.jpg","tariff":0,"price":0,"terms":"\u513f\u7ae5\u9605\u8bfb\u4ece\u542c\u5f00\u59cb,\u767e\u79d1\u77e5\u8bc6,\u79d1\u5b66\u542f\u8499","tags":"\u767e\u79d1,\u591a\u7eb3,\u8eab\u4f53,\u52a8\u7269,\u8ba4\u77e5","performer":"\u53e3\u888b\u6545\u4e8b \u591a\u7eb3","author":"\u591a\u7eb3","age_from":3,"age_to":10,"comment":"","description":"\u591a\u7eb3\u5b66\u767e\u79d1\u7cfb\u5217\uff0c\u5305\u542b\u5e2e\u5b9d\u5b9d\u8ba4\u8bc6\u81ea\u6211\u3001\u6d77\u91cc\u7684\u79d8\u5bc6\u3001\u53ef\u7231\u7684\u52a8\u7269\u4e16\u754c\u4e09\u5927\u90e8\u5206\u3002","rank":328,"score":8.6,"status":0},{"id":"ADwGMVA2DT0","name":"\u718a\u7238\u7238\u7684\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48 1","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/9qojo9ur.jpg","tariff":0,"price":0,"terms":"\u767e\u79d1\u77e5\u8bc6","tags":"\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48,\u718a\u7238\u7238,\u79d1\u666e\u77e5\u8bc6,\u65e5\u5e38\u77e5\u8bc6,\u81ea\u7136\u77e5\u8bc6","performer":"\u53e3\u888b\u6545\u4e8b \u718a\u7238\u7238","author":"\u718a\u7238\u7238","age_from":3,"age_to":12,"comment":"","description":"\u300a\u718a\u7238\u7238\u7684\u5341\u4e07\u4e2a\u4e3a\u4ec0\u4e48\u300b\u7cfb\u5217\uff0c\u662f\u56fd\u5185\u9996\u521b\u7684\u4e92\u52a8\u95ee\u7b54\u7c7b\u667a\u6167\u542f\u8499\u8282\u76ee\u3002\r\n\u8ba9\u5b69\u5b50\u8d8a\u542c\u8d8a\u7231\u95ee\uff0c\u8d8a\u95ee\u8d8a\u806a\u660e\u3002\u6765\u81ea\u5b69\u5b50\u771f\u5b9e\u63d0\u95ee\uff0c\u539f\u521b\u4e92\u52a8\u95ee\u7b54\u6545\u4e8b\u3002\r\n3-12\u5c81\uff0c\u5f53\u5b69\u5b50\u95ee\u51fa\u7b2c\u4e00\u4e2a\u4e3a\u4ec0\u4e48\uff0c\u597d\u5947\u5fc3\u5f00\u59cb\u840c\u82bd\u3002\u5982\u679c\u5bb6\u957f\u6ca1\u80fd\u6b63\u786e\u5730\u5f15\u5bfc\u548c\u57f9\u517b\uff0c\u90a3\u5b69\u5b50\u7684\u597d\u5947\u5fc3\u5c06\u6e10\u6e10\u6cef\u706d\uff0c\u8f93\u5728\u8d77\u8dd1\u7ebf\u4e0a\u3002\r\n\u4e00\u4e2a\u62e5\u6709\u597d\u5947\u5fc3\u7684\u4eba\uff0c\u5c31\u50cf\u62e5\u6709\u6e90\u6e90\u4e0d\u65ad\u7684\u80fd\u91cf\u53bb\u5c1d\u8bd5\u3001\u63a2\u7d22\u548c\u5b66\u4e60\u3002\u67d0\u79cd\u7a0b\u5ea6\u4e0a\u8bf4\uff0c\u597d\u5947\u5fc3\u624d\u662f\u4e00\u4e2a\u4eba\u6700\u5927\u7684\u7ade\u4e89\u529b\u3002\r\n\u597d\u5947\u5fc3\u6539\u53d8\u4e16\u754c\uff0c\u8ba9\u6211\u4eec\u4ee5\u4fdd\u62a4\u597d\u5947\u5fc3\u7684\u65b9\u5f0f\u6765\u6539\u53d8\u4e16\u754c\u3002","rank":209,"score":9.2,"status":4}]},"retcode":0}

    a17164 ={"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0},{"id":"ADEGP1A8DTM","name":"\u6c49\u58f0\u7248\u897f\u6e38\u8bb0","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/qkjne5cb.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u540d\u8457,\u767e\u542c\u4e0d\u538c\u7684\u897f\u6e38\u8bb0","tags":"\u53e4\u5178,\u7ecf\u5178,\u5b59\u609f\u7a7a,\u56db\u5927\u540d\u8457,\u5927\u5723","performer":"\u53e3\u888b\u6545\u4e8b \u897f\u6e38\u6c49\u8bed\u4e50\u56ed\u56e2\u961f","author":"\u897f\u6e38\u6c49\u8bed\u4e50\u56ed\u56e2\u961f","age_from":3,"age_to":10,"comment":"","description":"\u897f\u6e38\u8bb0\u4e2d\u7684\u7cbe\u5f69\u3001\u7ecf\u5178\u7684\u6545\u4e8b\uff0c\u4f18\u7f8e\u7684\u80cc\u666f\u97f3\u4e50\uff0c\u7ed8\u58f0\u7ed8\u8272\u7684\u914d\u97f3\uff0c\u8ba9\u5c0f\u670b\u53cb\u4eec\u6109\u5feb\u5730\u5b66\u4e60\u7ecf\u5178\u3002","rank":305,"score":8.4,"status":0},{"id":"ADAGPlAxDTQ","name":"\u68a6\u5e7b\u9a91\u58eb","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/tjr1iz0q.jpg","tariff":0,"price":0,"terms":"\u5916\u56fd\u540d\u8457,\u7537\u5b69\u6545\u4e8b","tags":"\u5192\u9669,\u4e16\u754c\u540d\u8457,\u9a91\u58eb,\u5916\u56fd\u6587\u5b66,\u5802\u5409\u8bc3\u5fb7","performer":"\u53e3\u888b\u6545\u4e8b \u65b9\u5411\u6709\u58f0","author":"\u585e\u4e07\u63d0\u65af","age_from":6,"age_to":18,"comment":"","description":"\u300a\u68a6\u5e7b\u9a91\u58eb\u300b\u6539\u7f16\u81ea17\u4e16\u7eaa\u7684\u897f\u73ed\u7259\u4f5c\u5bb6\u585e\u4e07\u63d0\u65af\u6240\u5199\u7684\u53cd\u9a91\u58eb\u5c0f\u8bf4\u300a\u5802\u5409\u8bc3\u5fb7\u300b\uff0c\u6545\u4e8b\u53d1\u751f\u65f6\uff0c\u9a91\u58eb\u65e9\u5df2\u7edd\u8ff9\u4e00\u4e2a\u591a\u4e16\u7eaa\uff0c\u4f46\u4e3b\u89d2\u5374\u56e0\u4e3a\u6c89\u8ff7\u4e8e\u9a91\u58eb\u5c0f\u8bf4\uff0c\u65f6\u5e38\u5e7b\u60f3\u81ea\u5df1\u662f\u4e2a\u4e2d\u4e16\u7eaa\u9a91\u58eb\uff0c\u8fdb\u800c\u81ea\u5c01\u4e3a\u9a91\u58eb\u5802\u5409\u8bc3\u5fb7\uff0c\u62c9\u7740\u90bb\u5c45\u505a\u81ea\u5df1\u7684\u4ec6\u4eba\uff0c\u4e00\u8d77\u53bb\u201c\u884c\u4fa0\u4ed7\u4e49\u201d\u3001\u6e38\u8d70\u5929\u4e0b\uff0c\u7ed3\u679c\u5374\u56db\u5904\u78b0\u58c1\uff0c\u6700\u7ec8\u4ece\u68a6\u5e7b\u4e2d\u82cf\u9192\u8fc7\u6765\u3002","rank":285,"score":6.5,"status":0}]},"retcode":0}

    a17176={"data":{"works":[{"id":"ADQGP1A1","name":"\u8d1d\u591a\u82ac\u2014\u81f4\u7231\u4e3d\u4e1d","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/ku6t9vr0.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac,\u81f4\u7231\u4e3d\u4e1d","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":1,"age_to":1,"comment":"","description":"\u300a\u732e\u7ed9\u7231\u4e3d\u4e1d\u300b\uff08f\u00fcr Elise\uff09\u662f\u8d1d\u591a\u82ac\u521b\u4f5c\u7684\u4e00\u9996\u5176\u94a2\u7434\u5c0f\u54c1\u3002\u8d1d\u591a\u82ac\u662f\u96c6\u897f\u65b9\u53e4\u5178\u6d3e\u4e4b\u5927\u6210\uff0c\u5f00\u6d6a\u6f2b\u4e50\u6d3e\u4e4b\u5148\u6cb3\u7684\u4f1f\u5927\u4f5c\u66f2\u5bb6\u3002\u4eba\u4eec\u90fd\u6bd4\u8f83\u719f\u6089\u4ed6\u7684\u4ea4\u54cd\u66f2\u3001\u534f\u594f\u66f2\u3001\u5ba4\u5185\u4e50\u548c\u6b4c\u5267\u7b49\u5927\u578b\u4f5c\u54c1\uff0c\u4f46\u662f\uff0c\u4ed6\u7684\u4e3a\u6570\u4e0d\u591a\u7684\u5668\u4e50\u5c0f\u54c1\uff0c\u4e5f\u540c\u6837\u7ed9\u4eba\u7559\u4e0b\u4e86\u6df1\u523b\u7684\u5370\u8c61\u3002\u94a2\u7434\u5c0f\u54c1\u300a\u732e\u7ed9\u7231\u4e3d\u4e1d\u300b\u5c31\u662f\u5176\u4e2d\u6bd4\u8f83\u8457\u540d\u7684\u4e00\u9996\u3002\u4f46\u4e50\u8c31\u53d1\u73b0\u4e8e1867\u5e74\uff0c\u56e0\u6b64\u8d1d\u591a\u82ac\u751f\u524d\u5e76\u672a\u53d1\u8868\u3002","rank":199,"score":8.9,"status":0},{"id":"ADQGP1A2","name":"\u6b22\u4e50\u9882","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/3ws8i9cv.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50,\u8d77\u5e8a\u97f3\u4e50","tags":"\u53e4\u5178\u97f3\u4e50,\u8d1d\u591a\u82ac,\u6b22\u4e50\u9882,\u97f3\u4e50\u542f\u8499","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u6b22\u4e50\u9882\u300b\uff0c\u53c8\u79f0\u300a\u5feb\u4e50\u9882\u300b\uff08\u5fb7\u8bed\u4e3aAn die Freude\uff09\uff0c\u662f\u57281785\u5e74\u7531\u5fb7\u56fd\u8bd7\u4eba\u5e2d\u52d2\u6240\u5199\u7684\u8bd7\u6b4c\u3002\u8d1d\u591a\u82ac\u4e3a\u4e4b\u8c31\u66f2\uff0c\u6210\u4e3a\u4ed6\u7684\u7b2c\u4e5d\u4ea4\u54cd\u66f2\u7b2c\u56db\u4e50\u7ae0\u7684\u4e3b\u8981\u90e8\u4efd\uff0c\u5305\u542b\u56db\u72ec\u7acb\u58f0\u90e8\u3001\u5408\u5531\u3001\u4e50\u56e2\u3002\u800c\u8fd9\u7531\u8d1d\u591a\u82ac\u6240\u8c31\u66f2\u7684\u97f3\u4e50\uff08\u4e0d\u5305\u542b\u6587\u5b57\uff09\u6210\u4e3a\u4e86\u73b0\u4eca\u6b27\u6d32\u8054\u76df\u7684\u76df\u6b4c\u3002\u6b22\u4e50\u9882\uff0c\u73b0\u5728\u6700\u5e38\u63d0\u8d77\u7684\u662f\u8d1d\u591a\u82ac\u7684\u97f3\u4e50\u4f5c\u54c1\u3001\u5e2d\u52d2\u7684\u8bd7\u6b4c\u3001\u80e1\u98ce\u957f\u8bd7\u300a\u65f6\u95f4\u5f00\u59cb\u4e86\u300b\u4e2d\u7684\u7b2c\u4e00\u4e50\u7ae0\u548c\u4e00\u90e8\u79d1\u5e7b\u5c0f\u8bf4\u540d\u5b57\uff0c\u5c24\u5176\u662f\u524d\u4e24\u8005\uff0c\u66f4\u4e3a\u4eba\u4eec\u719f\u77e5\u3002","rank":245,"score":9,"status":0},{"id":"ADQGMFAzDTM","name":"\u65e5\u51fa\u6668\u5b89","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/mdhre9d0.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u8d77\u5e8a\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168","tags":"\u65e9\u6668,\u8d77\u5e8a,\u8f7b\u97f3\u4e50","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u7eaf\u97f3\u4e50\uff0c\u51fa\u81ea\u73ed\u5f97\u745e\u7684\u300a\u5fae\u98ce\u5c71\u8c37\u300b\u3002\u6ca1\u6709\u68a6\uff0c\u4e00\u70b9\u4e5f\u6ca1\u6709\u3002\u767d\u5154\u4e0e\u767d\u5154\u9760\u7740\u80a9\u7761\u4e86\u3002\u9e8b\u9e7f\u4e0e\u9e8b\u9e7f\u5e76\u5367\uff0c\u6a2a\u79fb\u7684\u662f\u6e05\u6668\u7684\u98ce\uff0c\u5439\u8fc7\u963f\u5c14\u5351\u65af\u5c71\u9e93\uff0c\u51c9\u51c9\u7684\u9732\u6c34\uff0c\u8f7b\u821e\u5728\u65e5\u51fa\u524d\u3002","rank":239,"score":9.1,"status":0},{"id":"ADQGPlA0DTQ","name":"\u68a6\u5e7b\u66f2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/vlxxc7no.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50","tags":"\u80ce\u6559,\u94a2\u7434\u66f2,\u8212\u66fc","performer":"\u53e3\u888b\u6545\u4e8b \u8212\u66fc","author":"\u4f5a\u540d","age_from":-1,"age_to":16,"comment":"","description":"\u300a\u68a6\u5e7b\u66f2\u300b\u662f\u5fb7\u56fd\u4f5c\u66f2\u5bb6\u8212\u66fc\u6240\u4f5c\u7684\u66f2\u5b50\u3002\u4eba\u4eec\u5bf9\u90a3\u56db\u4e2a\u5c0f\u8282\u65cb\u5f8b\u65e2\u719f\u6089\u53c8\u559c\u7231\uff0c\u90a3\u4e9b\u8f7b\u76c8\u878d\u60c5\u7684\u6b4c\uff0c\u662f\u6bcf\u4e2a\u8046\u542c\u6b64\u66f2\u7684\u4eba\u5fc3\u4e2d\u7684\u65cb\u5f8b\u3002\u5b83\u53d9\u8ff0\u7740\u4eba\u4eec\u513f\u65f6\u7684\u7f8e\u4e3d\u7684\u68a6\uff0c\u4e5f\u6292\u53d1\u7740\u7406\u60f3\u4e16\u754c\u7684\u6e29\u6696\u3001\u6df1\u8fdc\u4e0e\u751c\u871c\u3002\u8fd9\u652f\u65cb\u5f8b\u7ec6\u817b\u7684\u97f3\u4e50\u8868\u60c5\uff0c\u4e30\u5bcc\u7684\u548c\u58f0\u8bed\u8a00\uff0c\u5f15\u4eba\u5165\u80dc\u7684\u8868\u73b0\u529b\uff0c\u4f7f\u8fd9\u9996\u77ed\u8bd7\u5145\u6ee1\u4e86\u8bd7\u60c5\u753b\u610f\uff0c\u4ee4\u4eba\u767e\u542c\u4e0d\u538c\u3002","rank":239,"score":9.1,"status":0},{"id":"ADEGPlAyDTM","name":"\u5929\u624d\u5b9d\u5b9d\u80ce\u6559\u97f3\u4e50\u7cfb\u5217\u4e00","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/s2mj58u5.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u7761\u524d\u97f3\u4e50,\u7cbe\u54c1\u97f3\u4e50,2014\u5e74\u5ea6\u7cbe\u9009\u5408\u8f91,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50","tags":"\u80ce\u6559,\u97f3\u4e50,\u542f\u667a","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":3,"comment":"","description":"\u5929\u624d\u5b9d\u5b9d\uff08Genius Baby\uff09\u80ce\u6559\u97f3\u4e50\u7cfb\u5217\u662f\u7f8e\u56fd\u54c8\u4f5b\u5927\u5b66\u3001\u5317\u4eac\u5927\u5b66\u7684\u56fd\u9645\u9876\u7ea7\u79d1\u5b66\u5bb6\u3001\u5317\u4eac\u534f\u548c\u533b\u9662\u7684\u4e13\u5bb6\u591a\u5e74\u5408\u4f5c\u5f00\u53d1\uff0c\u4f9d\u636e\u53d1\u80b2\u5b66\u3001\u795e\u7ecf\u5b66\u3001\u4f18\u751f\u5b66\u7b49\u9886\u57df\u7684\u6700\u65b0\u8fdb\u5c55\uff0c\u91c7\u7528\u591a\u9879\u4e13\u5229\u6280\u672f\uff0c\u9488\u5bf9\u80ce\u513f\u7684\u7279\u70b9\u63a8\u51fa\u7684\u65b0\u4e00\u4ee3\u80ce\u6559\u97f3\u4e50\u3002","rank":244,"score":8.8,"status":0},{"id":"ADEGPlA9DTM","name":"\u5929\u624d\u5b9d\u5b9d\u80ce\u6559\u97f3\u4e50\u7cfb\u5217\u4e8c","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/nvegec9o.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,2014\u5e74\u5ea6\u7cbe\u9009\u5408\u8f91,\u80ce\u6559\u7cfb\u5217\u5927\u5168,\u80ce\u6559\u97f3\u4e50","tags":"\u80ce\u6559,\u97f3\u4e50,\u542f\u667a","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":-1,"age_to":3,"comment":"","description":"\u5929\u624d\u5b9d\u5b9d\uff08Genius Baby\uff09\u80ce\u6559\u97f3\u4e50\u7cfb\u5217\u662f\u7f8e\u56fd\u54c8\u4f5b\u5927\u5b66\u3001\u5317\u4eac\u5927\u5b66\u7684\u56fd\u9645\u9876\u7ea7\u79d1\u5b66\u5bb6\u3001\u5317\u4eac\u534f\u548c\u533b\u9662\u7684\u4e13\u5bb6\u591a\u5e74\u5408\u4f5c\u5f00\u53d1\uff0c\u4f9d\u636e\u53d1\u80b2\u5b66\u3001\u795e\u7ecf\u5b66\u3001\u4f18\u751f\u5b66\u7b49\u9886\u57df\u7684\u6700\u65b0\u8fdb\u5c55\uff0c\u91c7\u7528\u591a\u9879\u4e13\u5229\u6280\u672f\uff0c\u9488\u5bf9\u80ce\u513f\u7684\u7279\u70b9\u63a8\u51fa\u7684\u65b0\u4e00\u4ee3\u80ce\u6559\u97f3\u4e50\u3002","rank":257,"score":9.8,"status":0},{"id":"ADAGNlA0DTc","name":"\u52a8\u7269\u72c2\u6b22\u8282","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/za4g3og9.jpg","tariff":0,"price":0,"terms":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u97f3\u4e50","tags":"\u80ce\u6559,\u97f3\u4e50","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u5723\u6851","age_from":-1,"age_to":16,"comment":"\u542c\u542c\u770b\uff0c\u4f60\u80fd\u542c\u51fa\u51e0\u79cd\u52a8\u7269\u7684\u58f0\u97f3\u5462\uff1f","description":"\u300a\u52a8\u7269\u72c2\u6b22\u8282\u300b\u53c8\u79f0\u300a\u52a8\u7269\u56ed\u5927\u5e7b\u60f3\u66f2\u300b\u3002\u8457\u540d\u4f5c\u66f2\u5bb6\u5723-\u6851\u4f5c\u4e8e1886\u5e74\uff0c\u662f\u4e00\u9996\u5341\u5206\u72ec\u7279\u7684\u4f5c\u54c1\uff0c\u4ee5\u751f\u52a8\u7684\u624b\u6cd5\uff0c\u63cf\u5199\u52a8\u7269\u4eec\u5728\u70ed\u95f9\u7684\u8282\u65e5\u884c\u5217\u4e2d\uff0c\u5404\u79cd\u6ed1\u7a3d\u6709\u8da3\u7684\u60c5\u5f62\u3002\u7ec4\u66f2\u7531\u591a\u8fbe\u5341\u56db\u4e2a\u4e50\u7ae0\u7ec4\u6210\uff0c\u5927\u91cf\u91c7\u7528\u5355\u7eaf\u97f3\u54cd\u6a21\u4eff\u624b\u6cd5\uff0c\u5bcc\u4e8e\u7f8e\u611f\u3002","rank":242,"score":8,"status":0},{"id":"ADAGNlA2DTE","name":"\u65af\u7f8e\u5854\u90a3-\u4f0f\u5c14\u5854\u74e6\u6cb3","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/jm4fj8l0.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u8d77\u5e8a\u97f3\u4e50,\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168","tags":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559,\u97f3\u4e50,\u53eb\u9192\u8033\u6735","performer":"\u53e3\u888b\u6545\u4e8b \u65af\u7f8e\u5854\u90a3","author":"\u65af\u7f8e\u5854\u90a3","age_from":-1,"age_to":16,"comment":"","description":"\u6377\u514b\u4f5c\u66f2\u5bb6\u65af\u7f8e\u5854\u90a3\uff08\u6377\u514b\u65b0\u97f3\u4e50\u4e4b\u7236\uff09\u521b\u4f5c\u7684\u4ea4\u54cd\u8bd7\uff0c\u88ab\u79f0\u4e3a\u6377\u514b\u7b2c\u4e8c\u56fd\u6b4c\u3002","rank":244,"score":8.5,"status":0},{"id":"ADAGNFA3DTM","name":"\u6d77\u987f-\u519b\u961f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/gw4gfbxa.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168","tags":"\u53e4\u5178\u97f3\u4e50,\u80ce\u6559,\u6d77\u987f","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u6d77\u987f","age_from":-1,"age_to":16,"comment":"","description":"1794\u5e743\u670831\u65e5\uff0c\u6d77\u987f\u5728\u4f26\u6566\u7684\u6c49\u8bfa\u5a01\u5e7f\u573a\u97f3\u4e50\u5385\u9996\u6f14\u4e86\u65b0\u5b8c\u6210\u7684\u4e00\u90e8\u4ea4\u54cd\u66f2\uff0c\u5b83\u5728\u6d77\u987f\u7684\u5168\u90e8\u4ea4\u54cd\u66f2\u4e2d\u6392\u5728\u7b2c\u4e00\u767e\u53f7\u3002\u5982\u4eca\uff0c\u6d77\u987f\u7684\u4e00\u767e\u591a\u90e8\u4ea4\u54cd\u66f2\u4e2d\u7684\u5927\u90e8\u5206\u5f88\u5c11\u6709\u673a\u4f1a\u6f14\u594f\u4e86\uff0c\u53ea\u6709\u201c\u4f26\u6566\u4ea4\u54cd\u66f2\u201d\u4e2d\u7684\u5927\u90e8\u5206\u8fd8\u7ecf\u5e38\u4e0a\u6f14\uff0c\u800c\u7b2c\u4e00\u767e\u53f7\u300a\u519b\u961f\u4ea4\u54cd\u66f2\u300b\u5219\u662f\u6c38\u4e45\u6027\u4fdd\u7559\u66f2\u76ee\u3002","rank":246,"score":8.3,"status":0},{"id":"ADAGNFAyDTI","name":"\u7ef4\u74e6\u5c14\u7b2c-\u96ea\u82b1\u5929\u4e0a\u6765","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/bc1jkidm.jpg","tariff":0,"price":0,"terms":"\u80ce\u6559\u97f3\u4e50,\u53e4\u5178\u97f3\u4e50,\u80ce\u6559\u7cfb\u5217\u5927\u5168","tags":"\u53e4\u5178\u97f3\u4e50,\u7ef4\u74e6\u5c14\u7b2c","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u7ef4\u74e6\u5c14\u7b2c","age_from":-1,"age_to":16,"comment":"\u5e15\u65af\u6377\u5c14\u7eb3\u514b\u8bf4:\u5343\u767e\u5e74\u6765\u4f7f\u4eba\u7c7b\u51cc\u9a7e\u4e8e\u52a8\u7269\u4e4b\u4e0a\u7684\uff0c\u5e76\u4e0d\u662f\u68cd\u68d2\uff0c\u800c\u662f\u97f3\u4e50\u3002","description":"\u6b64\u4f5c\u54c1\u9009\u81ea\u300a\u56db\u5b63\u300b\uff08\u610f\u5927\u5229\u8bed\uff1aLe quattro stagioni\uff09\u662f\u610f\u5927\u5229\u97f3\u4e50\u5bb6\u5b89\u4e1c\u5c3c\u5965\u00b7\u97e6\u74e6\u7b2c\u57281723\u5e74\u521b\u4f5c\u7684\u5c0f\u63d0\u7434\u534f\u594f\u66f2\u3002\u8fd9\u4e5f\u662f\u4ed6\u6700\u8457\u540d\u7684\u4f5c\u54c1\u4e4b\u4e00\u3002","rank":247,"score":8.6,"status":0}]},"retcode":0}

    a17466={"data":{"works":[{"id":"ADMGNlA8DTI","name":"\u7a7a\u4e2d\u98de\u7f8a","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/giqu1ss.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u52a8\u7269\u6545\u4e8b,\u806a\u660e\u8c46,\u751f\u6d3b\u6210\u957f","tags":"\u5c0f\u7f8a,\u806a\u660e\u8c46\u7ed8\u672c","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u82f1\uff09\u5f7c\u5f97\u00b7\u672c\u7279\u5229","age_from":2,"age_to":6,"comment":"\u3000\u201c\u806a\u660e\u8c46\u7ed8\u672c\u7cfb\u5217\u201d\u662f\u4e16\u754c\u5404\u5730\u4f18\u79c0\u56fe\u753b\u4e66\u7684\u7cbe\u9009\u5408\u8f91\u3002\u4e4b\u6240\u4ee5\u79f0\u4e3a\u201c\u806a\u660e\u8c46\u201d\uff0c\u662f\u56e0\u4e3a\u5979\u7684\u786e\u806a\u660e\u2014\u2014\u8f7b\u677e\u5e7d\u9ed8\u7684\u6587\u5b57\u3001\u5145\u6ee1\u60f3\u8c61\u7684\u56fe\u753b\u3001\u5999\u8da3\u6a2a\u751f\u7684\u6545\u4e8b\uff0c\u5c06\u81ea\u6211\u8ba4\u77e5\u3001\u53cb\u8c0a\u3001\u7231\uff0c\u751a\u81f3\u662f\u751f\u547d\u7684\u901d\u53bb\u7b49\u9971\u542b\u54f2\u7406\u7684\u8bdd\u9898\u5a13\u5a13\u9053\u6765\u3002\u6ca1\u6709\u4e00\u53e5\u6559\u6761\uff0c\u5374\u80fd\u6ee1\u8db3\u5b69\u5b50\u7684\u6210\u957f\u9700\u8981\uff1b\u6ca1\u6709\u4e00\u4e1d\u8bf4\u7406\uff0c\u5374\u80fd\u542f\u53d1\u5b69\u5b50\u7684\u6df1\u5165\u601d\u8003\uff1b\u6ca1\u6709\u4e00\u70b9\u513f\u55a7\u95f9\uff0c\u5374\u80fd\u6fc0\u8d77\u5b69\u5b50\u7684\u4f1a\u5fc3\u5927\u7b11\u3002","description":"\u4e00\u7fa4\u5c0f\u7f8a\u603b\u5728\u5c71\u5761\u4e0a\u5403\u8349\uff0c\u8fd9\u6837\u7684\u65e5\u5b50\uff0c\u6bcf\u5929\u90fd\u5dee\u4e0d\u4e86\u591a\u5c11\u3002\u76f4\u5230\u6709\u4e00\u5929\uff0c\u6709\u4e00\u6837\u4e1c\u897f\u4ece\u4ed6\u4eec\u5934\u9876\u201c\u8f70\u201d\u5730\u98de\u8fc7\u3002\u597d\u5947\u7684\u5c0f\u7f8a\u4eec\u5230\u5c71\u9876\u4e00\u770b\uff0c\u539f\u6765\u9644\u8fd1\u6b63\u5728\u4e3e\u884c\u98de\u884c\u5927\u8d5b\u3002\u4ed6\u4eec\u8dd1\u53bb\u51d1\u70ed\u95f9\uff0c\u5374\u9634\u9519\u9633\u5dee\u5730\u767b\u4e0a\u4e86\u98de\u673a\uff0c\u5f00\u4e0a\u4e86\u5929\u3002\u6709\u8da3\u7684\u4e8b\u60c5\u53d1\u751f\u4e86\u2026\u2026\r\n","rank":264,"score":6.8,"status":0},{"id":"ADMGNlA9DTU","name":"\u9b54\u6cd5\u68d2","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/z13optnb.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u5973\u5b69\u6545\u4e8b,\u806a\u660e\u8c46,\u751f\u6d3b\u6210\u957f","tags":"\u9b54\u6cd5,\u806a\u660e\u8c46\u7ed8\u672c","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u6bd4\uff09\u57c3\u65af\u7279\u52d2\u00b7\u6885\u6069\u65af","age_from":2,"age_to":6,"comment":"\u3000\u201c\u806a\u660e\u8c46\u7ed8\u672c\u7cfb\u5217\u201d\u662f\u4e16\u754c\u5404\u5730\u4f18\u79c0\u56fe\u753b\u4e66\u7684\u7cbe\u9009\u5408\u8f91\u3002\u4e4b\u6240\u4ee5\u79f0\u4e3a\u201c\u806a\u660e\u8c46\u201d\uff0c\u662f\u56e0\u4e3a\u5979\u7684\u786e\u806a\u660e\u2014\u2014\u8f7b\u677e\u5e7d\u9ed8\u7684\u6587\u5b57\u3001\u5145\u6ee1\u60f3\u8c61\u7684\u56fe\u753b\u3001\u5999\u8da3\u6a2a\u751f\u7684\u6545\u4e8b\uff0c\u5c06\u81ea\u6211\u8ba4\u77e5\u3001\u53cb\u8c0a\u3001\u7231\uff0c\u751a\u81f3\u662f\u751f\u547d\u7684\u901d\u53bb\u7b49\u9971\u542b\u54f2\u7406\u7684\u8bdd\u9898\u5a13\u5a13\u9053\u6765\u3002\u6ca1\u6709\u4e00\u53e5\u6559\u6761\uff0c\u5374\u80fd\u6ee1\u8db3\u5b69\u5b50\u7684\u6210\u957f\u9700\u8981\uff1b\u6ca1\u6709\u4e00\u4e1d\u8bf4\u7406\uff0c\u5374\u80fd\u542f\u53d1\u5b69\u5b50\u7684\u6df1\u5165\u601d\u8003\uff1b\u6ca1\u6709\u4e00\u70b9\u513f\u55a7\u95f9\uff0c\u5374\u80fd\u6fc0\u8d77\u5b69\u5b50\u7684\u4f1a\u5fc3\u5927\u7b11\u3002","description":"\u8389\u8389\u662f\u4e00\u4e2a\u7269\u8d28\u751f\u6d3b\u6bd4\u8f83\u4e30\u5bcc\u7684\u5b69\u5b50\uff0c\u5979\u7684\u751f\u6d3b\u4e2d\u4ece\u6765\u90fd\u4e0d\u7f3a\u5c11\u73a9\u5177\uff0c\u81ea\u884c\u8f66\u3001\u5e03\u5a03\u5a03\u3001\u8db3\u7403\u2026\u2026\u5e94\u6709\u5c3d\u6709\uff0c\u53ef\u5979\u8fd8\u662f\u6709\u81ea\u5df1\u7684\u82e6\u607c\u3002\u540e\u6765\uff0c\u5979\u53bb\u627e\u90bb\u5c45\u5c0f\u7537\u5b69\u73a9\uff0c\u5374\u5728\u8def\u8fb9\u7684\u6811\u6797\u91cc\u53d1\u73b0\u4e86\u4e00\u6839\u9b54\u6cd5\u68d2\uff0c\u4e8e\u662f\u56f4\u7ed5\u7740\u8fd9\u6839\u9b54\u6cd5\u68d2\uff0c\u6545\u4e8b\u5f00\u59cb\u4e86\u2026\u2026","rank":265,"score":8.1,"status":0},{"id":"ADMGNlA9DTQ","name":"\u5c0f\u6b65\u70b9\u7684\u6536\u85cf\u54c1","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/u93gdfz4.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u52a8\u7269\u6545\u4e8b,\u806a\u660e\u8c46,\u7231\u4e0e\u60c5\u611f","tags":"\u575a\u6301\u68a6\u60f3,\u806a\u660e\u8c46\u7ed8\u672c,\u73cd\u85cf\u54c1","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u6bd4\uff09\u51ef\u8428\u7433\u00b7\u6885\u7279\u6885\u5c14","age_from":2,"age_to":6,"comment":"\u5c0f\u6545\u4e8b\u5927\u667a\u6167\uff1a\u6bcf\u4e00\u4ef6\u6536\u85cf\u54c1\u90fd\u4ee3\u8868\u4e00\u6bb5\u4e30\u539a\u7684\u4eba\u751f\u8bb0\u5fc6\uff0c\u7ffb\u770b\u7684\u8fc7\u7a0b\uff0c\u53c8\u4f55\u5c1d\u4e0d\u662f\u6162\u54c1\u751f\u6d3b\u7684\u8fc7\u7a0b\u5462\uff1f","description":"\u7530\u9f20\u5c0f\u6b65\u70b9\u6709\u4e2a\u7279\u522b\u7684\u7231\u597d\u2014\u2014\u6536\u96c6\u91d1\u8272\u7684\u6811\u53f6\u3002\u5f53\u522b\u7684\u52a8\u7269\u90fd\u5728\u79cb\u98ce\u4e2d\u745f\u745f\u53d1\u6296\u7684\u65f6\u5019\uff0c\u4ed6\u5374\u5728\u56db\u5904\u5bfb\u627e\u6700\u6f02\u4eae\u7684\u6811\u53f6\u2014\u2014\u4e0d\u6311\u6253\u4e86\u852b\u7684\uff0c\u4e0d\u9009\u8d77\u4e86\u76b1\u7684\u3002\u8fd9\u6b21\uff0c\u4ed6\u5728\u6811\u679d\u7684\u6700\u9876\u7aef\u53d1\u73b0\u4e86\u4e00\u7247\u5b8c\u7f8e\u7684\u91d1\u8272\u53f6\u5b50\u3002\u4f1a\u53d1\u751f\u4ec0\u4e48\u5462\uff1f","rank":263,"score":8.5,"status":0},{"id":"ADMGNlA9DTc","name":"\u5c0f\u5c0f\u7f8a\u4e0e\u5927\u5927\u72fc","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/2\/ebzi15y5.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u52a8\u7269\u6545\u4e8b,\u806a\u660e\u8c46,\u7231\u4e0e\u60c5\u611f","tags":"\u5c0f\u7f8a,\u52c7\u6c14,\u806a\u660e\u8c46\u7ed8\u672c","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u6cd5\uff09\u827e\u745e\u514b\u00b7\u7231\u683c\u96f7\u8d1d\u7279","age_from":2,"age_to":6,"comment":"\u5c0f\u6545\u4e8b\u5927\u667a\u6167\uff1a\u5b69\u5b50\u5c0f\u5c0f\u7684\u8eab\u4f53\u91cc\u90fd\u8574\u542b\u7740\u5f3a\u5927\u7684\u81ea\u6211\u8c03\u8282\u7684\u529b\u91cf\uff0c\u4ed6\u4eec\u53ef\u4ee5\u901a\u8fc7\u81ea\u5df1\u7684\u65b9\u6cd5\uff0c\u627e\u5230\u4e86\u6218\u80dc\u6050\u60e7\u7684\u52c7\u6c14\u3002","description":"\u7761\u524d\u6545\u4e8b\u8bb2\u5b8c\u4e86\uff0c\u5c0f\u7f8a\u8be5\u7761\u89c9\u4e86\u3002\u4f46\u662f\u7f8a\u5988\u5988\u4e00\u628a\u623f\u95e8\u5173\u4e0a\uff0c\u5c0f\u7f8a\u5c31\u4f1a\u770b\u5230\u5947\u602a\u7684\u4e8b\u60c5\uff0c\u4e00\u4f1a\u513f\u4ece\u8863\u67dc\u91cc\u4f38\u51fa\u72fc\u5c3e\u5df4\uff0c\u4e00\u4f1a\u513f\u53c8\u662f\u7a97\u5e18\u5728\u6447\u6643\u2026\u2026\u6700\u540e\uff0c\u5c0f\u7f8a\u542c\u5230\u5e8a\u5e95\u4e0b\u4f20\u6765\u5947\u602a\u7684\u58f0\u97f3\uff0c\u4ed6\u9f13\u8db3\u52c7\u6c14\uff0c\u4fef\u4e0b\u8eab\u5b50\u4e00\u770b\uff0c\u90a3\u91cc\u7adf\u7136\u771f\u7684\u85cf\u7740\u4e00\u53ea\u5927\u7070\u72fc\uff01","rank":266,"score":9.5,"status":0},{"id":"ADMGNlA9DTY","name":"\u65af\u5766\u5229\u7684\u68cd\u5b50","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/3\/kaoh9uo5.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u7537\u5b69\u6545\u4e8b,\u806a\u660e\u8c46,\u751f\u6d3b\u6210\u957f","tags":"\u60f3\u8c61\u529b,\u806a\u660e\u8c46\u7ed8\u672c","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u82f1\uff09\u7ea6\u7ff0\u00b7\u8d6b\u683c\u91cc","age_from":2,"age_to":6,"comment":"\u5c0f\u6545\u4e8b\u5927\u667a\u6167\uff1a\u5929\u9a6c\u884c\u7a7a\u7684\u60f3\u8c61\u5c31\u5982\u540c\u4e00\u628a\u94a5\u5319\uff0c\u5b83\u80fd\u5f00\u542f\u901a\u5f80\u9b54\u6cd5\u738b\u56fd\u7684\u5927\u95e8\uff0c\u4e3a\u5b69\u5b50\u4eec\u70b9\u4eae\u5c5e\u4e8e\u4ed6\u4eec\u7684\u4e16\u754c\u3002","description":"\u300a\u65af\u5766\u5229\u7684\u68cd\u5b50\u300b\uff1a\u65af\u5766\u5229\u7684\u68cd\u5b50\u662f\u4ece\u4e00\u68f5\u9ad8\u9ad8\u7684\u5927\u6811\u4e0a\u6389\u4e0b\u6765\u7684\uff0c\u53ef\u5b83\u4e0d\u53ea\u662f\u4e00\u6839\u68cd\u5b50\u3002\u5b83\u53ef\u4ee5\u53d8\u6210\u7b1b\u5b50\uff0c\u53ef\u4ee5\u53d8\u6210\u9493\u7aff\uff0c\u53ef\u4ee5\u53d8\u6210\u80ef\u4e0b\u7684\u6050\u9f99\uff0c\u8fd8\u53ef\u4ee5\u53d8\u6210\u98de\u5411\u6708\u7403\u7684\u98de\u884c\u5668\u2026\u2026\u8bf7\u53d1\u6325\u4f60\u7684\u60f3\u8c61\u529b\uff0c\u770b\u770b\u8fd9\u6839\u795e\u5947\u7684\u68cd\u5b50\u8fd8\u6709\u4ec0\u4e48\u7279\u522b\u7684\u9b54\u6cd5\uff01\r\n","rank":263,"score":1.6,"status":0},{"id":"ADMGNlA9DTE","name":"\u6708\u4eae\u7684\u793c\u7269","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/4\/zvcynk3y.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u5973\u5b69\u6545\u4e8b,\u806a\u660e\u8c46,\u751f\u6d3b\u6210\u957f","tags":"\u806a\u660e\u8c46\u7ed8\u672c,\u521b\u9020\u529b","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u82f1\uff09\u4f0a\u4e3d\u838e\u767d\u00b7\u62dc\u683c\u96f7","age_from":2,"age_to":6,"comment":"\u5c0f\u6545\u4e8b\u5927\u667a\u6167\uff1a\u6fc0\u53d1\u5b69\u5b50\u7684\u521b\u9020\u529b\uff0c\u8bd5\u7740\u5bf9\u65e5\u5e38\u751f\u6d3b\u91cd\u65b0\u6784\u9020\uff0c\u4f53\u4f1a\u201c\u65e0\u4e2d\u751f\u6709\u201d\u7684\u4e50\u8da3\u2014\u2014\u8fd9\u624d\u662f\u7559\u7ed9\u5b69\u5b50\u4eec\u7684\u201c\u6700\u597d\u7684\u793c\u7269\u201d\u3002","description":"\u300a\u6708\u4eae\u7684\u793c\u7269\u300b\uff1a\u7537\u5b69\u4eec\u4e0d\u613f\u610f\u548c\u6885\u5409\u00b7\u6708\u4eae\u73a9\uff0c\u56e0\u4e3a\u5979\u662f\u4e2a\u5973\u5b69\u5b50\uff01\u7537\u5b69\u4eec\u6709\u81ea\u5df1\u7684\u79d8\u5bc6\u9886\u5730\uff0c\u53ef\u4ed6\u4eec\u5e38\u5e38\u89c9\u5f97\u90a3\u513f\u4e5f\u6ca1\u6709\u4ec0\u4e48\u597d\u73a9\u7684\u3002\u6885\u5409\u00b7\u6708\u4eae\u5374\u4e0d\u8fd9\u4e48\u770b\uff0c\u5bf9\u5979\u6765\u8bf4\uff0c\u9662\u5b50\u91cc\u7684\u4e00\u5207\u90fd\u5145\u6ee1\u9b54\u529b\uff0c\u53ea\u8981\u5979\u5ff5\u58f0\u5492\u8bed\uff0c\u5c31\u80fd\u628a\u5e9f\u589f\u53d8\u6210\u5b9d\u7269\uff01\u662f\u554a\uff0c\u5f53\u5b69\u5b50\u4eec\u5728\u4e00\u8d77\uff0c\u4ec0\u4e48\u795e\u5947\u7684\u4e8b\u60c5\u90fd\u6709\u53ef\u80fd\u53d1\u751f\uff01\r\n","rank":264,"score":9.2,"status":0},{"id":"ADMGNVA0DTA","name":"\u66b4\u98ce\u96e8\u6765\u4e86","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/6ska25y6.jpg","tariff":0,"price":0,"terms":"\u52a8\u7269\u6545\u4e8b,\u7231\u4e0e\u60c5\u611f,\u7761\u524d\u6545\u4e8b","tags":"\u8001\u9f20,\u53cb\u60c5,\u66b4\u98ce\u96e8","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u82f1\uff09\u674e\u68ee","age_from":2,"age_to":7,"comment":"\u8be5\u6545\u4e8b\u9009\u81ea\u806a\u660e\u8c46\u7ed8\u672c\u7cfb\u5217\uff0c\u201c\u806a\u660e\u8c46\u7ed8\u672c\u7cfb\u5217\u201d\u662f\u4e16\u754c\u5404\u5730\u4f18\u79c0\u56fe\u753b\u4e66\u7684\u7cbe\u9009\u5408\u8f91\u3002","description":"\u5c0f\u8001\u9f20\u83ab\u8389\u548c\u5979\u7684\u5144\u5f1f\u59d0\u59b9\u88ab\u66b4\u98ce\u96e8\u56f0\u4f4f\u4e86\uff0c\u670b\u53cb\u4eec\u7eb7\u7eb7\u63d0\u4f9b\u4f4f\u6240\uff0c\u53ef\u662f\u4ed6\u4eec\u7684\u4f4f\u6240\u90fd\u4e0d\u592a\u5b89\u5168\u3002\u540e\u6765\uff0c\u83ab\u8389\u4ed6\u4eec\u627e\u5230\u4e86\u4e00\u4e2a\u5b89\u5168\u7684\u5730\u65b9\uff0c\u53ef\u662f\u83ab\u8389\u8fd8\u662f\u62c5\u5fc3\u670b\u53cb\u4eec\u3002\u5979\u80fd\u5e2e\u52a9\u670b\u53cb\u4eec\u5ea6\u8fc7\u8fd9\u4e2a\u98ce\u96e8\u5927\u4f5c\u7684\u591c\u665a\u5417\uff1f\u5979\u662f\u5982\u4f55\u505a\u7684\u5462\uff1f","rank":286,"score":8.2,"status":0},{"id":"ADMGNVA0DTw","name":"\u522b\u5bb3\u6015\uff0c\u5c0f\u5bb6\u4f19","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/1pxylmer.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u52a8\u7269\u6545\u4e8b,\u806a\u660e\u8c46,\u7231\u4e0e\u60c5\u611f","tags":"\u8001\u864e,\u6bcd\u7231,\u806a\u660e\u8c46,\u5206\u79bb\u7126\u8651","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u7f8e\uff09\u5df4\u7279\u52d2","age_from":2,"age_to":7,"comment":"","description":"\u4e1b\u6797\u91cc\uff0c\u8001\u864e\u5988\u5988\u548c\u4e24\u53ea\u5c0f\u8001\u864e\u751f\u6d3b\u5728\u4e00\u8d77\u3002\u4e24\u53ea\u5c0f\u8001\u864e\u6e10\u6e10\u957f\u5927\u4e86\uff0c\u4ed6\u4eec\u5b66\u4f1a\u4e86\u4e00\u4e9b\u672c\u9886\u3002\u6709\u4e00\u5929\uff0c\u8001\u864e\u5988\u5988\u51fa\u53bb\u89c5\u98df\uff0c\u53ef\u662f\u5929\u9ed1\u4e86\uff0c\u5979\u4e5f\u6ca1\u6709\u56de\u6765\u3002\u4e24\u53ea\u5c0f\u8001\u864e\u5728\u627e\u5988\u5988\u7684\u8def\u4e0a\uff0c\u4f3c\u4e4e\u9047\u5230\u4e86\u4e00\u53ea\u9cc4\u9c7c\u2014\u2014\u771f\u7684\u662f\u4e00\u53ea\u9cc4\u9c7c\u5417\uff0c\u5feb\u5230\u4e66\u4e2d\u5bfb\u627e\u7b54\u6848\u5427\uff01","rank":267,"score":8.4,"status":0},{"id":"ADMGNVA1DTU","name":"\u5f69\u8679\u7684\u5c3d\u5934","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/qds8hdx7.jpg","tariff":0,"price":0,"terms":"\u7231\u4e0e\u60c5\u611f,\u7761\u524d\u6545\u4e8b,\u806a\u660e\u8c46","tags":"\u597d\u670b\u53cb,\u5b9d\u8d1d,\u5f69\u8679,\u806a\u660e\u8c46","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"[\u82f1]A.H.\u672c\u6770\u660e","age_from":2,"age_to":7,"comment":"\u201c\u806a\u660e\u8c46\u7ed8\u672c\u7cfb\u5217\u201d\u662f\u4e16\u754c\u5404\u5730\u4f18\u79c0\u56fe\u753b\u4e66\u7684\u7cbe\u9009\u5408\u8f91\u3002","description":"\u737e\u548c\u72d0\u72f8\u8981\u53bb\u5bfb\u627e\u5f69\u8679\u5c3d\u5934\u7684\u5b9d\u8d1d\uff0c\u5b83\u4eec\u5728\u9014\u4e2d\u9047\u5230\u4e86\u677e\u9f20\uff0c\u5b83\u7684\u5b9d\u8d1d\u662f\u677e\u679c\uff1b\u9047\u5230\u4e86\u9e2d\u5988\u5988\uff0c\u5b83\u7684\u5b9d\u8d1d\u662f\u5c0f\u9e2d\uff1b\u8fd8\u9047\u5230\u4e86\u5154\u5b50\u7237\u7237\uff0c\u5154\u5b50\u7237\u7237\u8bf4\u5b83\u7684\u5b9d\u8d1d\u662f\u56de\u5fc6\uff1b\u5728\u5f69\u8679\u6d88\u5931\u3001\u5927\u96e8\u6765\u4e34\u7684\u65f6\u5019\uff0c\u737e\u548c\u72d0\u72f8\u7ec8\u4e8e\u627e\u5230\u4e86\u5b83\u4eec\u81ea\u5df1\u7684\u5b9d\u8d1d\uff0c\u90a3\u662f\u4ec0\u4e48\u5462\u2026\u2026","rank":264,"score":9.7,"status":0},{"id":"ADMGNVA1DTQ","name":"\u597d\u5947\u9b3c\u6ce2\u897f","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/1\/j2hxlczt.jpg","tariff":0,"price":0,"terms":"\u7761\u524d\u6545\u4e8b,\u52a8\u7269\u6545\u4e8b,\u806a\u660e\u8c46,\u751f\u6d3b\u6210\u957f","tags":"\u5c0f\u732a,\u597d\u5947\u5fc3,\u806a\u660e\u8c46","performer":"\u53e3\u888b\u6545\u4e8b \u8c46\u8c46\u59d0\u59d0","author":"\uff08\u82f1\uff09\u59ae\u53e4\u62c9\u00b7\u683c\u5170\u7279\u8457","age_from":2,"age_to":7,"comment":"\u201c\u806a\u660e\u8c46\u7ed8\u672c\u7cfb\u5217\u201d\u662f\u4e16\u754c\u5404\u5730\u4f18\u79c0\u56fe\u753b\u4e66\u7684\u7cbe\u9009\u5408\u8f91\u3002","description":"\u5c0f\u732a\u6ce2\u897f\u60f3\u77e5\u9053\u4e00\u5207\u4e8b\u60c5\uff01\u5979\u95ee\u516c\u9e21\uff1a\u201c\u6bcf\u5929\u65e9\u4e0a\u8c01\u53eb\u9192\u4f60\u8d77\u5e8a\uff1f\u201d\u5979\u95ee\u6bcd\u9e21\uff1a\u201c\u4e0b\u86cb\u75bc\u5417\uff1f\u201d\u5927\u5bb6\u90fd\u5bf9\u5979\u8bf4\uff1a\u201c\u522b\u597d\u5947\u4e86\uff01\u201d\u4f46\u6ce2\u897f\u505a\u4e0d\u5230\u3002\u6709\u4e00\u5929\uff0c\u5979\u542c\u5230\u7530\u91ce\u90a3\u8fb9\u4f20\u6765\u4e86\u5947\u602a\u7684\u58f0\u97f3\uff0c\u539f\u6765\u662f\u4e00\u53ea\u5976\u725b\u9047\u5230\u9ebb\u70e6\u4e86\u3002\u5c0f\u732a\u6ce2\u897f\u597d\u5947\u7684\u6027\u683c\u6551\u4e86\u5976\u725b\u3002","rank":266,"score":8.7,"status":0}]},"retcode":0}

    a19205= {"data":{"works":[{"id":"ADcGMFAwDTM","name":"\u4e1c\u5468\u5217\u56fd\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/7kxqs3lr.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u4e1c\u5468\u5217\u56fd\u6545\u4e8b,\u4e2d\u56fd\u540d\u8457,\u5386\u53f2\u6545\u4e8b,\u6559\u80b2\u90e8\u63a8\u8350\u4e66\u76ee","tags":"\u4e1c\u5468\u5217\u56fd,\u6625\u79cb\u4e94\u9738,\u6218\u56fd\u4e03\u96c4,\u5386\u53f2\u4eba\u7269","performer":"\u53e3\u888b\u6545\u4e8b \u66f9\u707f","author":"\u51af\u68a6\u9f99","age_from":7,"age_to":12,"comment":"\u66f9\u707f\uff0c\u8457\u540d\u8001\u4e00\u8f88\u6f14\u64ad\u827a\u672f\u5bb6\uff0c\u4e2d\u56fd\u56fd\u5bb6\u8bdd\u5267\u9662\u56fd\u5bb6\u4e00\u7ea7\u6f14\u5458\u3002\u6f14\u64ad\u4ee3\u8868\u4f5c\u6709\u5c11\u513f\u7248\u56db\u5927\u540d\u8457\u4e4b\u300a\u7ea2\u697c\u68a6\u7684\u6545\u4e8b\u300b\u3002","description":"\u5728\u4e1c\u5468\u8fd9\u4e2a\u52a8\u8361\u7684\u4e71\u4e16\u4e2d\uff0c\u6625\u79cb\u4e94\u9738\u3001\u6218\u56fd\u4e03\u96c4\u7b49\u5386\u53f2\u4eba\u7269\u8f6e\u756a\u767b\u573a\u63a8\u52a8\u7740\u4e1c\u5468\u5386\u53f2\u8f66\u8f6e\u7684\u524d\u8fdb\uff0c\u4e0a\u6f14\u4e86\u4e00\u51fa\u51fa\u7cbe\u5f69\u7684\u5386\u53f2\u5267\u76ee\u3002","rank":280,"score":9.6,"status":0},{"id":"ADAGMVA8DTw","name":"\u66f9\u51b2\u79f0\u8c61","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/l152qlzn.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u540d\u4eba\u6545\u4e8b,\u7761\u524d\u6545\u4e8b","tags":"\u6210\u8bed\u6545\u4e8b,\u667a\u6167\u6545\u4e8b","performer":"\u53e3\u888b\u6545\u4e8b \u745e\u4e01\u8001\u7238","author":"\u4f5a\u540d","age_from":-1,"age_to":7,"comment":"\u745e\u4e01\u8001\u7238\u662f\u70ed\u7231\u5b69\u5b50\u7684\u7ae5\u4e66\u521b\u4f5c\u4eba\uff0c\u81f4\u529b\u4e8e\u57f9\u517b\u5b69\u5b50\u7684\u535a\u7269\u77e5\u8bc6\u548c\u4f18\u79c0\u9605\u8bfb\u529b\uff0c\u5148\u540e\u5236\u4f5c\u300a\u745e\u4e01\u8001\u7238\u8bb2\u767e\u79d1\u300b\u548c\u300a\u745e\u4e01\u8001\u7238\u8bb2\u6545\u4e8b\u300b\u4e24\u6863\u8282\u76ee\uff0c\u8ba9\u5b69\u5b50\u7528\u6700\u8f7b\u677e\u7684\u65b9\u5f0f\uff0c\u8ba4\u8bc6\u5927\u5343\u4e16\u754c\u3002\u6b22\u8fce\u52a0\u5165\u745e\u4e01\u8001\u7238\u7684\u9605\u8bfb\u8ba8\u8bba\u7fa4\uff1a241042091\u3002","description":"\u66f9\u51b2\u662f\u4e09\u56fd\u65f6\u671f\u66f9\u64cd\u7684\u513f\u5b50\uff0c\u6709\u4e00\u6b21\u5b59\u6743\u9001\u6765\u4e00\u5934\u5de8\u5927\u7684\u8c61\uff0c\u66f9\u64cd\u60f3\u8981\u77e5\u9053\u8fd9\u8c61\u7684\u91cd\u91cf\uff0c\u5411\u4ed6\u7684\u4e0b\u5c5e\u8be2\u95ee\u8fd9\u4ef6\u4e8b\uff0c\u90fd\u4e0d\u80fd\u60f3\u51fa\u79f0\u8c61\u7684\u529e\u6cd5\u3002\u66f9\u51b2\u8bf4\uff1a\u201c\u628a\u8c61\u5b89\u653e\u5230\u5927\u8239\u4e0a\uff0c\u5728\u6c34\u6ca1\u8fc7\u8239\u75d5\u8ff9\u7684\u5730\u65b9\u523b\u4e0a\u8bb0\u53f7\uff0c\u79f0\u5b9e\u7269\u88c5\u4e0a\u8239\uff0c\u90a3\u4e48\u6bd4\u8f83\u5c31\u80fd\u77e5\u9053\u7ed3\u679c\u4e86\u3002\u201d\u66f9\u64cd\u542c\u4e86\u5f88\u9ad8\u5174\uff0c\u7acb\u523b\u5b9e\u65bd\u884c\u52a8\u3002","rank":257,"score":7.8,"status":0},{"id":"ADAGMFAwDTU","name":"\u542c\u6545\u4e8b\u5b66\u5386\u53f21","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/dofapyoh.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u5386\u53f2\u6545\u4e8b,\u5973\u5b69\u6545\u4e8b,\u7537\u5b69\u6545\u4e8b","tags":"\u5927\u79b9\u6cbb\u6c34,\u86a9\u5c24,\u8f69\u8f95\u9ec4\u5e1d","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":6,"age_to":18,"comment":"","description":"\u300a\u542c\u6545\u4e8b\u5b66\u5386\u53f2\u300b\u662f\u4e00\u5957\u7531\u8457\u540d\u5386\u53f2\u5b66\u5bb6\u4e13\u95e8\u4e3a\u4e2d\u5c0f\u5b66\u751f\u7f16\u5199\u7684\u4e2d\u56fd\u5386\u53f2\u6545\u4e8b\u8bfb\u672c\u3002\u5b83\u4ee5\u4e2d\u56fd\u5404\u671d\u4ee3\u7684\u8457\u540d\u5386\u53f2\u4eba\u7269\u548c\u4e8b\u4ef6\u4e3a\u4e3b\u7ebf\uff0c\u642d\u5efa\u4e86\u4e2d\u56fd\u5386\u53f2\u77e5\u8bc6\u7684\u4e3b\u4f53\u6846\u67b6\u3002\u8fd9\u4e9b\u6545\u4e8b\u4ee5\u751f\u52a8\u6709\u8da3\uff0c\u5999\u8da3\u6a2a\u751f\u7684\u60c5\u8282\u6df1\u6df1\u5730\u5438\u5f15\u7740\u8bfb\u8005\uff0c\u6fc0\u53d1\u4e86\u5e7f\u5927\u4e2d\u5c0f\u5b66\u751f\u5b66\u4e60\u4e2d\u56fd\u5386\u53f2\u3001\u638c\u63e1\u5386\u53f2\u77e5\u8bc6\u7684\u5174\u8da3\u3002","rank":260,"score":8.5,"status":0},{"id":"ADAGMFAyDTU","name":"\u542c\u6545\u4e8b\u5b66\u5386\u53f22","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/0\/o3i4ayai.jpg","tariff":0,"price":0,"terms":"\u4e2d\u56fd\u5386\u53f2,\u5386\u53f2\u6545\u4e8b,\u5973\u5b69\u6545\u4e8b,\u7537\u5b69\u6545\u4e8b","tags":"\u548c\u6c0f\u74a7,\u6625\u79cb,\u6218\u56fd,\u6fc0\u5c06\u6cd5","performer":"\u53e3\u888b\u6545\u4e8b","author":"\u4f5a\u540d","age_from":6,"age_to":18,"comment":"","description":"\u300a\u542c\u6545\u4e8b\u5b66\u5386\u53f2\u300b\u662f\u4e00\u5957\u7531\u8457\u540d\u5386\u53f2\u5b66\u5bb6\u4e13\u95e8\u4e3a\u4e2d\u5c0f\u5b66\u751f\u7f16\u5199\u7684\u4e2d\u56fd\u5386\u53f2\u6545\u4e8b\u8bfb\u672c\u3002\u5b83\u4ee5\u4e2d\u56fd\u5404\u671d\u4ee3\u7684\u8457\u540d\u5386\u53f2\u4eba\u7269\u548c\u4e8b\u4ef6\u4e3a\u4e3b\u7ebf\uff0c\u642d\u5efa\u4e86\u4e2d\u56fd\u5386\u53f2\u77e5\u8bc6\u7684\u4e3b\u4f53\u6846\u67b6\u3002\u8fd9\u4e9b\u6545\u4e8b\u4ee5\u751f\u52a8\u6709\u8da3\uff0c\u5999\u8da3\u6a2a\u751f\u7684\u60c5\u8282\u6df1\u6df1\u5730\u5438\u5f15\u7740\u8bfb\u8005\uff0c\u6fc0\u53d1\u4e86\u5e7f\u5927\u4e2d\u5c0f\u5b66\u751f\u5b66\u4e60\u4e2d\u56fd\u5386\u53f2\u3001\u638c\u63e1\u5386\u53f2\u77e5\u8bc6\u7684\u5174\u8da3\u3002","rank":258,"score":8.7,"status":0},{"id":"ADMGM1A3DTI","name":"\u597d\u5b69\u5b50\u6700\u60f3\u77e5\u9053\u7684\u4f20\u8bf4\u6545\u4e8b","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/9b19zga2.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u597d\u5b69\u5b50\u6700\u60f3\u77e5\u9053\u7684\u6545\u4e8b\u7cfb\u5217,\u7761\u524d\u6545\u4e8b","tags":"\u6c11\u95f4\u4f20\u8bf4,\u4e60\u4fd7,\u5143\u5bb5","performer":"\u53e3\u888b\u6545\u4e8b \u9ed1\u773c\u8c46\u8c46","author":"\u9648\u5929\u7b49","age_from":4,"age_to":10,"comment":"\u7cbe\u9009\u4e00\u7bc7\u7bc7\u810d\u7099\u4eba\u53e3\u7684\u4f20\u8bf4\u6545\u4e8b\uff0c\u8ba9\u5b69\u5b50\u5728\u54c1\u8bfb\u4f20\u8bf4\u7684\u540c\u65f6\uff0c\u63d2\u4e0a\u60f3\u8c61\u7684\u7fc5\u8180\uff0c\u9068\u6e38\u5728\u707f\u70c2\u7684\u4eba\u7c7b\u5386\u53f2\u6587\u660e\u7684\u5929\u7a7a\u4e2d\u3002\u9009\u81ea\u6d59\u6c5f\u5c11\u5e74\u513f\u7ae5\u51fa\u7248\u793e\u51fa\u7248\u7684\u300a\u597d\u5b69\u5b50\u6545\u4e8b\u9986\u300b\uff0c\u4e66\u4e2d\u8fd8\u6709\u66f4\u591a\u7684\u7cbe\u5f69\u6545\u4e8b\u3002\r\n\u4ec0\u4e48\u662f\u3010\u5de5\u7238inside\u3011\uff1f\r\n\u5de5\u7238\u65d7\u4e0b\u7684\u53e3\u888b\u6545\u4e8b\u5236\u4f5c\u4e86\u513f\u7ae5\u56fe\u4e66\u7684\u97f3\u9891\uff0c\u5e76\u5c06\u97f3\u9891\u4e8c\u7ef4\u7801\u690d\u5165\u513f\u7ae5\u56fe\u4e66\u4e2d\u3002\u7528\u6237\u4e70\u4e86\u8fd9\u4e9b\u56fe\u4e66\uff0c\u7528\u624b\u673a\u626b\u4e00\u626b\u56fe\u4e66\u540e\u7684\u4e8c\u7ef4\u7801\uff0c\u5373\u53ef\u6536\u542c\u8be5\u6545\u4e8b\u3002\u8be5\u4e66\u4e3a\u3010\u5de5\u7238inside\u3011\u7cfb\u5217\u4f5c\u54c1\u4e4b\u4e00\u3002","description":"\u7aef\u5348\u8282\u3001\u4e5d\u8272\u9e7f\u3001\u5973\u5a32\u9020\u4eba\u2026\u2026\u53e4\u8001\u6c38\u6052\u3001\u5f71\u54cd\u6df1\u8fdc\u7684\u4f20\u8bf4\u4e2d\u5305\u542b\u7740\u4eba\u7c7b\u5bf9\u7f8e\u597d\u7eaf\u771f\u7684\u5411\u5f80\uff0c\u7f8e\u4e3d\u52a8\u4eba\u7684\u6545\u4e8b\u66f4\u662f\u6ecb\u517b\u5b69\u5b50\u5fc3\u7075\u7684\u9187\u539a\u517b\u6599\u3002","rank":324,"score":9.3,"status":0},{"id":"ADMGMFAwDTA","name":"\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2\uff1a1\u76d8\u53e4\u5f00\u5929\u5730","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/5\/sw3ync5f.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2,\u7761\u524d\u6545\u4e8b","tags":"\u5386\u53f2,\u82e5\u8679\u5988\u5988,\u8fdc\u53e4,\u76d8\u53e4","performer":"\u53e3\u888b\u6545\u4e8b \u82e5\u8679\u5988\u5988","author":"\u82e5\u8679\u5988\u5988","age_from":4,"age_to":8,"comment":"\u8457\u540d\u513f\u7ae5\u6545\u4e8b\u4e3b\u64ad\u82e5\u8679\u5988\u5988\u7684\u6700\u65b0\u539f\u521b\u6f14\u64ad\u4f5c\u54c1\u3002","description":"\u54b1\u4eec\u4e2d\u56fd\u7684\u5386\u53f2\u662f\u4ece\u8fdc\u53e4\u4f20\u8bf4\u5f00\u59cb\u7684\uff0c\u4eba\u4eec\u7528\u795e\u5947\u7684\u6545\u4e8b\u6f14\u7ece\u7740\u4e16\u95f4\u4e07\u7269\u4ee5\u53ca\u4eba\u7c7b\u7684\u4ea7\u751f\uff0c\u4e5f\u63cf\u7ed8\u4e86\u8fdc\u53e4\u7684\u4eba\u7c7b\u5982\u4f55\u548c\u81ea\u7136\u754c\u7684\u5404\u79cd\u8270\u96be\u9669\u963b\u8fdb\u884c\u6597\u4e89\uff0c\u4e00\u6b65\u6b65\u8fc7\u4e0a\u7a33\u5b9a\u5b89\u5b81\u7684\u751f\u6d3b\u7684\u3002\u66f4\u5411\u6211\u4eec\u5c55\u793a\u4e86\u4eba\u7c7b\u5982\u4f55\u53d1\u6325\u81ea\u5df1\u7684\u806a\u660e\u624d\u667a\uff0c\u53d1\u73b0\u3001\u8fd0\u7528\u3001\u521b\u9020\u4e86\u706b\u79cd\u3001\u5929\u8c61\u3001\u8349\u836f\u3001\u6587\u5b57\u751a\u81f3\u7f8e\u9152\uff0c\u4e0d\u65ad\u53d1\u5c55\u4e30\u5bcc\u6587\u660e\u7684\u3002\u4ece\u73b0\u5728\u5f00\u59cb\uff0c\u82e5\u8679\u5988\u5988\u5c06\u628a\u8fd9\u4e9b\u5185\u5bb9\u68b3\u7406\u51fa\u6765\u8bb2\u7ed9\u5927\u5bb6\u542c\uff0c\u4f7f\u5927\u5bb6\u6210\u4e3a\u4e86\u89e3\u4e2d\u56fd\u6587\u8109\u7684\u4e00\u4e2a\u6709\u77e5\u8bc6\u6709\u6587\u5316\u7684\u5b69\u5b50\u3002","rank":270,"score":8.9,"status":0},{"id":"ADMGMFAwDTM","name":"\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2\uff1a8\u4f0f\u7fb2\u516b\u5366","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/6\/ce32k631.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2,\u7761\u524d\u6545\u4e8b","tags":"\u5386\u53f2,\u82e5\u8679\u5988\u5988,\u8fdc\u53e4,\u4f0f\u7fb2,\u516b\u5366","performer":"\u53e3\u888b\u6545\u4e8b \u82e5\u8679\u5988\u5988","author":"\u82e5\u8679\u5988\u5988","age_from":4,"age_to":8,"comment":"\u8457\u540d\u513f\u7ae5\u6545\u4e8b\u4e3b\u64ad\u82e5\u8679\u5988\u5988\u7684\u6700\u65b0\u539f\u521b\u6f14\u64ad\u4f5c\u54c1\u3002","description":"\u54b1\u4eec\u4e2d\u56fd\u7684\u5386\u53f2\u662f\u4ece\u8fdc\u53e4\u4f20\u8bf4\u5f00\u59cb\u7684\uff0c\u4eba\u4eec\u7528\u795e\u5947\u7684\u6545\u4e8b\u6f14\u7ece\u7740\u4e16\u95f4\u4e07\u7269\u4ee5\u53ca\u4eba\u7c7b\u7684\u4ea7\u751f\uff0c\u4e5f\u63cf\u7ed8\u4e86\u8fdc\u53e4\u7684\u4eba\u7c7b\u5982\u4f55\u548c\u81ea\u7136\u754c\u7684\u5404\u79cd\u8270\u96be\u9669\u963b\u8fdb\u884c\u6597\u4e89\uff0c\u4e00\u6b65\u6b65\u8fc7\u4e0a\u7a33\u5b9a\u5b89\u5b81\u7684\u751f\u6d3b\u7684\u3002\u66f4\u5411\u6211\u4eec\u5c55\u793a\u4e86\u4eba\u7c7b\u5982\u4f55\u53d1\u6325\u81ea\u5df1\u7684\u806a\u660e\u624d\u667a\uff0c\u53d1\u73b0\u3001\u8fd0\u7528\u3001\u521b\u9020\u4e86\u706b\u79cd\u3001\u5929\u8c61\u3001\u8349\u836f\u3001\u6587\u5b57\u751a\u81f3\u7f8e\u9152\uff0c\u4e0d\u65ad\u53d1\u5c55\u4e30\u5bcc\u6587\u660e\u7684\u3002\u4ece\u73b0\u5728\u5f00\u59cb\uff0c\u82e5\u8679\u5988\u5988\u5c06\u628a\u8fd9\u4e9b\u5185\u5bb9\u68b3\u7406\u51fa\u6765\u8bb2\u7ed9\u5927\u5bb6\u542c\uff0c\u4f7f\u5927\u5bb6\u6210\u4e3a\u4e86\u89e3\u4e2d\u56fd\u6587\u8109\u7684\u4e00\u4e2a\u6709\u77e5\u8bc6\u6709\u6587\u5316\u7684\u5b69\u5b50\u3002","rank":269,"score":9.6,"status":0},{"id":"ADMGMFAwDTI","name":"\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2\uff1a9\u795e\u519c\u5c1d\u767e\u8349","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/7\/8xp53o9x.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2,\u7761\u524d\u6545\u4e8b","tags":"\u5386\u53f2,\u82e5\u8679\u5988\u5988,\u8fdc\u53e4,\u795e\u519c","performer":"\u53e3\u888b\u6545\u4e8b \u82e5\u8679\u5988\u5988","author":"\u82e5\u8679\u5988\u5988","age_from":4,"age_to":8,"comment":"\u8457\u540d\u513f\u7ae5\u6545\u4e8b\u4e3b\u64ad\u82e5\u8679\u5988\u5988\u7684\u6700\u65b0\u539f\u521b\u6f14\u64ad\u4f5c\u54c1\u3002","description":"\u54b1\u4eec\u4e2d\u56fd\u7684\u5386\u53f2\u662f\u4ece\u8fdc\u53e4\u4f20\u8bf4\u5f00\u59cb\u7684\uff0c\u4eba\u4eec\u7528\u795e\u5947\u7684\u6545\u4e8b\u6f14\u7ece\u7740\u4e16\u95f4\u4e07\u7269\u4ee5\u53ca\u4eba\u7c7b\u7684\u4ea7\u751f\uff0c\u4e5f\u63cf\u7ed8\u4e86\u8fdc\u53e4\u7684\u4eba\u7c7b\u5982\u4f55\u548c\u81ea\u7136\u754c\u7684\u5404\u79cd\u8270\u96be\u9669\u963b\u8fdb\u884c\u6597\u4e89\uff0c\u4e00\u6b65\u6b65\u8fc7\u4e0a\u7a33\u5b9a\u5b89\u5b81\u7684\u751f\u6d3b\u7684\u3002\u66f4\u5411\u6211\u4eec\u5c55\u793a\u4e86\u4eba\u7c7b\u5982\u4f55\u53d1\u6325\u81ea\u5df1\u7684\u806a\u660e\u624d\u667a\uff0c\u53d1\u73b0\u3001\u8fd0\u7528\u3001\u521b\u9020\u4e86\u706b\u79cd\u3001\u5929\u8c61\u3001\u8349\u836f\u3001\u6587\u5b57\u751a\u81f3\u7f8e\u9152\uff0c\u4e0d\u65ad\u53d1\u5c55\u4e30\u5bcc\u6587\u660e\u7684\u3002\u4ece\u73b0\u5728\u5f00\u59cb\uff0c\u82e5\u8679\u5988\u5988\u5c06\u628a\u8fd9\u4e9b\u5185\u5bb9\u68b3\u7406\u51fa\u6765\u8bb2\u7ed9\u5927\u5bb6\u542c\uff0c\u4f7f\u5927\u5bb6\u6210\u4e3a\u4e86\u89e3\u4e2d\u56fd\u6587\u8109\u7684\u4e00\u4e2a\u6709\u77e5\u8bc6\u6709\u6587\u5316\u7684\u5b69\u5b50\u3002","rank":269,"score":9.5,"status":0},{"id":"ADMGMFAwDT0","name":"\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2\uff1a10\u708e\u9ec4\u4e4b\u6218","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/8\/ibgzxacs.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2,\u7761\u524d\u6545\u4e8b","tags":"\u5386\u53f2,\u82e5\u8679\u5988\u5988,\u8fdc\u53e4,\u708e\u5e1d,\u9ec4\u5e1d","performer":"\u53e3\u888b\u6545\u4e8b \u82e5\u8679\u5988\u5988","author":"\u82e5\u8679\u5988\u5988","age_from":4,"age_to":8,"comment":"\u8457\u540d\u513f\u7ae5\u6545\u4e8b\u4e3b\u64ad\u82e5\u8679\u5988\u5988\u7684\u6700\u65b0\u539f\u521b\u6f14\u64ad\u4f5c\u54c1\u3002","description":"\u54b1\u4eec\u4e2d\u56fd\u7684\u5386\u53f2\u662f\u4ece\u8fdc\u53e4\u4f20\u8bf4\u5f00\u59cb\u7684\uff0c\u4eba\u4eec\u7528\u795e\u5947\u7684\u6545\u4e8b\u6f14\u7ece\u7740\u4e16\u95f4\u4e07\u7269\u4ee5\u53ca\u4eba\u7c7b\u7684\u4ea7\u751f\uff0c\u4e5f\u63cf\u7ed8\u4e86\u8fdc\u53e4\u7684\u4eba\u7c7b\u5982\u4f55\u548c\u81ea\u7136\u754c\u7684\u5404\u79cd\u8270\u96be\u9669\u963b\u8fdb\u884c\u6597\u4e89\uff0c\u4e00\u6b65\u6b65\u8fc7\u4e0a\u7a33\u5b9a\u5b89\u5b81\u7684\u751f\u6d3b\u7684\u3002\u66f4\u5411\u6211\u4eec\u5c55\u793a\u4e86\u4eba\u7c7b\u5982\u4f55\u53d1\u6325\u81ea\u5df1\u7684\u806a\u660e\u624d\u667a\uff0c\u53d1\u73b0\u3001\u8fd0\u7528\u3001\u521b\u9020\u4e86\u706b\u79cd\u3001\u5929\u8c61\u3001\u8349\u836f\u3001\u6587\u5b57\u751a\u81f3\u7f8e\u9152\uff0c\u4e0d\u65ad\u53d1\u5c55\u4e30\u5bcc\u6587\u660e\u7684\u3002\u4ece\u73b0\u5728\u5f00\u59cb\uff0c\u82e5\u8679\u5988\u5988\u5c06\u628a\u8fd9\u4e9b\u5185\u5bb9\u68b3\u7406\u51fa\u6765\u8bb2\u7ed9\u5927\u5bb6\u542c\uff0c\u4f7f\u5927\u5bb6\u6210\u4e3a\u4e86\u89e3\u4e2d\u56fd\u6587\u8109\u7684\u4e00\u4e2a\u6709\u77e5\u8bc6\u6709\u6587\u5316\u7684\u5b69\u5b50\u3002","rank":269,"score":9,"status":0},{"id":"ADMGMFAwDTw","name":"\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2\uff1a11\u5211\u5929\u590d\u4ec7","icon":"http:\/\/img.ilisten.idaddy.cn\/b\/9\/sa4z3zxa.jpg","tariff":0,"price":0,"terms":"\u5386\u53f2\u5178\u6545,\u5386\u53f2\u6545\u4e8b,\u54ac\u6587\u56bc\u5b57\u8bb2\u5386\u53f2,\u7761\u524d\u6545\u4e8b","tags":"\u5386\u53f2,\u82e5\u8679\u5988\u5988,\u5211\u5929,\u8fdc\u53e4","performer":"\u53e3\u888b\u6545\u4e8b \u82e5\u8679\u5988\u5988","author":"\u82e5\u8679\u5988\u5988","age_from":4,"age_to":8,"comment":"\u8457\u540d\u513f\u7ae5\u6545\u4e8b\u4e3b\u64ad\u82e5\u8679\u5988\u5988\u7684\u6700\u65b0\u539f\u521b\u6f14\u64ad\u4f5c\u54c1\u3002","description":"\u54b1\u4eec\u4e2d\u56fd\u7684\u5386\u53f2\u662f\u4ece\u8fdc\u53e4\u4f20\u8bf4\u5f00\u59cb\u7684\uff0c\u4eba\u4eec\u7528\u795e\u5947\u7684\u6545\u4e8b\u6f14\u7ece\u7740\u4e16\u95f4\u4e07\u7269\u4ee5\u53ca\u4eba\u7c7b\u7684\u4ea7\u751f\uff0c\u4e5f\u63cf\u7ed8\u4e86\u8fdc\u53e4\u7684\u4eba\u7c7b\u5982\u4f55\u548c\u81ea\u7136\u754c\u7684\u5404\u79cd\u8270\u96be\u9669\u963b\u8fdb\u884c\u6597\u4e89\uff0c\u4e00\u6b65\u6b65\u8fc7\u4e0a\u7a33\u5b9a\u5b89\u5b81\u7684\u751f\u6d3b\u7684\u3002\u66f4\u5411\u6211\u4eec\u5c55\u793a\u4e86\u4eba\u7c7b\u5982\u4f55\u53d1\u6325\u81ea\u5df1\u7684\u806a\u660e\u624d\u667a\uff0c\u53d1\u73b0\u3001\u8fd0\u7528\u3001\u521b\u9020\u4e86\u706b\u79cd\u3001\u5929\u8c61\u3001\u8349\u836f\u3001\u6587\u5b57\u751a\u81f3\u7f8e\u9152\uff0c\u4e0d\u65ad\u53d1\u5c55\u4e30\u5bcc\u6587\u660e\u7684\u3002\u4ece\u73b0\u5728\u5f00\u59cb\uff0c\u82e5\u8679\u5988\u5988\u5c06\u628a\u8fd9\u4e9b\u5185\u5bb9\u68b3\u7406\u51fa\u6765\u8bb2\u7ed9\u5927\u5bb6\u542c\uff0c\u4f7f\u5927\u5bb6\u6210\u4e3a\u4e86\u89e3\u4e2d\u56fd\u6587\u8109\u7684\u4e00\u4e2a\u6709\u77e5\u8bc6\u6709\u6587\u5316\u7684\u5b69\u5b50\u3002","rank":269,"score":8.8,"status":0}]},"retcode":0}

    print(a19205)
    names_list = []
    data_list = a6707['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a6708['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a6948['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a7156['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a7716['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a16815['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a17164['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a17176['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a17466['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])
    data_list = a19205['data']['works']
    for i in data_list:
        # print(i['name'])
        names_list.append(i['name'])

    print(len(names_list))
    name_set = set()
    for i in names_list:
        i= chinese_num(i)
        i=quchubidian(i)
        print(i)
        name_set.add(i)
    print(len(name_set))
    # print(a19205)
    final_dict = dict()
    final_dict['dict']=[]
    cur_dict = dict()
    cur_dict['majorType']='koudaigushi_title'
    cur_dict['value']= list(name_set)
    final_dict['dict'].append(cur_dict)
    print(final_dict)

    with open('/home/gaozhiwei/Desktop/koudaigushi.json','w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=2))
def mainone():
    category = {
    "audioinfos": {
        "cats": [
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/qx7houcn.png",
                "cat_name": "\u513f\u6b4c",
                "cat_id": 6707,
                "cat_group_age_scope": "-1-8",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/vfj0epki.png",
                "cat_name": "\u6545\u4e8b",
                "cat_id": 6708,
                "cat_group_age_scope": "1+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/fk36owk7.png",
                "cat_name": "\u97f3\u4e50",
                "cat_id": 6948,
                "cat_group_age_scope": "0+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/9rlfhx3f.png",
                "cat_name": "\u82f1\u8bed",
                "cat_id": 7156,
                "cat_group_age_scope": "1+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/9y0vcvet.png",
                "cat_name": "\u56fd\u5b66",
                "cat_id": 7716,
                "cat_group_age_scope": "0+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/dvwcry5d.png",
                "cat_name": "\u5e7f\u64ad\u5267",
                "cat_id": 12724,
                "cat_group_age_scope": "5+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/9ez08ldk.png",
                "cat_name": "\u79d1\u666e",
                "cat_id": 16815,
                "cat_group_age_scope": "3+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/4ajjhpe0.png",
                "cat_name": "\u540d\u8457",
                "cat_id": 17164,
                "cat_group_age_scope": "5+",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/on77yoo6.png",
                "cat_name": "\u5b9d\u8d1d\u79c0",
                "cat_id": 17174,
                "cat_group_age_scope": "-1-18",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/aetyh99o.png",
                "cat_name": "\u80ce\u6559",
                "cat_id": 17176,
                "cat_group_age_scope": "-1-1",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/e3f42br0.png",
                "cat_name": "\u7ed8\u672c",
                "cat_id": 17466,
                "cat_group_age_scope": "1-8",
                "cat_parent": 0
            },
            {
                "cat_count": "0",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/9/c90txxr7.png",
                "cat_name": "\u5386\u53f2",
                "cat_id": 19205,
                "cat_group_age_scope": "4+",
                "cat_parent": 0
            }
        ]
    },
    "retcode": 0}

    info_list=category["audioinfos"]['cats']
    for i in info_list:
        print(i["cat_name"])
        print(i['cat_id'])
    second_category={
    "audioinfos": {
        "cats": [
            {
                "cat_count": "35",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/4/xs4ozwyc.jpg",
                "cat_name": "\u70ed\u95e8\u513f\u6b4c",
                "cat_id": 8118,
                "cat_group_age_scope": "-1-6",
                "cat_parent": 6707
            },
            {
                "cat_count": "6",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/4/nl9ezckp.jpg",
                "cat_name": "\u65e9\u6559\u513f\u6b4c",
                "cat_id": 10719,
                "cat_group_age_scope": "1-6",
                "cat_parent": 6707
            },
            {
                "cat_count": "5",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/4/dsws0q0o.jpg",
                "cat_name": "\u5e7c\u513f\u56ed\u7ae5\u8c23",
                "cat_id": 11423,
                "cat_group_age_scope": "1-6",
                "cat_parent": 6707
            },
            {
                "cat_count": "3",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/6/f5i1z0n9.jpg",
                "cat_name": "\u97f5\u5f8b\u7ae5\u8c23",
                "cat_id": 13945,
                "cat_group_age_scope": "2-6",
                "cat_parent": 6707
            },
            {
                "cat_count": "13",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/4/k5xrsszd.jpg",
                "cat_name": "\u5e7c\u5c0f\u8854\u63a5",
                "cat_id": 14655,
                "cat_group_age_scope": "2-6",
                "cat_parent": 6707
            },
            {
                "cat_count": "1",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/1/pmj9nc5v.jpg",
                "cat_name": "\u513f\u7ae5\u8c1c\u8bed",
                "cat_id": 14691,
                "cat_group_age_scope": "3-6",
                "cat_parent": 6707
            },
            {
                "cat_count": "49",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/6/mu74hudl.jpg",
                "cat_name": "\u82f1\u6587\u78e8\u8033",
                "cat_id": 19587,
                "cat_group_age_scope": "-1+",
                "cat_parent": 6707
            },
            {
                "cat_count": "1",
                "cat_icon_url": "https://img.ilisten.idaddy.cn/f/h/6/qls43mkv.jpg",
                "cat_name": "\u5730\u65b9\u7ae5\u8c23",
                "cat_id": 19589,
                "cat_group_age_scope": "-1-6",
                "cat_parent": 6707
            }
        ]
    },
    "retcode": 0
}
    info_list_second = second_category["audioinfos"]['cats']
    print("="*100)
    for i in info_list_second:
        print(i["cat_name"])
        print(i['cat_id'])


    third_category = {
        "audioinfos": {
            "contents": [
                {
                    "status": 0,
                    "name": "\u9c81\u51b0\u82b1",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/d234/soundAI000000001/201908200000/0/ADcGNFA9.YTY0LzkvZWpvbjBlZTcuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/d234/soundAI000000001/201908200000/0/ADcGNFA9.YTY0LzkvZWpvbjBlZTcuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u5531\u7ed9\u5988\u5988\u7684\u513f\u6b4c,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "dba6efbaf034ef75bc18e30680939e69",
                    "id": "ADcGNFA9",
                    "icon": "https://img.ilisten.idaddy.cn/b/9/oy1wtag7.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5c0f\u71d5\u5b50",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/4dab/soundAI000000001/201908200000/0/ADcGM1Ay.YS82LzN6YXg1bzVtLmF1ZGlv.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/4dab/soundAI000000001/201908200000/0/ADcGM1Ay.YS82LzN6YXg1bzVtLmF1ZGlv.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "2013\u5e74\u5ea6\u7cbe\u9009\u96c6,\u70ed\u95e8\u513f\u6b4c,\u8e0f\u6625\u90ca\u6e38\u4e13\u8f91",
                    "md5": "2a3fceb2c945e8ceeb63b63bfd168d40",
                    "id": "ADcGM1Ay",
                    "icon": "https://img.ilisten.idaddy.cn/b/6/d41jzfe9.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5c0f\u5154\u5b50\u4e56\u4e56",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/6f8d/soundAI000000001/201908200000/0/ADcGMlA9.YTY0LzAvaWFobzh3aS5hdWRpbw.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/6f8d/soundAI000000001/201908200000/0/ADcGMlA9.YTY0LzAvaWFobzh3aS5hdWRpbw.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "8b76683368bd9f32dde43722f8f3280e",
                    "id": "ADcGMlA9",
                    "icon": "https://img.ilisten.idaddy.cn/b/9/jup2nhe8.jpg"
                },
                {
                    "status": 0,
                    "name": "\u6349\u6ce5\u9cc5",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/2be0/soundAI000000001/201908200000/0/ADcGMVA1.YTY0LzEvcnJhd3c1eTMuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/2be0/soundAI000000001/201908200000/0/ADcGMVA1.YTY0LzEvcnJhd3c1eTMuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c,\u590f\u5929\u7684\u6b4c",
                    "md5": "0ed1e3b9d4da1e848d604fcfbaf1897b",
                    "id": "ADcGMVA1",
                    "icon": "https://img.ilisten.idaddy.cn/b/1/opfa77h.jpg"
                },
                {
                    "status": 0,
                    "name": "\u62d4\u841d\u535c",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/9fb4/soundAI000000001/201908200000/0/ADcGMFAz.YS83L2piMjZucjM2LmF1ZGlv.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/9fb4/soundAI000000001/201908200000/0/ADcGMFAz.YS83L2piMjZucjM2LmF1ZGlv.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "87b8ab46c634893e243f8a82f5927ef1",
                    "id": "ADcGMFAz",
                    "icon": "https://img.ilisten.idaddy.cn/b/7/doef3v7w.jpg"
                },
                {
                    "status": 0,
                    "name": "\u6211\u662f\u4e00\u4e2a\u7c89\u5237\u5320",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/2d7f/soundAI000000001/201908200000/0/ADYGN1A0.YTY0LzAvcDRyajFpcG0uYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/2d7f/soundAI000000001/201908200000/0/ADYGN1A0.YTY0LzAvcDRyajFpcG0uYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "6c232fcada7d4be2fb02f2f531cdf58a",
                    "id": "ADYGN1A0",
                    "icon": "https://img.ilisten.idaddy.cn/b/0/hurakqo7.jpg"
                },
                {
                    "status": 0,
                    "name": "\u846b\u82a6\u5a03\u4e3b\u9898\u66f2",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/cbce/soundAI000000001/201908200000/0/ADYGNlAy.YTY0LzYvYmVpejc0ajguYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/cbce/soundAI000000001/201908200000/0/ADYGNlAy.YTY0LzYvYmVpejc0ajguYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "db4f101acfa492bd7ab0c026619064a0",
                    "id": "ADYGNlAy",
                    "icon": "https://img.ilisten.idaddy.cn/b/6/6cqvkeqt.jpg"
                },
                {
                    "status": 0,
                    "name": "\u751f\u65e5\u5feb\u4e50\u6b4c",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/ffce/soundAI000000001/201908200000/0/ADYGNlAz.YTY0LzcvcmFhZW52dWYuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/ffce/soundAI000000001/201908200000/0/ADYGNlAz.YTY0LzcvcmFhZW52dWYuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "4f18f198490161f50e673dc65d54afe0",
                    "id": "ADYGNlAz",
                    "icon": "https://img.ilisten.idaddy.cn/b/7/uoknvbgm.jpg"
                },
                {
                    "status": 0,
                    "name": "\u866b\u513f\u98de",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/a731/soundAI000000001/201908200000/0/ADYGNVAz.YTY0LzcvMzBjOWtycmYuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/a731/soundAI000000001/201908200000/0/ADYGNVAz.YTY0LzcvMzBjOWtycmYuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c,\u6606\u866b\u6545\u4e8b",
                    "md5": "16472cd9a3ce05b8e36489cdc284b915",
                    "id": "ADYGNVAz",
                    "icon": "https://img.ilisten.idaddy.cn/b/7/c96iadag.jpg"
                },
                {
                    "status": 0,
                    "name": "\u4e09\u53ea\u5c0f\u732a",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/382f/soundAI000000001/201908200000/0/ADYGNFAx.YS81L3V5d3FtOGQ0LmF1ZGlv.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/382f/soundAI000000001/201908200000/0/ADYGNFAx.YS81L3V5d3FtOGQ0LmF1ZGlv.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "e763822ce4cb4b318351f2e40ee06821",
                    "id": "ADYGNFAx",
                    "icon": "https://img.ilisten.idaddy.cn/b/5/vf9wta3o.jpg"
                },
                {
                    "status": 0,
                    "name": "\u65b0\u5e74\u597d",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/6a0a/soundAI000000001/201908200000/0/AD0GNlAz.YTY0LzcvbzZ5OGYybzkuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/6a0a/soundAI000000001/201908200000/0/AD0GNlAz.YTY0LzcvbzZ5OGYybzkuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u65b0\u5e74\u4e13\u8f91,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "5d004b60b0b2a1766827d6fb7dd68efe",
                    "id": "AD0GNlAz",
                    "icon": "https://img.ilisten.idaddy.cn/b/7/7qxh0rfs.jpg"
                },
                {
                    "status": 0,
                    "name": "\u7aef\u5348\u8282",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/41b0/soundAI000000001/201908200000/0/ADYGNVA3DT0.YTY0LzgvbGV3bm5iNGwuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/41b0/soundAI000000001/201908200000/0/ADYGNVA3DT0.YTY0LzgvbGV3bm5iNGwuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "dcb9c4dc5af3c32ba12aca3374c2b2e0",
                    "id": "ADYGNVA3DT0",
                    "icon": "https://img.ilisten.idaddy.cn/b/8/a7g6x0r5.jpg"
                },
                {
                    "status": 0,
                    "name": "\u54ea\u5c4b\u5143\u5bb5\u6251\u9f3b\u9999",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/24fc/soundAI000000001/201908200000/0/ADEGM1AyDTE.YTY0LzQvNXJsdHU2Z3cuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/24fc/soundAI000000001/201908200000/0/ADEGM1AyDTE.YTY0LzQvNXJsdHU2Z3cuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "c93d019440805dcda4abc2afc84b2929",
                    "id": "ADEGM1AyDTE",
                    "icon": "https://img.ilisten.idaddy.cn/b/4/2bwwzcgz.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5143\u5bb5\u8282\u513f\u6b4c",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/b04f/soundAI000000001/201908200000/0/ADEGM1AyDT0.YTY0LzgvNHg1OG15cTMuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/b04f/soundAI000000001/201908200000/0/ADEGM1AyDT0.YTY0LzgvNHg1OG15cTMuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "2082186f77f4b4f101a541c5d70f98fa",
                    "id": "ADEGM1AyDT0",
                    "icon": "https://img.ilisten.idaddy.cn/b/8/gdqys187.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5c0f\u8df3\u86d9",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/b543/soundAI000000001/201908200000/0/ADEGPlAxDTA.YTY0LzUvMXQ3ZWNjdDQuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/b543/soundAI000000001/201908200000/0/ADEGPlAxDTA.YTY0LzUvMXQ3ZWNjdDQuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c,\u8d77\u5e8a\u97f3\u4e50",
                    "md5": "0485ed944f571afb5a882eccf0ca5564",
                    "id": "ADEGPlAxDTA",
                    "icon": "https://img.ilisten.idaddy.cn/b/5/uwryx96q.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5c0f\u661f\u661f",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/fad8/soundAI000000001/201908200000/0/ADAGNlA8DTQ.YTY0LzEvZHlmZjFpNjUuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/fad8/soundAI000000001/201908200000/0/ADAGNlA8DTQ.YTY0LzEvZHlmZjFpNjUuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "124aa3efbf2a416c100068d7821dea11",
                    "id": "ADAGNlA8DTQ",
                    "icon": "https://img.ilisten.idaddy.cn/b/1/muacavgt.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5fb7\u8bed\u5723\u8bde\u6b4c",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/ae8a/soundAI000000001/201908200000/0/ADAGNFA1DTE.YTY0LzMvaTlyNjVtcmYuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/ae8a/soundAI000000001/201908200000/0/ADAGNFA1DTE.YTY0LzMvaTlyNjVtcmYuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u5723\u8bde\u8282\u4e13\u8f91,\u70ed\u95e8\u513f\u6b4c,\u8d77\u5e8a\u97f3\u4e50",
                    "md5": "ecfd425921f270861afe6b4cb235ae46",
                    "id": "ADAGNFA1DTE",
                    "icon": "https://img.ilisten.idaddy.cn/b/4/ua7gy0um.jpg"
                },
                {
                    "status": 0,
                    "name": "\u6708\u5149\u5149\u7167\u5730\u5802\uff08\u7ca4\u8bed\uff09",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/c33c/soundAI000000001/201908200000/0/ADAGNFA3DTc.YTY0LzYvYnp5N3FtZTYuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/c33c/soundAI000000001/201908200000/0/ADAGNFA3DTc.YTY0LzYvYnp5N3FtZTYuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u70ed\u95e8\u513f\u6b4c",
                    "md5": "0d2947e8393cd136ce3b5d7ef7e8450e",
                    "id": "ADAGNFA3DTc",
                    "icon": "https://img.ilisten.idaddy.cn/b/2/j3ztic9x.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5bfb\u627e\u5c0f\u738b\u5b50",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/dbc0/soundAI000000001/201908200000/0/ADAGM1A9DTE.YTY0LzUvMXdwMXczNTguYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/dbc0/soundAI000000001/201908200000/0/ADAGM1A9DTE.YTY0LzUvMXdwMXczNTguYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u6d41\u884c\u513f\u6b4c,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "660328d4bf64f4e63d094530ace7aa28",
                    "id": "ADAGM1A9DTE",
                    "icon": "https://img.ilisten.idaddy.cn/b/4/psqxqe6a.jpg"
                },
                {
                    "status": 0,
                    "name": "\u5feb\u4e50\u513f\u7ae5",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/567d/soundAI000000001/201908200000/0/ADAGPlAxDTE.YTY0LzQvNnUwNHgydTguYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/567d/soundAI000000001/201908200000/0/ADAGPlAxDTE.YTY0LzQvNnUwNHgydTguYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u6d41\u884c\u513f\u6b4c,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "fdbfbc70f3404b0158aecbe1b1b0a117",
                    "id": "ADAGPlAxDTE",
                    "icon": "https://img.ilisten.idaddy.cn/b/4/nn5e9n96.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u88ab\u5b50\u7684\u5927\u5730",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/4d02/soundAI000000001/201908200000/0/ADMGM1AxDTc.YTY0LzIvc2Nyb3ZxdnQuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/4d02/soundAI000000001/201908200000/0/ADMGM1AxDTc.YTY0LzIvc2Nyb3ZxdnQuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "47c852101b75682f5b75823237cb0464",
                    "id": "ADMGM1AxDTc",
                    "icon": "https://img.ilisten.idaddy.cn/b/2/ahy4gjif.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u6324\u6324",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/0974/soundAI000000001/201908200000/0/ADMGM1AyDT0.YTY0LzgvNWx6NTdqZTQuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/0974/soundAI000000001/201908200000/0/ADMGM1AyDT0.YTY0LzgvNWx6NTdqZTQuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "b28842e8097997e536c6d017986bfbcf",
                    "id": "ADMGM1AyDT0",
                    "icon": "https://img.ilisten.idaddy.cn/b/8/pxwyapx5.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u7011\u5e03",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/4bf5/soundAI000000001/201908200000/0/ADMGMlA2DTM.YTY0LzgvcHk3MHdxNzMuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/4bf5/soundAI000000001/201908200000/0/ADMGMlA2DTM.YTY0LzgvcHk3MHdxNzMuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "7cedbb7881df4872e65f9c33d7840b33",
                    "id": "ADMGMlA2DTM",
                    "icon": "https://img.ilisten.idaddy.cn/b/6/rg06ofp8.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u503e\u542c",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/bdd5/soundAI000000001/201908200000/0/ADMGMlAxDT0.YTY0LzUvM2Rka2t1M3UuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/bdd5/soundAI000000001/201908200000/0/ADMGMlAxDT0.YTY0LzUvM2Rka2t1M3UuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "b9152bb8dc47aec74c136ac9c458284b",
                    "id": "ADMGMlAxDT0",
                    "icon": "https://img.ilisten.idaddy.cn/b/8/ivv1icvd.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u5982\u679c\u6211\u662f\u4e00\u7247\u96ea\u82b1",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/adf0/soundAI000000001/201908200000/0/ADMGMlAyDTA.YTY0LzIvYnMzYW5rMDQuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/adf0/soundAI000000001/201908200000/0/ADMGMlAyDTA.YTY0LzIvYnMzYW5rMDQuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "fcc2a90c9744fcbe2a5725b750a3d9c7",
                    "id": "ADMGMlAyDTA",
                    "icon": "https://img.ilisten.idaddy.cn/b/5/vr34ssrb.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u542c\u6545\u4e8b",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/b308/soundAI000000001/201908200000/0/ADMGMlA9DTM.YTY0LzYva2JuanllaHIuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/b308/soundAI000000001/201908200000/0/ADMGMlA9DTM.YTY0LzYva2JuanllaHIuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "003d6d1bb778babf6a6aeb8bd7e94157",
                    "id": "ADMGMlA9DTM",
                    "icon": "https://img.ilisten.idaddy.cn/b/6/ar9dcxkc.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u6e38\u620f\u7684\u5c0f\u732b",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/eef4/soundAI000000001/201908200000/0/ADMGMVAxDTQ.YTY0LzIvOWRtbTRmZ3AuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/eef4/soundAI000000001/201908200000/0/ADMGMVAxDTQ.YTY0LzIvOWRtbTRmZ3AuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "7a215499c9010cd931ba8368476434d5",
                    "id": "ADMGMVAxDTQ",
                    "icon": "https://img.ilisten.idaddy.cn/b/1/3seamaj7.jpg"
                },
                {
                    "status": 0,
                    "name": "\u53ee\u53ee\u7ae5\u8bd7\uff1a\u6349\u8ff7\u85cf",
                    "play_url": "http://cdn.open.idaddy.cn/apsmp3/f672/soundAI000000001/201908200000/0/ADMGMVAyDTI.YTY0LzIvNTBsamdkMDUuYXVkaW8.mp3",
                    "price": 0,
                    "has_chapter": 0,
                    "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/f672/soundAI000000001/201908200000/0/ADMGMVAyDTI.YTY0LzIvNTBsamdkMDUuYXVkaW8.mp3?token=wUYL-cK3IfPXSjBiI16SFg.Mw14MTAwMA0xOTA4Mjc",
                    "taxonomys": "\u8bd7\u6b4c\u7f8e\u6587,\u53ee\u53ee\u7ae5\u8bd7,\u70ed\u95e8\u513f\u6b4c",
                    "md5": "4a50af954a9460e0d7291912230424ad",
                    "id": "ADMGMVAyDTI",
                    "icon": "https://img.ilisten.idaddy.cn/b/7/ptn6f9wh.jpg"
                }
            ]
        },
        "retcode": 0}
    third_info=third_category['audioinfos']['contents']
    for i in third_info:
        print(i)
        print(i['name'])


def maintwo():
    import os,json
    total_data={}
    cmd_base="""APP_ID=soundAI000000001;APP_SECRET=5WYU1VQasIfYtek1AzHKtZg8ccALWRxp;TIMESTAMP=$(date +%s);SIGN_TYPE=sha1;SIGNATURE=$(echo -n "${APP_ID}${APP_SECRET}${TIMESTAMP}" | openssl dgst -$SIGN_TYPE -hex | cut -d' ' -f2);NONCE=$(openssl rand -base64 12)"""
    cmd_category_first="""curl -v --request POST --data-urlencode "app_id=${APP_ID}" --data-urlencode "device_id=x1000" --data-urlencode "timestamp=${TIMESTAMP}" --data-urlencode "nonce=${NONCE}" --data-urlencode "signature=${SIGNATURE}" --data-urlencode "offset=0" --data-urlencode "depth=1" --data-urlencode "cat_ids=[]" http://open.idaddy.cn/audio/v2/list"""
    cmd_category_second="""curl -v --request POST --data-urlencode "app_id=${APP_ID}" --data-urlencode "device_id=x1000" --data-urlencode "timestamp=${TIMESTAMP}" --data-urlencode "nonce=${NONCE}" --data-urlencode "signature=${SIGNATURE}" --data-urlencode "offset=0" --data-urlencode "depth=1" --data-urlencode "cat_ids=%s" http://open.idaddy.cn/audio/v2/list"""
    cmd_category_third="""curl -v --request POST --data-urlencode "app_id=${APP_ID}" --data-urlencode "device_id=x1000" --data-urlencode "timestamp=${TIMESTAMP}" --data-urlencode "nonce=${NONCE}" --data-urlencode "signature=${SIGNATURE}" --data-urlencode "offset=0" --data-urlencode "depth=1" --data-urlencode "cat_ids=%s" http://open.idaddy.cn/audio/v2/list"""
    # cmd = cmd_base+"&&"+cmd_category
    # a= os.popen(cmd_base+"""&&""""+cmd_category).read()
    a = os.popen(cmd_base+'&&'+cmd_category_first).read()
    print('='*100)
    # print(a)
    # print(json.loads(a))
    a= json.loads(a)
    info=a['audioinfos']['cats']
    index=0
    for i in info:
        name = i['cat_name']
        id = i['cat_id']
        # print(id,'dididididid')
        cur_dict = {}
        cur_dict['name']=name
        cur_dict['id']=id
        cur_dict['son_list']=[]
        total_data[name]=cur_dict
        # print("sfsff{}".format([id]))
        cmd_category_second_cur= cmd_category_second%([id])
        # print(cmd_category_second)
        second_info=os.popen(cmd_base+'&&'+cmd_category_second_cur).read()
        second_info=json.loads(second_info)
        # print(second_info)
        second_info_list = second_info['audioinfos']['cats']
        # print(second_info_list)
        for j in second_info_list:
            # print(j)
            second_cur_dict={}
            j_id=j['cat_id']
            j_name = j['cat_name']
            second_cur_dict['name']=j_name
            second_cur_dict['id']=j_id
            second_cur_dict['son_list']=[]
            cur_dict['son_list'].append(second_cur_dict)
            cmd_category_third_cur=cmd_category_third%([j_id])
            third_info = os.popen(cmd_base + '&&' + cmd_category_third_cur).read()
            third_info=json.loads(third_info)
            # print(third_info)
            third_info_list=third_info['audioinfos']['contents']
            for k in third_info_list:
                print(k)
                name=k['name']
                taxonomys=k['taxonomys']
                third_cur_dict={}
                third_cur_dict['name']=name
                third_cur_dict['taxonomys']=taxonomys
                second_cur_dict['son_list'].append(third_cur_dict)
                index+=1

        # print(name)
        # print(i)
    print(total_data)
    print(index,'index')
    with open("/home/gaozhiwei/Desktop/koudaistorytotal.json",'w') as f:
        f.write(json.dumps(total_data,indent=2,ensure_ascii=False))
    print('='*100)

def mainthere():
    import os,json
    cmd_base="""APP_ID=soundAI000000001;APP_SECRET=5WYU1VQasIfYtek1AzHKtZg8ccALWRxp;TIMESTAMP=$(date +%s);SIGN_TYPE=sha1;SIGNATURE=$(echo -n "${APP_ID}${APP_SECRET}${TIMESTAMP}" | openssl dgst -$SIGN_TYPE -hex | cut -d' ' -f2);NONCE=$(openssl rand -base64 12)"""
    cmd_category_first="""curl -v --request POST --data-urlencode "app_id=${APP_ID}" --data-urlencode "device_id=x1000" --data-urlencode "timestamp=${TIMESTAMP}" --data-urlencode "nonce=${NONCE}" --data-urlencode "signature=${SIGNATURE}"    http://open.idaddy.cn/audio/v2/glossary?format=json"""
    a = os.popen(cmd_base+'&&'+cmd_category_first).read()
    a=json.loads(a)
    print(a)
    info_list= a['audioinfos']['contents']
    final_data=[]

    for i in info_list:
        # print(i)
        cur_dict={}
        cur_dict['name']=i['name']
        cur_dict['tags']=i['tags']
        cur_dict['author']=i['author']
        cur_dict['taxonomys']=i['taxonomys']
        final_data.append(cur_dict)
    with open("/home/gaozhiwei/Desktop/koudai562.json",'w') as f:
        f.write(json.dumps(final_data,ensure_ascii=False,indent=2))
    print(final_data)
    print(len(info_list))


def mainfour():
    import json
    index=0
    with open("/home/gaozhiwei/Desktop/koudaistorytotal.json") as f:
        json_data= f.read()
    data= json.loads(json_data)
    print(data)
    category_one_list= list(data.keys())
    category_two_list = dict()
    title_name = dict()
    # print(category_one_list)
    for i in category_one_list:
        i_data_list= data[i]['son_list']
        # print(i_data_list)
        # print(len(i_data_list))
        category_two_list[i]=list()
        for j in i_data_list:
            # print(j['name'])
            category_two_list[i].append(j['name'])
            # print(j['son_list'])
            title_name[j['name']]=list()
            if len(j['son_list']) != 0:
                for k in j['son_list']:
                    index+=1
                    title_name[j['name']].append(k['name'])
                    # print(k)
    print(category_one_list)
    print(category_two_list)
    print(title_name)
    print(index)

    for i in category_one_list:
        i= chinese_num(i)
        i= quchubidian(i)
        print(i)
    final_dict = dict()
    final_dict['dict']=list()

    # with open("/home/gaozhiwei/Desktop/koudaistorycategoryfirst.json",'w') as f:
    #     f.write(json.dumps(final_dict,ensure_ascii=False,indent=2))
    print(category_two_list)
    print(category_two_list.values())
    list_cate_total=list()
    for i in category_two_list.values():
        list_cate_total.extend(i)
    print(len(list_cate_total))
    set_category=set(list_cate_total)
    print(len(set_category))
    cur_final_list = list()
    for i in set_category:
        print(i)
        i=chinese_num(i)
        i=quchubidian(i)
        cur_final_list.append(i)

    # with open("/home/gaozhiwei/Desktop/koudaistorycategorysecond.json",'w') as f:
    #     f.write(json.dumps(final_dict,ensure_ascii=False,indent=2))
    final_title_name=list()
    print(title_name)
    for i in title_name.values():
        final_title_name.extend(i)
        # print(i)
    final_title_name=list(set(final_title_name))
    vars=list()
    for i in final_title_name:
        i=chinese_num(i)
        i=quchubidian(i)
        vars.append(i)
        print(i)
    cur_final_json_dict = dict()
    cur_final_json_dict['majorType'] = "koudai_title"
    cur_final_json_dict['value'] = vars
    final_dict['dict'].append(cur_final_json_dict)
    with open("/home/gaozhiwei/Desktop/koudaistorytitle.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=2))





def mainfive():
    print({
    "audioinfos": {
        "contents": [
            {
                "performer": "\u53e3\u888b\u6545\u4e8b\u5185\u5bb9\u4e91",
                "lyrics": "",
                "rank": 8.0,
                "play_url_with_token": "http://cdn.open.idaddy.cn/apsmp3/51e3/soundAI000000001/201908210000/0/ADcGM1A8DTA.YTY0LzUvaG9mOHlrYmsuYXVkaW8.mp3?token=DEILs_2Qqdx8UjT7fZjfWw.Mw14MTAwMA0xOTA4Mjg",
                "duration": 114,
                "id": "ADcGM1A8DTA",
                "age_to": 6.0,
                "age_from": 2.0,
                "author": "\u4f5a\u540d",
                "play_url": "http://cdn.open.idaddy.cn/apsmp3/51e3/soundAI000000001/201908210000/0/ADcGM1A8DTA.YTY0LzUvaG9mOHlrYmsuYXVkaW8.mp3",
                "has_chapter": 0,
                "filesize": 919752,
                "taxonomys": "\u5730\u65b9\u7ae5\u8c23,\u7ca4\u8bed\u7ae5\u8c23",
                "editor_comment": "",
                "status": 0,
                "description": "\u5927\u5bb6\u90fd\u975e\u5e38\u719f\u6089\uff0c\u6211\u4eec\u8fc7\u751f\u65e5\u7684\u65f6\u5019\uff0c\u90fd\u4f1a\u5531\u4e00\u9996\u300a\u751f\u65e5\u5feb\u4e50\u300b\uff0c\u5148\u5531\u4e00\u904d\u6c49\u8bed\uff0c\u7136\u540e\u518d\u5531\u82f1\u8bed\u3002\u90a3\u5927\u5bb6\u77e5\u9053\u7ca4\u8bed\u7248\u7684\u751f\u65e5\u6b4c\u53c8\u662f\u600e\u4e48\u5531\u7684\u5417\uff1f\u8d76\u5feb\u542c\u4e00\u542c\u5427\uff01",
                "price": 0,
                "bitrate": 64002,
                "md5": "f840ff9519bfdc2971e7efc5343f21fd",
                "name": "\u751f\u65e5\u5feb\u4e50\uff08\u7ca4\u8bed\uff09",
                "icon": "https://img.ilisten.idaddy.cn/b/5/hof8ykbk.jpg"
            }
        ]
    },
    "retcode": 0
})

def maintest():
    a='1'
    def wrapper():
        def wrapper_one():
            return 'one'
        def wrapper_two():
            return 'two'
        return wrapper_one
    print(wrapper())



def mainmeiziinsert():
    import pymysql,json,os
    conn = pymysql.connect(host="172.16.10.237", user='root', password="rootROOT1$",
                 database='semantic_resource', port=3306,autocommit=False)
    cur= conn.cursor()
    sql = 'insert into dict(majorType, minorType, value) VALUES (%s,%s,%s);'
    base_dir_url='/home/gaozhiwei/Desktop/tmpinsert/'
    dir_name = os.listdir(base_dir_url)
    print(dir_name)
    final_list=list()
    for file_name in dir_name:
        with open(base_dir_url+file_name,'r') as f:
            data= f.read()
            # print(i)
            data = json.loads(data)
            for i in data['dict']:
                cur_marjortype= i.get('majorType')
                cur_minortype = i.get('minorType')
                cur_values=i.get('value')
                for value in cur_values:
                    cur_list=[]
                    if cur_marjortype and value:
                        cur_list.append(cur_marjortype)
                        cur_list.append(cur_minortype)
                        cur_list.append(value)
                        final_list.append(tuple(cur_list))
                        print(cur_list)
    # print(final_list)
    cur.executemany(sql,final_list)
    # cur.execute(sql,final_list[0])
    conn.commit()
    cur.close()
    conn.close()




def mainsix():
    import os,json
    base_address = "/home/gaozhiwei/Desktop/temperate/"
    base_address1= "/home/gaozhiwei/Desktop/"
    file_name_list=os.listdir(base_address)
    for file in file_name_list:
        # print(file)
        final_dict = dict()
        final_dict['dict'] = []
        with open(base_address+file,'r')as f:
            json_data = f.read()
            data = json.loads(json_data)
            cur_dict = data['dict'] [0]
            print(cur_dict)
            cur_final_dict = dict()
            cur_final_dict['majorType']=cur_dict['majorType']
            cur_value=list()
            for value in cur_dict['value']:
                if len(value)<=1:
                    print(value)
                else:
                    cur_value.append(value)
            cur_final_dict['value'] = cur_value
            final_dict['dict'].append(cur_final_dict)
        with open(base_address1+file,'w') as f:
            f.write(json.dumps(final_dict,indent=2,ensure_ascii=False))



def lajigenleistatistic():
    import requests
    with open("/home/gaozhiwei/Desktop/lajifenlei.json") as f:
        json_data = f.read()
    data = json.loads(json_data)
    all_values = list()
    fianl_list = list()
    lajimap={
             "wet_garbage":'湿垃圾',
             "dry_garbage":'干垃圾',
             "harmful_waste":'有害垃圾',
             "recyclable":'可回收垃圾'
             }
    for i in data:
        # print(i.values())
        if list(i.values())[0] in lajimap.keys():

            key = list(i.keys())[0]
            value = list(i.values())[0]
            value= lajimap[value]
            i[key] = value
            fianl_list.append(i)
        else:
            fianl_list.append(i)
    res_list = list()
    url = "http://api.tianapi.com/txapi/lajifenlei/"
    paramter = {'key': "2ee517d1df542bfeea2952e161dcef90",
                "word": ""}
    for i in fianl_list:
        cur_dict = dict()
        key= list(i.keys())[0]
        cur_dict['key']=key
        cur_dict['value']=i[key]
        # res_list.append(cur_dict)
        cur_paramter = paramter
        cur_paramter['word']=key
        print(cur_paramter)
        time.sleep(0.2)
        response = requests.get(url,params=cur_paramter)
        cur_dict['response']=response.text
        res_list.append(cur_dict)
    with open("/home/gaozhiwei/Desktop/allresponse.json",'w') as f:
        f.write(json.dumps(res_list,indent=2,ensure_ascii=False))




def poemfilter():
    import pymysql,re
    conn = pymysql.connect(host="172.16.10.11", user='root', password="root",
                 database='skill_data', port=3306,autocommit=True)
    cur = conn.cursor()
    sql = "select id,title,paragraphs from skill_data.poem_skill"
    sql_update ="update skill_data.poem_skill set title='{}',paragraphs='{}' where id='{}'"
    cur.execute(sql)
    data_list = cur.fetchall()
    for i in data_list:
        id = i[0]
        title = i[1]
        paragraphs = i[2]
        try:
            filter_paragraphs = json.loads(paragraphs)
        except Exception as e:
            filter_paragraphs= paragraphs
        if isinstance(filter_paragraphs,list):
            poem_total = ''.join(filter_paragraphs)
        else:
            poem_total = filter_paragraphs
        # print(poem_total)
        if re.search(' ',title):
            title = re.sub(' ','',title)
            # print(title,id)
        if re.search('（.*）',poem_total):
            print(poem_total,id)
            poem_total = re.sub('（.*）','',poem_total)
        # print(title,poem_total,id)
        print(sql_update.format(title,poem_total,id))
        # cur.execute(sql_update.format(title,poem_total,id))
    cur.close()
    conn.close()



def poemjson():
    import os,json
    base_url = "/home/gaozhiwei/Desktop/poem/"
    Desktop_url = "/home/gaozhiwei/Desktop/"
    file_name_list= os.listdir(base_url)
    for file_name in file_name_list:
        with open(base_url+file_name) as f:
            json_data = f.read()
        dict_data = json.loads(json_data)
        values = dict_data['dict'][0]['value']
        new_values = list()
        for value in values:
            # print(value)
            if re.search(' ',value):
                value = re.sub(' ','',value)
            new_values.append(value)
        dict_data['dict'][0]['value'] = new_values
        with open(Desktop_url+file_name,'w') as f:
            print(dict_data)
            f.write(json.dumps(dict_data,indent=2,ensure_ascii=False))

def re_test():
    type_map= {
        0:"可回收垃圾",
        1:"有害垃圾",
        2:"湿垃圾",
        3:"干垃圾"
    }
    with open("/home/gaozhiwei/Desktop/allresponse.json") as f:
        json_data = f.read()
    data = json.loads(json_data)
    code_250 = list()
    diff_value = list()
    same_value = list()

    print(len(data))

    for i in data:
        value = i['value']
        response = json.loads(i['response'])
        if response['code'] ==250:
            code_250.append(i)
        elif response['code']==200:
            res_value = response['newslist'][0]['type']
            res_value = type_map[res_value]
            if res_value!=value:
                diff_value.append(i)
            else:
                same_value.append(i)
    print(len(code_250))
    print(len(diff_value))
    print(len(same_value))
    print(len(data))
    final_dict = dict()
    final_dict['no_data']=code_250
    final_dict['diff_data']= diff_value
    final_dict['same_data'] = same_value
    with open("/home/gaozhiwei/Desktop/statistics_data.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=1))



def pdtest():
    import  json
    import pandas as pd
    with open("/home/gaozhiwei/Desktop/judge_title_in.txt") as f:
        data_list = f.readlines()
    for i in data_list:
        i = json.loads(i)
        print(i['target_title'])






def yinxiao():
    with open("/home/gaozhiwei/Desktop/zhangzhansucai.json") as f:
        json_data = f.read()
    data = json.loads(json_data)
    print(len(data['dict']))
    one_item = data['dict'][0]
    print(one_item)


def guoneicity():
    with open("/home/gaozhiwei/Desktop/国内城市全称.txt") as f:
        quancheng_list = f.readlines()
    with open("/home/gaozhiwei/Desktop/国内城市简称.txt") as f:
        jiancheng_list = f.readlines()
    num =0

    final_map = dict()
    for index,i in enumerate(quancheng_list):
        cur_quancheng = i.strip()
        cur_jiancheng = jiancheng_list[index].strip()
        spilt_quancheng = cur_quancheng.split("/")
        spilt_jiancheng = cur_jiancheng.split("/")
        # if len(spilt_jiancheng) ==3 and len(spilt_quancheng) ==3:
        # if len(spilt_jiancheng)!= len(spilt_quancheng):
        #     print(spilt_quancheng,'quancheng')
        #     print(spilt_jiancheng,'jiancheng')
        # try:
        if len(spilt_jiancheng)==3 and len(spilt_quancheng)==3:
            one = spilt_jiancheng[0]
            two = spilt_jiancheng[1]
            # if len(spilt_jiancheng) ==3:
            there = spilt_jiancheng[2]
            if one not in final_map.keys():
                final_map[one] = dict()
                final_map[one]['desc'] = spilt_quancheng[0]
                final_map[one][two] = dict()
                final_map[one][two]['desc']=spilt_quancheng[1]
                if two != there:
                    final_map[one][two][there] = spilt_quancheng[2]
            else:
                if two not in final_map[one].keys():
                    final_map[one][two]=dict()
                    final_map[one][two]['desc'] = spilt_quancheng[1]
                    if two != there:
                        final_map[one][two][there] = spilt_quancheng[2]
                else:
                    if there not in final_map[one][two].keys() and two != there:
                        final_map[one][two][there] = spilt_quancheng[2]
        else:
            if len(spilt_jiancheng) ==2 and len(spilt_quancheng)==2:
                one = spilt_jiancheng[0]
                two = spilt_jiancheng[1]
                if one not in final_map.keys():
                    final_map[one]=dict()
                    final_map[one]['desc']=spilt_quancheng[0]
                    final_map[one][two]=dict()
                    final_map[one][two]['desc']=spilt_quancheng[1]
                else:
                    if two not in final_map[one].keys():
                        final_map[one][two]= dict()
                        final_map[one][two]['desc'] = spilt_quancheng[1]
            else:
                num +=1
                if len(spilt_quancheng)!=2:
                    print(spilt_quancheng, 'quancheng')
                    print(spilt_jiancheng,'jiancheng')
    print(final_map)
    print(num)

    with open("/home/gaozhiwei/Desktop/guoneixianjishi.json",'w') as f:
        f.write(json.dumps(final_map,indent=2,ensure_ascii=False))


def migumusic():
    with open("/home/gaozhiwei/Desktop/migusearchtitle.json") as f:
        json_data = f.read()
    data = json.loads(json_data)
    migu_title_list = data['dict']
    final_dict = dict()
    final_dict['dict'] = list()
    cur_dict = dict()
    cur_dict['majorType'] = 'song'
    cur_dict['value'] = list()
    for i in migu_title_list:
        title = i['search_title']
        if title is not None:
            title = re.sub('\(.*\)','',title)
            res = chinese_num(title)
            res = quchubidian(res)
            if len(res)>1:
                cur_dict['value'].append(res)

            print(res)
        else:
            print(i)
    cur_dict['value']= list(set(cur_dict['value']))
    final_dict['dict'].append(cur_dict)
    with open("/home/gaozhiwei/Desktop/xinzengmusictitle1.json",'w') as f:
        f.write(json.dumps(final_dict,ensure_ascii=False,indent=2))

def tangshidanzi():
    import os,json
    base_dir = "/home/gaozhiwei/Desktop/tangshi/"
    base_dir = "/home/gaozhiwei/Desktop/songci/"
    new_dir = "/home/gaozhiwei/Desktop/tangshinew/"
    new_dir = "/home/gaozhiwei/Desktop/songcinew/"
    file_name_list = os.listdir(base_dir)
    print(file_name_list)
    cur_danzi = dict()
    cur_danzi['dict'] = list()
    cur_danzi_in = dict()
    cur_danzi_in['majorType']="poemTitle_danzi"
    cur_danzi_in['value'] = list()
    for file_name in file_name_list:
        with open(base_dir+file_name) as f:
            json_data = f.read()
        cur_common = dict()
        cur_common['dict'] = list()
        cur_common_in = dict()
        dict_data = json.loads(json_data)
        # print(len(dict_data['dict']))
        for title_dict in dict_data['dict']:
            # print(title_dict['majorType'])
            # if title_dict['majorType'] == "poemTitle" or title_dict['majorType'] == "poemName" or title_dict['majorType']=="poem_without_confusion":
            if title_dict['majorType'] == "songci_title":
                cur_common_in['majorType']=title_dict['majorType']
                cur_common_in['value']=list()
                cur_value = title_dict['value']
                for value  in cur_value:
                    # print(value)
                    if len(value) ==1:
                        cur_danzi_in['value'].append(value)
                        print(file_name)
                        print(value)
                    else:
                        cur_common_in['value'].append(value)
            else:
                cur_common['dict'].append(title_dict)
        cur_common['dict'].append(cur_common_in)
        with open(new_dir+file_name,'w') as f:
            f.write(json.dumps(cur_common,indent=1,ensure_ascii=False))
    cur_danzi['dict'].append(cur_danzi_in)
    with open(new_dir + 'danzi.json', 'w') as f:
        f.write(json.dumps(cur_danzi, indent=1, ensure_ascii=False))
















if __name__ == '__main__':
    # main()
    # mainone()
    # maintwo()
    # mainthere()
    # mainfour()
    # mainfive()
    # maintest()
    # mainmeiziinsert()
    # mainsix()
    # lajigenleistatistic()
    # poemfilter()
    # poemjson()
    # re_test()
    # pdtest()
    # yinxiao()
    # guoneicity()
    # migumusic()
    tangshidanzi()
