# db_select1.py demonstriert einen einfachen SELECT mit Cursor
import mysql.connector
try:
    cnx = mysql.connector.connect(host="localhost",user="jochen",
           password="geheim",database="beispiele")
except mysql.connector.Error as err:
    print('ERROR:',err)

mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM standort")
myresult = mycursor.fetchall()
print(myresult)

for r in myresult:
  print(r)

cnx.close()

