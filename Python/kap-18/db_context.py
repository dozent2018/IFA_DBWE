# db_context.py demonstriert einen Context Manager für MySQL
from datetime import datetime
import mysql.connector

class UseDB:
    def __init__(self, connection_data):
        self.configuration = connection_data

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    connection_data = {'host':'localhost',
                    'user':'jochen',
                    'passwd':'geheim',
                    'database':'beispiele'}

    query_str = """SELECT titel, beginn, ende FROM lehrveranstaltung
    WHERE beginn BETWEEN %s AND %s """
    beginn = datetime.strptime('2020-01-01','%Y-%m-%d')
    ende = datetime.strptime('2021-01-01','%Y-%m-%d')

    with UseDB(connection_data) as cursor:
        cursor.execute(query_str, (beginn,ende))
        result =  cursor.fetchall()

    for (titel, beginn, ende) in result:
        print("{}, beginnt {:%d.%m.%Y %H.%M}, "
        "endet {:%d.%m.%Y %H:%M}".format(titel, beginn, ende))





