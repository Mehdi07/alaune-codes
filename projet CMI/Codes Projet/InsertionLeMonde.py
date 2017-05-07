#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, lxml.html, Insertiondonnee, time, datetime

def unes(targetURL):
    aujourdhui = datetime.date.today()
    Insertiondonnee.insert_quotidien(('lemonde','http://www.lemonde.fr/'))
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    T = []
    L = []
    
    doc = lxml.html.document_fromstring(data)
    article_href = doc.xpath('//article[contains(@class, "titre_une")]/a/@href')
    
    doc=lxml.html.document_fromstring(data)
    articles_titles = doc.xpath('//h1[contains(@class, "tt3 ")]/text()')

    i = len(article_href)
    for k in range (0,i):
                T.append(articles_titles[k])
                L.append(article_href[k])
        

    for k in range (0,i):
            Insertiondonnee.insert_une(('lemonde',""+T[k]+"","http://www.lemonde.fr"+L[k]+"",aujourdhui))

if __name__ == '__main__':
        print unes("http://www.lemonde.fr/")

