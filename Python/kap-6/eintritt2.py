normalpreis = 20.0
faktor = 1.0
alter = int( input("Alter: "))

if alter < 6:
    faktor = 0.0
elif alter < 18:
    faktor = 0.5
elif alter < 65:
    faktor = 1.0
else:
    faktor = 0.75

print("Der Eintritt kostet:", normalpreis * faktor)