# -*- coding:utf-8 -*-

import urllib, lxml.html, Insertiondonnee, time, datetime

def unes(targetURL):
        Insertiondonnee.insert_quotidien(('courrierinternational','http://www.courrierinternational.com/'))
        aujourdhui = datetime.date.today()
        T = []
        L = []
        file = urllib.urlopen(targetURL)
        data = file.read().decode('utf8')
        file.close()

        doc = lxml.html.document_fromstring(data)
        articles_href = doc.xpath('//main/div/a/@href')

        doc = lxml.html.document_fromstring(data)
        article_titles = doc.xpath('//main/div/a/article//h1/text()')

        

        i = len(articles_href)
        for k in range (0,i):
                T.append(article_titles[k])
                L.append(articles_href[k])
        

        for k in range (0,i):
                Insertiondonnee.insert_une(('courrierinternational',""+T[k]+"","http://www.courrierinternational.com"+L[k]+"",aujourdhui))

if __name__ == '__main__':
        print unes("http://www.courrierinternational.com/")
