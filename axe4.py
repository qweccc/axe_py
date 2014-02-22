#!/usr/bin/env python
# encoding: utf-8
# http://axe.g0v.tw/level/4

import urllib, urllib2, re

lines = []
last_url = None

def parse_page(index):
	global last_url
	url = "http://axe-level-4.herokuapp.com/lv4/" if index == 1 \
		else "http://axe-level-4.herokuapp.com/lv4/?page=" + str(index)

	# The hint is that we shall make our bot look like a real browser.
	req = urllib2.Request(url)
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11')
	if (last_url):
		req.add_header('Referer', last_url)
	last_url = url

	html = urllib2.urlopen(req).read()
	pattern = r"<tr>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*</tr>"
	results = re.findall(pattern, html, re.MULTILINE)[1:]
	format = '{"town": "%s", "village": "%s", "name" : "%s"}'
	for result in results:
		lines.append(format % tuple(result))

for i in range(1, 25):
	parse_page(i)

with open("test.txt", "w") as f:
	f.write("[%s]" % ",\n".join(lines))
