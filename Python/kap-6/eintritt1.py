"""
eintritt1.py demonstriert das Verschachteln mehrerer if und
else Bedingungen. Nach jedem Doppelpunkt beginnt eine neue Suite,
die um vier Leerzeichen weiter eingerückt werden muss
"""
normalpreis = 20.0
alter = int( input("Alter: "))

if alter < 6:
    faktor = 0.0
else:
    if alter < 18:
        faktor = 0.5
    else:
        if alter >= 65:
            faktor = 0.75
        else:
            faktor = 1.0

print("Der Eintritt kostet:", normalpreis * faktor)

