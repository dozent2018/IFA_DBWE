# ist_zahl3.py nutzt str.isdecimal() um zu prüfen, ob
# ein String nur Zahlen enthält
ist_zahl = False

while ist_zahl == False:
    antwort = input('Geben Sie eine ganze Zahl ein: ')
    if antwort.isdecimal() :
        ist_zahl = True
        zahl = int(antwort)
        print('Die Zahl ist ', zahl)
    else:
        print('Ihre Eingabe ist keine ganze Zahl')
