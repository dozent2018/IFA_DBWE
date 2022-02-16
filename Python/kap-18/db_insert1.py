# db_insert.py demonstriert INSERT-Anweisungen mit Platzhalter
import mysql.connector

cnx = mysql.connector.connect(user='jochen', password='geheim', database='beispiele')
cursor = cnx.cursor()
add_address_sql = "INSERT INTO adresse (strasse, nr, plz, ort) VALUES (%s, %s, %s, %s)"
add_student_sql = "INSERT INTO student (name, email, klasse, adresse) VALUES (%s, %s, %s, %s)"
data_address = ('Saumstrasse', '27', '8003', 'Zürich')
# Die Adresse einfügen
cursor.execute(add_address_sql, data_address)
""" Die neue adr_id, die mit AUTO_INCREMENT von MySQL vergeben wurde
wird für das Einfügen in student gebraucht"""
new_adr_id = cursor.lastrowid
# Daten Studentin
data_student = ('Sara Seidel','sara.seidel@schule.ch', 7, new_adr_id)
cursor.execute(add_student_sql, data_student)
# Sicherstellen, das COMMIT erfolgt
cnx.commit()
cursor.close()
cnx.close()

