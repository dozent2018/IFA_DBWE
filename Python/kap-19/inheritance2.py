# inheritance2.py
class Person:
    def __init__(self,name):
        self.name = name

    def hallo(self):
        print('Hallo, mein Name ist',self.name)

class Student(Person):
    def __init__(self, name, fach, mat_nr):
        super().__init__(name)
        self.studienfach = fach
        self.matrikelnummer = mat_nr

    def hallo(self):
        super().hallo()
        print('Ich studiere', self.studienfach)
        print('Meine Matrikelnummer ist', self.matrikelnummer)

klara = Student('Klara Benz', 'Informatik', 10021)
jochen = Person('Jochen Reinholdt')
klara.hallo()
jochen.hallo()

