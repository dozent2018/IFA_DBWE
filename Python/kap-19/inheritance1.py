# inheritance1.py
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

    def auskunft(self):
        print('Ich studiere', self.studienfach)
        print('Meine Matrikelnummer ist', self.matrikelnummer)

klara = Student('Klara Benz', 'Informatik', 10021)
peter = Student('Peter Schmid', 'Elektrotechnik', 10190)
klara.hallo()
klara.auskunft()
peter.hallo()
peter.auskunft()

