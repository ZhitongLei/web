#! /usr/bin/env python

import re

class HtmlParser:

	@staticmethod
	def extract_url(page_content):
		link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,page_content)

		url_list = list()

		return url_list
