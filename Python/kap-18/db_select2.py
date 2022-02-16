# db_select2.py demonstriert die Verwendung von Platzhaltern
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='jochen',
                                password='geheim',
                                host='127.0.0.1',
                                database='beispiele')
cursor = cnx.cursor()
query = ("SELECT titel, beginn, ende FROM lehrveranstaltung "
         "WHERE beginn BETWEEN %s AND %s")
beginn_datum = datetime.datetime(2020, 1, 1, 0, 0, 0)
ende_datum = datetime.datetime(2020, 12, 31, 23, 59, 59)
cursor.execute(query, (beginn_datum, ende_datum))

for (titel, beginn, ende) in cursor:
  print("{}, beginnt {:%d.%m.%Y %H.%M}, "
        "endet {:%d.%m.%Y %H:%M}".format(titel, beginn, ende))

cursor.close()
cnx.close()

