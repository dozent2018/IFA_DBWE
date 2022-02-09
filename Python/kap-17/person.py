# person.py definiert eine Klasse Person und testet sie

class Person:

    def __init__(self, name, geburtstag):
        self.name = name
        self.set_geburtstag(geburtstag)

    def set_geburtstag(self, geburtstag):
        try:
            self.__geburtstag = datetime.strptime(geburtstag, '%d.%m.%Y')
        except ValueError:
            print('Fehler - Ungültiges Datum: ', geburtstag)

    def get_geburtstag(self):
        return self.__geburtstag

    def hallo(self):
        print('Hallo, mein Name ist', self.name, ', mein Geburtstag ist der',
               datetime.strftime(self.__geburtstag, '%d.%m.%Y'))

if __name__ == '__main__':
    person1 = Person('Hans Kunz','29.03.1990')
    person2 = Person('Clara Meier', '30.02.2000') # ungültiges Datum!
    person3 = Person('Petra Pauli', '01.02.1999')
    person1.hallo()
    print(person1.get_geburtstag())
    person3.hallo()
    person3.set_geburtstag('21.03.1999')
    person3.hallo()
    # person2.hallo()
    print('Name:', person1.name)
    print('Geburtstag:',person1.__geburtstag)

