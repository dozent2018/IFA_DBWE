""" copy_lines_try.py liest eine Textdatei zeilenweise und gibt jede
    gelesene Zeile in eine zweite Textdatei aus 
    zusätzlich werden Ausnahmen bei open() abgefangen """

zaehler = 0

in_dname = input("Name der Eingabdedatei: ")
out_dname = input("Name der Ausgabedatei: ")


try:
    with open(in_dname, 'r') as in_file, open(out_dname, 'w') as out_file :
        for zeile in in_file:
            zaehler += 1
            out_file.write( zeile.rstrip() + '\n' )
except FileNotFoundError :
    print('Fehler:', in_dname, 'oder', out_dname, 'nicht gefunden')
except PermissionError :
    print('Fehler:', in_dname, 'oder', out_dname, '- keine Berechtigung')
else:
    print(zaehler, 'Zeilen in', out_dname, 'geschrieben.')
