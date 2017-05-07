#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mysql.connector
import json
from datetime import date, timedelta
import operator

config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()

day = date.today() - timedelta(7)

def fonction(mot1,mot2,mot3,mot4,mot5):
	mot1 = '%'+mot1+'%'
	mot2 = '%'+mot2+'%'
	mot3 = '%'+mot3+'%'
	mot4 = '%'+mot4+'%'
	mot5 = '%'+mot5+'%'

	cursor.execute("""SELECT titre from unes  WHERE titre like %s AND date > %s """,(mot1,day))
	rows = cursor.fetchall()
	a = len(rows)

	cursor.execute("""SELECT titre from unes  WHERE titre like %s AND date > %s """,(mot2,day))
	rows = cursor.fetchall()
	b = len(rows)

	cursor.execute("""SELECT titre from unes  WHERE titre like %s AND date > %s """,(mot3,day))
	rows = cursor.fetchall()
	c = len(rows)

	cursor.execute("""SELECT titre from unes  WHERE titre like %s AND date > %s """,(mot4,day))
	rows = cursor.fetchall()
	d = len(rows)

	cursor.execute("""SELECT titre from unes  WHERE titre like %s AND date > %s """,(mot5,day))
	rows = cursor.fetchall()
	e = len(rows)

	return a,b,c,d,e


if __name__ == '__main__':
	print fonction('Macron','fillon','le pen','hamon','victoire')

