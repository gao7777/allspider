import yaml,time,os
from selenium import webdriver
url = 'https://system.address'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("username")
driver.implicitly_wait(5)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("password")
print("请输入验证码：")
# 手动输入验证码
security_code = input()
time.sleep(1)
driver.find_element_by_id("security_code").send_keys(security_code)
time.sleep(1)
driver.find_element_by_id('sign_btn').click()
driver.implicitly_wait(5)
# 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
time.sleep(5)
cookiesAfter = driver.get_cookies()
len1 = len(cookiesAfter)
# 已经知道需要第几个cookie，这里需要第3个cookie，所以选择cookie下标为2
cookie1 = cookiesAfter[2]
# 获取当前文件所在路径
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# 拼接config.yaml文件绝对路径
yamlPath = os.path.join(fileNamePath,'config.yaml')
# 以覆盖写入打开文件
fw = open(yamlPath,'w',encoding='utf-8')
# 构建数据
data = {"cookie1":cookie1}
# 装载写入yaml文件。
yaml.dump(data,fw)

driver.quit()