#!/usr/bin/env python
# encoding: utf-8
# http://axe.g0v.tw/level/3

import urllib2, re, cookielib

lines = []

# The hint is that we need to accept cookies.
jar = cookielib.FileCookieJar("cookies")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

for index in range(1, 77):
	url = "http://axe-level-1.herokuapp.com/lv3/" if index == 1 \
		else "http://axe-level-1.herokuapp.com/lv3/?page=next"
	html = opener.open(url).read()
	pattern = r"<tr>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*</tr>"
	results = re.findall(pattern, html, re.MULTILINE)[1:]
	format = '{"town": "%s", "village": "%s", "name" : "%s"}'
	for result in results:
		lines.append(format % tuple(result))

with open("test.txt", "w") as f:
	f.write("[%s]" % ",\n".join(lines))
