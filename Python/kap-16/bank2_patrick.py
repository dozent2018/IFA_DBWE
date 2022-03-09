###################################################
################ © Patrick Knuchel ################
#################### 28.02.2022 ###################
###################################################

# Klasse für OS Funktionen
import os
# Terminal leeren
os.system('cls||clear')

# Klasse für farbe importieren
from color import color

# Definition Klasse Kunde
class Kunde:
    zaehler = 0

    # Initialisierung Klasse mit Werten Name und Nr
    def __init__(self, name, nr):
        self.name = name
        self.kunde_nr = nr
        self.__konten = []

    # Decorator für Name
    @property
    def name(self):
        return self.__name

    # Methode für Name
    @name.setter
    def name(self, name):
        self.__name = name

    # Decorator für KundenNummer
    @property
    def kunde_nr(self):
        return self.__kunde_nr

    # Methode für Kundennummer
    @kunde_nr.setter
    def kunde_nr(self, nr):
        self.__kunde_nr = nr
    
    # Decorator für Konten
    @property
    def konten(self):
        return self.__konten

    # Funktion add_konto definieren
    def add_konto(self, konto):
        self.konten.append(konto)
        # Kontonummer = Kundennummer / Wenn Konto bereits vorhanden = Nummer +1
        if Kunde.zaehler == 1:
            konto.konto_nr = self.__kunde_nr + Kunde.zaehler
        else:
            ktnr = self.__kunde_nr
            konto.konto_nr = self.__kunde_nr
            Kunde.zaehler += 1

    # Funktion close_konto definieren
    def close_konto(self,konto):
        self.konten.remove(konto)

# Definition Klasse Konto
class Konto:
    # Initialisierung Klasse mit Werten Nr, Kunde, Saldo und Limit
    def __init__(self, kunde, art, saldo, limit):
        self.konto_nr = 0
        self.__kunde = kunde
        self.__art = art
        self.__saldo = saldo
        self.__limit = limit
        self.__bewegungen = []
    
    # Decorator für Kunde
    @property
    def kunde(self):
        return self.__kunde

    # Methode für Kunde
    @kunde.setter
    def name(self, kunde):
        self.__kunde = kunde
    
    # Decorator für Art
    @property
    def art(self):
        return self.__art

    # Methode für Kunde
    @art.setter
    def name(self, art):
        self.__art = art
    
    # Decorator für Saldo
    @property
    def saldo(self):
        return self.__saldo

    # Methode für Saldo
    @saldo.setter
    def name(self, saldo):
        self.__saldo = saldo
    
    # Decorator für Limit
    @property
    def limit(self):
        return self.__limit

    # Methode für Limit
    @limit.setter
    def name(self, limit):
        self.__limit = limit
    
    # Decorator für Bewegungen
    @property
    def bewegungen(self):
        return self.__bewegungen
    
    # Funktion einzahlen definieren
    def einzahlen(self, bewegung):
        self.__saldo = self.__saldo + bewegung.betrag
        self.bewegungen.append(bewegung)
    
    # Funktion auszahlen definieren
    def auszahlen(self, bewegung):
        # Prüfen ob Saldo nach Auszhalung < als Limit
        if (self.__limit < ( (self.__saldo + bewegung.betrag) *-1)):
            print(color.RED + "Limit ausgeschöpft" + color.END)
        else:
            # Betrag auszahlen und Bewegung hinzufügen
            self.__saldo = self.__saldo + bewegung.betrag
            self.bewegungen.append(bewegung)
    
    # Definition Funktion Kontoauszug
    def vermoegensausweis(self,kunde):
        self.__kunde = kunde
        
        print(color.BOLD + color.GREEN + "Vermögensausweis" + color.END)
        print(color.BOLD + 'Kunde:' + color.END, kunde.name, color.BOLD + 'Kundennummer'.rjust(17,' ') + color.END, kunde.kunde_nr)
        
        # Alle Konten und dazugehörigen Bewegungen ausgeben
        for konto in kunde.konten:
            print(color.BOLD + 'Kontonummer:'.rjust(10,' ') + color.END, konto.konto_nr, color.BOLD + 'Kontoart:'.rjust(14,' ') + color.END, konto.art, color.BOLD + 'Saldo:'.rjust(10,' ') + color.END, konto.saldo, color.BOLD + 'Limit:'.rjust(15,' ') + color.END, konto.limit)
            print()
            print(color.BOLD + "Datum".ljust(10,' '),"Bewegung".rjust(10,' '),"Zweck".ljust(20,' ') + color.END)
            for bewegung in konto.bewegungen:
                print(bewegung.datum.rjust(10,' '), str(bewegung.betrag).rjust(10,' '), str(bewegung.zweck).ljust(20,' '))
    
    # Definition Funktion Kontoauszug
    def kontoauszug(self,kunde):
        self.__kunde = kunde
        print(color.BOLD + color.GREEN + "Kontoauszug" + color.END)
        print(color.BOLD + 'Kontonummer:'.rjust(10,' ') + color.END, self.konto_nr, color.BOLD + 'Kontoart:'.rjust(10,' ') + color.END, self.art, color.BOLD + 'Saldo:'.rjust(10,' ') + color.END, self.saldo, color.BOLD + 'Limit:'.rjust(15,' ') + color.END, self.limit)
        print()
        # Alle Bewegungen des Kontos ausgeben
        for bewegung in self.bewegungen:
            print(bewegung.datum.rjust(10,' '), str(bewegung.betrag).rjust(10,' '), str(bewegung.zweck).ljust(20,' '))

    
    # Definition Funktion Kontobewegung
    def kontobewegung(self,konto):
        print(color.BOLD + color.BLUE + "Kontobewegungen" + color.END)
        print(color.BOLD + "Datum".ljust(10,' '),"Bewegung".rjust(10,' '),"Zweck".ljust(20,' ') + color.END)
        # Alle Bewegungen des Kontos ausgeben
        for bewegung in konto.bewegungen:
                print(bewegung.datum.rjust(10,' '), str(bewegung.betrag).rjust(10,' '), str(bewegung.zweck).ljust(20,' '))

# Definition Klasse Bewegung
class Bewegung:
    # Initialisierung Klasse mit Werten Betrag und Datum
    def __init__(self, betrag, zweck, datum):
        self.__betrag = betrag
        self.__zweck = zweck
        self.__datum = datum
    
    # Decorator für Betrag
    @property
    def betrag(self):
        return self.__betrag

    # Methode für Betrag
    @betrag.setter
    def name(self, betrag):
        self.__betrag = betrag
    
    # Decorator für Zweck
    @property
    def zweck(self):
        return self.__zweck

    # Methode für Zweck
    @zweck.setter
    def name(self, zweck):
        self.__zweck = zweck
    
    # Decorator für Datum
    @property
    def datum(self):
        return self.__datum

    # Methode für Datum
    @datum.setter
    def name(self, datum):
        self.__datum = datum

if __name__ == '__main__':
    ## Testdaten ##
    kunde1 = Kunde('Ruth Reich',2000)
    konto1 = Konto('kunde1','Sparkonto',0, 1000)
    kunde1.add_konto(konto1)
    konto2 = Konto('kunde1','Lohnkonto',0, 12000)
    kunde1.add_konto(konto2)
    bewegung1 = Bewegung(100,'Für Steuern','01-01-2021')
    konto1.einzahlen(bewegung1)
    bewegung2 = Bewegung(-200,'Für Ferien','01-01-2021')
    konto1.auszahlen(bewegung2)
    bewegung3 = Bewegung(-300,'Lohnzahlung','01-01-2022')
    konto2.auszahlen(bewegung3)
    bewegung4 = Bewegung(-400,'Spesen','01-01-2022')
    konto2.auszahlen(bewegung4)
    print()
    konto1.vermoegensausweis(kunde1)
    print()
    print("------------------------------------------")
    konto1.kontobewegung(konto1)
    print()
    konto2.kontobewegung(konto2)
    print()
    print("------------------------------------------")
    konto1.kontoauszug(konto1)