# -*- coding:utf-8 -*- 

import mysql.connector
import json

config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()

def acceuilunes():
	A =[]
	B =[]
	cursor.execute("""SELECT titre, URL from unes ORDER BY id DESC LIMIT 0,5""")
	rows = cursor.fetchall()
	i = len(rows)
	for k in range(i):
		A.append(rows[k][0])
		B.append(rows[k][1])
	return A,B

if __name__ == '__main__':
	print acceuilunes()

