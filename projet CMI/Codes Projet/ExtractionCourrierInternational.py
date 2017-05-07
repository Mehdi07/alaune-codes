# -*- coding:utf-8 -*-

import urllib, lxml.html

def unes(targetURL):
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()

	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//main/div/a/@href')

	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//main/div/a/article//h1/text()')

	return zip(article_titles, articles_href)

'''
class CourrierInternational(object):

	def __init__(self):
		print 'Init class'
		self.targetURL = 'http://www.courrierinternational.com'

	def __crawl__(self):
		print 'Opening URL'
		file = urllib.urlopen(self.targetURL)
		print 'URL opened'
		data = file.read().decode('utf8')
		file.close()

		doc = lxml.html.document_fromstring(data)
		print 'Processed HTML'
		articles_href = doc.xpath('//main/div/a/@href')

		print len(articles_href)
		for a in articles_href:
			print a
			print

		doc = lxml.html.document_fromstring(data)
		print '(Re)Processed HTML'
		article_titles = doc.xpath('//main/div/a/article//h1/text()')

		print len(article_titles)
		for a in articles:
			print a
			print

		return zip(article_titles, articles_href)

	def unes(self):
		titles_and_href = self.__crawl__()
		html = ''
		for item in titles_and_href:
			html += '<h2>'
			html += '<a href="' + self.targetURL + item[1] + '">' + item[0].strip() + '</a></h2>\n'
		print html
		return html

if __name__ == '__main__':
	hc = HeadlinesCrawler('http://www.liberation.fr')
	hc = CourrierInternational()
	print 'Class instance ok'
	print hc.unes()
'''



