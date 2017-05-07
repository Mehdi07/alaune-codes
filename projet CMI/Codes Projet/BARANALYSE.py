# -*- coding:utf-8 -*- 

import mysql.connector
import json
from datetime import date, timedelta


config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()

def mot(mot):
	today = date.today()
	yesterday = date.today() - timedelta(1)
	yesterday2 = date.today() - timedelta(2)
	yesterday3 = date.today() - timedelta(3)
	yesterday4 = date.today() - timedelta(4)
	yesterday5 = date.today() - timedelta(5)
	yesterday6 = date.today() - timedelta(6)
	mot = '%'+mot+'%'

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,today))
	rows = cursor.fetchall()
	a = len(rows)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,yesterday))
	rows = cursor.fetchall()
	b = len(rows)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,yesterday2))
	rows = cursor.fetchall()
	c = len(rows)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,yesterday3))
	rows = cursor.fetchall()
	d = len(rows)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,yesterday4))
	rows = cursor.fetchall()
	e = len(rows)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,yesterday5))
	rows = cursor.fetchall()
	f = len(rows)

	cursor.execute("""SELECT titre from unes WHERE titre like %s AND  date = %s """,(mot,yesterday6))
	rows = cursor.fetchall()
	g = len(rows)

	

  	return a,b,c,d,e,f,g


if __name__ == '__main__':
	print mot('Macron')