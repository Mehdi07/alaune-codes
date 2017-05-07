#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, lxml.html, Insertiondonnee, time, datetime

def unes(targetURL):
    aujourdhui = datetime.date.today()
    Insertiondonnee.insert_quotidien(('ouestfrance','http://www.ouest-france.fr/'))
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    T = []
    L = []
    
    doc = lxml.html.document_fromstring(data)
    article_href = doc.xpath('//article[@data-vr-contentbox]/a/@href')
    
    doc=lxml.html.document_fromstring(data)
    articles_titles = doc.xpath('//article[@data-vr-contentbox]//h2[@class="title "]/text()')

    i = len(article_href)
    k = len(articles_titles)
    #for k in range (i):
                #T.append(articles_titles[k])
                #L.append(article_href[k])
    return i,k
        

    #for k in range (0,i):
            #Insertiondonnee.insert_une(('ouestfrance',""+T[k]+"","http://www.ouest-france.fr/"+L[k]+"",aujourdhui))

if __name__ == '__main__':
        print unes("http://www.ouest-france.fr/")