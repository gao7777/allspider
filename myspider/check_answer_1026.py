#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/30 下午4:18
# @Author  : Luohy
# @Site    :
# @File    : monitor.py
# @Software: Notepad++

#-*-coding:utf-8 -*-
import time
import sys
import json
import requests
import random
import logging

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='/tmp/zabbix.log',filemode='a')
logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)
reload(sys)
sys.setdefaultencoding('utf8')
get_time=time.strftime('%Y.%m.%d-%H:%M:%S',time.localtime(time.time()))
hostName="bcloud.zabbix-server"
babel_url = " http://47.94.206.115:9100/hugo/semantic/v2"

def writeErrLog(lineTx):
    errLog = open("/tmp/chatErr.log","a")
    errLog.write(lineTx + "\n")
    errLog.close
    pass

def sendMail(mTitle,mContent):
    receiver = ["wangle@soundai.com","gaozhiwei@soundai.com",]
    #receiver = "ops@soundai.com,caijinsong@soundai.com,chenyong@soundai.com,siwenlei@soundai.com"
    # receiver = "luohaiyuan@soundai.com"
    encoding = "utf-8"
    message = MIMEText("巡检主机：\n" + hostName + "\n\n" + mContent, 'plain', 'utf-8')
    message['Subject'] = Header(mTitle, encoding)
    message['From'] = "alert@soundai.com"
    message['To'] = ", ".join(receiver)
    #message['To'] = receiver
    message['Date'] = formatdate()
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        smtpObj.ehlo()
        smtpObj.login('alert@soundai.com', 'SoundA1online')
        smtpObj.sendmail('alert@soundai.com', receiver, message.as_string())
        #print "send mail success"
    except Exception:
        print "send mail error"

def sendDing(dContent):
    dUrl = "https://oapi.dingtalk.com/robot/send?access_token=e85f26ab2f08c07efdcaf6b01fe2016eee881ad8ab7be12a497915577b2ea118"
    dHeaders = {'Content-Type': 'application/json;charset=utf-8'}
    text_info= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
              "18311056169",
            ],
            "isAtAll": False
            #"isAtAll": True
        },
        "text": {
            "content": dContent
        }
    }
    print requests.post(dUrl,json.dumps(text_info),headers=dHeaders).content


class check_answer(object):
    def __init__(self,query,skill_name):
        self.userid = str(random.randint(10000,3456876))
        self.query = query
        self.skill_name = skill_name

    def write_log(self,result,params):
        logging.info(params)
        logging.info(result + '\n\n')

    def get_answer(self):
        dialogId = str(random.randint(10000,3456876))
        #url = "https://hugo.soundai.cn/bot/semantic/v2"
        url = 'https://hugo.soundai.cn/hugo/semantic/v2'
        url= babel_url
        values = {"merchantId": "7501012293520623844","clientId": "monitor."+hostName,"deviceId":"monitor."+hostName,"dialogId": dialogId, "ip": "222.67.93.182", "query": "今天天气"}
        headers = {"Content-Type":"application/json"}
        values['query'] = self.query
        values['clientId'] = "monitor." + self.userid
        data = json.dumps(values)
        response = requests.post(url,data=data,headers=headers,timeout=5)
        self.write_log(response.text,data)
        #print(json.loads(response.text)['domain'])
        return response.text

    def get_multi_answer(self,statuscode=None):
        dialogId = str(random.randint(10000,3456876))
        params = {"merchantId":"7501012293520623844", "query": "呼叫幺五九零幺零三幺二三四","dialogId": dialogId, "clientId":"monitor."+hostName, "deviceId":"monitor."+hostName, "rate":1.0}
        headers = {"Content-Type":"application/json"}
        params['query'] = self.query
        params['clientId'] = "monitor" + self.userid
        url = 'https://hugo.soundai.cn/hugo/semantic/v2'
        url = babel_url
        #url = 'https://hugo.soundai.cn/bot/semantic/v2'
        r = requests.post(url, data=json.dumps(params), headers=headers,timeout=5)
        result = r.text
        item = json.loads(result)
        self.write_log(r.text,json.dumps(params))
        data = json.loads(item['data'])
        skill = self.skill_name.split('_')[0]

        try:
            if item['domain'] == 'phone':
                if '打电话' in  data['answer']:
                    statuscode = 1
                if 'operation' in data['parameters']:
                    if data['parameters']['operation'] == 'ACCEPT':
                        statuscode = 1
            if item['domain'] == 'home':
                if 'number' in data['parameters'] :
                    if data['parameters']['number'] == '200' or data['parameters']['number'] == 'max':
                        statuscode = 1
                if data['parameters']['operation'] == 'TURN_ON':
                        statuscode = 1
            if item['domain'] == 'chat':
                #sendMail("[SVK Answer巡检告警] Domain由%s偏移为chat" % skill,"时间：\n %s \n\n输入：\n %s \n\n输出：\n %s \n" % (get_time,json.dumps(params),result))
                #sendDing("===测试===\n[SVK Answer巡检告警] Domain偏移为chat\n\n时间：\n %s \n\n输入：\n %s \n\n输出：\n %s \n===测试===" % (get_time,json.dumps(params),result))
                writeErrLog("%s###%s###%s###%s" % (skill,get_time,json.dumps(params),result))
                statuscode = 1
        except:
            sendMail("【SVK Answer巡检告警】%s Answer异常！" % skill,"multi_answer\n时间：\n %s \n\n输入：\n %s \n\n输出：\n %s \n" % (get_time,json.dumps(params),result))
            statuscode = 0


        return statuscode

    def session_answer(self,list_query,statuscode=None):
        dialogId = "9999999"
        list_query = list_query
        params = {"dialogId": dialogId,"merchantId": "154", "query": "呼叫幺五九零幺零三幺二三四", "clientId": "monitor."+hostName,
                  "deviceId": "monitor."+hostName + self.userid, "rate": 1.0}
        headers = {"Content-Type": "application/json"}
        url = 'https://hugo.soundai.cn/hugo/semantic/v2'
        url = babel_url
        #url = 'https://hugo.soundai.cn/bot/semantic/v2'
        params['clientId'] = "monitor" + self.userid
        result = "空"
        skill = self.skill_name.split('_')[0]
        try:
            for  i in  list_query:
                #if i == '退出' :
                #    url = 'https://hugo.soundai.cn/hugo/semantic/v2'
                params['dialogId'] = str(random.randint(10000,3456876))
                params['query'] = i
                r = requests.post(url, data=json.dumps(params), headers=headers,timeout=5)
                result = r.text
                time.sleep(0.3)
                item = json.loads(result)
                print result
                self.write_log(r.text, json.dumps(params))
                if item['domain'] == 'dictionary' or item['domain'] == 'translation' or  item['domain'] == 'music' or item['domain'] == 'mxmusic' or item['domain'] == 'audio' :
                    #sendMail("【SVK Answer巡检调试】%s Answer正常！" % skill,"session_answer\n时间：\n %s \n\n请求：\n %s \n\n响应：\n %s \n" % (get_time,json.dumps(params),result))
                    statuscode = 1
                else:
                    sendMail("【SVK Answer巡检告警】%s 的Domain偏移！" % skill,"session_answer\n时间：\n %s \n\n请求：\n %s \n\n响应：\n %s \n" % (get_time,json.dumps(params),result))
                    #domain偏移异常降级告警，向zbx返回正常
                    statuscode = 1
                    break
        except Exception as e:
            print("报错e%s"%e)
            sendMail("【SVK Answer巡检告警】%s Answer异常！" % skill,"session_answer\n时间：\n %s \n\n请求：\n %s \n\n响应：\n %s \n 报错%s \n" % (get_time,json.dumps(params),result,e))
            statuscode = 0
        return  statuscode


def weather_answer(statuscode=None):
    try:
        result = check_answer('今天天气','weather_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'weather':
            if '摄氏度' in data['answer'] or '温度' in  data['answer'] :
                statuscode = 1
        if item['domain'] == 'chat':
            #sendMail("[SVK Answer巡检告警] Domain偏移为chat","巡检时间：\n %s \n\n测试项：\n“今天天气”\n\n响应值：\n %s \n" % (get_time,result.get_answer()))
            writeErrLog("weather###%s###测试“今天天气”###%s" % (get_time,item))
            statuscode = 1
    except:
        statuscode = 0

    return statuscode

def baike_answer(statuscode=None):
    try :
        result = check_answer('爸爸的爸爸叫什么', 'baike_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'baike':
            if '爷爷' in data['answer'] :
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("baike###%s###测试“爸爸的爸爸叫什么”###%s" % (get_time,item))
            statuscode = 1
    except:
            statuscode = 0

    return statuscode

def time_answer(statuscode=None):
      try :
        result = check_answer("现在几点了", 'time_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'time':
            if '北京时间' in  data['answer']  or '星期' in data['answer']:
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("time###%s###测试“现在几点了”###%s" % (get_time,item))
            statuscode = 1
      except:
            statuscode = 0

      return statuscode

def audio_answer(statuscode=None):
    try:
        result = check_answer("播放赵本山的小品", 'audio_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'audio':
            if '播放' in  data['answer']:
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("audio###%s###测试“播放赵本山的小品”###%s" % (get_time,item))
            statuscode = 1
    except:
            statuscode = 0

    return statuscode

def playcontrol_answer(statuscode=None):
    try:
        result = check_answer("停止播放", 'playcontrol_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'playcontrol':
            if '停止播放' in  data['answer']:
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("playcontrol###%s###测试“停止播放”###%s" % (get_time,item))
            statuscode = 1
    except:
            statuscode = 0

    return statuscode

def volume_answer(statuscode=None):
    try:
        result = check_answer("小点声", 'volume_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'volume':
            if '音量' in  data['answer']:
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("volume###%s###测试“小点声”###%s" % (get_time,item))
            statuscode = 1
    except:
            statuscode = 0

    return statuscode

def phone_answer(statuscode=None):
        r1 = check_answer("呼叫幺五九零幺零三幺二三四",'phone_answer')
        result1 = r1.get_multi_answer()
        r2 = check_answer("接通来电",'phone_answer')
        result2= r2.get_multi_answer()
        if result1 == 1 and result2 == 1 :
          statuscode = 1
        else :
          statuscode = 0

        return statuscode

def home_answer(statuscode=None):
        r1 = check_answer("卧室机顶盒音量增加200", 'home_answer')
        result1 = r1.get_multi_answer()
        r2 = check_answer("打开开关", 'home_answer')
        result2 = r2.get_multi_answer()
        if result1 == 1 and result2 == 1 :
             statuscode = 1
        else:
             statuscode = 0

        return statuscode

def home2_answer(statuscode=None):
        r3 = check_answer("打开空调", 'home_answer')
        result3 = r3.get_multi_answer()
        r4 = check_answer("空调风速调到最大", 'home_answer')
        result4 = r4.get_multi_answer()
        r5 = check_answer("打开灯", 'home_answer')
        result5 = r5.get_multi_answer()
        if (result3 == 1 and result4 == 1 and result5 == 1) :
             statuscode = 1
        else:
             statuscode = 0

        return statuscode

def alarm_answer(statuscode=None):
    try:
        result = check_answer("设置明早7点的闹钟", 'alarm_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'alarm':
            if  data['parameters']['operation'] == 'SET':
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("alarm###%s###测试“设置明早7点的闹钟”###%s" % (get_time,item))
            statuscode = 1
    except:
            statuscode = 0

    return statuscode

def schedule_answer(statuscode=None):
    try:
        result = check_answer("明天早上8点半提醒我吃饭", 'schedule_answer')
        item = json.loads(result.get_answer())
        data = json.loads(item['data'])
        if item['domain'] == 'schedule':
            if  data['parameters']['operation'] == 'SET' :
                statuscode = 1
        if item['domain'] == 'chat':
            writeErrLog("schedule###%s###测试“明天早上8点半提醒我吃饭”###%s" % (get_time,item))
            statuscode = 1
    except:
            statuscode = 0

    return statuscode

def domain_answer(query,statuscode=None):
    try:
        if query == "forex":
            params = '美元对人民币的汇率是多少'
        if query == "poem":
            params = '播放李白的秋风词'
        if query == 'cookbook':
            params = '豆腐怎么做'
        if query == 'astrology':
            params0 = ['我是摩羯座','我是狮子座','我是处女座','我是射手座','我是白羊座','我是天秤座','','我是双子座','我是金牛座','我是双鱼座','我是巨蟹座']
            params = random.choice(params0)
            print(params)
        if query == 'limitLine':
            params = '今天限行吗'
        if query == 'huangli':
            params = '今天的黄历'
        if query == 'stock':
            params = '查询中国移动的股价'

        if query == 'shengyin':
            params = '老虎怎么叫'

        if query == 'workout':
            params = ['五分钟健身', '平板运动','今天天气', '退出']

        if query == 'mxmusic':
            params = ['打开冥想音乐','流水声']

        if query == 'dictionary':
            params = ['打开汉语词典','不期而遇是什么意思','退出']

        if query == 'translation':
            params = ['打开中译英', '今天天气', '退出']

        if query == 'music':
            params = ['播放音乐','随便来首歌','播放周杰伦的稻香']

        if isinstance(params,list):
            result = check_answer(['Iitializing','Initialized'], query+'_answer')
            statuscode = result.session_answer(params)

        else :
            result = check_answer(params, query+'_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] in ['forex','astrology', 'cookbook', 'poem', 'limitLine','huangli','stock','audio']:
                statuscode = 1
    except:

        statuscode = 0

    return  statuscode

if __name__  == "__main__":
    try:
        result=sys.argv[1]
        logging.info('\n#############' + get_time + ' '  + result  +  '################\n')
        if result == 'weather_answer':
           statuscode = weather_answer()

        if result == 'baike_answer' :
            statuscode = baike_answer()

        if result == 'time_answer' :
            statuscode = time_answer()

        if result == 'music_answer' :
            statuscode = domain_answer('music')

        if result == 'audio_answer' :
            statuscode =  audio_answer()

        if result == 'playcontrol_answer' :
            statuscode = playcontrol_answer()

        if result == 'volume_answer' :
            statuscode= volume_answer()

        if result == 'phone_answer' :
            statuscode = phone_answer()

        if result == 'home_answer' :
            statuscode = home_answer()

        if result == 'home2_answer' :
            statuscode = home2_answer()

        if result == 'alarm_answer' :
            statuscode = alarm_answer()

        if result == 'schedule_answer' :
            statuscode = schedule_answer()

        if result == 'forex_answer' :
             statuscode = domain_answer('forex')

        if result == 'astrology_answer' :
            statuscode = domain_answer('astrology')

        if result == 'poem_answer':
            statuscode = domain_answer('poem')

        if result == 'cookbook_answer':
            statuscode = domain_answer('cookbook')

        if result == 'limitLine_answer':
            statuscode = domain_answer('limitLine')

        # if result == 'dictionary_answer':
        #     statuscode = domain_answer('dictionary')

        if result == 'translation_answer':
            statuscode = domain_answer('translation')

        if result == 'huangli_answer':
            statuscode = domain_answer('huangli')

        if result == 'shengyin_answer':
            statuscode = domain_answer('shengyin')

        # if result == 'workout_answer':
        #     statuscode = domain_answer('workout')

        if result == 'mxmusic_answer':
            statuscode = domain_answer('mxmusic')

        if result == 'stock_answer':
            statuscode = domain_answer('stock')

    except:
        statuscode = 0

    print(statuscode)



