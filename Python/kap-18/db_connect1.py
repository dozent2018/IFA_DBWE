import mysql.connector

cnx = mysql.connector.connect(user='jochen', password='geheim',
                              host='127.0.0.1',database='beispiele')
cnx.close()

