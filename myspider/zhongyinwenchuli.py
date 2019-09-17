import re
import jieba
_MAPPING = (
u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九')
_P0 = (u'', u'十', u'百', u'千',u'万')
_S4 = 10 ** 5
def Chuling(str1):
    if str1[-1] =='零':
        str1=str1[:-1]
    # re.sub()
    return str1
def Year_to_chinese(num):
    # print(num)
    str =''
    lst1=[]
    # print(lst1)
    while num>10:
        # print(num%10)
        lst1.append(num % 10)
        num = num//10
    lst1.append(num)
    lst1.reverse()
    # print(lst1)
    for i,j in enumerate(lst1):
        str+= _MAPPING[j]
    return str

def To_chinese4(num):
    # print(num,'hhhh')
    # assert (0 <= num and num < _S4)
    if not 0<=num and num <_S4:
        return ''
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num // 10
        lst.append(num)
        c = len(lst)  # 位数
        result = ''
        # print(lst)
        try:
            for idx, val in enumerate(lst):
                val = int(val)
                if val != 0:
                    result += _P0[idx] + _MAPPING[val]

                    # print(type(lst[idx - 1]))
                    # print(lst[idx + 1])
                    if idx < c - 1 and lst[idx + 1] == 0:
                        # print(type(lst[idx+1]))
                        # print(lst[idx+1])
                        result += u'零'
                else:
                    pass
                    # result+="零"
            return result[::-1]
        except Exception as e:
            print(e)
            return ''


# print(Year_to_chinese(2009))
# print(Chuling("三千零九十零"))
# print(To_chinese4(210))

def fun():
    con_list = []
    with open('/home/gaozhiwei/Desktop/only_title.txt','r+') as f:
        while True:
            a = f.readline()
            if a:
                b= re.sub("[～,­]+",'至',a)
                # print(b)
                b = re.sub("（.+?）","",b)
                num_list = re.findall("\d+",b)
                if num_list != []:
                    for i in num_list:
                        # print(i)
                        # print(b,'1')
                        if len(i) ==4:
                            # print(i)
                            zw_str = Year_to_chinese(int(i))
                            # print(zw_str)
                            b = re.sub(i,zw_str,b)
                            # print(b)
                        else:
                            # print(b)
                            zw_str= To_chinese4(int(i))
                            b= re.sub(i,zw_str,b)
                            # print(b,'===xiyuu44')
                            # print(num_list)


                    # print(b)


                # print(b1)
                b = re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]",'',b)
                # print(b)
                b= re.sub('contentName','contentName:',b)

                con_list.append(b)

            else:
                with open('/home/gaozhiwei/Desktop/filter.txt', 'a+') as f:
                    for i in con_list:
                        f.write(i+'\n')
                break
#
# if __name__=="__main__":
#     fun()
if __name__=='__main__':
    fun()
