""" Aufgabe2.py enthält Lösungsvorschläge zur Aufgabe 2 im Kapitel "Weitere Datenstrukturen"
    Die Lösungen können in der REPL ausprobiert werden. Es gibt jeweils eine Lösung mit Mengenoperator
    und allenfalls eine gleichwertige Lösung mit einer Methode.
"""

Deutsch = { 'D', 'A', 'CH', 'L', 'LI' }
Franzoesisch = { 'F', 'B', 'L', 'CH' }
Italienisch = { 'I', 'CH' }
Englisch = {'GB', 'US'}

# 1.	Erzeugen Sie eine Menge AlleSprachen, die alle Sprachen der 4 anderen Sprachmengen enthält / Vereinigung
AlleSprachen = Deutsch | Franzoesisch | Italienisch | Englisch
AlleSprachen = Deutsch.union(Franzoesisch, Italienisch, Englisch)

# 2.	Gesucht sind die Länder, in denen sowohl Franzoesisch wie auch Deutsch gesprochen wird / Schnittmenge 
Deutsch & Franzoesisch
Deutsch.intersection(Franzoesisch)

# 3.	Gesucht sind die Länder, in denen Französisch, aber nicht Deutsch gesprochen wird. 
Franzoesisch - Deutsch
Franzoesisch.difference(Deutsch)

# 4.	Gesucht sind die Länder, in denen Deutsch, aber nicht Französisch gesprochen wird. 
Deutsch - Franzoesisch
Deutsch.difference(Franzoesisch)

# 5.	Gesucht sind die Länder, in denen entweder Französisch oder Deutsch gesprochen wird, aber nicht beide Sprachen.
Franzoesisch ^ Deutsch
Franzoesisch.symmetric_difference(Deutsch)

# 6.	Gesucht sind die Länder, in denen kein Deutsch gesprochen wird
AlleSprachen - Deutsch
AlleSprachen.difference(Deutsch)


# 7.	Gesucht sind die Länder, in denen weder Italienisch noch Französisch gesprochen wird.
AlleSprachen - Italienisch - Franzoesisch
AlleSprachen.difference(Italienisch, Franzoesisch)