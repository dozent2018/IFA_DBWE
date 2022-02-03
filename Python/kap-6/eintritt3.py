"""
eintritt_elif.py hat die gleiche Logik wie eintritt.py,
allerdings wird statt mit geschachtelten if- und else-
Anweisungen gearbeitet
"""

normalpreis = 20.0
faktor = 1.0

student = False

alter = int( input("Alter: "))

if alter > 17 and alter < 41 :
    antwort = input("Sind sie Student? (J/N)")
    if antwort == 'J' or antwort == 'j':
        student = True

if alter < 6:
    faktor = 0.0
elif alter < 18:
    faktor = 0.5
elif student == True:
    faktor = 0.75
elif alter < 65:
    faktor = 1.0
else:
    faktor = 0.75

print("Der Eintritt kostet:", normalpreis * faktor)