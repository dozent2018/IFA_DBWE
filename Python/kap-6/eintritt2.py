normalpreis = 20.0
alter = int( input("Alter: "))

if alter < 6:
    faktor = 0.0
elif alter < 18:
    faktor = 0.5
elif alter <= 65:
    faktor = 0.75
else:
    faktor = 1.0

print("Der Eintritt kostet:", normalpreis * faktor)

