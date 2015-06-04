#!/usr/bin/env python

from fetcher import RequestInfo
from fetcher import Fetcher
from html_parser import HttpParser

if __name__ == '__main__':
	init_url = 'http://zhihu.com'
	request = RequestInfo(init_url) 
	request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

	fetcher = Fetcher()
	response = fetcher.request(request)
#h = HttpParser()
	if response:
		url_list = HttpParser.extract_url(response)
		if url_list:
			for url in url_list:
				print url
