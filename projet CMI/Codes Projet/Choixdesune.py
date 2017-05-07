# -*- coding:utf-8 -*- 

import mysql.connector
import json
from datetime import date, timedelta


config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()


def phrase(phrase):
	A=[]
	B =[]
	yesterday3 = date.today() - timedelta(2)
	phrase = '%'+phrase+'%'
	cursor.execute("""SELECT titre, URL from unes WHERE titre like %s AND date > %s """,(phrase,yesterday3))
	rows = cursor.fetchall()
	i = len(rows)
	for k in range(i):
		A.append(rows[k][0])
		B.append(rows[k][1])
	return A,B

if __name__ == '__main__':
	print phrase("Fillon")
