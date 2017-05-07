# -*- coding:utf-8 -*-
 
import urllib, lxml.html, Insertiondonnee, time, datetime
 
#http://www.journaldunet.com/
def unes(targetURL):
        aujourdhui = datetime.date.today()
        Insertiondonnee.insert_quotidien(('journaldunet','http://www.journaldunet.com/'))
        T = []
        L = []
        file = urllib.urlopen(targetURL)
        data = file.read().decode('utf8')
        file.close()
 
        doc = lxml.html.document_fromstring(data)
        articles_href = doc.xpath('//h2[@class="app_title"]/a/@href')
        doc = lxml.html.document_fromstring(data)
        article_titles = doc.xpath('//h2[@class="app_title"]/a/text()')
	
        i = len(articles_href)
        for k in range (0,i):
                T.append(article_titles[k])
                L.append(articles_href[k])
        

        for k in range (0,i):
                Insertiondonnee.insert_une(('journaldunet',""+T[k]+"",""+L[k]+"",aujourdhui))



if __name__ == '__main__':
        print unes("http://www.journaldunet.com/")
