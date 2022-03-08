# bank2b.py ist ein Lösungsvorschlag für Aufgabe 2 in Kap 16.12
# Die Instanzvariablen von Konto sind jetzt privat

class Kunde:
    def __init__(self, name, nr):
        self.name = name
        self.kunde_nr = nr
        self.__konten = []

    @property
    def name(self):
        return self.__name

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
        # alternativ, falls statt Properties
        # get_ und set_ methoden verwendet
        # werden:
        # self.set_konto_nr(nr)
        # self.set_konto_art(art)
        # self.set_saldo(saldo)

    def __str__(self):
        return '<class Konto> {}, {}, {}'.format(self.konto_nr, self.konto_art, self.saldo)

    @property
    def konto_nr(self):
        return self.__konto_nr
    # alternativ zu der Methode mit @property:
    # def get_konto_nr(self):
    #    return self.__konto_nr
    @konto_nr.setter
    def konto_nr(self,nr):
        self.__konto_nr = nr
    # alternativ zu der Methode mit @konto_nr.setter:
    # def set_konto_nr(self,nr):
    #    return self.__konto_nr = nr

    @property
    def konto_art(self):
        return self.__konto_art
    @konto_art.setter
    def konto_art(self,art):
        self.__konto_art = art

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,new_saldo):
        self.__saldo=new_saldo

if __name__ == '__main__':
    konto1 = Konto(10001,'Privatkonto', 100.00)
    konto2 = Konto(10002,'Sparkonto',5.00)
    kunde1 = Kunde('Ruth Reich',1000)
    kunde1.add_konto(konto1)
    kunde1.add_konto(konto2)

    print('Kunde:', kunde1.name, 'Kundennummer', kunde1.kunde_nr)
    for konto in kunde1.konten:
        print('Art:', konto.konto_art, 'Kontonummer:', konto.konto_nr, 'Saldo:', konto.saldo)


