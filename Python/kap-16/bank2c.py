# bank2c.py ist ein Lösungsvorschlag für Aufgabe 2c in Kap 16.12
# Die Instanzvariablen von Konto sind jetzt privat
# Die Methode Konto.add_konto() legt jetzt automatisch ein Konto an
# Der Kunde wird jetzt auch beim Konto gespeichert

class Kunde:
    def __init__(self, name, nr):
        self.name = name
        self.kunde_nr = nr
        self.__konten = []

    def __str__(self):
        return '<class Kunde> {}, {}, {}'.format(self.name, self.kunde_nr, self.konten)

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

    def add_konto(self, art='undefiniert', saldo=0.0):
        if len(self.konten) == 0:
            # es gibt noch kein Konto
            new_nr = self.kunde_nr + 1
        else:
            # es gibt schon Konten. Die neue nr soll
            # gleich der bisher höchsten nr + 1 sein
            new_nr = max([k.konto_nr for k in kunde1.konten]) + 1
            # Statt list comprehension wäre auch For-Schleife möglich
        new_konto = Konto(nr=new_nr, kunde=self, art=art, saldo=saldo)
        self.konten.append( new_konto )

class Konto:
    def __init__(self, nr, kunde, art='', saldo=0.0):
        self.konto_nr = nr
        self.konto_art = art
        self.saldo = saldo
        self.__kunde = kunde

    def __str__(self):
        return '<class Konto> {}, {}, {}'.format(self.konto_nr, self.konto_art, self.saldo)

    @property
    def konto_nr(self):
        return self.__konto_nr

    @konto_nr.setter
    def konto_nr(self,nr):
        self.__konto_nr = nr

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

    @property
    def kunde(self):
        return self.__kunde

    @kunde.setter
    def kunde(self,kunde):
        self.__kunde=kunde


if __name__ == '__main__':
    kunde1 = Kunde('Ruth Reich',1000)
    kunde1.add_konto()
    kunde1.add_konto(art='Privatkonto', saldo=100)
    kunde1.add_konto(art='Sparkonto', saldo=20000)

    print('Kunde:', kunde1.name, 'Kundennummer', kunde1.kunde_nr)
    print('Konten:')
    for konto in kunde1.konten:
        print('Art:', konto.konto_art, 'Kontonummer:', konto.konto_nr, 'Saldo:', konto.saldo)

