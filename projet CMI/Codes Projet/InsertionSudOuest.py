#-*- coding:utf-8 -*-
 
import urllib, lxml.html, Insertiondonnee, time, datetime
 
# targetURL = 'http://www.sudouest.fr/'
# passe en parametre depuis le script de la requete
 
def unes(targetURL):
        aujourdhui = datetime.date.today()
        T = []
        L = []
        file = urllib.urlopen(targetURL)
        data = file.read().decode('utf8')
        file.close()
 
        doc = lxml.html.document_fromstring(data)
        articles_href = doc.xpath('//section[@class="articles essentiel "]//div[@class="article-wrapper"]/a/@href') + doc.xpath('//section[@class="articles default "]//div[@class="article-wrapper"]/a/@href')
		#L.append(articles_href)
 
        doc = lxml.html.document_fromstring(data)
        article_titles = doc.xpath('//section[@class="articles essentiel "]//div[@class="article-wrapper"]/a/h2/text()') + doc.xpath('//section[@class="articles default "]//div[@class="article-wrapper"]/a/h2/text()')
        i = len(articles_href)
        for k in range (0,i):
                T.append(article_titles[k])
                L.append(articles_href[k])
        

        for k in range (0,i):
                Insertiondonnee.insert_une(('sudouest',""+T[k]+"","http://www.sudouest.fr"+L[k]+"",aujourdhui))

        	#T.append(articles_titles)
        #for i in range(0,len(articles_href)):
                #T = [article_titles[i],articles_href[i]]
        #for k in range(0,i):
                #print "'"+ T[k]+ "'"
        
        
        

if __name__ == '__main__':
        print unes("http://www.sudouest.fr/")
	
