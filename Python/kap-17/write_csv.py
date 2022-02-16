# write_csv.py schreibt eine CSV-Datei, die in Microsoft Excel importiert
# werden kann

import csv

zeilen = [ ['Zeile 1 Spalte A', 'Zeile 1 Spalte B', 'Zeile 1 Spalte C'],
           ['Zeile 2 Spalte A', 'Zeile 2 Spalte B', 'Zeile 2 Spalte C'],
           ['Zeile 3 Spalte A', '', 'Zeile 3 Spalte C'] ]

with open( 'spam.csv', 'w', encoding = 'utf-8-sig' ) as out_file :
    writer_obj = csv.writer(out_file, dialect = 'excel', delimiter = ';')
    for zeile in zeilen:
        writer_obj.writerow(zeile)
 
