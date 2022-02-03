# oldschool.py demonstriert den Umgang mit Dateien ohne with

in_dname = input("Name der Eingabdedatei: ")
out_dname = input("Name der Ausgabedatei: ")

in_file = open(in_dname, 'r')
out_file = open(out_dname, 'w')
for zeile in in_file:
    out_file.write( zeile.rstrip() )

# Die Dateien sollten nach Benutzung geschlossen werden
in_file.close()
out_file.close()

