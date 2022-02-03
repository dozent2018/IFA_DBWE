# write_file.py schreibt fünf Zeilen Text in eine Datei
zeilen_liste = ['Der Panther (von Robert Gernhard)',
          'Der Panther, der Panther',
          'Erst lag er, dann stand er'
          'worauf er so erschrak',
          'dass er gleich wieder lag' ]

with open('panther.txt', 'w') as datei_objekt :
    for zeile in zeilen_liste :
        datei_objekt.write(zeile + '\n')
