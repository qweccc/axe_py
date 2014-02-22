#!/usr/bin/env python
# encoding: utf-8
# http://axe.g0v.tw/level/2

import urllib, urllib2, re

lines = []

def parse_page(index):
	url = "http://axe-level-1.herokuapp.com/lv2/?page=" + str(index)
	html = urllib2.urlopen(url).read()
	pattern = r"<tr>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*</tr>"
	results = re.findall(pattern, html, re.MULTILINE)[1:]
	format = '{"town": "%s", "village": "%s", "name" : "%s"}'
	for result in results:
		lines.append(format % tuple(result))

for i in range(1, 13): parse_page(i)

with open("test.txt", "w") as f:
	f.write("[%s]" % ",\n".join(lines))
