# beipack.py gibt aus, in welchen Sprachen der Beipackzettel für ein
# bestimmtes Land vorhanden sein muss

# Ein Dictionary mit Strings als Schlüssel und Tupeln als Werte
# Achtung: Tupel mit nur einem Element müssen ein Komma enthalten!
landessprachen = {
    'D' : ('Deutsch',),
    'A' : ('Deutsch',),
    'F' : ('Französisch',),
    'B' : ('Französisch', 'Flämisch'),
    'I' : ('Ialienisch',),
    'L' : ('Deutsch', 'Französisch'),
    'CH' : ('Deutsch', 'Französisch','Italienisch', 'Rumantsch')
}

land = input('Welches Land? ')
for sprache in landessprachen[land] :
    print(sprache)