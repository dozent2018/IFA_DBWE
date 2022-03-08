# bank2c.py ist ein Lösungsvorschlag für Aufgabe 2c+d in Kap 16.12
# Die Instanzvariablen von Konto sind jetzt privat
# Die Methode Konto.add_konto() legt jetzt automatisch ein Konto an
# Der Kunde wird jetzt auch beim Konto gespeichert
# Die Klasse Kontobewegung ist implementiert
# In der Klasse Konto gibt es eine Liste der Bewegungen
# Ein Kontoauszug kann mit Konto.kontoauszug() erzeugt werden
# Die Methoden Konto.einzahlen() und Konto.auszahlen() sind implementiert
# Es wurden durchgehend Typ-Annotationen eingefügt

from datetime import datetime

class Kunde:

    def __init__(self, name:str, nr:int) -> None:
        self.name = name
        self.kunde_nr = nr
        self.__konten = []

    def __str__(self) -> str:
        return '<class Kunde> {}, {}, {}'.format(self.name, self.kunde_nr, self.konten)

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name:str) -> int:
        self.__name = name

    @property
    def kunde_nr(self) -> int:
        return self.__kunde_nr
    @kunde_nr.setter
    def kunde_nr(self, nr:int) ->None:
        self.__kunde_nr = nr

    @property
    def konten(self) -> None:
        return self.__konten
    def add_konto(self, art:str='undefiniert', saldo:float=0.0,limit:float=0.0) -> object:
        if len(self.konten) == 0:
            # es gibt noch kein Konto
            new_nr = self.kunde_nr + 1
        else:
            # es gibt schon Konten. Die neue nr soll
            # gleich der bisher höchsten nr + 1 sein
            new_nr = max([k.konto_nr for k in self.konten]) + 1
            # Alternative zu list comprehension : For-Schleife möglich
        new_konto = Konto(nr=new_nr, kunde=self, art=art, limit=limit)
        self.konten.append( new_konto )
        return new_konto

class Konto:
    def __init__(self, nr:int, kunde:Kunde, art:str, limit:float) -> None:
        self.konto_nr = nr
        self.konto_art = art
        self.kunde = kunde
        self.limit = limit
        self.saldo = 0.0
        self.__bewegungen = []

    def __str__(self) -> str:
        return '<class Konto> nr:{}, art:{}, saldo:{}, limit:{}'.format(self.konto_nr, self.konto_art, self.saldo,self.__limit)

    @property
    def konto_nr(self) -> int:
        return self.__konto_nr
    @konto_nr.setter
    def konto_nr(self,nr) -> None:
        self.__konto_nr = nr

    @property
    def konto_art(self) -> str :
        return self.__konto_art
    @konto_art.setter
    def konto_art(self, art : str) -> None:
        self.__konto_art = art

    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, new_saldo:float) -> None:
        self.__saldo=new_saldo

    @property
    def kunde(self) -> Kunde:
        return self.__kunde
    @kunde.setter
    def kunde(self,kunde : Kunde) -> None:
        self.__kunde=kunde

    @property
    def limit(self) -> float:
        return self.__limit
    @limit.setter
    def limit(self, limit:float) -> None:
        self.__limit=limit

    def einzahlen(self, betrag:float, text:str) -> bool:
        if betrag > 0:
            try:
                k = Kontobewegung(self, betrag, datetime.today(), text)
                self.__bewegungen.append(k)
                self.saldo += betrag
                return True
            except Exception as e:
                print('Fehler beim Erzeugen der Kontobewegung: {}'.format(str(e)))
                return False
        else:
            print('Einzahlungsbetrag muss grösser 0 sein')
            return False

    def auszahlen(self, betrag:float, text:str) -> bool:
        if betrag < 0:
            print('Auszahlungsbetrag muss grösser 0 sein')
            return False
        if self.saldo - betrag < self.limit:
            print('Auszahlung von {:.2f} nicht möglich. Saldo: {:.2f} Limit: {:.2f}'.format(betrag, self.saldo, self.limit))
            return False
        try:
            k = Kontobewegung(self, -betrag, datetime.today(), text)
            self.__bewegungen.append(k)
            self.saldo -= betrag
            return True
        except Exception as e:
            print('Fehler beim Erzeugen der Kontobewegung: {}'.format(str(e)))
            return False

    def auszug(self):
        print('Kunde: {} Kunden-Nr: {}, Konto: {}'.format(self.kunde.name, self.kunde.kunde_nr, self.konto_nr))
        for b in self.__bewegungen:
            print('{} {:20s} {:>12.2f}'.format(datetime.strftime(b.zeit, '%d.%m.%Y %H:%M'), b.text, b.betrag))
        print('Saldo: {:>43.2f}'.format(self.saldo) )

class Kontobewegung:
    def __init__(self, konto: Konto, betrag: float, zeitpunkt: datetime, text: str) -> None:
        self.betrag = betrag
        self.zeit = zeitpunkt
        self.text = text

    @property
    def betrag(self) -> float:
        return self.__betrag
    @betrag.setter
    def betrag(self, b) -> None:
        self.__betrag = b

    @property
    def zeit(self) -> datetime:
        return self.__zeit
    @zeit.setter
    def zeit(self, z: datetime ) -> None:
        try:
            self.__zeit = z
        except ValueError:
            print('Fehler bei der Zuweisung von datetime')

    @property
    def text(self) -> str:
        return self.__text
    @text.setter
    def text (self, text: str) -> None:
        self.__text = text

if __name__ == '__main__':
    kunde1 = Kunde('Ruth Reich',1000)
    konto1 = kunde1.add_konto(art='Privatkonto', limit=-5000.00)
    konto2 = kunde1.add_konto(art='Sparkonto', limit=0.0)

    print('Kunde:', kunde1.name, 'Kundennummer', kunde1.kunde_nr)
    print('Konten:')
    for konto in kunde1.konten:
        print(konto)
    konto1.einzahlen(1020.22,'Erstattung KK')
    konto1.einzahlen(9000.00,'Lohn')
    konto1.auszahlen(3000.00,'Miete')
    konto1.auszahlen(10000.00,'Shopping')
    konto2.einzahlen(1000.00,'Sparen')
    konto2.einzahlen(500.00,'Sparen')
    konto1.auszug()
    konto1.auszahlen(3000.00,'Miete')
    konto2.auszug()
