

class AllMethod():

    def weather_answer():
        try:
            print("method start")
            result = check_answer('今天天气', 'weather_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'weather':
                if '摄氏度' in data['answer'] or '温度' in data['answer']:
                    statuscode = 1
            if item['domain'] == 'chat':
                # sendMail("[SVK Answer巡检告警] Domain偏移为chat","巡检时间：\n %s \n\n测试项：\n“今天天气”\n\n响应值：\n %s \n" % (get_time,result.get_answer()))
                writeErrLog("weather###%s###测试“今天天气”###%s" % (get_time, item))
                statuscode = 1
            print("result", result.get_answer())
        except Exception as e:
            print("error", e)
            statuscode = 0

        return statuscode

    def baike_answer():
        try:
            result = check_answer('爸爸的爸爸叫什么', 'baike_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'baike':
                if '爷爷' in data['answer']:
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("baike###%s###测试“爸爸的爸爸叫什么”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def time_answer():
        try:
            result = check_answer("现在几点了", 'time_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'time':
                if '北京时间' in data['answer'] or '星期' in data['answer']:
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("time###%s###测试“现在几点了”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def audio_answer():
        try:
            result = check_answer("播放赵本山的小品", 'audio_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'audio':
                if '播放' in data['answer']:
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("audio###%s###测试“播放赵本山的小品”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def playcontrol_answer():
        try:
            result = check_answer("停止播放", 'playcontrol_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'playcontrol':
                if '停止播放' in data['answer']:
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("playcontrol###%s###测试“停止播放”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def volume_answer():
        try:
            result = check_answer("小点声", 'volume_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'volume':
                if '音量' in data['answer']:
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("volume###%s###测试“小点声”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def phone_answer():
        r1 = check_answer("呼叫幺五九零幺零三幺二三四", 'phone_answer')
        result1 = r1.get_multi_answer()
        r2 = check_answer("接通来电", 'phone_answer')
        result2 = r2.get_multi_answer()
        if result1 == 1 and result2 == 1:
            statuscode = 1
        else:
            statuscode = 0

        return statuscode

    def home_answer():
        r1 = check_answer("卧室机顶盒音量增加200", 'home_answer')
        result1 = r1.get_multi_answer()
        r2 = check_answer("打开开关", 'home_answer')
        result2 = r2.get_multi_answer()
        if result1 == 1 and result2 == 1:
            statuscode = 1
        else:
            statuscode = 0

        return statuscode

    def home2_answer():
        r3 = check_answer("打开空调", 'home_answer')
        result3 = r3.get_multi_answer()
        r4 = check_answer("空调风速调到最大", 'home_answer')
        result4 = r4.get_multi_answer()
        r5 = check_answer("打开灯", 'home_answer')
        result5 = r5.get_multi_answer()
        if (result3 == 1 and result4 == 1 and result5 == 1):
            statuscode = 1
        else:
            statuscode = 0

        return statuscode

    def alarm_answer():
        try:
            result = check_answer("设置明早7点的闹钟", 'alarm_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'alarm':
                if data['parameters']['operation'] == 'SET':
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("alarm###%s###测试“设置明早7点的闹钟”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def schedule_answer():
        try:
            result = check_answer("明天早上8点半提醒我吃饭", 'schedule_answer')
            item = json.loads(result.get_answer())
            data = json.loads(item['data'])
            if item['domain'] == 'schedule':
                if data['parameters']['operation'] == 'SET':
                    statuscode = 1
            if item['domain'] == 'chat':
                writeErrLog("schedule###%s###测试“明天早上8点半提醒我吃饭”###%s" % (get_time, item))
                statuscode = 1
        except:
            statuscode = 0

        return statuscode

    def domain_answer(query):
        try:
            if query == "forex":
                params = '美元对人民币的汇率是多少'
            if query == "poem":
                params = '播放李白的秋风词'
            if query == 'cookbook':
                params = '豆腐怎么做'
            if query == 'astrology':
                params0 = ['我是摩羯座', '我是狮子座', '我是处女座', '我是射手座', '我是白羊座', '我是天秤座', '', '我是双子座', '我是金牛座', '我是双鱼座', '我是巨蟹座']
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
                params = ['五分钟健身', '平板运动', '今天天气', '退出']

            if query == 'mxmusic':
                params = ['打开冥想音乐', '流水声']

            if query == 'dictionary':
                params = ['打开汉语词典', '不期而遇是什么意思', '退出']

            if query == 'translation':
                params = ['打开中译英', '今天天气', '退出']

            if query == 'music':
                params = ['播放音乐', '随便来首歌', '播放周杰伦的稻香']

            if isinstance(params, list):
                result = check_answer(['Iitializing', 'Initialized'], query + '_answer')
                statuscode = result.session_answer(params)


            else:
                result = check_answer(params, query + '_answer')
                item = json.loads(result.get_answer())
                data = json.loads(item['data'])
                if item['domain'] in ['forex', 'astrology', 'cookbook', 'poem', 'limitLine', 'huangli', 'stock',
                                      'audio']:
                    statuscode = 1
        except:

            statuscode = 0

        return statuscode






if __name__ == '__main__':
    main()