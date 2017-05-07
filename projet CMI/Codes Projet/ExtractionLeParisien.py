# -*- coding:utf-8 -*-

import urllib, lxml.html


def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
	doc = lxml.html.document_fromstring(data)
	articles_href =  doc.xpath('//article/h1/a/@href')+doc.xpath('//article//h2/a/@href')+doc.xpath('//article//h3/a/@href')
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//article/h1/a//text()')+doc.xpath('//article//h2/a/text()')+doc.xpath('//article//h3/a/text()')
	return zip(article_titles, articles_href)

