#! /usr/bin/env python

import re

class HtmlParser:

	@staticmethod
	def extract_url(url, page_content):
		link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,page_content)

		#url_list = list()
		#for link in link_list:
			
		return link_list
