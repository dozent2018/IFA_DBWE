""" copy_lines.py liest eine Textdatei mit dem Namen in .txt 
    zeilenweise und gibt jede gelesene Zeile auf den Bildschirm aus """

with open('panther.txt', 'r') as datei_objekt :
    for zeile in datei_objekt:
        print( zeile.rstrip() )

        
