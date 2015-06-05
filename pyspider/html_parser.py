#! /usr/bin/env python

import re
import urlparse

class HtmlParser:

	@staticmethod
	def extract_url(url, page_content):
		link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,page_content)

		url_list = list()
		for link in link_list:
			base, flag = urlparse.urldefrag(link)
			if base.strip():
				url_list.append(base)
		return url_list
