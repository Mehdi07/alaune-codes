# -*- coding:utf-8 -*-
     
import urllib, lxml.html
     
def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    titres=doc.xpath("//a[@class='titre']/text()")
    liens=doc.xpath("//a[@class='titre']/@href")
   
    return zip(titres, liens)
