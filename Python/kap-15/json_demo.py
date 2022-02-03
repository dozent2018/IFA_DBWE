# json_load.py Demonstriert das Einlesen von JSON-Daten
# aus einer Textdatei
import json, pprint

with open('MontyPython.json', 'r') as json_file :
    python_data = json.load(json_file)

pprint.pprint(python_data)
print()
print(python_data['Pythons'][1]['name'])
print(python_data['Pythons'][1]['born'])
    

