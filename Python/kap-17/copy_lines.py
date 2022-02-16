""" copy_lines.py liest eine Textdatei zeilenweise und gibt jede
    gelesene Zeile in eine zweite Textdatei aus """

zaehler = 0

in_dname = input("Name der Eingabdedatei: ")
out_dname = input("Name der Ausgabedatei: ")


with open(in_dname, 'r') as in_file, open(out_dname, 'w') as out_file :
    for zeile in in_file:
        zaehler += 1
        out_file.write( zeile.rstrip() + '\n' )


print(zaehler, 'Zeilen in', out_dname, 'geschrieben.')
