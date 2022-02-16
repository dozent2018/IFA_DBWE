# mitarbeiter_property.py
class Mitarbeiter:
    lohnklassen = {
        1:{'low_limit':40000.00,'high_limit':69999.00},
        2:{'low_limit':70000,'high_limit':99999.00},
        3:{'low_limit':100000.00,'high_limit':150000.00}
    }

    def __init__(self, name, lohnklasse, lohn):
        self.name = name
        self.lohnklasse = lohnklasse
        self.lohn = lohn

    @property
    def lohnklasse(self):
        return self.__lohnklasse

    @lohnklasse.setter
    def lohnklasse(self,lohnklasse):
        if lohnklasse in Mitarbeiter.lohnklassen:
            self.__lohnklasse = lohnklasse
        else:
            print( 'Fehler, Lohnklasse', lohnklasse, 'existiert nicht')

    @property
    def lohn(self):
        return self.__lohn

    @lohn.setter
    def lohn(self,lohn):
        if lohn >= Mitarbeiter.lohnklassen[self.lohnklasse]['low_limit'] and \
        lohn <= Mitarbeiter.lohnklassen[self.lohnklasse]['high_limit'] :
            self.__lohn = lohn
        else:
            print( 'Fehler, Lohn liegt ausserhalb der Grenzwerte für Lohnklasse', self.lohnklasse)

if __name__ == '__main__':
    Klaus = Mitarbeiter('Klaus Meier', 2, 80000.00)
    print(Klaus.name, Klaus.lohnklasse, Klaus.lohn)
    Klaus.lohn = 20000
    Klaus.lohn = 100000
    Klaus.lohnklasse = 4


