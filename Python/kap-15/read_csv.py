# read_csv.py liest eine aus Microsoft Excel exportierte CSV-Datei

import csv

with open( 'Adressen.csv', 'r', encoding = 'utf-8-sig' ) as in_file :
    reader_obj = csv.reader(in_file, dialect = 'excel', delimiter = ';')
    for zeile in reader_obj:
        print(zeile)
 
