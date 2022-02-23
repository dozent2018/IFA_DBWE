# mitarbeiter.py
class Mitarbeiter:
    lohnklassen = {
        1:{'low_limit':40000.00,'high_limit':69999.00},
        2:{'low_limit':70000,'high_limit':99999.00},
        3:{'low_limit':100000.00,'high_limit':150000.00}
    }

    def __init__(self, name, lohnklasse, lohn):
        self.name = name
        self.set_lohnklasse(lohnklasse)
        self.set_lohn(lohn)

    def set_lohnklasse(self,lohnklasse):
        if lohnklasse in Mitarbeiter.lohnklassen:
            self.__lohnklasse = lohnklasse
        else:
            print( 'Fehler, Lohnklasse', lohnklasse, 'existiert nicht')

    def set_lohn(self,lohn):
        if lohn > Mitarbeiter.lohnklassen[self.__lohnklasse]['low_limit'] and \
        lohn < Mitarbeiter.lohnklassen[self.__lohnklasse]['high_limit'] :
            self.__lohn = lohn
        else:
            print( 'Fehler, Lohn liegt ausserhalb der Grenzwerte für Lohnklasse', self.__lohnklasse)

    def get_lohn(self):
        return self.__lohn

    def get_lohnklasse(self):
        return self.__lohnklasse

if __name__ == '__main__':
    Klaus = Mitarbeiter('Klaus Meier', 2, 80000.00)
    print(Klaus.name, Klaus.get_lohnklasse(), Klaus.get_lohn())
    Klaus.set_lohn(20000)
    Klaus.set_lohn(100000)
    Klaus.set_lohnklasse(4)
    Peter = Mitarbeiter('Peter Schmidt', 3, 10250.00)
    print(Peter.lohnklassen)
    print(Klaus.lohnklassen)
    Peter.lohnklassen[3]['high_limit'] = 200000.00
    print(Peter.lohnklassen)
    print(Klaus.lohnklassen)
else:
    print(__name__ , 'wurde importiert')


