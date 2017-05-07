# -*- coding:utf-8 -*-
 
import urllib, lxml.html, Insertiondonnee, time, datetime

def unes(targetURL):
    aujourdhui = datetime.date.today()
    Insertiondonnee.insert_quotidien(('ledauphine','http://www.ledauphine.com/'))
    T = []
    L = []
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    titres=doc.xpath("//a[@class='titre']/text()")
    liens=doc.xpath("//a[@class='titre']/@href")

    i = len(titres)
    for k in range (0,i):
            T.append(titres[k])
            L.append(liens[k])

    
    for k in range (0,i):
        Insertiondonnee.insert_une(('ledauphine',""+T[k]+"",""+L[k]+"",aujourdhui))



if __name__ == '__main__':
        print unes("http://www.ledauphine.com/")
