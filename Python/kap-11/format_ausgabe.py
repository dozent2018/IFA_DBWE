eingabe = input('Eingabe der Nettopreise, durch Leerzeichen getrennt: ')
eingaben_liste = eingabe.split()
steuersatz = float(input("steuersatz in %: "))
print("{0:>15s} {1:>15s}".format('Netto', 'Brutto'))
for eingabe in eingaben_liste :
    nettopreis = float(eingabe)
    bruttopreis = nettopreis + nettopreis / 100 * steuersatz
    print("{0:15.2f} {1:>15.2f}".format(nettopreis, bruttopreis))
