# pickle_load.py demonstriert das Laden einer komplexen 
# Datenstruktur aus einer pickle-Datei
import pickle, pprint

with open('students.pkl', 'rb') as in_file :
       students = pickle.load(in_file)

pprint.pprint(students)

