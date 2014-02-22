#!/usr/bin/env python
# encoding: utf-8
# http://axe.g0v.tw/level/1

import urllib, urllib2, re

html = urllib2.urlopen("http://axe-level-1.herokuapp.com").read()
pattern = r"<tr>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*</tr>"
results = re.findall(pattern, html, re.MULTILINE)[1:]
format = '{"name": "%s", "grades": {"國語": %s, "數學": %s, "自然": %s, "社會": %s, "健康教育": %s}}'
results = [format % tuple(x) for x in results]

with open("test.txt", "w") as f:
	f.write("[%s]" % ",\n".join(results))
