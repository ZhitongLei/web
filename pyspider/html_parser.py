#! /usr/bin/env python

import re
import urlparse

class HtmlParser:

	@staticmethod
	def extract_url(page_content, host=''):
		link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,page_content)

		url_list = list()
		for link in link_list:
			# condense URLs into some canonical form
			# so zhihu.com#signup becomes zhihu.com
			base, flag = urlparse.urldefrag(link)
			if base.strip().find(host) != -1 :
				url_list.append(base)
		return url_list
