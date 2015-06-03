#! /usr/bin/env python

import fetcher
import Queue

class Spider:
	def __init__(self, init_request_info, depth_limit):
		self.root_request_info = init_request_info
		self.depth_limit = depth_limit

	def start():
		url_queue = Queue()
		url_queue.put((self.root_request_info.url, 0))

		while not url_queue.empty():
			curr_url, depth = url_queue.get()		

			if depth > self.depth_limit:
				continue
