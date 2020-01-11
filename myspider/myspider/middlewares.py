# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64

import requests
from scrapy import signals
import random


# 隧道id和密码
tid = "t17595826405381"
password = "91qwoo84"
# 隧道host和端口
tunnel_master_host = "tps181.kdlapi.com"
tunnel_master_port = 15818
# 备用隧道host和端口
tunnel_slave_host = "tps189.kdlapi.com"
tunnel_slave_port = 15818
# 切换阀值
threshold = 3


# 代理中间件
class ProxyDownloadMiddleware(object):

    def process_request(self, request, spider):
        global threshold
        if threshold > 0:
            host, port = tunnel_master_host, tunnel_master_port
        else:
            host, port = tunnel_slave_host, tunnel_slave_port
        if request.url.startswith("http://"):
            proxy_url = 'http://{host}:{port}'.format(host=host, port=port)
        elif request.url.startswith("https://"):
            proxy_url = 'https://{host}:{port}'.format(host=host, port=port)
        request.meta['proxy'] = proxy_url  # 设置代理
        print("using proxy: {}".format(request.meta['proxy']))
        # 隧道代理需要进行身份验证
        #
        # 用户名和密码需要先进行base64编码，然后再赋值
        username_password = "{tid}:{password}".format(tid=tid, password=password)
        b64_username_password = base64.b64encode(username_password.encode('utf-8'))
        request.headers['Proxy-Authorization'] = 'Basic ' + b64_username_password.decode('utf-8')
        threshold -= 1
        return None


class MyspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # with open('./myspider/ip.txt','r+') as f:
        #     ip_list = f.readlines()
        # print(ip_list)
        # print(type(ip_list[1]))
        # print(random.choice(ip_list).strip(),'dfadf')
        # print(type(random.choice(ip_list).strip()),'dfadf')
        # proxy = 'http://'+random.choice(ip_list).strip()
        # print(proxy)
        # request.meta['proxy']=proxy
        # request.meta['proxy'] = proxy
        # print('ip',request.meta['proxy'])
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # if response.status != '200' and response.status != '302' and response.status != '301':
        #     print('ipbukeyong',request.meta['proxy'])
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Proxy_Middleware():

    def __init__(self):
        self.s = requests.session()
    def process_request(self, request, spider):
        try:
            url = " http://tpv.daxiangdaili.com/ip/?tid=558847662461809&num=10  "
            r = self.s.get(url)
            proxy_ip_port = r.text
            ip_list = proxy_ip_port.split('\r\n')
            # print(ip_list)
            index = random.randint(0, len(ip_list) - 1)
            # print(index)
            ip_proxy = ip_list[index].strip()
            print(ip_proxy)
            # request.meta['proxy'] = 'http://' + ip_proxy
            request.meta['proxy'] = 'http://' + ip_proxy
        except requests.exceptions.RequestException:
            print('***get xdaili fail!')
            spider.logger.error('***get xdaili fail!')
    def process_response(self, request, response, spider):
        if response.status != 200:
            try:
                url = " http://tpv.daxiangdaili.com/ip/?tid=558847662461809&num=10  "
                r = self.s.get(url)
                proxy_ip_port = r.text
                ip_list = proxy_ip_port.split('\r\n')
                index = random.randint(0, len(ip_list) - 1)
                ip_proxy = ip_list[index].strip()
                request.meta['proxy'] = 'http://' + ip_proxy
            except requests.exceptions.RequestException:
                print('***get xdaili fail!')
                spider.logger.error('***get xdaili fail!')
            return request
        return response
    def process_exception(self, request, exception, spider):
        try:
            url = " http://tpv.daxiangdaili.com/ip/?tid=558847662461809&num=10  "
            r = self.s.get(url)
            proxy_ip_port = r.text
            ip_list = proxy_ip_port.split('\r\n')
            index = random.randint(0, len(ip_list) - 1)
            ip_proxy = ip_list[index].strip()
            print(ip_proxy)
            request.meta['proxy'] = 'http://' + ip_proxy
        except requests.exceptions.RequestException:
            print('***get xdaili fail!')
            spider.logger.error('***get xdaili fail!')

        return request

class DoubanDownloadMiddleware(object):

    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # def __init__(self):
        # with open('./ip.txt','r') as f:
        #     ip_list = f.readlines()
        # self.ip_list = ip_list

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # with open('./myspider/ip.txt','r+') as f:
        #     ip_list = f.readlines()
        # print(ip_list)
        # print(type(ip_list[1]))
        # print(random.choice(ip_list).strip(),'dfadf')
        # print(type(random.choice(ip_list).strip()),'dfadf')
        # proxy = 'http://'+random.choice(ip_list).strip()
        # print(proxy)
        # request.meta['proxy']=proxy
        # request.meta['proxy'] = proxy
        # print('ip',request.meta['proxy'])
        # ip_list = self.ipfile.readlines()
        # print(ip_list)
        # print(type(ip_list))
        url = " http://tpv.daxiangdaili.com/ip/?tid=558847662461809&num=10  "
        response = requests.request('get', url,timeout=2)
        str = response.text
        # print(response.content)
        # print(type(response.text))
        ip_list = str.split('\r\n')
        # print(ip_list)
        index = random.randint(0,len(ip_list)-1)
        print(index)
        ip_proxy = ip_list[index].strip()
        print(ip_proxy)
        request.meta['proxy']='http://'+ip_proxy

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # if response.status != '200' and response.status != '302' and response.status != '301':
        #     print('ipbukeyong',request.meta['proxy'])
        if response.status == 200:
            print('200')

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        print('chuzuole')
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# class RandomUserAgent(object):
#     def process_request(self, request, spider):
#         user_agent = random.choice(USER_AGENS)
#         request.headers.setdefault('User-Agent', user_agent)

# class RandomProxy(object):
#     def process_request(self, request, spider):
#         proxy = random.choice(PROXIES)  # 随机选出一个代理
#         if proxy.get('auth') is None:  # 免费代理
#             request.meta['proxy'] = 'http://' + proxy['host']
#         else:  # 收费代理
#             auth = base64.b64encode(proxy['auth'])
#             request.headers['Proxy-Authorization'] = 'Basic ' + auth
#             request.meta['proxy'] = 'http://' + proxy['host']