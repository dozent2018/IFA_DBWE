""" argv.py demonstriert, wie die Kommandozeile beim 
Aufruf eines Programms ausgewertet werden kann"""
import sys
for wort in sys.argv :
    print(wort)
print(len(sys.argv), 'Argumente gelesen')

