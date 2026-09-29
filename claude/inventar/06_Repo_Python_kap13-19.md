# Inventar 06: Repo Python kap-13 bis kap-19

Kurs DBWE.TA1A "Datenbanken und Web-Entwicklung", IFA Hoehere Fachschule. Lehrmittel PYGR von Jochen Reinholdt.
Gegenstand: `Python/kap-13` bis `Python/kap-19` im oeffentlichen Fork (Codestand Januar 2024).
Erstellt: 29.09.2026. Bezug: KI-Handoff v2.0, Zeilen 53-86 (Repo-Material) und 419-542 (WP2 Units 6-7).

Legende Typ: **Buchaufgabe** = Musterloesung zu einer Aufgabe im Lehrmittel (laut Kopfkommentar oder Inhalt), **Beispiel** = Codebeispiel aus dem Lehrmittel, **Fremdmaterial** = nicht vom Lehrmittelautor bzw. nicht kursbezogen, **Artefakt** = Laufzeitausgabe, Duplikat, Entwurf oder private Datei.
Legende 3.11: Ergebnis der Ausfuehrung mit Python 3.11.15 in einer Kopie; "statisch" = nur kompiliert und gelesen.

---

## 1 Gelesener Umfang und Methode

| Ordner | Dateien | davon .py | davon Daten | vollstaendig gelesen |
|---|---|---|---|---|
| kap-13 | 10 | 10 | 0 | ja |
| kap-14 | 9 | 9 | 0 | ja |
| kap-15 | 15 | 15 | 0 | ja |
| kap-16 | 12 | 12 | 0 | ja |
| kap-17 | 37 | 24 | 13 | ja |
| kap-18 | 6 | 6 | 0 | ja |
| kap-19 | 6 | 6 | 0 | ja |
| **Total** | **95** | **82** | **13** | **ja** |

Methode:
- Jede Datei vollstaendig gelesen (Python- und Textdateien zeilennummeriert). CSV/JSON/TXT zusaetzlich auf BOM, Trennzeichen, Zeilenenden und Spaltenzahl geprueft.
- XLSX mit openpyxl 3.1.5 (venv im Scratchpad) und durch Entpacken der XML-Teile inspiziert. `students.pkl` ausschliesslich mit `python3 -m pickletools` disassembliert (kein `pickle.load`).
- Ausfuehrung aller lauffaehigen Skripte mit Python 3.11.15, jeweils in einer frischen Kopie des Kapitelordners unter `scratchpad/repo_run_py2/_runs/`, interaktive Skripte mit vorgegebenen stdin-Eingaben, argv-Skripte mit Argumenten. Kompilierpruefung aller 82 Skripte zusaetzlich mit Python 3.12 und 3.13.
- Nicht ausgefuehrt: `pickle_load.py`, `pickle_modify.py` (Regel: kein `pickle.load`), alle kap-18 Skripte (kein MySQL; statische Pruefung gegen `SQL/create_beispiele.sql`, Treiber `mysql-connector-python` 26.7.0 im venv installiert, nur Import und Quelltext geprueft).
- Im Repo wurde ausser dieser Datei nichts angelegt oder geaendert.

---

## 2 Kurzfazit

1. **Private Kalenderdaten im oeffentlichen Repo**: `kap-17/IFA-TimeOverlap.csv` und `kap-17/daten.csv` sind reale Kalenderexporte 2019-2020 mit privaten, teils sensiblen Eintraegen und Namen Dritter (Details bewusst nicht wiedergegeben). Entfernen, auch aus der Git-Historie.
2. **bank2c.py-Bug bestaetigt** (Z.42, globales `kunde1` statt `self`). Mit zweitem Kunden entstehen falsche und doppelte Kontonummern (2001, 1004, 1004). Die korrigierte Fassung steht oeffentlich in `bank2d.py` Z.47.
3. **kap-18-Demo liefert gegen `create_beispiele.sql` ein leeres Ergebnis**: `db_select2.py` und `db_context.py` fragen das Jahr 2020 ab, die Tabelle `lehrveranstaltung` enthaelt nur Daten vom 01.07.2021 bis 15.12.2026. Credentials sind in allen 6 Dateien hardcodiert (Handoff bestaetigt).
4. **Adressen.csv**: `;`, UTF-8 mit BOM, CRLF bestaetigt, aber nur 1 Kopfzeile plus 3 Datensaetze mit 7 Spalten. Die Adressbuch-Skripte erwarten ein anderes Format (5 Spalten, ohne Kopf, wie `Adressbuch.csv`).
5. **Viele Musterloesungen sind fehlerhaft**: 3 Dateien mit SyntaxError, 7 weitere brechen mit Laufzeitfehler ab oder rechnen falsch (u. a. `kap-14/myfunctions.py`, `kap-15/myfunctions.py`, `fib_rekursiv.py`, `autos.py`, `kap-19/computer.py`, `wordstat2.py`, `lotto_mengen.py`).
6. **Windows-Risiko (BYOD)**: CSV wird ohne `newline=''` geschrieben und gelesen, Textdateien ohne `encoding`. Speichern und Neuladen in `adressbuch06/07.py` endet unter Windows mit IndexError (simuliert).
7. **Studierenden-Abgabe mit vollem Namen und Copyright** (`bank2_patrick.py`, `color.py`) liegt im oeffentlichen Repo.

---

## 3 Inventar pro Kapitel

### 3.1 kap-13 (Weitere Datenstrukturen, Adressbuch-Reihe)

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| Aufgabe2.py | 38 | Loesungen Mengenaufgabe (Aufgabe 2, Kapitel "Weitere Datenstrukturen") | set, Operatoren und Methoden (union, intersection, difference, symmetric_difference) | nein | Buchaufgabe | keine | ja, aber ohne Ausgabe (fuer REPL gedacht) | Ausdruecke ohne print, als Skript wirkungslos; Menge `AlleSprachen` enthaelt Laender (Benennung irrefuehrend) | Laender und Sprachen |
| adressbuch.py | 97 | Fruehe Adressbuch-Variante mit create/show/find/update | dict, Funktionen, Typannotationen, pprint, str.format | ja | Beispiel (Variante) | pprint | teilweise: (N) ok, (A) und (S) NameError | Z.35-36 `formatstr`/`ueberschrift` nur lokal in show(), in Z.81/83/87 undefiniert; Z.64/92 update() liefert None und speichert None im dict; Docstring Z.1 "Erste Version" falsch; find()-Docstring verspricht leeres dict, liefert None; `!= None` | Adressbuch |
| adressbuch002.py | 61 | Zwischenstand mit read_name/read_adr | Funktionen, dict, while True/break | ja | Beispiel (Variante) | pprint | ja | Docstring nennt "adressbuch.py, Zweite Version"; Dublette zur Reihe 01-05 | Adressbuch |
| adressbuch01.py | 27 | Schritt 1: Menuefunktion | def, Rueckgabewert, Endlosschleife | ja | Beispiel | keine | ja | keine | Adressbuch |
| adressbuch02.py | 45 | Schritt 2: read_name/read_adr | Funktionen mit dict-Rueckgabe | ja | Beispiel | keine | ja | neue Funktionen im Hauptprogramm nicht aufgerufen; Tippfehler Docstring | Adressbuch |
| adressbuch03.py | 65 | Schritt 3: Eintrag anlegen, Duplikatpruefung | dict, `in`, continue | ja | Beispiel | pprint | ja | Docstring Z.1-2 falsch (nennt create()); menu() ohne strip() | Adressbuch |
| adressbuch04.py | 74 | Schritt 4: show/showall | Funktionen, globale Variable | ja | Beispiel | keine | ja | show()/showall() lesen globales `adressen` (Z.38, 44); Docstring "Dritte Version" | Adressbuch |
| adressbuch05.py | 138 | Schritt 5: CRUD komplett, Import aus CSV | csv.reader, utf-8-sig, with, Suche, Update | ja | Beispiel | csv; Datei `Adressen.csv` | nein im Ordner (FileNotFoundError, Datei liegt nur in kap-17); mit 5-Spalten-CSV ja | Z.100 liest `Adressen.csv` (7 Spalten mit Kopf), Code erwartet 5 Spalten ohne Kopf; Z.20-22 Eingabe ohne lower() zurueckgegeben: `A`/`B` werden akzeptiert, aber ignoriert (Beenden mit `B` unmoeglich); Z.6 Annotation `-> None`, liefert dict; kein Speichern; globales `adressen` in showlist/find | Adressbuch |
| beipack.py | 18 | Landessprachen fuer Beipackzettel je Land | dict mit Tupel-Werten, Einer-Tupel | ja | Beispiel | keine | ja | Z.11 Tippfehler "Ialienisch"; Z.17 KeyError bei Kleinschreibung oder unbekanntem Land | Beipackzettel/Sprachen |
| lotto_mengen.py | 37 | Lotto mit set statt Liste | set, randint, isdecimal, Schnittmenge | ja | Beispiel | random | laeuft, Logikfehler | Z.9 Tipp mit 6 Zahlen vorbelegt, dadurch ist Z.25 `len(tipp) < 6` nie wahr: Benutzereingabe wird immer ignoriert; Kommentar Z.28 im falschen Zweig; Docstring nennt lotto3.py; `sorted(list(...))` | Lotto 6 aus 49 |

### 3.2 kap-14 (Funktionen)

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| annotate.py | 9 | Funktionsannotationen | Type Hints | nein | Beispiel | keine | ja (keine Ausgabe) | nur Definitionen | Summe |
| function_demo.py | 29 | Entwurf maximum/ist_zahl/read_int | return, try/except | (ja) | Artefakt (Entwurf) | keine | nein: SyntaxError Z.19 | Z.19 Zuweisung statt Vergleich in `while`; read_int gibt auch nach Korrektur eine Funktion statt der Zahl zurueck; Z.3 Semikolon | Zahleneingabe |
| import_demo1.py | 12 | `from ... import` einer eigenen Funktion | Import | nein | Beispiel | myfunctions (kap-14) | ja | `== True` | Zahlvalidierung |
| import_demo2.py | 11 | `import` Modul mit Punktnotation | Import | nein | Beispiel | myfunctions (kap-14) | ja | `== True` | Zahlvalidierung |
| myfunctions.py | 122 | Loesungen Aufgaben 1-11 (Kopf: "Aufgaben in Kap. 13") | try/except, Schleifen, Wiederverwendung | Funktionen mit input() | Buchaufgabe | keine | Import ja, mehrere Funktionen defekt | Z.63-70 read_float: `instring` vor Zuweisung (UnboundLocalError), Annotation `int`, Meldung "ganze Zahl"; Z.108-109 kgv: `ggt(x)` ohne 2. Argument (TypeError), Formel falsch; Z.36-48 mittel: Docstring nach Anweisungen, Debug-print Z.43, `summe + element` ohne float() (TypeError bei Strings); Z.84-97 is_prime(0) und is_prime(1) liefern True; is_int(111.33) liefert True; Variable `sum` ueberschattet Builtin | Zahlen, Primzahlen, ggT/kgV |
| read_int.py | 14 | Ganze Zahl einlesen mit Wiederholung | while True, try/except ValueError | ja | Beispiel | keine | ja | keine | Anzahl/Alter |
| reihenfolge.py | 14 | Fehlerdemo: Aufruf vor Definition | Definitionsreihenfolge | nein | Beispiel (Fehlerdemo) | keine | NameError Z.9 (beabsichtigt) | Tippfehler Kopf | Summe/Differenz |
| return_list.py | 14 | Liste als Rueckgabewert | range, append, return | nein | Beispiel | keine | ja | Parameter `zahl` wird von Schleifenvariable ueberschattet (Z.6) | Zahlenreihe |
| testfunctions.py | 29 | Testaufrufe fuer myfunctions | Import, manuelles Testen | ja (am Ende) | Artefakt (Testskript) | myfunctions (kap-14) | nein: TypeError Z.18 (`summe()` ohne Argument) | Ueberschriften Z.8-13 falsch (testet is_int unter "is_float"); doppelter Import Z.17 | Zahlvalidierung |

### 3.3 kap-15 (Funktionen vertieft, Module, Rekursion)

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| adressbuch07.py | 204 | Wie adressbuch06, mit `__main__`-Guard | CSV lesen/schreiben, os.listdir, Ausnahmen, `__name__` | ja | Beispiel | csv, os; beliebige *.csv im Arbeitsverzeichnis | ja (Linux); Windows siehe PY2-F09 | Z.2 Docstring schreibt `__name`; Z.73-77 toter Code; showlist/find lesen globales `adressen`, das nur im Main-Block existiert (Import plus Aufruf ergibt NameError); Z.193 `geaendert` auch ohne Uebernahme; kein `newline=''` (Z.20, 38); Kopfzeile nicht behandelt; IndexError bei kurzen Zeilen nicht abgefangen; `pprint` ungenutzt | Adressbuch |
| default_demo.py | 9 | Default-Parameter | Defaults, Keyword-Argumente | nein | Beispiel | keine | ja | keine | Begruessung |
| fak_rekursiv.py | 33 | Fakultaet iterativ vs. rekursiv, Laufzeitmessung | Rekursion, time.perf_counter, sys.argv | argv | Beispiel | sys, time | ja mit Argument; ohne Argument IndexError; n=3000 RecursionError | Z.3-5 fak_i(0) liefert 0 statt 1 | Fakultaet |
| fib_rekursiv.py | 54 | Fibonacci iterativ, rekursiv, memoisiert | Rekursion, Memoisierung mit dict, argv | argv | Beispiel | sys, time | ja mit Argument; n=3000 RecursionError in fib_m | Z.15-17 fib_i um eins verschoben (liefert fib(n-1), z. B. fib_i(3)=1): Laufzeitvergleich vergleicht unterschiedliche Werte; auskommentierter Code | Fibonacci |
| ggt_rekursiv.py | 18 | ggT iterativ vs. rekursiv | Rekursion, argv | argv | Beispiel oder Aufgabe | sys | ja mit 2 Argumenten | `time` importiert, ungenutzt | ggT |
| kommandozeile.py | 7 | Kommandozeilenargumente ausgeben | sys.argv | argv | Beispiel | sys | ja | Docstring nennt argv.py | Kommandozeile |
| kwargs_demo.py | 14 | Aufruf mit Schluesselwort-Argumenten | Keyword-Argumente | nein | Beispiel | keine | ja | Annotation `-> list`, liefert None | Liste multiplizieren |
| module1.py | 8 | Modul mit `__name__`-Pruefung | `if __name__ == '__main__'` | nein | Beispiel | keine | ja | `return(...)` in Klammern | Module |
| module2.py | 4 | Import von module1 | Import, Seiteneffekt beim Import | nein | Beispiel | module1 | ja | keine | Module |
| myfunctions.py | 65 | Eingabe- und Validierungsmodul | try/except, Modul | Funktionen mit input() | Beispiel (Modul) | keine | Import ja; read_int/read_float defekt | Z.28 und Z.41 `int(zahl)`/`float(zahl)`: NameError (richtig: `eingabe`); Z.50 `ergebnis += zahl` TypeError bei String-Zahlen; API weicht von kap-14/myfunctions.py ab (yes mit 1 statt 2 Parametern) | Eingabevalidierung |
| pos_demo.py | 14 | Falsche Reihenfolge von Positionsargumenten | Positionsparameter | nein | Beispiel (Fehlerdemo) | keine | TypeError Z.13 (beabsichtigt) | Annotation `-> list`, liefert None | Liste multiplizieren |
| reihenfolge.1.py | 22 | Erweiterte Kopie von reihenfolge.py | *args, **kwargs, keyword-only | nein | Artefakt (Kopie) | keine | ja | Dateiname mit Punkt nicht importierbar; Docstring nennt reihenfolge.py; inhaltlich die vollstaendigere Version | Parameterarten |
| reihenfolge.py | 16 | Reihenfolge der Parameterarten | *args, keyword-only | nein | Beispiel | keine | TypeError Z.15 (keyword-only fehlt, vermutlich beabsichtigt) | Fehlerabsicht nicht kommentiert | Parameterarten |
| var_demo.py | 10 | Variable Argumentliste | *args, Slicing | nein | Beispiel | keine | ja | keine | Zahlen multiplizieren |
| var_kwargs_demo.py | 9 | Beliebige Keyword-Argumente | **kwargs | nein | Beispiel | keine | ja | `for arg in kwargs.keys()` | Argumente |

### 3.4 kap-16 (Klassen und Objekte)

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| bank1.py | 52 | Kunde/Konto Version 1 | Klassen, @property, private Attribute, Aggregation | nein | Beispiel | keine | ja | Konto noch ohne Kapselung (gewollt) | Bank |
| bank2b.py | 86 | Loesung Aufgabe 2 Kap. 16.12: Konto-Attribute privat | Properties, __str__ | nein | Buchaufgabe | keine | ja | Z.59 auskommentierte Alternative waere SyntaxError (`return` mit Zuweisung) | Bank |
| bank2c.py | 98 | Loesung Aufgabe 2c: add_konto erzeugt Konto, Kunde am Konto gespeichert | Properties, Default-Parameter, List Comprehension, bidirektionale Referenz | nein | Buchaufgabe | keine | ja, korrekt nur mit genau einer Instanz namens `kunde1` | Z.42 globales `kunde1` statt `self` (Details Kap. 4); Z.3 Kommentar nennt `Konto.add_konto()`; Z.13 __str__ zeigt Objektadressen; Kontonummern kollidieren zwischen Kunden | Bank |
| bank2d.py | 183 | Loesung Aufgabe 2c+d: Kontobewegung, ein-/auszahlen, Kontoauszug, Typannotationen | Komposition, datetime, Typannotationen, Ausnahmen | nein | Buchaufgabe | datetime | ja | Z.1 Kopf nennt bank2c.py; Z.40/49 Parameter `saldo` wird ignoriert (Saldo immer 0.0); Z.115 `betrag < 0` erlaubt Auszahlung von 0; Z.27 Setter-Annotation `-> int`, Z.38 `-> None` fuer Liste; Z.137 Parameter `konto` ungenutzt; Z.154-157 try um reine Zuweisung; `datetime.strftime(obj, ...)`; `except Exception` | Bank |
| bank2_patrick.py | 231 | Studierenden-Loesung Bank mit Farbausgabe | Klassen, Properties, ANSI-Farben | nein | Fremdmaterial | color.py, os | laeuft; loescht beim Import das Terminal | Kopf Z.1-4 mit vollem Namen und Copyright (Personendaten Studierende); Z.81-113 und Z.183-205 alle Setter heissen `name` (Properties ohne Setter, Zuweisung wirft AttributeError); Z.16/53-58 Klassenzaehler: Kontonummern doppelt und kundenuebergreifend (nachgewiesen 2000, 2001, 2001); Z.210/212 Kunde als String uebergeben; Z.151-152 mit Z.231 kontoauszug() ueberschreibt Kunde mit Konto; Z.9 `os.system` beim Import | Bank |
| color.py | 16 | ANSI-Farbkonstanten fuer bank2_patrick | Klassenattribute | nein | Fremdmaterial | keine | ja (keine Ausgabe) | Kopf mit Name und Copyright; Klassenname klein | Terminalfarben |
| computer.py | 35 | Loesung Aufgabe 1 Kap. 16 | Klasse, privates Attribut, __str__ | nein | Buchaufgabe | keine | ja | Z.4-5 mutable Default-Argumente (geteilte Liste nachgewiesen); `peripherie` wird nie gespeichert; Z.33 `c1.ping` ohne Klammern; `== True`; Z.28 inventar_nr int statt str; print beim Import | Computer-Inventar |
| haus.py | 18 | Einfachste Klasse mit Methoden | Klasse, Attribute, Methoden | nein | Beispiel | keine | ja | kein Main-Guard | Haus |
| ma_magic.py | 71 | Magische Methoden | __str__, __repr__, __eq__, Klassenvariable, Properties mit Validierung | nein | Beispiel | keine | ja | Z.22-26 __eq__ ohne Typpruefung (AttributeError bei Vergleich mit str), Parametername `__o`, kein __hash__ (Objekt unhashbar); Validierung per print laesst Objekt halb initialisiert (AttributeError bei ungueltiger Lohnklasse); Variablennamen gross | Mitarbeiter/Lohnklassen |
| mitarbeiter.py | 48 | Getter/Setter und Klassenvariable | get_/set_, Klassenvariable, Mutation ueber Instanz | nein | Beispiel | keine | ja | Z.21-22 strikte Grenzen: Lohn 70000 in Klasse 2 abgelehnt (Property-Version inklusiv); Z.39 ungueltiger Lohn laesst Attribut ungesetzt | Mitarbeiter/Lohnklassen |
| mitarbeiter_property.py | 44 | Gleiche Klasse mit @property | Properties, Validierung | nein | Beispiel | keine | ja | Validierung per print statt Exception | Mitarbeiter/Lohnklassen |
| person.py | 34 | Person mit Geburtsdatum | datetime.strptime, Name Mangling | nein | Beispiel | datetime | AttributeError Z.33 (beabsichtigt, Name Mangling) | ungueltiges Datum laesst Attribut ungesetzt, hallo() wirft dann AttributeError; `datetime.strftime(obj, ...)` | Person/Geburtstag |

### 3.5 kap-17 (Dateien, CSV, JSON, Pickle)

Details zu den Datendateien in Kap. 7.

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| Adressbuch.csv | 6 | Testdaten fuer adressbuch06/07 | CSV 5 Spalten ohne Kopf | nein | Beispieldaten | von adressbuch06/07 (Default-Speichername) | n/a | siehe Kap. 7 | Adressbuch |
| Adressen.csv | 4 | Excel-Export, 7 Spalten mit Kopf | CSV | nein | Beispieldaten | read_csv.py, adressbuch05.py | n/a | siehe Kap. 5 | Adressen |
| Adressen.xlsx | bin | Leere Arbeitsmappe | XLSX | nein | Artefakt | nicht referenziert | n/a | leer, nur Metadaten | keines |
| IFA-TimeOverlap.csv | 256 | Privater Kalenderexport | CSV | nein | Artefakt (privat) | nicht referenziert | n/a | Personendaten, siehe PY2-F01 | Kalender |
| MontyPython.json | 4 | JSON-Beispieldaten | JSON | nein | Beispieldaten | json_demo.py | n/a | reale Personen des oeffentlichen Lebens | Personenliste |
| adressbuch06.py | 204 | Adressbuch mit CSV-Import und -Export | csv, os.listdir, Ausnahmen, Aenderungsflag | ja | Beispiel | csv, os; *.csv im Arbeitsverzeichnis | ja (Linux) | wie adressbuch07 ohne Main-Guard; Docstring verspricht Speichern in derselben Datei, fragt aber neuen Namen ab; mit Adressen.csv falsche Feldzuordnung (Kopfzeile wird Eintrag) | Adressbuch |
| append.py | 7 | Zeile mit Zeitstempel anhaengen | open('a'), time.strftime | nein | Beispiel | schreibt out.txt | ja | kein `encoding` | Logdatei |
| copy_lines.py | 16 | Textdatei zeilenweise kopieren | with, zwei Dateien, rstrip | ja | Beispiel | Eingabedatei | ja | kein `encoding`; gleiche Ein- und Ausgabedatei loescht den Inhalt; Tippfehler "Eingabdedatei" | Datei kopieren |
| copy_lines_try.1.py | 23 | Unfertige Kopie von copy_lines_try | except mit Variable | ja | Artefakt | keine | nein: SyntaxError Z.20 | Z.17 `fnf` undefiniert; Z.20 `except OSError oe` ohne `as`, leerer Block | Datei kopieren |
| copy_lines_try.py | 21 | Kopieren mit Fehlerbehandlung | try/except/else, FileNotFoundError, PermissionError | ja | Beispiel | Eingabedatei | ja | kein `encoding`; Fehlermeldung nennt pauschal beide Dateien | Datei kopieren |
| daten.csv | 165 | Kalenderexport (34 Spalten), Eingabe fuer find_overlap | CSV | nein | Artefakt (privat) | find_overlap.py, test_ics_package.py | n/a | Personendaten, siehe PY2-F01 | Kalender |
| file_name | 5 | Ausgabe eines Testlaufs von adressbuch06/07 | CSV | nein | Artefakt | keine | n/a | identisch mit "file_name 2"; letzte Zeile PLZ und Ort vertauscht | Adressbuch |
| file_name 2 | 5 | Finder-Duplikat von file_name | CSV | nein | Artefakt | keine | n/a | Leerzeichen im Dateinamen | Adressbuch |
| find_overlap.py | 101 | Terminueberschneidungen und Reisezeiten in Kalender-CSV finden | csv, datetime, timedelta, dict mit Tupel-Schluesseln, copy() | nein | Fremdmaterial (Werkzeug des Autors) | daten.csv | ja (meldet 5 Ueberlappungen) | arbeitet nur mit privaten Daten; ungenutzte Imports (pprint, copy); Funktionsrumpf `pass` Z.34-35; globale Variablen; englische Kommentare | Stundenplan-Konflikte |
| json_demo.py | 13 | JSON-Datei laden | json.load, pprint | nein | Beispiel | MontyPython.json | ja | Kopf nennt json_load.py; kein `encoding` | Personenliste |
| json_dump.py | 19 | Verschachteltes dict als JSON speichern | json.dump | nein | Beispiel | schreibt students.json | ja | int-Schluessel werden zu Strings (Roundtrip-Falle, nicht erklaert); Schluessel " Studiengang " mit Leerzeichen; pprint ungenutzt; kein `encoding` | Studierende/Noten |
| num_lines.py | 16 | Zeilen nummeriert kopieren | Format-Spezifikation mit Breite | ja | Beispiel | Eingabedatei | ja | kein `encoding` | Datei kopieren |
| oldschool.py | 14 | Dateien ohne with | open/close | ja | Beispiel | Eingabedatei | laeuft, Ergebnis falsch | Z.9 `rstrip()` ohne neues `\n`: Ausgabe ist eine einzige Zeile | Datei kopieren |
| panther.txt | 5 | Gedicht als Lesedatei | Text | nein | Beispieldaten | read_file.py, write_file.py | n/a | Urheberrecht pruefen (PY2-F29) | Gedicht |
| pickle_dump.py | 16 | dict mit pickle speichern | pickle.dump, Modus 'wb' | nein | Beispiel | schreibt students.pkl | ja | pprint ungenutzt; Einrueckung 7 Leerzeichen | Studierende/Noten |
| pickle_load.py | 9 | pickle laden | pickle.load | nein | Beispiel | students.pkl | statisch (Regel: nicht ausgefuehrt) | kein Sicherheitshinweis zu pickle.load | Studierende/Noten |
| pickle_modify.py | 16 | Laden, aendern, zurueckschreiben | pickle-Roundtrip | nein | Beispiel | students.pkl (ueberschreibt) | statisch (Regel: nicht ausgefuehrt) | Kopf nennt pickle_mod.py; die Repo-pkl ist bereits der modifizierte Zustand | Studierende/Noten |
| read_csv.py | 9 | Excel-CSV lesen | csv.reader, utf-8-sig, delimiter | nein | Beispiel | Adressen.csv | ja | kein `newline=''`; Kopfzeile wird als Datenzeile ausgegeben; keine Fehlerbehandlung | Adressen |
| read_file.py | 8 | Textdatei zeilenweise lesen | Iteration ueber Dateiobjekt | nein | Beispiel | panther.txt | ja | Docstring nennt copy_lines.py; kein `encoding` | Gedicht |
| spam.csv | 3 | Ausgabe von write_csv.py | CSV | nein | Beispieldaten | keine | n/a | reproduzierbar identisch | Tabelle |
| spam.xlsx | bin | Leere Arbeitsmappe | XLSX | nein | Artefakt | nicht referenziert | n/a | leer, nur Metadaten | keines |
| students.json | 1 | Ausgabe von json_dump.py | JSON | nein | Beispieldaten | keine | n/a | reproduzierbar identisch | Studierende/Noten |
| students.pkl | bin | pickle-Datei (Protokoll 3) | Pickle | nein | Artefakt (Laufzustand) | pickle_load/modify | n/a | Zustand nach pickle_modify, nicht nach pickle_dump | Studierende/Noten |
| test_ics_package.py | 103 | Defekte Kopie von find_overlap mit Import des Drittpakets `ics` | keine neuen | nein | Artefakt | ics (PyPI, ungenutzt), daten.csv | nein: SyntaxError Z.44 | Z.44 Tippfehler im dict-Literal; csv, datetime, timedelta nicht importiert; `ics` nie verwendet; Kopf nennt find_overlap | Kalender |
| testos.py | 11 | Verzeichnisfunktionen | getcwd, listdir, mkdir, chdir, rmdir | nein | Beispiel | os; legt Verzeichnis an | nein: AttributeError Z.11 (Z.1-10 laufen) | Z.11 abgeschnitten (`os.r`); kein Kopfkommentar | Verzeichnisse |
| wordcount1.py | 60 | Woerter zaehlen | str.maketrans/translate, split, Funktionen | ja | Beispiel | Textdatei | ja; Fehlerpfad NameError | Z.29 nutzt globales `in_fname` statt Parameter; Z.32-41 `in_dname` undefiniert (NameError statt Meldung); Z.51 kein None-Check; Z.53 ungueltige Escapes (3.12+: SyntaxWarning); clean_string1 ungenutzt und fehlerhaft (liefert '' wenn kein Zeichen vorkommt) | Wortzaehlung |
| wordcount2.py | 67 | Zusaetzlich Anzahl verschiedener Woerter | set | ja | Beispiel | Textdatei | ja; Fehlerpfad NameError | wie wordcount1 (Z.32-45, 56); `sys` ungenutzt | Wortzaehlung |
| wordstat.py | 82 | Worthaeufigkeiten | dict als Zaehler, sorted, sys.exit | ja | Beispiel oder Aufgabe | Textdatei | ja; Fehlerpfad NameError | wie wordcount1 (Z.32-45, 63), aber mit None-Check Z.58; `lines == None` | Wortstatistik |
| wordstat2.py | 83 | Worthaeufigkeit nach Haeufigkeit sortiert | Tupel-Liste, Sortierung | ja | Beispiel | Textdatei | nein: AttributeError Z.81 | Z.81 `statistics.sorted(...)` existiert nicht (richtig `sorted(statistics, reverse=True)`); None-Check entfernt; Escapes Z.60 | Wortstatistik |
| write_csv.py | 14 | Excel-kompatible CSV schreiben | csv.writer, utf-8-sig, delimiter | nein | Beispiel | schreibt spam.csv | ja | kein `newline=''` (Windows: Leerzeilen) | Tabelle |
| write_demo1.py | 7 | writelines | writelines | nein | Beispiel | schreibt out.txt | ja | kein `encoding`, kein Kopfkommentar | Gedicht |
| write_file.py | 10 | Fuenf Zeilen schreiben | write, `\n` | nein | Beispiel | ueberschreibt panther.txt | laeuft, Ergebnis falsch | Z.4-5 fehlendes Komma: zwei Zeilen verschmelzen, 4 statt 5 Zeilen; ueberschreibt die Repo-Datei panther.txt | Gedicht |

### 3.6 kap-18 (Datenbankzugriff)

Nur statisch geprueft (Details und Demo-Anpassungen in Kap. 6).

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| db_connect1.py | 6 | Verbindung oeffnen und schliessen | connect() | nein | Beispiel | mysql-connector-python, DB beispiele | statisch ok | Credentials hardcodiert (Z.3) | Schul-DB |
| db_connect2.py | 19 | Verbindung mit Fehlerbehandlung | errorcode, try/except/else | nein | Beispiel, nach offizieller Connector-Doku | dito | statisch ok | Credentials Z.5-6; 2er-Einrueckung und englische Meldungen (Doku-Uebernahme) | Schul-DB |
| db_context.py | 41 | Kontext-Manager UseDB, SELECT mit Platzhaltern | __enter__/__exit__, `%s`-Parameter, fetchall, datetime-Formatierung | nein | Beispiel | dito, datetime | statisch ok; Abfrage liefert 0 Zeilen | Credentials Z.20-23 (Schluessel `passwd`, Kompatibilitaets-Alias); Z.14-17 commit auch bei Exception, kein rollback; Z.27-28 Zeitraum 2020; Z.35 `%H.%M` vs. `%H:%M` | Lehrveranstaltungen |
| db_insert1.py | 21 | INSERT adresse und student mit lastrowid | `%s`-Parameter, lastrowid, commit | nein | Beispiel | dito | statisch ok; Spalten passen | Credentials Z.4; fiktive Person mit E-Mail-Adresse unter einer nicht reservierten, moeglicherweise realen Domain; nicht idempotent; kein rollback; Kommentar nennt `adr_id` (Spalte heisst `adresse_id`) | Studierende/Adresse |
| db_select1.py | 18 | SELECT * mit Cursor | cursor, fetchall | nein | Beispiel | dito | statisch: Fehlerpfad NameError | Credentials Z.4-5; Z.6-9 nach Verbindungsfehler weiter mit `cnx` (NameError); `SELECT *` | Standorte |
| db_select2.py | 22 | SELECT mit Platzhaltern, Iteration ueber Cursor | `%s`-Parameter, datetime | nein | Beispiel, Muster der Connector-Doku | dito, datetime | statisch ok; Abfrage liefert 0 Zeilen | Credentials Z.5-8; Z.12-13 Zeitraum 2020; Z.17 `%H.%M` | Lehrveranstaltungen |

### 3.7 kap-19 (Vererbung)

| Datei | Z. | Zweck | Konzepte | Inter. | Typ | Abhaengigkeiten | 3.11 | Bugs, veraltete Idiome | Szenario |
|---|---|---|---|---|---|---|---|---|---|
| autos.py | 83 | Auto, Cabrio, Transporter | Vererbung, super(), Default-Parameter, __repr__, pass | nein | Beispiel | keine | ja (nur Definitionen) | Z.68 `ladung += kg` statt `self.ladung`: UnboundLocalError, beladen() nie funktionsfaehig; Z.35 Attribut `reichweite` ausserhalb __init__; Tippfehler in Docstrings | Autos |
| computer.py | 96 | Loesung Aufgabe 1 Kap. 19: Computer, Server, Laptop | Vererbung, Properties, private Attribute | nein | Buchaufgabe | datetime, time | nein: AttributeError Z.60 | Z.12/20 `datetime.today` ohne Klammern; Z.35-36 uptime() ohne self, falsche Attribute; Z.39 `\s` ungueltige Escape-Sequenz; Z.53 `self.__running` in Unterklasse (Name Mangling, AttributeError); Z.60 Zuweisung an Property ohne Setter; Z.65 und Z.36 lesen `start_time`, das erst nach zuklappen() (Z.75) existiert, die Basisklasse nutzt `__start_time`; Z.71/74 setzen eigenes privates Attribut statt dem der Basis; Z.79 `hostname` fehlt bei Laptop; mutable Defaults; Z.90 `c1.ping` ohne Klammern; ungenutzte Imports | Computer-Inventar |
| diamond.py | 18 | Mehrfachvererbung, MRO | Diamant-Problem, MRO | nein | Beispiel | keine | ja | Einrueckung Z.15 inkonsistent; Mehrfachvererbung laut Handoff U7.2 ausklammern | Fahrzeuge/Pedelec |
| inheritance1.py | 25 | Unterklasse erweitert Basisklasse | super().__init__, neue Methode | nein | Beispiel | keine | ja | kein Main-Guard | Person/Student |
| inheritance2.py | 24 | Methode ueberschreiben mit super() | Ueberschreiben, super().methode() | nein | Beispiel | keine | ja | Jochen Reinholdt als Beispielperson | Person/Student |
| simple_person.py | 27 | person, student, dozent | Vererbung, super() | nein | Beispiel | keine | ja (keine Ausgabe) | Klassennamen klein (PEP 8); kein Testcode | Person/Student/Dozent |

### 3.8 Uebergreifende veraltete Idiome (fuer Kasten "Aktuelle Schreibweise")

| Idiom im Repo | Vorkommen (Auswahl) | Aktuelle Schreibweise |
|---|---|---|
| `str.format()` und `+`-Verkettung | fast alle Dateien | f-Strings |
| `== True`, `== None`, `!= None` | import_demo1/2, computer.py (16/19), adressbuch.py, wordstat.py | `if x:`, `is None`, `is not None` |
| `for k in d.keys()` | adressbuch*, var_kwargs_demo.py | `for k in d`, `d.items()` |
| `open()` ohne `encoding` | copy_lines*, num_lines, oldschool, append, read_file, write_file, write_demo1, json_demo, json_dump | immer `encoding='utf-8'` (Windows-Default ist bis Python 3.14 die Systemcodepage) |
| CSV ohne `newline=''` | adressbuch05/06/07, read_csv, write_csv, find_overlap | `open(..., newline='')` gemaess csv-Doku |
| `datetime.strftime(obj, fmt)` | bank2d.py, person.py, kap-19/computer.py | `obj.strftime(fmt)` |
| Validierung per `print` statt Exception | mitarbeiter*, ma_magic, person, bank2d | `raise ValueError(...)` |
| Mutable Default-Argumente | kap-16/computer.py, kap-19/computer.py | `None` als Default |
| Getter/Setter-Methoden | mitarbeiter.py, person.py | @property (im Repo als Kontrast gewollt) |
| Typannotationen ohne Elementtyp | myfunctions, bank2d | `list[str]`, `dict[str, int]` |
| Ungueltige Escape-Sequenzen in Strings | wordcount1/2, wordstat/2, kap-19/computer.py | Raw-String oder `\\`; ab 3.12 SyntaxWarning |

---

## 4 bank2c-Analyse (Handoff Kurzaufgabe U7.0)

### 4.1 Befund: bestaetigt

Die Handoff-Aussage ist korrekt. `Python/kap-16/bank2c.py`, Methode `Kunde.add_konto()` (Z.35-45), Zeile 42:

```python
new_nr = max([k.konto_nr for k in kunde1.konten]) + 1
```

Die Methode liest die Konten des globalen Objekts `kunde1` aus dem Hauptprogramm (Z.89) statt `self.konten`. Der erste Zweig (Z.38, erstes Konto) verwendet korrekt `self.kunde_nr`, nur der zweite Zweig ist falsch. Das Programm liefert nur deshalb das erwartete Ergebnis (1001, 1002, 1003), weil das Hauptprogramm genau einen Kunden anlegt und dieser zufaellig an den globalen Namen `kunde1` gebunden ist. Praeziser als im Handoff: Es braucht nicht nur "eine Instanz", sondern die Instanz muss `kunde1` heissen und das Skript muss als Hauptprogramm laufen.

### 4.2 Wirkung und Reproduktion (in Kopie ausgefuehrt, Python 3.11)

| Szenario | Vorgehen | Ergebnis |
|---|---|---|
| A: Zweiter Kunde im Hauptprogramm | Am Ende des Main-Blocks einen `kunde2` mit Kundennummer 2000 anlegen und 3x `add_konto()` aufrufen | Kontonummern `kunde2`: **2001, 1004, 1004** (erwartet 2001, 2002, 2003). Falsches Nummernpraefix und doppelte Kontonummer innerhalb desselben Kunden, ohne Fehlermeldung. |
| B: Import als Modul | `import bank2c`, Kunde anlegen, zweimal `add_konto()` | 2. Aufruf: `NameError: name 'kunde1' is not defined` |
| C: `kunde1` existiert, hat aber noch keine Konten | anderer Kunde ruft `add_konto()` zweimal auf | 2. Aufruf: `ValueError: max() arg is an empty sequence` |
| D: Umbenennung (abgeleitet aus B) | Hauptprogramm nennt die Variable anders (z. B. `k1`) | NameError beim 2. Konto |
| Fix | Z.42 `kunde1.konten` durch `self.konten` ersetzen | `kunde2`: 2001, 2002, 2003 (verifiziert) |

Szenario A erfuellt das Handoff-Abnahmekriterium "Fehler reproduzierbar durch ein zweites Kunde-Objekt". Die drei unterschiedlichen Symptome (falsche Daten, NameError, ValueError) je nach Platzierung von `kunde2` eignen sich gut fuer die Besprechung am Beamer.

### 4.3 Weitere Maengel in bank2c.py (fuer staerkere Paare oder Besprechung)

| Zeile | Befund |
|---|---|
| 3 | Kommentar nennt `Konto.add_konto()`, die Methode gehoert zu `Kunde`. |
| 12-13 | `Kunde.__str__` gibt die Kontenliste aus; Listen verwenden `repr()`, daher erscheinen Objektadressen statt Kontodaten (Konto hat nur `__str__`). |
| 38, 42 | Nummernschema "Kundennummer + laufende Nummer" ist nicht global eindeutig: Kunde 1000 mit drei Konten belegt 1001-1003, Kunde 1001 erhaelt als erstes Konto 1002 (Kollision, auch in bank2d.py nachgewiesen). |
| 35-45 | `add_konto()` gibt das neue Konto nicht zurueck (in bank2d.py nachgeruestet). |
| 48-52 | `saldo` als float (Geldbetrag); fuer Best-Practice-Diskussion `Decimal` erwaehnen. |

### 4.4 Weitere Bugs in kap-16 (bank1, bank2b, bank2d, bank2_patrick)

| Datei | Befund |
|---|---|
| bank1.py | keine Fehler; Konto bewusst ohne Kapselung. |
| bank2b.py | keine Laufzeitfehler; Z.59 auskommentierte Getter/Setter-Alternative waere syntaktisch falsch. |
| bank2d.py | Bug aus bank2c behoben (Z.47 `self.konten`). Neu: Z.40/49 Parameter `saldo` wird angenommen, aber nicht an Konto weitergegeben (Startsaldo immer 0.0); Z.115 Auszahlung von 0 wird akzeptiert und als Bewegung gebucht, Einzahlung von 0 dagegen abgelehnt; Kontonummern-Kollision zwischen Kunden; Z.1 Kopf nennt bank2c.py; falsche Annotationen Z.27, Z.38; Z.137 `konto` ungenutzt. |
| bank2_patrick.py | Fremdmaterial einer Studierenden-Person (Name und Copyright im Kopf). Setter-Methoden alle `name` benannt, dadurch keine Setter fuer kunde/art/saldo/limit/betrag/zweck/datum (`konto.saldo = 999` wirft AttributeError); Klassenzaehler fuehrt zu Kontonummern 2000, 2001, 2001 bzw. 3001, 3001, 3001; Kunde als String `'kunde1'` uebergeben; `kontoauszug(konto1)` ersetzt den Kunden des Kontos durch das Konto; Terminal wird beim Import geloescht. Nicht im Unterricht verwenden. |

### 4.5 Eignung als Code-Review-Aufgabe (K4)

Einschaetzung: **geeignet, mit Anpassungen im Auftrag**.

Pro:
- Der Fehler ist realistisch (funktioniert im Normalfall, faellt erst bei Erweiterung auf) und verlangt Analyse von Gueltigkeitsbereich und `self`, also echtes K4.
- Reproduktion mit wenigen Zeilen moeglich; Symptome sind sichtbar und diskutierbar.
- Code ist ueberschaubar (98 Zeilen, davon rund 45 Property-Boilerplate), passt zum Input Properties unmittelbar davor.

Risiken:
- **Loesung ist oeffentlich**: `bank2d.py` Z.47 enthaelt die korrigierte Zeile; ein Diff bank2c/bank2d verraet den Fix. Auftrag deshalb auf Begruendung ausrichten (warum laeuft es im Original, welche drei Symptome, warum ist `self` zwingend), die sich nicht kopieren laesst.
- bank2c.py ist die Musterloesung der Buchaufgabe 16.12/2c. Die Uebung ist nicht identisch mit der Buchaufgabe (Review statt Implementierung), TN mit eigener Loesung kennen den Code aber.
- 15 Minuten fuer Klassendiagramm, Fehlersuche, Reproduktion und Fix ist knapp. Empfehlung: 4 min Diagramm, 5 min Suche, danach Hinweis "Schau dir add_konto an", 3 min Reproduktion, 3 min Fix und Begruendung.
- Der Suchbegriff `kunde1` innerhalb der Klasse faellt schnell auf; als Zusatz fuer schnelle Paare die Nummernkollision zwischen Kunden (Kap. 4.3) anbieten.

---

## 5 kap-17: Adressen.csv und read_csv.py (Handoff Partneruebung U6.2)

### 5.1 Befund Adressen.csv

| Merkmal | Befund | Handoff-Angabe |
|---|---|---|
| Trennzeichen | `;` | bestaetigt |
| Encoding | UTF-8 **mit BOM** (EF BB BF); ohne `utf-8-sig` lautet der erste Spaltenname `\ufeffVorname` (verifiziert) | bestaetigt |
| Zeilenenden | CRLF, letzte Zeile ohne abschliessenden Zeilenumbruch | nicht erwaehnt |
| Kopfzeile | Vorname;Name;Telefon;Strasse;Nr.;PLZ;Ort (7 Spalten) | bestaetigt, exakt |
| Zeilenzahl | 4 Zeilen: 1 Kopfzeile plus **3 Datensaetze** | "auf ~20 Zeilen erweitern" noetig, bestaetigt |
| Inhalt | fiktive Personen mit Telefonnummer und Adresse; Orte in ZH und AG; ein Umlaut, eine Hausnummer mit Buchstabe | Personendaten: ja, fiktiv; Telefonnummern im realen Schweizer Format (Vorwahlen 043/062), Existenz nicht geprueft |
| Excel-Pendant | `Adressen.xlsx` ist leer (nur Metadaten) | nicht erwaehnt |

### 5.2 Befund read_csv.py

9 Zeilen; oeffnet `Adressen.csv` mit `encoding='utf-8-sig'`, `csv.reader(..., dialect='excel', delimiter=';')`, gibt jede Zeile als Liste aus (Kopfzeile inklusive). Kein `newline=''`, keine Fehlerbehandlung, keine Verarbeitung. Laeuft unter 3.11. Als Referenz fuer U6.2 brauchbar; die Zusatzaufgabe "Datei fehlt" ist im Repo nur in `copy_lines_try.py` vorgebildet.

### 5.3 Konflikt mit den Adressbuch-Skripten

`adressbuch05.py` (kap-13, Z.100) liest `Adressen.csv`, erwartet aber das 5-Spalten-Format ohne Kopf von `Adressbuch.csv` (Name;Strasse;Nr.;PLZ;Ort). Folge: Die Kopfzeile wird zum Eintrag "Vorname", die Felder verschieben sich (Strasse erhaelt den Nachnamen, PLZ die Strasse, Ort die Hausnummer), PLZ und Ort der Datei werden ignoriert. Zudem liegt `Adressen.csv` nicht in kap-13 (FileNotFoundError). Gleiches gilt fuer `adressbuch06/07.py`, wenn dort `Adressen.csv` gewaehlt wird. Wird `adressbuch0x.py` im Material als Stilreferenz neben `Adressen.csv` mitgeliefert, muss dieser Formatunterschied erklaert oder vermieden werden.

### 5.4 Hinweise fuer die Erweiterung auf ~20 Zeilen

- Format exakt beibehalten: BOM, `;`, CRLF, gleiche Kopfzeile; abschliessenden Zeilenumbruch ergaenzen.
- 19-20 Datensaetze mit PLZ aus mehreren Regionen (z. B. 1xxx, 3xxx, 4xxx, 6xxx, 8xxx, 9xxx), damit der PLZ-Bereichsfilter sinnvolle Treffer und Nicht-Treffer liefert; Grenzwerte (erste und letzte PLZ des Bereichs) einbauen.
- Umlaute (ae/oe/ue als echte Umlaute) und Sonderfaelle (Hausnummer mit Buchstabe, leeres Telefonfeld) aufnehmen; fuer Fortgeschrittene ein Feld mit `;` in Anfuehrungszeichen.
- Eindeutig fiktive Namen und Telefonnummern verwenden; bestehende drei Nummern ersetzen.
- Encoding-Falle erklaeren: Excel "CSV UTF-8" schreibt BOM (daher `utf-8-sig`), Excel "CSV (Trennzeichen-getrennt)" unter Windows schreibt Systemcodepage ohne BOM.
- In der Musterloesung `newline=''` beim Lesen und Schreiben verwenden (sonst Leerzeilen unter Windows, siehe PY2-F09) und PLZ fuer den Bereichsvergleich mit `int()` umwandeln.
- Da das Adressbuch-Szenario aus dem Lehrmittel stammt, ist der Auftrag (PLZ-Filter plus Ergebnis-CSV) neu; im Repo existiert kein solches Skript.

---

## 6 kap-18: Grundlage der Live-Demo U6 "Datenbankzugriff aus Python"

### 6.1 Statische Pruefung

| Pruefpunkt | Befund |
|---|---|
| Treiber | `mysql.connector` (PyPI-Paket `mysql-connector-python`, nicht das veraltete Paket `mysql-connector`). Mit Version 26.7.0 im venv importierbar; `passwd` wird weiterhin als Kompatibilitaets-Alias fuer `password` akzeptiert. |
| Credentials | In allen 6 Dateien hardcodiert, Benutzername (Vorname des Autors) und Passwort (trivialer Platzhalterwert, in allen Dateien identisch). Vorhanden: db_connect1.py:3, db_connect2.py:5-6, db_context.py:20-23, db_insert1.py:4, db_select1.py:4-5, db_select2.py:5-8. Host uneinheitlich (`127.0.0.1` bzw. `localhost`, db_insert1 ohne Host), DB `beispiele`. **Handoff bestaetigt.** |
| Platzhalter vs. String-Formatierung | Alle parametrisierten Abfragen verwenden `%s` mit Tupel (db_context Z.25-31, db_insert1 Z.6-16, db_select2 Z.10-14); db_select1 nutzt eine statische Abfrage. **Keine SQL-Injection-Stelle.** Ein Negativbeispiel fuer die 2-Minuten-Demo fehlt im Repo und muss neu erstellt werden. |
| Spalten gegen create_beispiele.sql | `lehrveranstaltung(titel, beginn, ende)` vorhanden; `standort` vorhanden; `adresse(strasse, nr, plz, ort)` mit AUTO_INCREMENT `adresse_id` passt zu `lastrowid`; `student(name, email, klasse, adresse)` vorhanden, `klasse`-Wert 7 existiert. Alle Spalten stimmen. |
| Daten gegen create_beispiele.sql | **Abweichung**: `lehrveranstaltung` enthaelt 2310 Zeilen mit `beginn` vom 01.07.2021 bis 15.12.2026. db_select2.py (01.01.2020-31.12.2020) und db_context.py (01.01.2020-01.01.2021) liefern **0 Zeilen**. Nachgezaehlt: Jahr 2026 = 185, November 2026 = 14, Woche 16.-22.11.2026 = 3, Tag 20.11.2026 = 1 Treffer. |
| Fehlerbehandlung | db_select1.py Z.6-9 faengt Verbindungsfehler ab und arbeitet danach mit undefiniertem `cnx` weiter (NameError). db_context.py `__exit__` committet auch bei Exception, kein rollback. db_insert1.py ohne try und rollback, jeder Lauf fuegt erneut ein. |
| Kosmetik | Z.35 bzw. Z.17: Beginn mit `%H.%M`, Ende mit `%H:%M` formatiert. db_connect2.py und db_select2.py folgen eng den Beispielen der offiziellen Connector-Dokumentation (2er-Einrueckung, englische Meldungen). |

### 6.2 Anpassungen fuer die Demo

1. **Zeitraum anpassen**: z. B. November 2026 (14 Treffer) oder Woche um den Unterrichtstag; im Drehbuch die erwartete Trefferzahl nennen. Ohne Anpassung zeigt die Demo ein leeres Ergebnis.
2. **Credentials auslagern**: `config.py` (in `.gitignore`) oder Umgebungsvariablen (`os.environ`), Schluessel `password` statt `passwd`, Host einheitlich `127.0.0.1`. Lernpunkt: das Repo ist oeffentlich, hardcodierte Zugangsdaten landen in der Historie.
3. **Installation**: im venv `pip install mysql-connector-python`; Hinweis auf das gleichnamige veraltete Paket `mysql-connector`.
4. **Kontext-Manager**: `__exit__` mit rollback bei Exception, commit nur im Erfolgsfall; Kasten "Aktuelle Schreibweise": Verbindung und Cursor des Connectors unterstuetzen selbst `with` (geprueft mit 26.7.0), `__exit__` der Verbindung schliesst aber nur und committet nicht; `commit()` bleibt explizit noetig.
5. **SQL-Injection-Demo neu erstellen**: bewusst verwundbare f-String-Variante (z. B. Suche nach `titel`) gegen die `%s`-Variante stellen; das Repo liefert nur die sichere Variante.
6. **db_select1.py nicht als Vorlage verwenden** oder Fehlerpfad korrigieren (Abbruch nach Verbindungsfehler).
7. **SQLite-Fallback**: Platzhalter sind dort `?` statt `%s`, `datetime` wird als Text gespeichert; im Drehbuch ausdruecklich auf diese Unterschiede hinweisen, sonst ist die Demo nicht "identisch".
8. **db_insert1.py** hoechstens als Ausblick zeigen: nicht idempotent, schreibt in die gemeinsame Muster-DB; enthaelt eine fiktive E-Mail-Adresse unter einer moeglicherweise realen Domain (fuer Beispiele `example.org` verwenden).
9. Formatstring vereinheitlichen (`%H:%M`).

---

## 7 Datendateien-Uebersicht

| Datei | Format | Encoding/BOM | Trenner | Zeilenenden | Umfang | Inhalt | Personendaten | Genutzt von | Bewertung |
|---|---|---|---|---|---|---|---|---|---|
| Adressbuch.csv | CSV | UTF-8 mit BOM | `;` | CRLF | 6 Zeilen, 5 Spalten, ohne Kopf | Name;Strasse;Nr.;PLZ;Ort | ja, fiktive Namen und Adressen | adressbuch06/07 (Default-Speichername) | behalten |
| Adressen.csv | CSV | UTF-8 mit BOM | `;` | CRLF, letzte ohne | 1 Kopf + 3 Datensaetze, 7 Spalten | Vorname;Name;Telefon;Strasse;Nr.;PLZ;Ort | ja, fiktive Namen, Telefonnummern im Realformat, Adressen | read_csv.py, adressbuch05.py | erweitern (Kap. 5) |
| Adressen.xlsx | XLSX | n/a | n/a | n/a | 1 Blatt "Tabelle1", **leer** | nur Metadaten (erstellt 01.06.2019, Mac-Excel) | ja, Metadaten mit Ersteller- und Bearbeitername (nicht Jochen Reinholdt) | nicht referenziert | entfernen oder befuellen |
| spam.csv | CSV | UTF-8 mit BOM | `;` | CRLF | 3 Zeilen, 3 Spalten | Platzhaltertext "Zeile x Spalte y", eine leere Zelle | nein | Ausgabe von write_csv.py | behalten (reproduzierbar) |
| spam.xlsx | XLSX | n/a | n/a | n/a | 1 Blatt, **leer** | nur Metadaten | ja, Metadaten wie oben | nicht referenziert | entfernen oder befuellen |
| MontyPython.json | JSON | ASCII | n/a | LF | 3 Objekte | Name, Beruf, Geburtsjahr, Gruendungsmitglied | ja, reale Personen des oeffentlichen Lebens (Mitglieder einer Komikergruppe) | json_demo.py | unkritisch, ggf. durch fiktive Daten ersetzen |
| students.json | JSON | ASCII (json.dump mit ensure_ascii) | n/a | ohne Zeilenumbruch | 1 Zeile, 3 Datensaetze | Studiengang, Name, Vorname, Noten; ein Schluessel mit Leerzeichen, ein Datensatz ohne Noten | ja, fiktive Namen mit Noten | Ausgabe von json_dump.py | behalten (reproduzierbar) |
| students.pkl | Pickle Protokoll 3 | binaer | n/a | n/a | 418 Bytes, dict mit int-Schluesseln | wie JSON, aber Zustand nach pickle_modify (geaenderter Vorname, zusaetzliche Noten) | ja, fiktiv | pickle_load/modify | pickletools: nur dict/str/int, keine GLOBAL/REDUCE-Opcodes, unbedenklich; als Laufzustand entfernen, im Unterricht selbst erzeugen |
| panther.txt | TXT | ASCII | n/a | LF, letzte ohne | 5 Zeilen | Scherzgedicht, im Kopf einem zeitgenoessischen Autor zugeschrieben (Name vermutlich falsch geschrieben) | nein | read_file.py, write_file.py (ueberschreibt) | Urheberrecht pruefen, durch eigenen Text ersetzen |
| file_name | CSV | UTF-8 mit BOM | `;` | CRLF | 5 Zeilen, 5 Spalten | 4 Zeilen aus Adressbuch.csv plus 1 Testeintrag mit vertauschter PLZ/Ort | ja, fiktiv | keines (Laufausgabe) | entfernen |
| file_name 2 | CSV | wie file_name | `;` | CRLF | identisch (gleiche Pruefsumme) | Duplikat | ja, fiktiv | keines | entfernen |
| IFA-TimeOverlap.csv | CSV | UTF-8 ohne BOM | `;`, alle Felder in Anfuehrungszeichen | LF | 256 Zeilen, 6 Spalten (Datum, Start, Ende, Titel, Ort, Dauer) | Kalenderexport 30.08.2019 bis 30.09.2020 | **ja, real**: Unterrichtstermine und private, teils sensible Termine, Namen Dritter (Details bewusst nicht wiedergegeben) | nicht referenziert | **sofort entfernen, auch aus Historie** |
| daten.csv | CSV | UTF-8 ohne BOM | `;`, quotiert | LF | 165 Zeilen, 34 Spalten (Outlook-artiger Export mit Zeitzonen) | Kalenderexport 31.10.2019 bis 04.12.2020 | **ja, real**: wie oben (Details bewusst nicht wiedergegeben) | find_overlap.py, test_ics_package.py | **sofort entfernen, auch aus Historie** |

---

## 8 Verbrauchte Szenarien und Aufgabentypen

Diese Szenarien sind durch Lehrmittel und oeffentliches Repo belegt und fuer neue Unterrichtsuebungen zu meiden (oder nur mit klar neuer Aufgabenstellung zu verwenden).

| Szenario | Dateien | Aufgabentyp und Konzepte |
|---|---|---|
| Adressbuch (Name zu Adresse) | kap-13 adressbuch*, kap-15 adressbuch07, kap-17 adressbuch06, Adressbuch.csv, Adressen.csv, read_csv | Menuegesteuertes CRUD-Konsolenprogramm, schrittweiser Ausbau, dict, Funktionen, CSV-Import/-Export |
| Bank: Kunde, Konto, Kontobewegung | kap-16 bank1/2b/2c/2d, bank2_patrick | Klassen mit Properties, Kontonummern-Generierung, Ein-/Auszahlung mit Limit, Kontoauszug |
| Mitarbeiter mit Lohnklassen | kap-16 mitarbeiter, mitarbeiter_property, ma_magic | Klassenvariable, Validierung im Setter, Getter/Setter vs. Property, __eq__/__repr__ |
| Computer, Server, Laptop (Inventar) | kap-16 computer, kap-19 computer | Klasse mit Zustand (boot/shutdown/ping), Vererbung, Batterie-Property |
| Haus | kap-16 haus | Erste Klasse mit Attributen und Methoden |
| Person mit Geburtstag | kap-16 person | Datumsvalidierung, Name Mangling |
| Person, Student, Dozent | kap-19 inheritance1/2, simple_person | Vererbung, super(), Methoden ueberschreiben |
| Autos: Auto, Cabrio, Transporter | kap-19 autos | Vererbung mit Tank/Verbrauch/Ladung |
| Fahrzeug, Motorfahrzeug, Velo, Pedelec | kap-19 diamond | Mehrfachvererbung, MRO |
| Studierende mit Noten | kap-17 json_dump, pickle_*, students.* | Verschachteltes dict, JSON- und Pickle-Roundtrip |
| Wortzaehlung, Wortstatistik | kap-17 wordcount1/2, wordstat, wordstat2 | Text bereinigen, set fuer verschiedene Woerter, dict als Zaehler, Sortierung |
| Datei kopieren, nummerieren, anhaengen | kap-17 copy_lines*, num_lines, append, oldschool | Zeilenweises Lesen/Schreiben, with, Fehlerbehandlung beim Oeffnen |
| Gedicht schreiben/lesen | kap-17 write_file, write_demo1, read_file | write/writelines |
| Excel-CSV (spam) | kap-17 write_csv, read_csv | csv mit `;` und utf-8-sig |
| Terminueberschneidung/Reisezeit | kap-17 find_overlap | Kalender-CSV, datetime-Arithmetik |
| Verzeichnisoperationen | kap-17 testos | os-Modul |
| Laender und Sprachen, Beipackzettel | kap-13 Aufgabe2, beipack | Mengenoperationen, dict mit Tupeln |
| Lotto 6 aus 49 | kap-13 lotto_mengen (auch fruehere Kapitel) | set, Zufallszahlen |
| Zahlen-Validierung und Eingabe | kap-14/15 myfunctions, read_int, import_demo* | is_int/is_float/read_int/yes, Modul-Import |
| Primzahl, ggT, kgV, Primfaktoren | kap-14 myfunctions, kap-15 ggt_rekursiv | Algorithmen als Funktionen |
| Fakultaet, Fibonacci | kap-15 fak_rekursiv, fib_rekursiv | iterativ vs. rekursiv, Laufzeitmessung, Memoisierung |
| Parameterarten | kap-15 default/kwargs/pos/var/var_kwargs_demo, reihenfolge | Defaults, *args, **kwargs, keyword-only |
| Schul-DB: Lehrveranstaltungen nach Datum, Standorte, neue Adresse plus Student | kap-18 | SELECT mit Datumsbereich, SELECT *, INSERT mit lastrowid (Master-Detail) |

Folgerungen fuer das Handoff:
- U6.1 "Spesenabrechnung" ist im Repo nicht belegt: frei.
- U7.1 "Kurs und Teilnehmer" ist frei, liegt aber nahe an Person/Student/Dozent (kap-19); keine Klassen `Person`/`Student`/`Dozent` verwenden.
- U7.2 neues Szenario waehlen; Autos, Fahrzeuge, Computer, Mitarbeiter und Person sind belegt; `diamond.py` nicht als Referenz nutzen (Mehrfachvererbung).
- Selbststudium U6: Beispielideen ausserhalb von Adressbuch, Bank, Wortstatistik, Studierende/Noten und Kalender waehlen.

---

## 9 Bereinigungsliste (Rework)

| Prio | Datei(en) | Grund | Massnahme |
|---|---|---|---|
| 1 | kap-17/IFA-TimeOverlap.csv, kap-17/daten.csv | Reale private Personendaten des Autors und Dritter im oeffentlichen Repo | Entfernen und Git-Historie bereinigen (Loeschen im aktuellen Stand genuegt bei oeffentlichem Fork nicht); Autor informieren |
| 1 | kap-16/bank2_patrick.py, kap-16/color.py | Studierenden-Abgabe mit vollem Namen und Copyright-Vermerk | Entfernen (oder nur mit Einwilligung anonymisiert behalten) |
| 2 | kap-17/find_overlap.py, kap-17/test_ics_package.py | Persoenliches Werkzeug ohne Kursbezug; test_ics_package defekt und importiert ungenutztes Drittpaket | Entfernen oder find_overlap mit synthetischen Daten als Zusatzbeispiel neu aufsetzen |
| 2 | kap-17/file_name, kap-17/file_name 2 | Laufausgabe und Finder-Duplikat | Entfernen |
| 2 | kap-17/copy_lines_try.1.py, kap-15/reihenfolge.1.py | Editor-/Finder-Kopien, .1 teils defekt, Dateiname nicht importierbar | copy_lines_try.1 entfernen; reihenfolge.1 inhaltlich in reihenfolge.py uebernehmen |
| 2 | kap-17/students.pkl | Binaerer Laufzustand (nach pickle_modify) | Entfernen, durch pickle_dump.py erzeugen lassen |
| 2 | kap-17/Adressen.xlsx, kap-17/spam.xlsx | Leere Arbeitsmappen, nicht referenziert, Ersteller-Metadaten | Entfernen oder mit Inhalt passend zur CSV fuellen und Metadaten leeren |
| 3 | kap-14/function_demo.py, kap-14/testfunctions.py, kap-17/testos.py, kap-17/wordstat2.py, kap-19/computer.py | Entwurf bzw. abbrechende Skripte | Korrigieren oder bewusst als Fehlersuch-Material kennzeichnen |
| 3 | kap-14/myfunctions.py und kap-15/myfunctions.py | Gleicher Modulname, unterschiedliche API, beide mit Fehlern | Eine korrigierte Fassung, klar benannt |
| 3 | kap-15/adressbuch07.py und kap-17/adressbuch06.py; kap-13/adressbuch.py, adressbuch002.py | Nahezu identische Dateien in verschiedenen Kapiteln; Nebenvarianten mit falschen Docstrings | Reihe konsolidieren, Varianten entfernen |
| 3 | kap-17/panther.txt, write_file.py, write_demo1.py, read_file.py | Vollstaendiges Gedicht mit unklarer Rechtelage | Durch eigenen oder gemeinfreien Text ersetzen |
| 3 | kap-18/*.py | Hardcodierte Credentials | Auslagern (config.py/.env, .gitignore) |
| 4 | Docstrings mit falschen Dateinamen | adressbuch.py, adressbuch002.py, adressbuch03.py, adressbuch04.py, lotto_mengen.py, kommandozeile.py, json_demo.py, read_file.py, pickle_modify.py, bank2d.py, test_ics_package.py, reihenfolge.1.py | Korrigieren |

Hinweis: Im Umfang kap-13 bis kap-19 gibt es keine `__pycache__`-Ordner und keine weiteren Binaerdateien ausser den zwei XLSX und der PKL-Datei.

---

## 10 Findings

| ID | Schwere | Datei:Zeile | Befund | Vorschlag |
|---|---|---|---|---|
| PY2-F01 | hoch | kap-17/IFA-TimeOverlap.csv:1-256; kap-17/daten.csv:1-165 | Private Kalenderexporte 2019-2020 im oeffentlichen Repo mit privaten, teils sensiblen Eintraegen und Namen Dritter (Details bewusst nicht wiedergegeben). IFA-TimeOverlap.csv wird von keinem Skript genutzt. | Beide Dateien entfernen und Historie bereinigen; find_overlap nur mit synthetischen Daten weiterfuehren; Autor informieren. |
| PY2-F02 | hoch | kap-18/db_select2.py:12-13; kap-18/db_context.py:27-28 | Datumsbereich 2020 liefert gegen create_beispiele.sql 0 Zeilen (Daten 01.07.2021 bis 15.12.2026). Live-Demo U6 zeigt ohne Anpassung ein leeres Ergebnis. | Zeitraum auf z. B. November 2026 (14 Treffer) setzen und Trefferzahl im Drehbuch nennen. |
| PY2-F03 | hoch | kap-16/bank2c.py:42 | `add_konto()` nutzt globales `kunde1.konten` statt `self.konten` (Handoff bestaetigt). Zweiter Kunde erhaelt Kontonummern 2001, 1004, 1004; Import als Modul ergibt NameError; leerer `kunde1` ergibt ValueError. | Fuer U7.0 wie geplant nutzen; Auftrag auf Begruendung und drei Symptome ausrichten, da bank2d.py:47 die Korrektur oeffentlich zeigt. |
| PY2-F04 | hoch | kap-16/bank2_patrick.py:1-4; kap-16/color.py:1-4 | Studierenden-Abgabe mit vollem Namen und Copyright-Vermerk im oeffentlichen Repo (Personendaten, Rechte unklar). | Entfernen oder nur mit Einwilligung anonymisieren; nicht im Unterricht zeigen. |
| PY2-F05 | mittel | kap-18: db_connect1.py:3, db_connect2.py:5-6, db_context.py:20-23, db_insert1.py:4, db_select1.py:4-5, db_select2.py:5-8 | Benutzername und Passwort hardcodiert, in allen Dateien identisch; Schluessel `passwd` (Alias); Host uneinheitlich. | config.py in .gitignore oder Umgebungsvariablen; `password`; Host einheitlich; als Lernpunkt im Drehbuch. |
| PY2-F06 | mittel | kap-18/db_select1.py:3-9 | Verbindungsfehler wird nur ausgegeben, danach `cnx.cursor()` mit undefiniertem `cnx` (NameError). | Nach Fehler abbrechen oder Code in `else`-Block. |
| PY2-F07 | mittel | kap-18/db_context.py:14-17 | `__exit__` committet immer, auch bei Exception; kein rollback. | Bei Exception rollback, sonst commit; Kasten "Aktuelle Schreibweise" mit `with` des Connectors (schliesst nur, committet nicht). |
| PY2-F08 | mittel | kap-17/Adressen.csv:1-4; kap-13/adressbuch05.py:100 | Nur 3 Datensaetze; 7 Spalten mit Kopf. adressbuch05 liest diese Datei, erwartet aber 5 Spalten ohne Kopf (falsche Feldzuordnung) und findet sie im eigenen Ordner nicht. | Datei gemaess Kap. 5.4 auf ~20 Zeilen erweitern; Formatunterschied zu Adressbuch.csv im Material erklaeren oder adressbuch05 auf Adressbuch.csv umstellen. |
| PY2-F09 | mittel | kap-17/adressbuch06.py:20,38; kap-15/adressbuch07.py:20,38; kap-17/write_csv.py:10; kap-17/read_csv.py:5; kap-13/adressbuch05.py:8 | CSV ohne `newline=''`: unter Windows schreibt csv.writer `\r\r\n`; beim Wiedereinlesen entstehen Leerzeilen, `read_csv_data()` bricht mit IndexError ab (simuliert). Relevant fuer BYOD Windows. | Im Material durchgaengig `newline=''`; leere Zeilen beim Lesen ueberspringen. |
| PY2-F10 | mittel | kap-17: copy_lines.py:10, copy_lines_try.py:12, num_lines.py:10, oldschool.py:6-7, append.py:5, read_file.py:4, write_file.py:8, write_demo1.py:6, json_demo.py:5, json_dump.py:16 | `open()` ohne `encoding`: unter Windows Systemcodepage, unter macOS UTF-8; Umlaute verhalten sich je nach Laptop unterschiedlich. | `encoding='utf-8'` als Regel im Material. |
| PY2-F11 | mittel | kap-14/myfunctions.py:36-48, 63-70, 84-97, 108-109; kap-14/testfunctions.py:18 | Musterloesungen fehlerhaft: read_float UnboundLocalError, kgv TypeError und falsche Formel, mittel mit Debug-print und TypeError bei Strings, is_prime(0/1) True; Testskript bricht ab. | Nicht als Musterloesung weitergeben; eigene, getestete Loesungen erstellen. |
| PY2-F12 | mittel | kap-15/myfunctions.py:28, 41, 50 | read_int/read_float verwenden undefiniertes `zahl` (NameError); summe TypeError bei String-Zahlen; API unterscheidet sich von kap-14/myfunctions.py. | Korrigieren; nur eine Fassung des Moduls fuehren. |
| PY2-F13 | mittel | kap-15/fib_rekursiv.py:15-17; kap-15/fak_rekursiv.py:3-5 | fib_i liefert fib(n-1) (Laufzeitvergleich vergleicht verschiedene Werte); fak_i(0) liefert 0. | Korrigieren; bei Einsatz als Demo Testausgabe der Werte ergaenzen. |
| PY2-F14 | mittel | kap-19/computer.py:12, 20, 35-36, 39, 53, 60, 65, 71-79, 90 | Musterloesung Aufgabe 1 Kap. 19 bricht mit AttributeError ab; mehrere Fehler zu Name Mangling, Property ohne Setter, fehlende Klammern, ungueltige Escape-Sequenz. | Nicht als Referenz verwenden; allenfalls als zweite Code-Review-Aufgabe (anspruchsvoller als bank2c). |
| PY2-F15 | mittel | kap-19/autos.py:68 | `ladung += kg` statt `self.ladung += kg`: beladen() wirft immer UnboundLocalError (ausser bei Ueberladung). | Korrigieren, falls als Vererbungsbeispiel gezeigt. |
| PY2-F16 | mittel | kap-13/lotto_mengen.py:9, 25 | Tipp ist mit 6 Zahlen vorbelegt, die Benutzereingabe wird daher immer ignoriert. | `tipp = set()` initialisieren. |
| PY2-F17 | mittel | kap-13/adressbuch.py:35-36, 64, 81-87, 92 | NameError bei Anzeigen/Suchen (`ueberschrift`, `formatstr` nur lokal); update() speichert None bei unbekanntem Namen. | Variante entfernen (Reihe 01-05 genuegt). |
| PY2-F18 | mittel | kap-13/adressbuch05.py:20-22 | menu() gibt die Eingabe ohne lower() zurueck: Grossbuchstaben werden akzeptiert, aber ignoriert, mit `B` kann nicht beendet werden. | `return auswahl.lower()`. |
| PY2-F19 | mittel | kap-17/wordcount1.py:29-42,51,53; wordcount2.py:32-45,54,56; wordstat.py:32-45,63; wordstat2.py:32-45,60,81 | file_to_list() ignoriert den Parameter und nutzt globale Variable; Fehlerpfad NameError (`in_dname`); fehlender None-Check; wordstat2 `list.sorted` AttributeError; ungueltige Escape-Sequenzen (ab 3.12 SyntaxWarning). | Korrigieren; gutes Beispiel fuer Refactoring (U6.1-Kriterium "keine globalen Variablen"). |
| PY2-F20 | mittel | kap-14/function_demo.py:19; kap-17/copy_lines_try.1.py:17-21; kap-17/test_ics_package.py:3, 44, 59-64; kap-17/testos.py:11 | Drei Dateien mit SyntaxError, eine abgeschnitten (AttributeError). | Entfernen oder vervollstaendigen (Bereinigungsliste). |
| PY2-F21 | mittel | kap-16/bank2d.py:40, 49, 115; kap-16/bank2c.py:38 | bank2d ignoriert den Parameter `saldo`, erlaubt Auszahlung 0; Kontonummern kollidieren in bank2c und bank2d zwischen Kunden mit benachbarten Kundennummern. | Als Zusatzfrage im Code-Review nutzen; in eigenen Loesungen globalen Zaehler verwenden. |
| PY2-F22 | tief | kap-16/bank2_patrick.py:9, 16, 53-58, 81-113, 151-152, 183-205, 210-212 | Setter unter falschem Namen, Kontonummern-Duplikate, String statt Objekt, Kunde wird ueberschrieben, Terminal-Loeschung beim Import. | Mit PY2-F04 entfernen. |
| PY2-F23 | tief | kap-17/write_file.py:4-5, 8 | Fehlendes Komma verschmilzt zwei Zeilen (4 statt 5); Skript ueberschreibt die Repo-Datei panther.txt. | Komma ergaenzen, in eigene Ausgabedatei schreiben. |
| PY2-F24 | tief | kap-17/oldschool.py:9 | `rstrip()` ohne neues `\n`: Ausgabe ist eine einzige Zeile. | `+ '\n'` ergaenzen. |
| PY2-F25 | tief | kap-16/computer.py:4-5, 33; kap-19/computer.py:5-6, 43-44, 57-58, 90 | Mutable Default-Argumente (geteilte Liste nachgewiesen); `peripherie` in kap-16 nie gespeichert; `c1.ping` ohne Klammern. | Im Best-Practice-Input U7 als Beispiel nutzen. |
| PY2-F26 | tief | kap-16/ma_magic.py:22-26; kap-16/mitarbeiter.py:21-22; kap-16/person.py:10-13 | __eq__ ohne Typpruefung und ohne __hash__; Validierung per print laesst Objekte halb initialisiert; Grenzwerte in mitarbeiter.py strikt, in der Property-Version inklusiv. | In eigenen Beispielen `raise ValueError` und `NotImplemented` verwenden. |
| PY2-F27 | tief | kap-13/beipack.py:11, 17 | Tippfehler "Ialienisch"; KeyError bei Kleinschreibung oder unbekanntem Land. | Korrigieren, `.upper()` und `.get()`. |
| PY2-F28 | tief | kap-17/file_name, "file_name 2", students.pkl, Adressen.xlsx, spam.xlsx | Laufausgaben, Duplikat, leere Arbeitsmappen mit Ersteller-Metadaten, Pickle im modifizierten Zustand (pickletools: unbedenklich). | Gemaess Bereinigungsliste entfernen. |
| PY2-F29 | tief | kap-17/panther.txt:1-5; write_file.py:2-6; write_demo1.py:1-4 | Vollstaendiges Gedicht mit unklarer Rechtelage im oeffentlichen Repo; Autorname vermutlich falsch geschrieben. | Durch eigenen oder gemeinfreien Text ersetzen. |
| PY2-F30 | tief | kap-17/Adressen.csv:2-4 | Telefonnummern im realen Schweizer Format, Existenz ungeprueft. | Beim Erweitern eindeutig fiktive Nummern verwenden. |
| PY2-F31 | tief | kap-17/pickle_load.py:5-6; kap-17/pickle_modify.py:6-7 | Kein Hinweis, dass `pickle.load` nur fuer vertrauenswuerdige Daten zulaessig ist. | Sicherheitshinweis im Material ergaenzen; JSON bevorzugen. |
| PY2-F32 | tief | kap-14/myfunctions.py:1; kap-16/computer.py:1; kap-19/computer.py:1; kap-16/bank2d.py:1 u. a. | Kopfkommentare mit falschen Dateinamen oder uneinheitlicher Kapitelzuordnung (kap-14 nennt "Kap. 13"). | Bei Verweisen auf PYGR-Kapitel die Ordnernamen nicht ungeprueft uebernehmen. |
| PY2-F33 | tief | kap-18/db_context.py:35; kap-18/db_select2.py:17; kap-18/db_insert1.py:6-18 | Zeitformat `%H.%M` vs. `%H:%M`; db_insert1 nicht idempotent, ohne rollback, fiktive E-Mail unter moeglicherweise realer Domain; Kommentar nennt `adr_id`. | Vereinheitlichen; INSERT-Demo mit try/rollback und Beispieldomain. |
| PY2-F34 | tief | kap-19/diamond.py:14; kap-19/simple_person.py:1, 9, 19 | Mehrfachvererbung (laut Handoff U7.2 ausklammern); Klassennamen klein. | Nicht als Stilreferenz verwenden. |
| PY2-F35 | tief | kap-15/fak_rekursiv.py:18; fib_rekursiv.py:32; ggt_rekursiv.py:15-16 | Ohne Kommandozeilenargument IndexError; ab n rund 1000 RecursionError (bei 3000 getestet). | In der Demo Rekursionsgrenze thematisieren; Argumentpruefung ergaenzen. |
| PY2-F36 | tief | kap-15/adressbuch07.py:73-77, 106-118, 193; kap-17/adressbuch06.py:1-2 | Toter Code in menu(); showlist/find haengen von globaler Variable ab (bei Import NameError); Aenderungsflag auch ohne Uebernahme; Docstring verspricht Speichern in dieselbe Datei. | Guter Ausgangspunkt fuer Refactoring-Diskussion, nicht als Musterloesung. |

---

## 11 Abgleich mit Handoff v2.0

| Handoff-Aussage | Ergebnis |
|---|---|
| Adressen.csv: `;`-Trenner, `utf-8-sig`, Kopfzeile Vorname;Name;Telefon;Strasse;Nr.;PLZ;Ort | bestaetigt (zusaetzlich: CRLF, nur 3 Datensaetze) |
| Adressen.csv auf ~20 Zeilen erweitern | noetig, bestaetigt; Format beibehalten, fiktive Telefonnummern (Kap. 5.4) |
| db_select2.py/db_context.py: mysql-connector, Platzhalter, Kontext-Manager UseDB | bestaetigt |
| Zugangsdaten hardcodiert | bestaetigt, in allen 6 kap-18 Dateien |
| Demo "laeuft gegen create_beispiele.sql" | **nicht ohne Anpassung**: Datumsbereich 2020 liefert 0 Zeilen (PY2-F02) |
| bank2c.py: `add_konto()` nutzt `kunde1` statt `self` | bestaetigt, Z.42; Reproduktion mit `kunde2` ergibt 2001, 1004, 1004 |
| bank2c.py "unveraendert mitliefern" | moeglich; Risiko: Fix steht oeffentlich in bank2d.py Z.47 |
| kap-13 adressbuch01-05 als Stilreferenz | geeignet (01-04 laufen); 05 benoetigt Adressbuch.csv-Format und hat den Grossbuchstaben-Fehler |
| kap-15/kap-19 als Niveaureferenz U6/U7 | geeignet fuer kap-15 (ausser myfunctions, fib_i) und inheritance1/2; kap-19 computer.py und autos.py fehlerhaft, diamond.py ausklammern |
