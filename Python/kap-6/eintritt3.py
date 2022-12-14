"""
eintritt3.py demonstriert die Verknüpfung von
zwei Bedingungen mit and
"""

normalpreis = 20.0
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
elif alter <= 65:
    faktor = 0.75
else:
    faktor = 1.0

print("Der Eintritt kostet:", normalpreis * faktor)