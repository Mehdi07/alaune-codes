#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mysql.connector
import json
from datetime import date, timedelta
import operator

def worlds2(quotidien):
	journal = quotidien
	mots_inutiles = ['Sous','D2','Mais','Font','Faut','Ces','Vos','Aux','A','Pas','Par','En','Une',"De",'Ou','Les','Sans','Des','Sur','A','Le','La','Se','Son','et','Est','Que','Qui','Ce','',':','?','Du','Un','Le','Au','Dans','Pour','Plus','Les','Sa','Ne','La','Avec','Il','Ses','-','aux','Ce','fait','1','Ans','Un','Va','Sont','!','Deux','EN','Et','On','Ont']
	Z = []
	A = []
	W = []
	X = []
	C = []

	M = []

	config = json.loads(open('config.txt', 'r').read())
 
	cnx = mysql.connector.connect(** config)
 
	cursor = cnx.cursor()

	day = date.today() - timedelta(2)

	cursor.execute("""SELECT titre from unes INNER JOIN quotidiens ON quotidiens.id = unes.quotidien_id WHERE quotidiens.nom = %s AND date >= %s """,(journal,day))
	rows = cursor.fetchall()
	for i in rows:
		Z.append(i[0])
	for k in Z:
		k.split()
		for q in k.split():
			W.append(q)
	for i in W:
		i.split(",")
		for k in i.split(","):
			C.append(k)
	a = len(C)
	for i in range(a):
		C[i] = C[i].capitalize()

	
	nouveaux_mots = {}
	for c in C:
		nouveaux_mots[c] = nouveaux_mots.get(c,0) + 1

	for i in mots_inutiles:
		for cle in nouveaux_mots.keys():
			if i == cle:
				del nouveaux_mots[i]

	mots_inutiles2 = [u'\xe0',u'\u2013',u'\xab',u'\xc0',u'\xbb',u'Apr\xe8s']			
	
	for i in mots_inutiles2:
		for cle in nouveaux_mots.keys():
			if i == cle:
				del nouveaux_mots[i]

	dico_trie = sorted(nouveaux_mots.iteritems(), reverse=True, key=operator.itemgetter(1))
	
	dico_trie2 = []
	for i in range(20):
		dico_trie2.append(dico_trie[i])

#for i in dico_trie2:
    #print 
	return dico_trie2


if __name__ == '__main__':
	print worlds2('lefigaro')
