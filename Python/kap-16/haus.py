class Haus:
    def __init__(self, farbe):
        self.farbe = farbe
        self.tuer_offen = False
        self.heizung_an = False

    def aufschliessen(self):
        self.tuer_offen = True

    def heizen(self):
        self.heizung_an = True

haus3 = Haus('grün')
print(haus3.farbe, haus3.tuer_offen, haus3.heizung_an)
haus3.farbe = 'gelb'
print(haus3.farbe, haus3.tuer_offen, haus3.heizung_an)
haus3.aufschliessen()
print(haus3.farbe, haus3.tuer_offen, haus3.heizung_an)

