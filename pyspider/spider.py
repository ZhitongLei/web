#! /usr/bin/env python

import urllib2 as http # http

REQUEST_TIMEOUT = 10
PAGE_DECODE = 'utf8'

class SpiderRequest:
	def __init__(self, url, data = None, headers = {}):
		self.url = url
		self.data = data
		self.headers = headers

	def set_data(self, data):
		self.data = data

	def add_header(self, key, value):
		self.headers[key] = value


class Spider:
	def __init__(self, timeout = REQUEST_TIMEOUT, page_decode = PAGE_DECODE):
		self.set_timeout(timeout)
		self.page_decode = PAGE_DECODE

	def request(self, spider_request):
		request = http.Request(spider_request.url, spider_request.data, spider_request.headers)
		try:
			response = http.urlopen(request)
		except http.URLError, e:
		 	if hasattr(e, 'code'):
				print('Error code: ', e.code)
			elif hasattr(e, 'reason'):
				print('Fail to reach server, reason: ', e.reason)
		else:
			return response.read().decode(self.page_decode)
		
	def set_timeout(self, timeout):
		http.socket.setdefaulttimeout(timeout)


if __name__ == '__main__':
	zhihu_lasest_news_url = 'http://news-at.zhihu.com/api/3/news/latest'
 	USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
  	HTTP_HEADER = { 'User-Agent' : USER_AGENT }

	request = SpiderRequest(zhihu_lasest_news_url) 
	request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')


	spider = Spider()
	response = spider.request(request)
	if response:
		print(response)

