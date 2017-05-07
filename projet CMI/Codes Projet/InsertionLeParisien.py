# -*- coding:utf-8 -*-
 
import urllib, lxml.html, Insertiondonnee, time, datetime

def unes(targetURL):
        aujourdhui = datetime.date.today()
        Insertiondonnee.insert_quotidien(('leparisien','http://www.leparisien.fr/'))
        T = []
        L = []
        file = urllib.urlopen(targetURL)
        data = file.read().decode('utf8')
        file.close()
        doc = lxml.html.document_fromstring(data)
        articles_href =  doc.xpath('//article/h1/a/@href')+doc.xpath('//article//h2/a/@href')+doc.xpath('//article//h3/a/@href')
        doc = lxml.html.document_fromstring(data)
        article_titles = doc.xpath('//article/h1/a//text()')+doc.xpath('//article//h2/a/text()')+doc.xpath('//article//h3/a/text()')

        i = len(articles_href)
        for k in range (0,i):
                T.append(article_titles[k])
                L.append(articles_href[k])
        

        for k in range (0,i):
                Insertiondonnee.insert_une(('leparisien',""+T[k]+"",""+L[k]+"",aujourdhui))



if __name__ == '__main__':
        print unes("http://www.leparisien.fr/")
