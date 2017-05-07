# -*- coding:utf-8 -*- 

import mysql.connector
import json
 
config = json.loads(open('config.txt', 'r').read())
 
cnx = mysql.connector.connect(** config)
 
cursor = cnx.cursor()

#quotidien = ("sudouest","http://www.sudouest.fr/")
#une = ('sudouest','penloppe chez les juges','http://www.sudouest.fr/2017/03/26/penelope-fillon-chez-les-juges-cette-semaine-ce-qu-elle-a-dit-aux-enqueteurs-3310528-4706.php','2017-01-01')

def insert_quotidien(quotidien):
    cursor.execute("""SELECT id, URL from quotidiens WHERE nom = %s""",(quotidien[0],))
    rows = cursor.fetchall()
    if not rows:
        cursor.execute("""INSERT INTO quotidiens (nom, URL) VALUES(%s, %s)""",quotidien)
    else:
        return True
        
def insert_une(une):
    cursor.execute("""SELECT id from unes WHERE titre = %s""",(une[1],))
    rows = cursor.fetchall()
    if not rows:
        cursor.execute("""SELECT id from quotidiens WHERE nom = %s""",(une[0],))
        n = cursor.fetchall()
        cursor.execute("""INSERT INTO unes (titre, URL, date, quotidien_id) VALUES(%s, %s, %s, %s)""",(une[1],une[2],une[3],(n[0])[0]))
    else:
       return True

def select_une(quotidien):
    cursor.execute("""SELECT id from quotidiens WHERE nom = %s""",(quotidien[0],))
    p = cursor.fetchall()
    cursor.execute("""SELECT titre, URL, date from unes WHERE quotidien_id = %s""",((p[0])[0],))
    a = cursor.fetchall()
    print a


if __name__ == '__main__':
    quotidien = ("sudouest","http://www.sudouest.fr/")
    insert_quotidien(quotidien)


    une = ('sudouest','penloppe chez les juges','http://www.sudouest.fr/2017/03/26/penelope-fillon-chez-les-juges-cette-semaine-ce-qu-elle-a-dit-aux-enqueteurs-3310528-4706.php','2017-01-01')
    insert_une(une)

    select_une(quotidien)
    
