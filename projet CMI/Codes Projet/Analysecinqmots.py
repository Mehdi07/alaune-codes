# -*- coding:utf-8 -*- 

import mysql.connector
import json
from datetime import date, timedelta

config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()


def mots(mot1,mot2,mot3,mot4,mot5):
	yesterday7 = date.today() - timedelta(7)

	A = []
	B = []
	C = []
	D = []
	E = []
	F = []

	m1 = 0
	m2 = 0
	m3 = 0
	m4 = 0
	m5 = 0

	cursor.execute("""SELECT titre from unes WHERE date > %s""",(yesterday7,))
	rows = cursor.fetchall()
	for i in rows:
		A.append((i)[0])
	for i in A:
		i.split()
		for k in i.split():
			B.append(k)
	for i in B:
		i.split(",")
		for k in i.split(","):
			C.append(k)
	C.remove('')
	i = len(C)
	for k in range(i):
		C[k] = C[k].capitalize()

	for i in C:
   		if i == mot1:
   			m1 = m1 + 1
   		elif i == mot2:
			m2 = m2 + 1
		elif i == mot3:
			m3 = m3 +1
		elif i == mot4:
			m4 = m4 +1
		elif i == mot5:
			m5 = m5 +1

	return m1,m2,m3,m4,m5
	#return C

if __name__ == '__main__':
	print cinqmots(mot1,mot2,mot3,mot4,mot5)
