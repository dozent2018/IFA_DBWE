# append.py demonstriert das Anhängen von Zeilen an eine bestehende Datei

import time

with open( 'out.txt', 'a') as out_file :
    out_file.write(time.strftime('Geschrieben am %d.%m.%y %H:%M\n'))

