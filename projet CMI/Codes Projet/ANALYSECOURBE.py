# -*- coding:utf-8 -*- 

import mysql.connector
import json
from datetime import date, timedelta


config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()

def mot(mot):
	today = date.today()
	y = date.today() - timedelta(1)
	y2 = date.today() - timedelta(2)
	y3 = date.today() - timedelta(3)
	y4 = date.today() - timedelta(4)
	y5 = date.today() - timedelta(5)
	y6 = date.today() - timedelta(6)
	y7 = date.today() - timedelta(7)
	y8 = date.today() - timedelta(8)
	y9 = date.today() - timedelta(9)
	y10 = date.today() - timedelta(10)
	y11 = date.today() - timedelta(11)
	y12 = date.today() - timedelta(12)
	y13 = date.today() - timedelta(13)
	y14 = date.today() - timedelta(14)
	y15 = date.today() - timedelta(15)
	y16 = date.today() - timedelta(16)
	y17 = date.today() - timedelta(17)
	y18 = date.today() - timedelta(18)
	y19 = date.today() - timedelta(19)
	y20 = date.today() - timedelta(20)
	y21 = date.today() - timedelta(21)
	y22 = date.today() - timedelta(22)
	y23 = date.today() - timedelta(23)
	y24 = date.today() - timedelta(24)
	y25 = date.today() - timedelta(25)
	y26 = date.today() - timedelta(26)
	y27 = date.today() - timedelta(27)
	y28 = date.today() - timedelta(28)
	y29 = date.today() - timedelta(29)
	y30 = date.today() - timedelta(30)
	mot = '%'+mot+'%'
	

	Tableau = []


	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,today))
	rows = cursor.fetchall()
	a = len(rows)
	Tableau.append(a)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y))
	rows = cursor.fetchall()
	b = len(rows)
	Tableau.append(b)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y2))
	rows = cursor.fetchall()
	c = len(rows)
	Tableau.append(c)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y3))
	rows = cursor.fetchall()
	d = len(rows)
	Tableau.append(d)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y4))
	rows = cursor.fetchall()
	e = len(rows)
	Tableau.append(e)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y5))
	rows = cursor.fetchall()
	f = len(rows)
	Tableau.append(f)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y6))
	rows = cursor.fetchall()
	g = len(rows)
	Tableau.append(g)


	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y7))
	rows = cursor.fetchall()
	h = len(rows)
	Tableau.append(h)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y8))
	rows = cursor.fetchall()
	i = len(rows)
	Tableau.append(i)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y9))
	rows = cursor.fetchall()
	j = len(rows)
	Tableau.append(j)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y10))
	rows = cursor.fetchall()
	k = len(rows)
	Tableau.append(k)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y11))
	rows = cursor.fetchall()
	l = len(rows)
	Tableau.append(l)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y12))
	rows = cursor.fetchall()
	m = len(rows)
	Tableau.append(m)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y13))
	rows = cursor.fetchall()
	n = len(rows)
	Tableau.append(n)


	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y14))
	rows = cursor.fetchall()
	o = len(rows)
	Tableau.append(o)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y15))
	rows = cursor.fetchall()
	p = len(rows)
	Tableau.append(p)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y16))
	rows = cursor.fetchall()
	q = len(rows)
	Tableau.append(q)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y17))
	rows = cursor.fetchall()
	r = len(rows)
	Tableau.append(r)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y18))
	rows = cursor.fetchall()
	s = len(rows)
	Tableau.append(s)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y19))
	rows = cursor.fetchall()
	t = len(rows)
	Tableau.append(t)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y20))
	rows = cursor.fetchall()
	u = len(rows)
	Tableau.append(u)


	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y21))
	rows = cursor.fetchall()
	v = len(rows)
	Tableau.append(v)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y22))
	rows = cursor.fetchall()
	w = len(rows)
	Tableau.append(w)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y23))
	rows = cursor.fetchall()
	x = len(rows)
	Tableau.append(x)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y24))
	rows = cursor.fetchall()
	y = len(rows)
	Tableau.append(y)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y25))
	rows = cursor.fetchall()
	z = len(rows)
	Tableau.append(z)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y26))
	rows = cursor.fetchall()
	A = len(rows)
	Tableau.append(A)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y27))
	rows = cursor.fetchall()
	B = len(rows)
	Tableau.append(B)


	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y28))
	rows = cursor.fetchall()
	C = len(rows)
	Tableau.append(C)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y29))
	rows = cursor.fetchall()
	D = len(rows)
	Tableau.append(D)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,y30))
	rows = cursor.fetchall()
	E = len(rows)
	Tableau.append(E)

	# Cherche le maximum
	k = len(Tableau)
	m = 0
	for i in range(k):
		if Tableau[i] > m:
			m = Tableau[i]

	# Convertis les valeur pour le svg

	if m != 0:
		for i in range(k):
			Tableau[i] = (abs(Tableau[i]-m)*400)/m
	else:
		for i in range(k):
			Tableau[i] = 400 # 400 est la valeur 0 sur le graphique svg

	Tableau.append(m)

	return Tableau
	#return m

if __name__ == '__main__':
	print mot('')

