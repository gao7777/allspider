import json
import re,pymysql
from zhongyinwenchuli import Year_to_chinese,To_chinese4

def quchubidian(str):
    if re.search('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]',str):
        str=re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", '', str)
    if re.search('丨',str):
        str = re.sub('丨','',str)
    return str
def chinese_num(str_data):
    num_list = re.findall("\d+", str_data)
    if num_list != []:
        for i in num_list:
            # print(i)
            # print(b,'1')
            if len(i) == 4:
                # print(i)
                zw_str = Year_to_chinese(int(i))
                # print(zw_str)
                str_data = re.sub(i, zw_str, str_data)
                # print(b)
            else:
                # print(b)
                zw_str = To_chinese4(int(i))
                str_data = re.sub(i, zw_str, str_data)
                # print(b,'===xiyuu44')
                # print(num_list)
    return str_data

def main():
    conn = pymysql.connect(host='127.0.0.1', user='root', password="gaozhiwei",
                     database='nlpdata', port=3306, unix_socket=None,
                     charset='utf8',autocommit=True)
    cur= conn.cursor()
    # quchong_list=['音乐日记', 'Umizoomi', 'movies', '交际德语教程第二版', 'Studio[21]', '心理学与生活', 'TANG.MUSIC', '亲子教育', '【法语】', '比尔·布莱森', '旧版', '耳听经典', 'Horrid', '股票', '阿斯顿互动英语', 'Kill', '有声文学', 'live', 'Fire', '小牛顿恐龙系列100问', '【米粒妈团购】', "What's", '童音跟读', '阅读', 'MUSIC', '【隽语出品】', '【直播回放】', '《匆匆》', '跟上兔子', '♪', '【思享】', 'Am', 'Accent', 'Guide', 'Stray', '英语诗歌', 'Tape', '《振毕高呼》', 'Tallman', 'Morning', '跟老外学职场英语', '芬兰语', 'Poem', '《佛医禅观》', 'Nursery', '聊斋', '微信公众号', '直销', '《官场斗》', 'Dreams', '【第二季】', '生活小窍门', 'Side', 'POP', '台湾大学', 'Games', '❤', 'have', '【视频精品】', '分享', 'Guess', '听法国文学', 'way', 'Top100【私货】', '追风筝的人', '缠中说禅', 'an', '童声示范/伴奏', '慢摇', "kid's", 'LIVE', '浮音厨房', '自我提升', '四世同堂', '《富兰克林自传》', '悲惨世界', 'Fonética', '胎教', '邱野世界观:', '邱野世界观', 'Reader', '《海底两万里》', '配套听力', '北外', '名家朗读', '12', 'Ⅰ', '（五）', '捷克语', '【 曲黎敏 】', '《人民的名义》', '【小鱼阿姨讲故事】', 'Horse', 'GOOSE', '佛教故事', '舞曲', '那些年', '梁凯恩', '节目', '每天五分钟', 'Away', 'phonics', '仓央嘉措', '叔本华', 'Golden', '完|', '冀教版', 'Sense', 'activités', '心灵疗愈', '禅茶一味', '大曹王寺', '《窗边的小豆豆》', '华飞', '易中天中华史', '《妙法莲华经》', '中华上下五千年', '《雪中悍刀行》', 'Stars', '心理', 'Tot', '第三版', '神奇的α波', 'Nature', '暮光之城', '爱源悦读', 'Sky', '跨境电商雨果网', '晚安故事', 'Horrible', '武家坡', '审计', '【 相声 】', 'Purple', '《龙猫》', 'dj慢摇吧大神', 'des', 'chat', '中国皇家唱诗', '配乐版', '英语Join', '李玫瑾', '主编', '汪广辉', '英雄联盟', '格列佛游记', '～', 'Beauty', '王玥波播讲', 'Nate', '【原创广播剧】', '【mini课堂】', 'WORLD', '考研', '刺激战场', '意大利语', '珍藏版', 'Our', '北京-', 'Rhythm', '船山全书', '挑战', '《劳动关系协调师》', 'pod', '节奏', '六年级下册', '字幕', '全年龄广播剧', '小桥流水', '多学多用', '李多奎', '百大DJ', '销售技巧', 'be', '200', '自创', 'a-z', '读诵', '一花一世界', 'we', 'see', '李胜素', 'Z', '精华版', '《民法总则》', 'Pod', '《贵妃醉酒》', 'Star', '叶嘉莹', 'Conversations', '最强大脑', '一本搞定', '上海特训', '战略', '剑桥雅思听力完整', '整理版', '大自然的声音', 'BEC高级', 'Reggae', '梅花大鼓', '木偶奇遇记', 'Valentine', '3A', '《玉蜻蜓》', 'Was', '爆笑植物学校', '课文朗读', '中国文学史', '刘丰', '文言文', '营销', '剑桥少儿英语天天练', '二级', '小品', '第一卷', 'Hot', 'Kid`s', '【纯音乐】', '广州英语沪教版', '蓝星球英语', '毛姆', '《韩非子》', 'Where', 'Yourself', '课本音频', '新概念英语第一册', 'Raz', '古筝', '江怡', '秘密', '牡丹亭', '【职场大穿越之红楼系列】', '治愈', 'Verve', '爵士乐', '社会热点', 'Movies', 'ego+', '2015北京工体DJ音乐盒', '儿童睡前故事', '品书悦读', 'Room', '湘少版', '《幽灵公主》', '翟山鹰', '剑桥英语青少版EIM', 'A2.1', '2019年|注册会计师|CPA', '夏洛的网', 'Free', 'Sea', '休闲音乐', 'Minecraft', '《易经杂说》', 'orale', '《朝花夕拾》', 'Mary', '《思维方式》', '王佩瑜', 'Ich', '法国香颂', '【附PDF】', 'Letter', 'Sawyer', 'Straight', '【港影留声】', 'Modern', '大隋风云', '中国文化要略', '朗诵版', '1A', '《十万个为什么》', '六年级下', '社群营销', '∣', '税法', '《白鹿原》', '《山海经》', '纳尼亚传奇', '【小学生】', 'John', '番外篇', 'Goodbye', 'Three', 'Das', '词以类记', '用美国幼儿园课本学英语', 'Bass', '贝多芬交响曲全集', '销售', '钱文忠', '美音版', '商务英语教程Level', '（八）', '新rock', 'shool', 'Island', 'Bryson', '牧羊少年奇幻之旅', '《古文观止》', '台湾大学公开课', 'JY', '韩语口语', '@DJRomaStone', '黄香莲歌仔戏', '내곁에', 'Talking', 'Anne', '每天3分钟', 'goose', '电视原声带', '《四圣心源》', 'Elephant', '《保险法》', 'Head', '《麦田里的守望者》', '[7-10岁]', '早泄', '杂谈', 'Beyond', '一年级英语（下）HQ', '《大乘妙法莲华经》', '日有所诵', '长篇小说', 'TCF', '五音治疗音乐之', '爱探险的朵拉', '名人传记', '神笔马良', '【精华版】', 'A2.2', '藏在地图里的成语', 'Wolf', '平说文学', '【未完结】', '鬼谷子', '详解', '钱穆', '노래를', '찾는', '사람들', 'Remember', 'Eule', 'Runner', '下）', 'Pola', 'RetRadio', '程鸣梁爽评书', '历史', 'Girls', '英文名著', '《白蛇》', 'Putumayo', 'Llama', '胡小闹日记', 'Farm', 'short', '【上妻宏光】', 'Tale', 'Forever', '【双播】', '【幽默志怪评书】聊斋', 'Move', '哲学概论', '当代大学德语', '精灵宝可梦', '熊逸', '《儒林外史》', 'READ', '健康养生', '少儿法语', 'Case', '杨家将', 'Java', '《夏洛的网》', 'River', 'Gang', 'Taylor', 'Thomas', '百家姓', '《慈禧》', 'Dawn', '《夜读》', 'Special', '奇迹男孩', '《天空之城》', 'Bang', '从入门到精通', '民国那些事儿', '海底两万里', 'HSK', '四年级下', '《捕捉儿童敏感期》', '林江', '苏州评弹', '第三卷', '翻唱专辑', '北京', 'Bossa', 'Park', '讲座', '童谣', 'Travel', 'Under', '上帝之眼', 'Boom', '【国学经典】', '金银岛', 'Adventure', '哈佛家训', '翻译', '爱', 'treehouse', '《四季》', 'Nothing', 'KET', '张汝伦', '七色花', '2A', '世界历史', '唱', 'Fish', '《曾国藩家训》', '诗歌之声', 'world', '《坛经》', '【官方正版】', '【全民朗读】', '《地藏经》', '勃拉姆斯', 'Here', '《三体》', '周易', '每日一句', '《四郎探母》', '职业规划', '《神奇校车》', '健康中国', '公考', '伊索寓言', '06', '单口相声', '第四季', '【绘本】', '治愈系', '现代广播剧', 'HipHop丨Funky', 'VOL', '熊汝霖音乐大师课', 'Home', '《摩登家庭》', '昂立国际幼儿英语', 'Feel', '公务员面试', '蜜蜂声药', '|新日语能力考试考前对策', '【独家歌路】2016', '上海', '《三国志》', 'Rhymes', '【洛天依原创】', '刘立福', '剑网三树洞/818b站UP', 'SHOW', 'Toad', 'Español', 'Summer', '龚一', 'like', 'Dr', '《人间词话》', 'Pete', '【9.9元福袋】', '名师导学', '【唯一童年】', '陈春花管理经典', '脱口秀', '健康减肥', '英文有声书', '《悦读联播美文精选》', 'Every', '苏教版', '京剧之星', '《苏东坡传》', 'TOUCHSTONE', '有声朗读版', '商业模式', '黄梅戏', '《三笑》', '【全本】', '《聊斋志异》', '深度睡眠', '音乐|', '钢琴曲', '单词朗读', 'Mum', '第二卷', '入门级', '【多人广播剧】', '完结', 'AI', '双语故事', '[全网汇集版]', '远离疾病', '《如何修证佛法》', '《流浪地球》', 'Have', '【1】', '昂立少儿新进阶英语', '《看见》', 'Willows', '叶青歌仔戏', '《醒来》', '《珍珠塔》', '【独家私货】4月大神', '注册会计师', '中医针灸', '钱老师', 'B1.1', 'Movie', '名词解释', '英语启蒙', '鱼眼驾道', 'Teddy', '南禅七日', '《百年孤独》', 'sing', 'Andrew', '字幕版', '商务英语', 'Max', 'Will', '自信', 'CD3', '【梁邦彦】', '中国历史', '《理想国》', 'Nu', '《半生缘》', '疗愈', '夜听', '古风BG', '【晓月】', '郁莉', '带电的今晚', 'Too', '《了不起的盖茨比》', 'Without', 'Classical', 'Paris', '《牡丹亭》', 'Wonderland', '汪诘', 'Word', '轻小说', '《世界上下五千年》', '【卡修Rui】', '娓娓学语文', '∕', '【媒趣儿FM】', '一年级下', '[加]', '921名书场', '《孟丽君》', '《茶经》', '奇诺之旅', 'Beginner', '车载音乐', '广州小学英语', '李家祥', '清华大学', 'Mc梦柯', '活法', '小学生快乐课堂周周练', '五年级下册', '于魁智', 'Wonder', 'BEST', 'Toots', 'Thielemans', '爱情', '有声小说', '期货', '【转采】', '周国平', 'Complete', '人工智能', '诗词', 'That', '《我的世界》', '《爱情公寓》', '【晚安】', '李萌', 'BGM', 'Speeches', '全一期', 'night', 'Pop', '【dj慢摇吧】', '（完）', '【轻松英语名著欣赏】', '中国交响乐团作品选', '广州沪教牛津版', '课本录音', '【译林双语】', '小学数学', '娱乐香饽饽', 'Week', 'Tonight', 'Key', '《冰鉴》', 'super', '一年级', 'Lean', '十分钟名著故事', '田艺苗', 'PS', '平面设计', 'Photoshop', '三', '实验班提优训练', '秦文君', '【情感方程式】', '美文', '翻配', '《传世书》', 'Arbeitsbuch', '访谈', 'Bedtime', '四季养生', 'Call', 'Beat', '中医针灸教学', 'book', '梁冬说庄子', 'Zoo', '七年级下', '《生命喜悦的祈祷》', '黑猫有声名著阶梯阅读', '[高质量]', '七年级下册', '【众合】', '初级听力', 'mp3', 'Alice', '万物简史', '《狸猫换太子》', '【玉谦讲堂】', '第一期', '古风音乐', '古风音乐人', '【相声】', 'Begegnungen', 'F', '三年级下', '合辑', '快捷英语', '心经', '내사랑', '重生', 'Work', 'mother', 'E.D.M', '中级1', '互联网创业', 'Don', '《骆驼祥子》', '四年级', '（完结）', 'baby', 'Return', 'Chinese', '中英字幕', '《六祖坛经》', '蒙曼', '词汇', '【制作:湮花泪】', '湮花泪】', 'Fly', '绘本故事', '纯乐', '第三集', '袁世海', '庄子', 'Top', '亲密关系', '社群经济', '《单元双测》', '《三国》', 'Short', '神奇校车', '野史下酒', '《心理营养》', 'Never', '【双播精品】', 'Opera', '【幽默志怪评书】', '万历十五年', 'Light', 'Course', 'Brand', '【道子说生命】', 'Now', '6分', '六年级', '走遍美国', '《唐诗三百首》', '宝宝儿歌', 'Eric', '《镜花缘》', '简爱', '奇先生妙小姐', 'starter', '《大登殿》', '小提琴', '电音小站', '[21]', 'Classic', '《万历十五年》', '安妮花', '《乔我说：游戏解剖室》', '【国外代购】', '《雷雨》', 'Gone', '飞鸟集', '译', 'NBA', 'Boy', '经典儿歌', 'JT叔叔', 'Are', '基督山伯爵', '【全一期】', '【畅销书目】', 'kids', 'B2', '《水浒智慧》', 'Electro', '2016年1月', '启航', '–', '河北梆子', '原文朗读', '延世韩国语', '语文', 'Castle', '开讲啦', '意林小小姐', '小AI说', '养生音乐', '【章鱼讲故事】', '配音', '唐调吟诵', '《傅雷家书》', '创业', 'Blue', '【推荐】', '’', 'Coco', '飘', 'Mixtape', '财商', 'Family', '四年级下册', '【秦腔】', '瑞思Rise', '附PDF', '纪录片', '叶曼', 'A1.1', '易中天', 'Let', 'Real', '跟读版', '绝对内涵', '旅行', '三国新说', '听故事', '高月明', 'DVD', '@2015', '翟鸿燊', '昂立少儿进阶英语', '【更新中】', '原版音频', '《赵氏孤儿》', '了凡四训', '走遍法国', 'Masters', '【美】', '股权激励', '《金匮要略》', '金刚经', '南怀谨先生主讲', 'Speak', '成语故事', '零基础', 'Clements', 'Fat', '周文强', '直播回放', '焦虑症', '睡眠', '【高考地理】', '婚姻', 'Disco', 'B.', 'du', 'Rock', '（六）', 'was', 'phonics+', 'Jones', '中华经典素读范本', '【优优私塾】', '李和曾', '悦享听', '《傲慢与偏见》', 'G1', '管理', '【有视频版】', '曲剧', '段子', '《自卑与超越》', 'Beautiful', '易经', 'His', '维克多', '爱才有道', '【文期会】', '《世说新语》', 'Jack', '[', '延世韩国语1', '】康震', '唐宋八大家', '申凤梅', '【炫罗】', '沪教牛津版', 'Corner', '【一】', '《财务自由之路》', '柴可夫斯基', '365', 'EDM電音实验室.Club.MelbourneBounce.商业', 'Biscuit', '【独家私货】6月大神', 'Ivy', 'Greatest', '听', 'Rise', '了不起的盖茨比', 'Gatsby', '直播', '名人经典', '丸子演播', '单曲', 'Last', 'Station', '【优思铭想】', '~', '03', 'nouveau', 'Two', '【千里共良宵】', '中高级听力', '《朱子治家格言》', '【片段】', '说唱', 'Susie', 'Monkeys', 'More', 'Civilization', '《白蛇传》', 'Made', '【貳】', '国学启蒙', '菲伯尔钢琴基础教程', '【经典】', '复旦大学', 'Vocabulary', '高考英语', '言慧珠', 'Lady', 'Culture', '朗诵', '完整版', '故事', '【艺休哥】', '录音', '宝宝剧场', 'big', '科学大探险', '张君秋', '三字儿歌', '《寿康宝鉴》', '《锁麟囊》', '《单词速记》', '社交恐惧症', '中国通史', '济公传', '三年级下册', 'life', '原声带', '原声', '【情感电台】', 'Lola', '附文本', '《水浒》', 'Lee', 'house', 'words', 'Seuss', 'Soul', '家庭教育', '安徒生童话', '杜保瑞', '剑桥少儿英语', '磨耳朵', '精选BGM', '【十三经】', 'Cambridge', '《大家的日语》', '绕口令', '私改榜单E.D.M', 'Mashup', '【京剧角儿们的老唱片】', '1-4', 'Be', '【独家代购】', 'BEC', 'Il', '曾国藩', '耐听的布鲁斯', '名家朗读版', 'at', 'True', 'Do', '三年级', 'Dr.', "Man's", '乱序版', '《鬼谷子》', '一路上有诗', '郭德纲单口精品', 'box', 'O.S.T', '《同步课堂》', '沪教版', '格林童话', 'Echo', 'Wonderful', '（三）', '【完整版】', '【 太美京剧 】', '太美京剧', 'Miss', '[精简]', 'Mr.', 'Things', '【剧情歌】', '【星之梦】', '《读者》', '【Colorful~】', '正能量', 'Dragon', 'Essential', 'x', 'Eyre', 'Jeff', '情商', 'about', '巫娜古琴', '房产', '这时应该怎么说', 'Readers', 'DELF', '第二部', 'Rap', "爵士Man's", '人教版英语', '[連載の劇]', 'français', 'German', 'Season', 'News', '课程', '老版', '杨宝森', '（', 'Take', '+', '阿斯顿英语', 'OUR', '《三命通会》', '《听着音乐去旅行》', '二', 'Box', '【风流逐声】', '背景音乐', '周锐', '爵味', 'Library', '朗读者', 'Gold', '儿歌', 'Easy', '《素书》', '三十六计', 'Hop', '《非暴力沟通》', '微信262654043', '产品会说话', '知行合一', 'Future', 'history', 'radio', 'BC', 'God', '【晓月作文屋】', '一卷搞定', 'it', 'Funky', '稻盛和夫', 'China', '经典', '【粤语】', '轻松读书', '上海教育出版社', 'Fun', 'Rainbow', 'von', '吟唱', '【头陀渊】', '评剧', '国学', '04', '【韩语口语】', '9', '11', 'Heart', '说话技巧', '【合集】', 'en', '羊皮卷', '[籽妈推荐绘本]', '中文版', '粤语广播剧', 'III', 'Know', '新版', '80', 'TIME', '刘强东', '北京大学', '越调', 'Twerk', '每天10分钟', 'CAN', 'first', 'Around', '诵读', 'Lost', '一千零一夜', '《中华上下五千年》', 'Christmas', '黄金古典十合集（珍藏版）—', 'El', 'Like', '13', 'Richard', '《美国乡村音乐选》', '【免费】', '你好', '晚安', 'Football', '失传的营养学', 'Way', '世界著名古典音乐选', '官场小说', '静心', '大学', '中庸', '古风', 'time', 'J', 'Coffee', '瑜伽', '北京工体DJ音乐盒', 'Get', 'Japanese', '放松', '小说', '变形金刚', 'Poems', '剑桥双语小说馆', '微营销', 'Tom', 'Frog', '杨丽花歌仔戏', '公开', '《爱的教育》', '1B', '唐诗三百首', '新世纪钢琴', 'Mr', 'i', 'den', 'story', 'Album', '卡耐基', '水浒传', 'show', '《The', 'Street', '《秘密》', 'this', '日语', 'Rich', 'James', 'Country', 'Or', 'War', '李文槐', '陈四文', '“人文清华”讲坛', 'Yoga', 'Menschen', '情绪', 'song', '李强', 'Art', 'Speaking', '【豫剧】', '名师领读', '《西厢记》', 'Pimsleur', '《老友记》', 'Break', 'Power', 'Science', '原声大碟', '俞凌雄', '中医养生', 'By', 'Dream', '【第一季】', 'Sight', 'songs', '自考', '【东仪秀树】', 'am', 'Narnia', 'Down', '弟子规', '《简爱》', '《富爸爸穷爸爸》', 'Alek-Z', 'Training', '牛津版', '喵博士听名著', '又又国学堂', 'Vol.', '儿童相声', '《原则》', 'Mind', 'White', 'Alter', '张火丁', "Child's", 'Ⅱ', '私改榜单暖场早场酒吧必备单曲', 'Critter', '【一丝小乐】', '第二辑', '节选', '《左传》', '二年级', 'Wir', 'Brown', '学英语', '【疯狂磨耳英语】', 'Explorer', '【十四桥出品】', 'Friends', 'et', 'Henry', '蚂蚁求知|', 'Twilight', '第二集', '基金', 'word', '【古风】', 'Spanish', '剧情歌', 'Charlie', 'Petit', '名师郦波', '演讲', '课本', '中级', 'Children', 'Der', '新东方', '轻音乐', 'Not', 'Plus', 'Listening', '汽车音乐', '一周一英文名著', "Don't", '夜话', 'Jane', '呼儿', '《羊皮卷》', '挽回爱情', 'Animal', 'Sing', '杜云生', '上教社牛津全国版', 'step', '《', '第二册', '音乐疗法', '情感', 'Deep', 'Web', 'An', 'Bear', '第一辑', '毕淑敏', 'Learn', '五年级', '作者', '配文稿', '中国国家地理百科全书.', '睡眠音乐', '每天5分钟', '【 民乐名家 】', '民乐名家', 'Garden', '【独家资源】', 'IN', 'Peter', '马连良', '绿野仙踪', '人和路', '夜读', '肖邦', 'Michael', 'Jackson', 'Play', '智慧人生之', '张少佐评书', '十万个为什么', 'Road', 'Dad', '大家的日语', 'Pride', '傲慢与偏见', 'do', '世纪乐典之', '《朗读者》', 'C', '第2版', '纯爱', 'Prejudice', '[世界古典乐精选(10CD)]', 'Out', 'Learning', '11.30-12', '《乔我说', '【越剧】', '投资理财', '莫扎特', '2013', '戏曲天地-京剧名家', '入门', '俞敏洪', 'Young', 'kleine', 'Welcome', ']', 'So', 'Smart', '北路梆子', '汤婧平', '【轻松英语名着欣赏】', 'Les', 'Green', '【制作:凉情】', '凉情】', 'George', '西河大鼓', '国学宝', 'can', 'read', 'Newbery）', 'Baby', '吸引力法则', 'Starter', '《儀禮鄭注》', '大斌小说', '鹅妈妈童谣', 'Minds', "Charlotte's", '班得瑞', '《江城不眠夜》', '英语口语', 'Girl', '【巴巴妈妈讲故事】', '《三十六计》', '绝地求生', 'King', '101', 'Step', '《将进酒》', '青少版', '私改榜单暖场', 'Deutschland', 'la', 'Club', 'David', '评书', '经典诵读', '【 倪海厦 】', '王阳明', 'le', '小学语文', '三年级英语（下）HQ', '现代BG', '美版原音', 'stories', '新世纪', '【全】', '王紫杰', '公务员考试', '恋爱', 'Playway', '千字文', 'Red', 'Who', 'Game', '第二版', 'Tales', '英文', 'Adventures', '★', '植物世界', '05', '《实验班提优训练》', '春雨教育', '7', 'VIP', '声律启蒙', 'Curious', '小孔子', '孙子兵法', '单词', '国学经典', 'X', '诗经', '《金瓶梅》', '陈安之', '老子', '翻唱', '弹词', '财务自由之路', '【碎岛玄舸】', 'Sound', '下册', 'DJAlek-Z', '安利你一下', '.', '【精品】', 'Listen', '【评书】', '早场', '上册', '中国名师微课程', '伴奏', 'Song', 'little', '10', 'Bus', 'About', '8', 'FM', 'reading', '夜店DJ夜曲·夜汇美&音悦荟', 'Sherlock', 'Holmes', '小学生必读', '歌曲', 'Join', '越剧', '【超级导师】', '儿童故事', 'A2', '第一集', 'Night', '音乐', '【优声由色】', '【已完结】', '——', '第一部', 'Day', '信不信由你', 'Ella', 'This', '【天涯醉音剧社】', '东区音频', 'into', ':', '电影原声', '100', '全', '【高音质版】', '普通话', '相声集', '巴赫', '《百家讲坛》', 'Mystery', '考古拼图', '京韵大鼓', 'With', '新零售', '已完结', 'Days', 'Five', '曹文轩', '刘兰芳', '合集', '大自然声音', '初级', '【音乐】', '《活法》', '【3D环绕】', 'Books', 'It', '直播回听', 'K', 'OF', 'G', 'Deutsch', '红楼梦', "Let's", '贝多芬', 'Business', '《菜根谭》', '王珮瑜', 'Why', '星云大师', '游戏音乐', '三字经', '微信shmusicbank', '曲黎敏', '相声', '（二）', '完結', '《周易》', '《伤寒论》', '课文', 'R&B', '‖', '蒲剧', '【视频】', 'Man', 'Podcast', 'Audio', '（一）', '--', 'talk', 'Da', 'Good', 'American', 'La', '02', 'Moon', '琴书', '《楞严经》', '裘盛戎', 'go', 'Schritte', '【精选】', '｜', '驴迹导游', 'Wind', '潮汕讲古', '著）', '读书', '[美]', 'Stories', 'Princess', 'Collection', '小野丽莎', '【 戏曲 】', '新概念英语', 'Dance', '英文版', '剑网三/树洞/818！b站UP', 'Blues', '一', '论语', 'We', 'What', '甜甜阿姨', 'die', '音频', 'Weird', '谭富英', '2014', 'No', 'love', '《孝经》', 'Diaries', 'From', '原创', 'ABC', '练习册', '【直播回听】', '【 中医 】', 'Kursbuch', '《增广贤文》', '[AUDIOBOOK附电子书]', '朗读', '全民朗读', '韩语', '第三季', 'Chronicles', 'Band', '《老子》', '怪叔叔讲故事', 'music', 'B1', 'Show', '[CV杨东旭]', '钱儿爸', 'Daily', '粤语', 'Kokosnuss', '评弹', 'Best', 'Words', 'Hello', '《笠翁对韵》', '中医', 'Up', '道德经', '有声书', '西区音频', '植物大战僵尸2', '《孟子》', '【翻唱】', 'History', '黄老师读书', 'How', '我爱配音', 'Voice', '杨红樱', '【 百家争鸣 】', 'Goose', 'Secret', '《声律启蒙》', '倪海厦', 'Happy', '【翼之声】', '戏曲', 'Money', '解读', 'Series', '极致', 'Phonics', '富爸爸', '冥想', '专辑', 'Just', '催眠', 'II', '《传习录》', '之', 'Very', 'French', '听力', 'TED', 'Trap', '【最全】', '《千字文》', 'Allan', '全集更新中', '【晓月讲名著】', 'my', '久石让Joe', 'Hisaishi', '百家争鸣', '上', 'One', '区块链', 'EP', '《庄子》', '（完本）', 'CD', '小王子', '6', '【裔美声社】', '西游记', 'Can', 'Piano', 'City', '[20世纪中华歌坛名人百集珍藏版]', '《再别康桥》', '巫娜', 'Prince', '【和平之月】', 'IELTS', '《资治通鉴》', 'On', 'DV爱才有道', 'l', '2019', '《飞鸟集》', '【独家歌路】', '东方雅韵', '下', 'Your', '【KA.U】', 'from', '爵士', 'Is', '三国演义', '《70在路上》', 'All', 'Go', 'Mother', 'der', 'Great', '】', '德语', 'you', '01', '•', 'Die', '—', '》', 'Magic', '[完結の劇]', 'Kids', '昆曲', 'is', '【全集】', 'Songs', '原声音乐', '《那些年》', '《了凡四训》', '节目录音', 'Me', '【完】', 'For', '河南坠子', '邓晓芒', '【粤语学院】', 'CD2', 'Le', '2016', '别致园', '【原创】', '[评书]', '胎教音乐', 'And', '【完结】', '《小王子》', 'Level', '达照法师', '【叶曼课堂】', '第一册', 'First', '黄帝内经', '2015', '睡前故事', '【完本】', 'Live', '【Always】', '《三国演义》', 'Time', '系列', 'Read', 'Cat', 'Radio', '）', '2017', '学生用书', '完', 'A1', '植物大战僵尸', '《弟子规》', 'World', 'CRAZY', 'TEENS', '《心经》', 'Life', 'Black', 'und', 'me', 'B', 'EDM', 'Super', '沈石溪', 'THE', '马云', 'Big', 'de', 'CD1', 'New', 'on', 'Talk', '《三字经》', '法语', 'Book', '/', '《中庸》', '《水浒传》', '5', '南怀瑾', '【广播剧】', 'House', '英语', 'ENGLISH', 'MP3', '《金刚经》', '古琴', '《史记》', '中华经典故事', 'Story', '中篇弹词', 'OST', 'with', '《孙子兵法》', 'School', '古典音乐', '《易经》', '【独家私货】', '文', '《诗经》', 'Reading', 'You', 'To', '广播剧', '《第子规》', '2018', '豫剧', 'In', '【超清】', '《西游记》', 'Jazz', '《大学》', '纯音乐', '第二季', 'Love', '4', 'RAZ', 'for', '《红楼梦》', 'by', '第一季', 'DJ', 'Music', 'a', '伍美珍', '百家讲坛', '320K', 'AI导读', '[全集]', '全集', '我的世界', '著', '《黄帝内经》', '3', 'Little', 'Of', 'My', '【已授权】', '晋剧', '《道德经》', '喜马讲书', '《论语》', 'to', '【动漫原声】', 'A', '【京剧】', 'I', '&', 'in', 'and', 'English', '京剧', '1', '·', '2', '【', 'the', '♫', 'of', '精选', '', 'The', '-', '|']
    sql = 'select albumtitle from ximalayatwo'
    data_list = cur.execute(sql)
    data_list= cur.fetchall()
    data_list= list(set(data_list))
    num = 0
    final_list =[]
    for i in data_list:

        cur_dict = dict()
        data_str = i[0]
        data_str=data_str.strip()
        # str.find()
        cur_dict['resource']=i[0]
        # hhh= re.search('\[.+\]|＜.+＞|\{.+\}|<.+>|【.+】|\(.+\)|《.+》|:.+',data_str)
        # if hhh:
        #     print(data_str)
        #     num+=1
        data = re.search('\[.+\]',data_str)
        if data:
            cur_str = re.search('\[.+\]',data_str)
            cur_dict['[]']=cur_str.group()
            # print(cur_str.group())
        data = re.search('\{.+\}',data_str)
        if data:
            data_str = re.sub('\{.+\}','',data_str)
            # print(cur_str)
        data = re.search('＜.+＞',data_str)
        if data:
            data_str = re.sub('＜.+＞','',data_str)
            # print(cur_str)
        data = re.search('<.+>',data_str)
        if data:
            cur_str = re.search('<.+>',data_str)
            cur_dict['<.+>']=cur_str.group()
            # print(cur_str.group())
        # data = re.search('丨', data_str)
        # if data:
        #     data_str = re.sub('丨','',data_str)
        data = re.search('【.+】',data_str)
        if data:
            cur_str = re.search('【.+】',data_str)
            cur_dict['【】']=cur_str.group()
        data = re.search('\(.+\)',data_str)
        if data:
            data_str = re.sub('\(.+\)','',data_str)
            # cur_dict['【】']=cur_str.group()
        data = re.search('《.+》', data_str)
        if data:
            cur_str = re.search('《.+》', data_str)
            cur_dict['《》']=cur_str.group()
            # cur_dict['【】']=cur_str.group()
            # print(cur_dict['《》'])
        data= re.search(' ',data_str)
        if data:
            # num+=1
            # print(data_str)
            cur_list = data_str.split(' ')
            cur_dict['spacesplit']=cur_list
            # print(cur_list)

        data = re.search(':', data_str)
        if data:
            # print(data_str)
            cur_list = data_str.split(':')
            cur_dict[':split']=cur_list
            # print(cur_list)
        data = re.search('：', data_str)
        if data:
            # print(data_str)
            cur_list = data_str.split('：')
            cur_dict['：split'] = cur_list
            # print(cur_list)
        # Todo
        cur_dict['final']=data_str
        if cur_dict.keys():
            final_list.append(cur_dict)

    statistic_list= []
    statistic_dict=dict()
    for i in final_list:
        cur_dict= {}
        cur_dict[i['resource']]=[]
        for j in i.values():
            if isinstance(j,list):
                for k in j:
                    # if k in quchong_list:
                    #     print(k)
                    # else:
                    #     cur_dict[i['resource']].append(k)
                    cur_dict[i['resource']].append(k)
            else:
                # if j in quchong_list:
                #     print(j)
                # else:
                #     cur_dict[i['resource']].append(j)
                cur_dict[i['resource']].append(j)
        statistic_list.append(cur_dict)


    for i in statistic_list:
        values = list(i.values())
        for i in values:
            for j in i:
                if j in statistic_dict:
                    statistic_dict[j]= statistic_dict[j]+1
                else:
                    statistic_dict[j]=1
    list_one=sorted(statistic_dict.items(),key=lambda i:i[1])
    num_one = 0
    quchong_list =[]
    for i in list_one:
        if i[1]>4:
            # num_one +=1
            quchong_list.append(i[0])
            # print(i)
    new_statistic = []
    for i in statistic_list:
        newcur_dict = dict()
        newcur_dict[list(i.keys())[0]]=[]
        for j in list(i.values())[0]:
            if j in quchong_list:
                # print(i)
                i[list(i.keys())[0]].remove(j)
                # print(j)
                # print(list(i.keys())[0],list(i.values())[0])
                # print(i)
                # print('='*10)
            else:
                j =quchubidian(j).strip()
                # print(j)
                j = chinese_num(j)
                newcur_dict[list(i.keys())[0]].append(j)
        if  len(list(i.values())[0])!=0:
            # num_one+=1
            new_statistic.append(newcur_dict)
            # print(newcur_dict)
    # print(num_one)
    finalnlpdict = {}
    finalnlpdict['dict']=[]
    for i in new_statistic:
        cur_dict = {}
        cur_dict['majorType'] = 'question'
        cur_dict['minorType'] = list(i.keys())[0]
        cur_dict['value'] = []
        for j in list(i.values())[0]:
            if j !='':
                num_one+=1
                cur_dict['value'].append(j)
        cur_dict['value']=list(set(cur_dict['value']))
        finalnlpdict['dict'].append(cur_dict)
    josn_data = json.dumps(finalnlpdict,ensure_ascii=False)
    print(num_one)
    with open('./shujuqingxi.json','w') as f:
        f.write(josn_data)




    # print(num_one)
    # print(quchong_list)



if __name__ == '__main__':
    main()
