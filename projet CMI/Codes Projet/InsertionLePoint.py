# -*- coding:utf-8 -*-
 
import urllib, lxml.html, Insertiondonnee, time, datetime
 
def unes(targetURL):
        aujourdhui = datetime.date.today()
        Insertiondonnee.insert_quotidien(('lepoint','http://www.lepoint.fr/'))
        T = []
        L = []
        file = urllib.urlopen(targetURL)
        data = file.read().decode('utf8')
        file.close()
 
        doc = lxml.html.document_fromstring(data)
        articles_href = doc.xpath('//article[@class="en-continu-li"]//a/@href') + doc.xpath('//div[@class="row keep-cols"]/figure/a/@href')
 
        doc = lxml.html.document_fromstring(data)
        article_titles = doc.xpath('//h2[@class="art-lead"]/text()') + doc.xpath('//div[@class="col plm"]//a/h2[@class="art-title"]/text()')
 
	
        i = len(articles_href)
        for k in range (0,i):
                T.append(article_titles[k])
                L.append(articles_href[k])
        

        for k in range (0,i):
                Insertiondonnee.insert_une(('lepoint',""+T[k]+"","http://www.lepoint.fr"+L[k]+"",aujourdhui))

if __name__ == '__main__':
        print unes("http://www.lepoint.fr/")
