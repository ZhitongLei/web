#! /usr/bin/env python

from fetcher import RequestInfo
from fetcher import Fetcher
from html_parser import HtmlParser

import Queue

class Spider:
	def __init__(self, init_request_info, depth_limit):
		self.root_request_info = init_request_info
		self.depth_limit = depth_limit

	def start(self):
		url_queue = Queue.Queue()
		url_queue.put((self.root_request_info.url, 0))

		request_info = RequestInfo('', None, self.root_request_info.headers)
		fetcher = Fetcher()

		while not url_queue.empty():
			curr_url, depth = url_queue.get()		
			print 'url=%s, depth=%d' % (curr_url, depth)

			if depth > self.depth_limit:
				continue
			
			depth += 1
			request_info.url = curr_url
			page_content = fetcher.request(request_info)

			## parse page
			## Content.parse(page_content)

			url_list = HtmlParser.extract_url(page_content)
			if url_list:
				for url in url_list:
					url_queue.put((url, depth))


if __name__ == '__main__':
	init_url = 'http://zhihu.com'
	request = RequestInfo(init_url) 
	request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

	spider = Spider(request, 0)
	spider.start()
