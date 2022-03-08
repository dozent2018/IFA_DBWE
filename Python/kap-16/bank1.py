# bank1.py implementiert eine 1. Version der Klassen Kunde und Konto

class Kunde:
    def __init__(self, name, nr):
        self.name = name
        self.kunde_nr = nr
        self.__konten = []

    # Der Ersatz für eine get_name Methode
    # Die Variable __name wird als 'name' zur Verfügung gestellt
    @property
    def name(self):
        return self.__name

    # Der Ersatz für eine set_name Methode
    # Die Variable __name kann nun mit name = Wert gesetzt werden
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kunde_nr(self):
        return self.__kunde_nr

    @kunde_nr.setter
    def kunde_nr(self, nr):
        self.__kunde_nr = nr

    @property
    def konten(self):
        return self.__konten

    def add_konto(self, konto):
        self.konten.append(konto)

class Konto:
    def __init__(self, nr, art, saldo):
        self.konto_nr = nr
        self.konto_art = art
        self.saldo = saldo

if __name__ == '__main__':
    konto1 = Konto(10001,'Privatkonto', 100.00)
    konto2 = Konto(10002,'Sparkonto',5.00)
    kunde1 = Kunde('Ruth Reich',1000)
    kunde1.add_konto(konto1)
    kunde1.add_konto(konto2)

    print('Kunde:', kunde1.name, 'Kundennummer', kunde1.kunde_nr)
    for konto in kunde1.konten:
        print('Art:', konto.konto_art, 'Kontonummer:', konto.konto_nr, 'Saldo:', konto.saldo)

