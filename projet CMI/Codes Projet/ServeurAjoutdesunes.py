#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request


import InsertionCourrierInternational
import InsertionLePoint
import InsertionJournalduNet
import InsertionLesEchos
#import InsertionLeDauphine 
#import LaTribune 
import InsertionSudOuest
import InsertionLeFigaro
import InsertionLeParisien
#import  _20minutes 
import InsertionLeMonde
import InsertionOuestFrance  

app = Flask('Ajoutons')

@app.route('/')
def index():
	page_content = ''
	page_content += '<h2>Ajouter des journaux dans la base de donnée</h2>'
	page_content += '<form action="/ajouter" method="post">'
	#page_content += '</select>'
	page_content += '<input type="submit" value="Ajouter"></input>'
	page_content += '</form>'
	return page_content

@app.route('/ajouter', methods = ['POST'])
def quel_journal():
	InsertionLeParisien.unes('http://www.leparisien.fr/')
	InsertionLeFigaro.unes('http://www.lefigaro.fr/')
	InsertionLesEchos.unes('https://www.lesechos.fr/')
	InsertionLeMonde.unes('http://www.lemonde.fr/')
	InsertionLePoint.unes('http://www.lepoint.fr/')
	InsertionCourrierInternational.unes('http://www.courrierinternational.com/')
	InsertionJournalduNet.unes("http://www.journaldunet.com/")
	InsertionSudOuest.unes("http://www.sudouest.fr/")
	#InsertionLeDauphine.unes("http://www.ledauphine.com/")
	#InsertionOuestFrance.unes('http://www.ouest-france.fr/')
	return ("Les unes ont étés ajoutés avec succès !")



if __name__ == '__main__':
	app.run(debug=True)