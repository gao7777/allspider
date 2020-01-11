import json
import re
import time

import pymysql
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED,ProcessPoolExecutor
from threading import Lock



def getmp3url(url,conn,id,lock):
    try:
        cursor=conn.cursor()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome("/opt/google/chrome/chromedriver/chromedriver",chrome_options=chrome_options)
        sql="update qiankuntingshu set url_mp3={} where id={}; "
    except Exception as e:
        print("firstchuzuole"+e)
        return None
    try:
        # lock.acquire()
        driver.maximize_window()
        driver.get(url)
        driver.switch_to.frame("xplayer")
        # time.sleep(1)
        driver.implicitly_wait(1)
        # WebDriverWait(driver,timeout=1).until(lambda driver:driver.find_element_by_xpath("//body/audio"))
        src=driver.find_element_by_xpath("//body/audio")
        # print(src)
        aa= src.get_attribute("src")
        aa = json.dumps(aa)
        # print(type(aa),"typeaaaa")
        driver.quit()
        cur_sql = sql.format(aa,id)
        # print(id)
        # print(cur_sql)
        cursor.execute(cur_sql)
        cursor.close()
        print(aa)
        return aa
    except Exception as e:
        driver.quit()
        print("secound chuzuole"+id)
        cursor.close()
        raise NotADirectoryError
    # finally:
    #     lock.release()
        # return e



def main():
    # mp3url=getmp3url("http://m.qktsw.com/playbook/37760-1-64.html")
    # print(mp3url)
    conn = pymysql.connect(host="localhost", database="nlpdata", user='root', password='gaozhiwei',
                                autocommit=True)
    cursor = conn.cursor()
    lock = Lock()
    sql = "insert into qiankuntingshu(category,title,url) values(%s,%s,%s);"
    sql="select id,url ,url_mp3 from qiankuntingshu"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    data_list= data_list
    execute = ThreadPoolExecutor(max_workers=15)
    # execute = ProcessPoolExecutor()
    all_task_list = []
    # final_list = []
    cursor.close()
    try:
        num = 0
        for i in data_list:
            id=i[0]
            url2=i[1]
            url3 = re.sub("www","m",url2,count=1)
            urlmap = i[2]
            # cur_list = (url3,conn,id)
            # final_list.append(cur_list)
            if urlmap == None or "":
                task = execute.submit(getmp3url,url3,conn,id,lock)
                all_task_list.append(task)
                num+=1
                print(id)
            # url4= getmp3url(url3,conn,id)
            # print(url4)
        # for i in final_list:
        #     print(i)
        print(num)
    except Exception as e:
        print("mainchuzuole"+e)

    wait(all_task_list,return_when=ALL_COMPLETED)
    # execute.shutdown()

    print("finish")
    conn.close()



if __name__ == '__main__':
    main()