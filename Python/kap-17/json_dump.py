# json_dump.py demonstriert die Speicherung einer komplexen 
# Datenstruktur in einer Datei im JSON-Format
import json, pprint
students = {
1001: {'Studiengang': 'Chemie',
        'Name': 'Sommer',
        'Noten': {'Anorganik': 4, 'Organik': 5, 'Physik': 3},
        'Vorname': 'Susi'},
1002: {'Studiengang': 'Jura',
        'Name': 'Winter',
        'Noten': {'BWL': 5, 'Buchhaltung': 3, 'Statistik': 3, 'VWL': 4},
        'Vorname': 'Walter'},
1078: {' Studiengang ': 'Informatik', 'Name': 'Sommer', 'Vorname': 'Susi'}
}

with open('students.json', 'w') as out_file :
    json.dump(students, out_file)

    