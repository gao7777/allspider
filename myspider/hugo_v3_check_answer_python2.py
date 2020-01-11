#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-*-coding:utf-8 -*-
import json
import logging, time, sys, os
import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formatdate
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait

import requests

# reload(sys)
# sys.setdefaultencoding('utf8')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(name)s- %(levelname)s - %(funcName)s - %(message)s',
                    filename='/tmp/zabbix.log', filemode='a')
logger = logging.getLogger(__name__)
get_time = time.strftime('%Y.%m.%d-%H:%M:%S', time.localtime(time.time()))
hostName = "bcloud.zabbix-server"
babel_url = " http://47.94.206.115:9100/hugo/semantic/v3?app_id=154"


def sendemail(mTitle, mContent):
    receiver = ["wangle@soundai.com", "gaozhiwei@soundai.com", "ops@soundai.com", "zhengshurui@soundai.com",
                "zhangyalei@soundai.com"]
    receiver = [ "gaozhiwei@soundai.com"]
    message = MIMEText("巡检主机：\n" + hostName + "\n\n" + mContent, 'plain', 'utf-8')
    message['Subject'] = Header(mTitle, "utf-8")
    message['From'] = "alert@soundai.com"
    message['To'] = ", ".join(receiver)
    # message['To'] = receiver
    message['Date'] = formatdate()
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        smtpObj.ehlo()
        smtpObj.login('alert@soundai.com', 'SoundA1online')
        smtpObj.sendmail('alert@soundai.com', receiver, message.as_string())
        return 1
    except Exception as e:
        return 0
        logger.error('邮件发送出错 %s') % e


# def sendding(dcontent):
#     dUrl = "https://oapi.dingtalk.com/robot/send?access_token=e85f26ab2f08c07efdcaf6b01fe2016eee881ad8ab7be12a497915577b2ea118"
#     dHeaders = {'Content-Type': 'application/json;charset=utf-8'}
#     text_info = {
#         "msgtype": "text",
#         "at": {
#             "atMobiles": [
#                 "18311056169",
#             ],
#             "isAtAll": False
#             # "isAtAll": True
#         },
#         "text": {
#             "content": dcontent
#         }
#     }
#     response = requests.post(dUrl, json.dumps(text_info), headers=dHeaders)
#     print(response.content)


def hugorequest(query, skill_name, url=babel_url):
    dialogId = str(random.randint(10000, 3456876))
    parameter_dict = {"clientId": "88888122",
                      "deviceId": "monitor." + hostName,
                      "dialogId": '88888122', "query": query,
                      "merchandId":'154'}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=parameter_dict, headers=headers, timeout=5)
        print(response.content.decode('utf-8'))

        return response
    except Exception as e:
        logger.error("request error %s query %s skill_name %s" % (e, query, skill_name))
        sendemail("【SVK Answer巡检告警】%s Request访问异常！" % skill_name,
                  "answer\n时间：\n %s \n\n请求：\n %s \n\n 报错%s \n" % (
                      get_time, json.dumps(parameter_dict, ensure_ascii=False), e))
        return 0


def answerconfirm(query, skill_name, correct_domian, keywords):
    statuscode = 0
    if isinstance(query, list):
        cur_code = 1
        for query_str in query:
            code = answerconfirm(query_str, skill_name, correct_domian, keywords)
            cur_code = cur_code and code
            # time.sleep(0.3)
        return cur_code
    else:
        response = hugorequest(query, skill_name)
        if response == 0:
            return 0
        logger.info('request_query %s response content %s'%(query,response.content))
        # print(response.content)
        answer_dict = json.loads(response.content)
        # data = json.loads(answer_dict['data'])
        data = answer_dict['data']
        if answer_dict['domain'] == correct_domian:
            if keywords == 'default':
                statuscode = 1
            elif isinstance(keywords, list):
                for cur_key in keywords:
                    if cur_key in data['answer']:
                        statuscode = 1
                        return statuscode
            elif isinstance(keywords, dict):
                if 'answer' in keywords.keys() and 'answer' in data.keys():
                    cur_keys = keywords['answer']
                    if isinstance(cur_keys, list):
                        for i_key in cur_keys:
                            if i_key in data['answer']:
                                statuscode = 1
                    elif isinstance(cur_keys, str):
                        if cur_keys in data['answer']:
                            statuscode = 1
                if 'parameters' in keywords.keys() and 'parameters' in data.keys():
                    cur_param = keywords['parameters']
                    for key, value in cur_param.items():
                        if key in data['parameters'].keys():
                            if isinstance(value, list):
                                for one_value in value:
                                    if data['parameters'][key] == one_value:
                                        statuscode = 1
                            elif isinstance(value, str):
                                if data['parameters'][key] == value:
                                    statuscode = 1

        elif answer_dict['domain'] == 'chat':
            statuscode = 1
            dialogId = str(random.randint(10000, 3456876))
            logger.error("###%s###测试%s###%s" % (get_time, query, json.dumps(answer_dict, ensure_ascii=False)))
            parameter_dict = {"merchantId": "7501012293520623844", "clientId": "monitor." + hostName,
                              "deviceId": "monitor." + hostName,
                              "dialogId": dialogId, "ip": "222.67.93.182", "query": query}
            sendemail("【SVK Answer巡检告警】%s 的Domain偏移！" % skill_name,
                      "本地session_answer\n时间：\n %s \n\n请求：\n %s \n\n响应：\n %s \n" % (
                          get_time, json.dumps(parameter_dict, ensure_ascii=False), json.dumps(response.content.decode('utf-8'),ensure_ascii=False)))
    return statuscode


def main(parameter):

    test_method_list = {
        'weather_answer': ['今天天气', 'weather_answer', 'weather', ['摄氏度', '温度']],
        'baike_answer': ['爸爸的爸爸叫什么', 'baike_answer', 'baike', ['爷爷']],
        'time_answer': ['现在几点了', 'time_answer', 'time', ['时间', '星期']],
        'music_answer': [['播放音乐', '随便来首歌', '播放周杰伦的稻香'], 'music_answer', 'music', 'default'],
        'audio_answer': ['播放赵本山的小品', 'audio_answer', 'audio', ['播放']],
        'playcontrol_answer': ['停止播放', 'playcontrol_answer', 'playcontrol', ['停止播放']],
        'volume_answer': ['小点声', 'volume_answer', 'volume', ['音量']],
        'phone_answer': [['呼叫幺五九零幺零三幺二三四', '接通来电'], 'phone_answer', 'phone',
                         {'answer': '打电话', 'parameters': {'operation': 'ACCEPT'}}],
        'home_answer': [['卧室机顶盒音量增加200', '打开开关'], 'home_answer', 'smarthome',
                        {'parameters': {'operation': 'TURN_ON', 'number': ['200', 'max']}}],
        'home2_answer': [['打开空调', '空调风速调到最大', '打开灯'], 'home2_answer', 'smarthome',
                         {'parameters': {'operation': ['ACCEPT', 'TURN_ON'], 'number': ['200', 'max']}}],
        'alarm_answer': ['设置明早7点的闹钟', 'alarm_answer', 'alarm', {'parameters': {'operation': 'SET'}}],
        'schedule_answer': ['明天早上8点半提醒我吃饭', 'schedule_answer', 'schedule', {'parameters': {'operation': 'SET'}}],
        'forex_answer': ['美元对人民币的汇率是多少', 'forex_answer', 'forex', 'default'],
        'astrology_answer': [['我是摩羯座', '我是狮子座', '我是射手座', '我是白羊座', '我是天秤座', '我是双子座', '我是金牛座', '我是双鱼座', '我是巨蟹座'],
                             'astrology_answer', 'astrology', 'default'],
        'poem_answer': ['播放李白的秋风词', 'poem_answer', 'poem', 'default'],
        'cookbook_answer': ['豆腐怎么做', 'cookbook_answer', 'cookbook', 'default'],
        'limitLine_answer': ['今天限行吗', 'limitLine_answer', 'limitLine', 'default'],
        # 'translation_answer': [['打开中译英', '今天天气', '退出'], 'translation_answer', 'translation', 'default'],
        'huangli_answer': ['今天的黄历', 'huangli_answer', 'huangli', 'default'],
        'shengyin_answer': ['老虎怎么叫', 'shengyin_answer', 'audio', ['老虎']],
        # 'mxmusic_answer': [['打开冥想音乐','流水声'], 'mxmusic_answer', 'mxmusic', 'default'],
        'stock_answer': ['查询中国移动的股价', 'stock_answer', 'stock', 'default']
    }

    if parameter in test_method_list.keys():
        final_statuscode = answerconfirm(*test_method_list[parameter])
        return final_statuscode
    else:
        print('%s is not in methods') % parameter
    # for i in test_method_list:
    #     final_statuscode=answerconfirm(*test_method_list[i])
    #     print(final_statuscode)


if __name__ == '__main__':
    test_method_list = {
        'weather_answer': ['今天天气', 'weather_answer', 'weather', ['摄氏度', '温度']],
        'baike_answer': ['爸爸的爸爸叫什么', 'baike_answer', 'baike', ['爷爷']],
        'time_answer': ['现在几点了', 'time_answer', 'time', ['时间', '星期']],
        'music_answer': [['播放音乐', '随便来首歌', '播放周杰伦的稻香'], 'music_answer', 'music', 'default'],
        'audio_answer': ['播放赵本山的小品', 'audio_answer', 'audio', ['播放']],
        'playcontrol_answer': ['停止播放', 'playcontrol_answer', 'playcontrol', ['停止播放']],
        'volume_answer': ['小点声', 'volume_answer', 'volume', ['音量']],
        'phone_answer': [['呼叫幺五九零幺零三幺二三四', '接通来电'], 'phone_answer', 'phone',
                         {'answer': '打电话', 'parameters': {'operation': 'ACCEPT'}}],
        'home_answer': [['卧室机顶盒音量增加200', '打开开关'], 'home_answer', 'smarthome',
                        {'parameters': {'operation': 'TURN_ON', 'number': ['200', 'max']}}],
        'home2_answer': [['打开空调', '空调风速调到最大', '打开灯'], 'home2_answer', 'smarthome',
                         {'parameters': {'operation': ['ACCEPT', 'TURN_ON'], 'number': ['200', 'max']}}],
        'alarm_answer': ['设置明早7点的闹钟', 'alarm_answer', 'alarm', {'parameters': {'operation': 'SET'}}],
        'schedule_answer': ['明天早上8点半提醒我吃饭', 'schedule_answer', 'schedule', {'parameters': {'operation': 'SET'}}],
        'forex_answer': ['美元对人民币的汇率是多少', 'forex_answer', 'forex', 'default'],
        'astrology_answer': [['我是摩羯座', '我是狮子座', '我是射手座', '我是白羊座', '我是天秤座', '我是双子座', '我是金牛座', '我是双鱼座', '我是巨蟹座'],
                             'astrology_answer', 'astrology', 'default'],
        'poem_answer': ['播放李白的秋风词', 'poem_answer', 'poem', 'default'],
        'cookbook_answer': ['豆腐怎么做', 'weather_answer', 'cookbook', 'default'],
        'limitLine_answer': ['今天限行吗', 'limitLine_answer', 'limitLine', 'default'],
        # 'translation_answer': [['打开中译英', '今天天气', '退出'], 'translation_answer', 'translation', 'default'],
        'huangli_answer': ['今天的黄历', 'huangli_answer', 'huangli', 'default'],
        'shengyin_answer': ['老虎怎么叫', 'shengyin_answer', 'audio', ['老虎']],
        # 'mxmusic_answer': [['打开冥想音乐','流水声'], 'mxmusic_answer', 'mxmusic', 'default'],
        'stock_answer': ['查询中国移动的股价', 'stock_answer', 'stock', 'default']
    }
    # aaa= random.choices('home2_answer','home_answer')
    executer =  ThreadPoolExecutor(max_workers=100)
    all_task = [executer.submit(main(random.choice(list(test_method_list.keys())))) for i in range(500)]
    wait(all_task, return_when=ALL_COMPLETED)
    print('compelet')

    # if len(sys.argv) >= 2:
    #     parameter = sys.argv[1]
    #     if parameter is None:
    #         print('please input parameter_answer')
    #     else:
    #         final_code = main(parameter)
    #         if final_code is not None:
    #             print(final_code)


