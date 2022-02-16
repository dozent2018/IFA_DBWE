# pickle_mod.py demonstriert das Laden einer komplexen 
# Datenstruktur aus einer pickle-Datei, die Modifikation
# des Objekts und das erneute Sichern
import pickle, pprint

with open('students.pkl', 'rb') as in_file :
       students = pickle.load(in_file)

students[1078]['Vorname'] = 'Susanne'
students[1078]['Noten'] = { 'Mathematik' : 3, 'Python' : 4, 'Datenbanken' : 4 }
pprint.pprint(students)

with open('students.pkl', 'wb') as out_file :
       pickle.dump(students, out_file)


