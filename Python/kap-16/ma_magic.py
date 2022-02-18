# ma_magic.py
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

    def __str__(self) :
        return "Klasse: Mitarbeiter name: " + self.name + " lohnklasse: " + \
               str(self.__lohnklasse) + " lohn: " + str(self.__lohn)

    def __repr__(self) :
        return "Mitarbeiter(" + self.name + "," + str(self.__lohnklasse) + "," + str(self.__lohn) + ")"

    def __eq__(self, __o: object) -> bool:
        if self.name == __o.name and self.lohnklasse == __o.lohnklasse and self.lohn == __o.lohn:
            return True
        else:
            return False

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
    print(Klaus)
    print(repr(Klaus))


