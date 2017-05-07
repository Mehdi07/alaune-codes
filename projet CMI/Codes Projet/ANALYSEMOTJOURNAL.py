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

def fonction(mot1,mot2,mot3,mot4,mot5,journal):
	mot1 = '%'+mot1+'%'
	mot2 = '%'+mot2+'%'
	mot3 = '%'+mot3+'%'
	mot4 = '%'+mot4+'%'
	mot5 = '%'+mot5+'%'
	quotidien = journal

	cursor.execute("""SELECT titre from unes INNER JOIN quotidiens ON unes.quotidien_id = quotidiens.id WHERE titre like %s AND date > %s AND quotidiens.nom = %s """,(mot1,day,quotidien))
	rows = cursor.fetchall()
	a = len(rows)

	cursor.execute("""SELECT titre from unes INNER JOIN quotidiens ON unes.quotidien_id = quotidiens.id WHERE titre like %s AND date > %s AND quotidiens.nom = %s """,(mot2,day,quotidien))
	rows = cursor.fetchall()
	b = len(rows)

	cursor.execute("""SELECT titre from unes INNER JOIN quotidiens ON unes.quotidien_id = quotidiens.id WHERE titre like %s AND date > %s AND quotidiens.nom = %s """,(mot3,day,quotidien))
	rows = cursor.fetchall()
	c = len(rows)

	cursor.execute("""SELECT titre from unes INNER JOIN quotidiens ON unes.quotidien_id = quotidiens.id WHERE titre like %s AND date > %s AND quotidiens.nom = %s """,(mot4,day,quotidien))
	rows = cursor.fetchall()
	d = len(rows)

	cursor.execute("""SELECT titre from unes INNER JOIN quotidiens ON unes.quotidien_id = quotidiens.id WHERE titre like %s AND date > %s AND quotidiens.nom = %s """,(mot5,day,quotidien))
	rows = cursor.fetchall()
	e = len(rows)

	return a,b,c,d,e,quotidien


if __name__ == '__main__':
	print fonction('Macron','fillon','le pen','hamon','victoire','sudouest')