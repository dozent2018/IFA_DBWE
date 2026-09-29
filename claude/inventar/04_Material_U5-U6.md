# Inventar 04: Material Unit 5 und Unit 6 (Google Drive)

Kurs DBWE.TA1A "Datenbanken und Web-Entwicklung", IFA Höhere Fachschule, Präsenz, BYOD. Lehrmittel PYGR/DBSQL von Jochen Reinholdt.
Gegenstand: Drive-Ordner `02_Materialien/Unit_5_*`, `02_Materialien/Unit_6_*` (je inkl. `code/`) und zwei Aufträge aus `04_Selbststudium`.
Erstellt: 29.09.2026. Bezug: KI-Handoff v2.0 (Zeilen 1-110, 254-284, 373-418, 419-542), WP1-Übersicht vom 02.09.2026, Unterrichtsplan S2610 vom 18.09.2026 (Abschnitt 4, WP 3 / KT3 am 20.11.2026).

Hinweis zum öffentlichen Repo: Diese Datei enthält bewusst keine Musterlösungen, keine Kontrollwerte, keine Quiz-Lösungen, keine Drive-IDs und keine Personennamen aus den Testdaten. Kontrollwerte werden nur als "stimmt / stimmt nicht" berichtet.

---

## 1 Gelesener Umfang und Methode

### 1.1 Vollständig gelesene Drive-Dateien

| Nr | Datei (Drive-Pfad) | Art der Beschaffung | Grösse Drive | Grösse lokal | vollständig gelesen |
|---|---|---|---|---|---|
| 1 | Unit_5/Partneruebung_U5.1_Sequenztypen.md | read_file_content | - | - | ja |
| 2 | Unit_5/Partneruebung_U5.2_Dictionaries.md | read_file_content | - | - | ja |
| 3 | Unit_5/Quiz_U5_Datenstrukturen.md | read_file_content | - | - | ja |
| 4 | Unit_5/Coaching-Leitfaden_U5_Review-Datenmodelle.md | read_file_content | - | - | ja |
| 5 | Unit_5/code/loesung_u5_1_sequenztypen.py | download (base64), byte-genau | 4982 B | 4982 B | ja |
| 6 | Unit_5/code/loesung_u5_2_dictionaries.py | download (base64), byte-genau | 5561 B | 5561 B | ja |
| 7 | Unit_6/Partneruebung_U6.1_Funktionen-entwerfen.md | read_file_content | - | - | ja |
| 8 | Unit_6/Partneruebung_U6.2_Dateien-Kontextmanager.md | read_file_content | - | - | ja |
| 9 | Unit_6/Live-Demo-Drehbuch_U6_Datenbankzugriff.md | read_file_content | - | - | ja |
| 10 | Unit_6/Quiz_U6_Module-Persistenz.md | read_file_content | - | - | ja |
| 11 | Unit_6/code/spesen_monolith.py | download, byte-genau | 3709 B | 3709 B | ja |
| 12 | Unit_6/code/loesung_u6_1_spesen_refactored.py | download, byte-genau | 7093 B | 7093 B | ja |
| 13 | Unit_6/code/loesung_u6_2_csv.py | download, byte-genau | 8492 B | 8492 B | ja |
| 14 | Unit_6/code/demo_u6_sqlite.py | download, siehe Hinweis | 6176 B | 6176 B | ja |
| 15 | Unit_6/code/demo_u6_mysql.py | download, siehe Hinweis | 6123 B | 6123 B | ja |
| 16 | Unit_6/code/config_beispiel.py | download, byte-genau | 921 B | 921 B | ja |
| 17 | Unit_6/code/Adressen.csv | download, byte-genau | 1156 B | 1156 B | ja |
| 18 | 04_Selbststudium/Selbststudium_U5_PYGR_Kap9-13.md | read_file_content | - | - | ja |
| 19 | 04_Selbststudium/Selbststudium_U6_Programm-mit-Persistenz.md | read_file_content | - | - | ja |

Hinweis zu Nr. 14 und 15: Beim Übertragen des base64-Texts gingen in Kommentar-Trennlinien (`# ====...`) 2 bzw. 3 Zeichen verloren. Alle übrigen Trennlinien aller Codedateien sind einheitlich 71 Zeichen lang; die fünf kurzen Linien wurden auf 71 Zeichen ergänzt. Danach stimmen die Byte-Grössen exakt mit den Drive-Metadaten überein, `py_compile` ist fehlerfrei. Inhaltlich (Code, Strings) war nichts betroffen.

Rohkopien der Codedateien für andere Agents: `scratchpad/drive/Unit_5/code/` und `scratchpad/drive/Unit_6/code/` (Dateinamen wie im Drive). Die Markdown-Dateien wurden nur gelesen, nicht lokal abgelegt; `scratchpad/drive/04_Selbststudium/` ist leer.

Inhalt des Drive-Ordners `Unit_6/code/` per Ordnerabfrage geprüft: genau 7 Dateien (Nr. 11 bis 17). **`beispiele.sqlite` und eine `.gitignore` fehlen.**

### 1.2 Referenzen

- Handoff v2.0 lokal: Zeilen 1-110, 254-284, 373-418, 419-542 vollständig.
- WP1-Übersicht (Drive) vollständig.
- Unterrichtsplan S2610 (Drive) vollständig, Schwerpunkt Abschnitt 4 (WP 3 / KT3) und PP8-Outline.
- Repo, vollständig gelesen: `Python/kap-16/bank2c.py` (plus Diff zu `bank2b.py`, `bank2d.py`), alle 6 Dateien in `Python/kap-18/`, `Python/kap-17/read_csv.py`, `write_csv.py`, `copy_lines_try.py`, `copy_lines_try.1.py`, `adressbuch06.py`, `append.py`, `Adressen.csv`; teilweise: `kap-13/adressbuch05.py` (Z. 1-80), `kap-13/Aufgabe2.py`, `kap-13/lotto_mengen.py` (Kopf), `kap-15/adressbuch07.py` (Struktur), `kap-17/wordstat.py` (Kopf), Kopfzeilen aller Dateien in `kap-9`, `kap-11`, `kap-12`, `kap-14`. `SQL/create_beispiele.sql`: Tabellen `adresse`, `fach`, `lehrveranstaltung`, `pruefung`, `raum`, `standort` (Spalten, Collation).

### 1.3 Ausgeführte Codes (Übersicht, Details in Abschnitt 5)

Alle Läufe in Kopien unter `scratchpad/run/u5u6/` (nie im Repo). Python 3.11.15 (Standard), zusätzlich 3.12 und 3.13.

| Datei | ausgeführt | Versionen |
|---|---|---|
| loesung_u5_1_sequenztypen.py | ja | 3.11, 3.12, 3.13 |
| loesung_u5_2_dictionaries.py | ja, plus 3 Randfall-Varianten | 3.11, 3.12, 3.13 |
| spesen_monolith.py | ja, plus Tarif-Variante | 3.11, 3.12, 3.13 |
| loesung_u6_1_spesen_refactored.py | ja, plus diff, 2b-Test, Tarif-Variante | 3.11, 3.12, 3.13 |
| loesung_u6_2_csv.py | ja, plus Aufgabe-1a-Code gegen Drive- und Repo-CSV | 3.11, 3.12, 3.13 |
| demo_u6_sqlite.py | ja: ohne DB und mit einer vorhandenen SQLite-Portierung (Kurztest) | 3.11 |
| demo_u6_mysql.py | nein, nur statisch (Auftrag; MySQL-8-Test macht ein anderer Agent) | Kompilierung 3.11 |
| config_beispiel.py | statisch | - |
| Repo `kap-16/bank2c.py` | ja (für U7-Lücke), mit zweitem Kunden und als Import | 3.11 |

Keine eigene SQLite-Datenbank gebaut. Für den Kurztest wurde die bereits im Scratchpad liegende `beispiele.sqlite` verwendet (von einem anderen Agenten mit `scratchpad/parse_dump.py` aus `SQL/create_beispiele.sql` erzeugt), in eine Kopie gelegt und danach wieder entfernt.

---

## 2 Inventar-Tabelle

Legende Einsatz: "Material" = Angabe im Material bzw. Handoff; "Plan" = Unterrichtsplan S2610, KT3 (Fr, 20.11.2026).

| Nr | Datei | Typ | Umfang | Einsatz laut Material | Einsatz laut Plan KT3 | Kurzinhalt |
|---|---|---|---|---|---|---|
| 1 | Partneruebung_U5.1_Sequenztypen.md | Übungsblatt mit Auftragsfolie und Dozententeil | 5 Aufgaben, 13 Teilaufgaben; Dozententeil mit Streichliste, 6 Zirkulier-Hinweisen, Debriefing 8 min | U5, Übung, 30 min + 8 min Debriefing, Partner (Driver/Navigator), K3, KI-Stufe 0 | 08:35-09:05 (30 min) [PARTNER] | Teilnehmerliste einer Weiterbildung: Liste erweitern, Slicing, Kopie vs. Verweis beim Sortieren, Tupel unveränderlich, str-Methoden |
| 2 | Partneruebung_U5.2_Dictionaries.md | Übungsblatt mit Auftragsfolie und Dozententeil | 3 Aufgaben, 10 Teilaufgaben; verifizierter Output, Zirkulier-Hinweise, Zeitsteuerung | U5, Übung, 25 min, Partner, K3, KI-Stufe 0 | 09:40-10:05 (25 min) [PARTNER] | Bestellungen eines Lebensmittel-Grosshandels: Datensatz als dict, Zählen mit dict, Liste von dicts mit zwei unterschiedlichen Lücken (Standardwert vs. melden) |
| 3 | Quiz_U5_Datenstrukturen.md | Quiz (Particify, Karten als Fallback) | 8 Fragen (6 Struktur-, 2 Stdlib-Fragen), Lösungstabelle mit Distraktor-Begründung, Besprechung 6 min, Auswertungstabelle | U5, Sicherung, 15 min, Plenum | 10:20-10:35 (15 min) [QUIZ] | "Welche Datenstruktur passt?" inkl. 2-min-Einschub zu `set` |
| 4 | Coaching-Leitfaden_U5_Review-Datenmodelle.md | Leitfaden Dozierende + Review-Bogen (Teil A) | Teil A: Ablauf, 6 Kriterienblöcke mit 21 Prüfpunkten, Feedback-Regeln, Notizvorlage; Teil B: Vorbereitung, Zirkulieren, 8 typische Schwächen, Ersatzmodell (4 Tabellen) mit Lösungsnotiz | U5, Coaching, 35 min + 5 min Plenum, Gruppen à 3, K4/K5 | 10:35-11:10 (35 min) [GRUPPE] + 11:10-11:35 Debriefing (25 min) | Peer-Review der PA-Datenmodelle aus Selbststudium U3 |
| 5 | code/loesung_u5_1_sequenztypen.py | Musterlösung | 127 Zeilen, ca. 50 Codezeilen, 6 Dozentenhinweise am Dateiende | Dozierende | - | Lösung U5.1 |
| 6 | code/loesung_u5_2_dictionaries.py | Musterlösung | 150 Zeilen, ca. 66 Codezeilen, 5 Dozentenhinweise am Dateiende | Dozierende | - | Lösung U5.2 |
| 7 | Partneruebung_U6.1_Funktionen-entwerfen.md | Übungsblatt (Refactoring) | Aufgabe 0 (3), Aufgabe 1 (5 Kriterien, 2 Schritte), Aufgabe 2 (a, b), Zusatz Modul; Dozententeil mit Debriefing 10 min und KI-Regel | U6, Übung, 30 min + 10 min Debriefing, Partner, K4, KI-Stufe 1 | 13:20-13:50 (30 min) [PARTNER] | Monolithische Spesenabrechnung in Funktionen zerlegen, Abnahme per `diff` |
| 8 | Partneruebung_U6.2_Dateien-Kontextmanager.md | Übungsblatt | Aufgaben 1 (a-d), 2 (a-c), 3, 2 Zusatzaufgaben; Dozententeil mit Debriefing 8 min | U6, Übung, 25 min + 8 min Debriefing, Partner, K3, KI-Stufe 1 | 13:50-14:15 (25 min) [PARTNER] | Excel-Export `Adressen.csv` lesen (BOM-Falle), nach PLZ filtern, `versandliste.csv` schreiben |
| 9 | Live-Demo-Drehbuch_U6_Datenbankzugriff.md | Demo-Drehbuch, zweispaltig Code / Sprechnotiz | 5 Blöcke, 4 Stopp-Marken, Schlussnotiz, Einzelarbeit (3 + 1 Aufgaben), Fallback-Tabelle, Notfallplan | U6, Demo 20 min + Einzelarbeit 15 min, Plenum/Einzel, K3 | 14:30-14:50 (20 min, "danach 10 min nachvollziehen" ohne eigenen Slot) | mysql-connector, config.py statt Klartext-Passwort, Liste von Tupeln/dicts, SQL-Injection-Demo, Kontext-Manager, Brücke zu SQLAlchemy |
| 10 | Quiz_U6_Module-Persistenz.md | Quiz | 7 Fragen, Lösungstabelle mit Fehlkonzepten, Besprechung 7 min, Auswertung | U6, Sicherung, 15 min, Plenum | 16:30-16:45 "Quiz OOP-Begriffe und Persistenz" (15 min, kombiniert) | import, `__name__`, venv/pip, `with`, dict-Cursor, SQL-Injection |
| 11 | code/spesen_monolith.py | Ausgangsskript | 85 Zeilen, ca. 65 Codezeilen | TN-Material zu U6.1 | - | Spesenliste März, Prüfung, Detail, Zusammenzug ohne Funktionen |
| 12 | code/loesung_u6_1_spesen_refactored.py | Musterlösung | 187 Zeilen, ca. 95 Codezeilen, 5 Hinweise am Dateiende | Dozierende | - | 9 Funktionen, Trennung Rechnen/Ausgeben |
| 13 | code/loesung_u6_2_csv.py | Musterlösung | 218 Zeilen, ca. 92 Codezeilen, 9 Hinweise am Dateiende | Dozierende | - | Lesen, Filtern, Schreiben, defensive Lesefunktion |
| 14 | code/demo_u6_sqlite.py | Demo-Code (Fallback) | 167 Zeilen, ca. 108 Codezeilen | Dozent + TN ohne MySQL | - | SQLite-Fassung der Demo, erwartet `beispiele.sqlite` neben dem Skript |
| 15 | code/demo_u6_mysql.py | Demo-Code (Referenz) | 171 Zeilen, ca. 113 Codezeilen | Dozent | - | mysql-connector-Fassung, liest `config.py` |
| 16 | code/config_beispiel.py | Vorlage Zugangsdaten | 30 Zeilen | TN | - | Platzhalter-Dict `DB_ZUGANG`, Anleitung Kopieren und `.gitignore`-Eintrag |
| 17 | code/Adressen.csv | Testdaten | 1 Kopfzeile + 20 Datensätze, 7 Spalten, `;`, UTF-8 **ohne BOM**, LF | TN zu U6.2 | - | Erweiterung der Repo-Datei `Python/kap-17/Adressen.csv` (Repo: 3 Datensätze, mit BOM, CRLF) |
| 18 | Selbststudium_U5_PYGR_Kap9-13.md | Selbststudiumsauftrag | 3 Zeitblöcke, Eskalation, Selbstcheck (5 Aufgaben), Vorbereitung U6, 5 Dozentenhinweise | nach U5, 90 min, Einzel, K3, ohne Abgabe | 11:35-11:45 Ausblick | PYGR Kap. 9-13 lösen, Selbstcheck dict/list |
| 19 | Selbststudium_U6_Programm-mit-Persistenz.md | Selbststudiumsauftrag | Anforderungen A1-A4, 2 Ideen + eigene, Zeitplan, Selbstcheck (9 Punkte), Abgabevorlage, KI-Regel, Vorbereitung U7, Dozentenhinweise | nach U6, 90 min, Einzel, K4/K3, Abgabe "vor Unit 7" | 16:45-17:00 Ausblick | eigenes kleines Programm mit Datei- oder DB-Persistenz |

Nicht vorhanden (im Handoff für U6/U7 beauftragt oder im Plan KT3 vorgesehen): siehe Abschnitt 8.

---

## 3 Handoff-Konformität je Material

Legende: erfüllt / teilweise / nein / n. a. (nicht anwendbar). Globale Pflichtbestandteile laut Handoff: Aufgabenstellung, Zeitbudget, Sozialform, erwartetes Ergebnis, Musterlösung oder Bewertungshinweise, projizierbare Auftragsfolie und Handout, Zirkulier-Hinweise, K-Stufe, neue Szenarien, Präsenztauglichkeit.

### 3.1 Partnerübung U5.1 Sequenztypen

| Kriterium | Status | Begründung |
|---|---|---|
| Typ Übungsblatt, 30 min, Partnerübung, LZ 1 K3 | erfüllt | Kopfzeile und Auftragsfolie stimmen |
| 5 Aufgaben zu list/tuple/str an durchgängigem Szenario | erfüllt | Teilnehmerliste durchgehend |
| anlegen, slicen, sortieren, Mutabilität, str-Methoden | erfüllt | Aufgaben 1-5 decken alles ab |
| Abnahme: mindestens eine Aufgabe macht mutable/immutable erlebbar | erfüllt | 3b/3c (Kopie vs. Verweis) und 4b (TypeError) |
| Format Markdown + Auftragsfolie + Musterlösung als Python | erfüllt | vorhanden, Lösung läuft |
| Zeitbudget | teilweise | 30 min Aufgaben plus 8 min Debriefing, Plan hat 30 min (U5-F01) |
| Erwartetes Ergebnis | teilweise | "lauffähige Datei" widerspricht dem absichtlichen Absturz in 4b (U5-F02) |
| Zirkulier-Hinweise | erfüllt | 6 konkrete Hinweise |
| Handout getrennt von Dozentenfassung | nein | eine Datei, Dozententeil enthält Lösungen (KT3-F10) |
| K-Stufe | erfüllt | K3 |
| Szenario neu | erfüllt | kein Buchpaar (siehe 6) |
| Präsenztauglich, keine Remote-Reste | erfüllt | Laptop wandert, Beamer, Wandtafel |

### 3.2 Partnerübung U5.2 Dictionaries

| Kriterium | Status | Begründung |
|---|---|---|
| 25 min, Partner, LZ 1 und LZ 2 K3 | erfüllt | |
| 3 Aufgaben: dict, Zählen/Gruppieren, Liste von dicts | erfüllt | |
| defensive Behandlung fehlender Schlüssel | erfüllt | Aufgabe 3c mit zwei unterschiedlich zu behandelnden Lücken |
| anderes Szenario als adressbuch05 | erfüllt | Bestellungen statt Adressen |
| Abnahme: Aufgaben bauen aufeinander auf | teilweise | konzeptionell ja; Daten von Aufgabe 2 ohne Bezug zu 1 und 3 (U5-F10) |
| Abnahme: defensive Programmierung explizit geprüft | teilweise | im Blatt ja; Musterlösung ersetzt fehlende Menge still durch 0 (U5-F08) |
| Musterlösung als Python | erfüllt | Ausgabe stimmt mit "verifiziertem Output" im Blatt |
| Auftragsfolie, Zirkulier-Hinweise | erfüllt | |
| Handout getrennt | nein | Zirkulier-Hinweis verweist TN sogar auf die Tabelle im Dozententeil (KT3-F10) |

### 3.3 Quiz U5 Datenstrukturen

| Kriterium | Status | Begründung |
|---|---|---|
| 6 Szenario-Fragen list/tuple/dict/set + 2 Stdlib-Fragen | erfüllt | |
| Markdown-Tabelle mit Lösungen und Begründung | erfüllt | inkl. Distraktor-Begründung |
| Particify-Importformat | teilweise | nur copy-paste-fähiger Text, keine Importdatei (WP1-Annahme 1) (KT3-F11) |
| Szenarien realistisch | erfüllt | CSV-Import, Kantonskürzel, E-Mail-Dubletten usw. |
| genau eine richtige Option je Frage | nein | Frage 4 laut Lösungsteil mit zwei vertretbaren Optionen (U5-F12) |
| Begründungen fachlich korrekt | teilweise | Frage 5: Aussage zur Reihenfolge bei dicts veraltet (U5-F13) |
| Zeitbudget 15 min | erfüllt | 8 × 45 s + 6 min + 2 min set-Einschub |

### 3.4 Coaching-Leitfaden U5

| Kriterium | Status | Begründung |
|---|---|---|
| Ablauf 35 min, 3 × ca. 10 min | erfüllt | 2 + 3 × 10 + 3 min |
| Kriterienliste: 3NF, Beziehungen/Kardinalitäten, Namenskonventionen, PA-Tauglichkeit | erfüllt | plus Verständlichkeit und zeitliche Gültigkeit |
| typische Schwächen mit Coaching-Fragen | erfüllt | 8 Zeilen |
| Rolle Dozent (zirkuliert, greift nur bei Fehlurteilen ein) | erfüllt | Fehler als Frage an Reviewer |
| Eskalation TN ohne Modell, Ersatzmodell | teilweise | vorhanden; Ablauf der Gruppe in dieser Runde unklar (U5-F22); Schwäche 2 fachlich angreifbar (U5-F19) |
| Review-Bogen einseitig druckbar | nein | 21 Prüfpunkte plus Ablauf, Regeln, Notizfeld: realistisch 2 A4-Seiten (U5-F17) |
| Abnahme: auch schwächere Gruppen geben substanzielles Feedback | teilweise | Prüffragen konkret, aber zu viele für 6 min Review |
| Auftragsfolie, K-Stufe (K4/K5), Präsenz | erfüllt | |
| Passung Plan (3 Prüffragen, 25 min Debriefing) | nein | U5-F17, U5-F18 |

Prüfung des Ersatzmodells (drei eingebaute Schwächen):

| Schwäche laut Leitfaden | echte Schwäche? | 3NF-Aussage korrekt? |
|---|---|---|
| 1 Trainer als Freitext in `durchfuehrung` | ja: Wiederholungsgruppe, Änderungsanomalie, Auswertung unzuverlässig | ja, sofern Trainerdaten von der Person (nicht von der Durchführung) abhängen: transitive Abhängigkeit |
| 2 `plz`/`ort` in `teilnehmer` (plus `firma`) | nur bedingt | teilweise: Formulierung "hängt nicht vom Primärschlüssel ab" unpräzise (transitiv); PLZ bestimmt in der Schweiz den Ort nicht eindeutig; Muster-DB `beispiele` modelliert `adresse` selbst mit plz und ort; `firma` als reiner Textwert ist keine Normalform-Verletzung (U5-F19) |
| 3 kein Preis in `anmeldung` | ja: Historisierung, alte Rechnungen nicht rekonstruierbar | keine Normalform-Frage, korrekt dem Kriterium "zeitliche Gültigkeit" zugeordnet |

### 3.5 Selbststudium U5

| Kriterium | Status | Begründung |
|---|---|---|
| Übungen PYGR 9-13 mit Vergleich Repo | erfüllt | |
| Ergebnis lauffähige Lösungen | erfüllt | |
| Selbstcheck "dict filtern/sortieren ohne Nachschlagen" | erfüllt | 5 Aufgaben; keine Lösung zur Selbstkontrolle (Absicht, aber Selbstcheck dann nur Zeitmessung) |
| Vorbereitung Unit 6 benennen (PYGR 13-15, 17-18, PA-Entwurf) | teilweise | vorhanden, unter S2610 nicht durchführbar (KT3-F01) |
| Abnahme: Zeitbudget realistisch aufgeteilt | teilweise | Summe 90 min stimmt; Kapitelzuordnung der Blöcke passt nicht (U5-F25) |

### 3.6 Partnerübung U6.1 Funktionen entwerfen

| Kriterium | Status | Begründung |
|---|---|---|
| 30 min, Partner, LZ 1 K4 | erfüllt | Entwurf auf Papier vor dem Code |
| monolithisches Skript ca. 50 Zeilen, Spesenabrechnung | teilweise | 85 Zeilen, ca. 65 Codezeilen, vertretbar |
| Kriterien gute Zerlegung (eine Aufgabe, keine Globals) | erfüllt | 5 Kriterien |
| Debriefing: 2 Paare am Beamer | erfüllt | 10 min, nicht im Plan-Slot (U6-F02) |
| Abnahme: Ausgangsskript lauffähig | erfüllt | ausgeführt |
| Abnahme: Musterlösung klare Verbesserung, TN-Niveau | erfüllt | Ausgabe per `diff` identisch |
| Problemstellung (Tarifänderung an einer Stelle) fachlich stimmig | nein | Ansatz ist im Monolithen bereits eine Konstante (U6-F01) |
| Auftragsfolie, Zirkulier-Hinweise, erwartetes Ergebnis | erfüllt | |
| Handout getrennt | nein | KT3-F10 |

### 3.7 Partnerübung U6.2 Dateien und Kontext-Manager

| Kriterium | Status | Begründung |
|---|---|---|
| 25 min, Partner, LZ 1 K3, LZ 4-Vorstufe | erfüllt | |
| Repo-CSV auf ca. 20 Zeilen erweitern und mitliefern | teilweise | 20 Datensätze, Kopfzeile unverändert; BOM und CRLF des Excel-Exports gingen verloren (U6-F06) |
| `with open` + `csv.reader`, Referenz read_csv.py | erfüllt | |
| nach PLZ-Bereich filtern, Ergebnis-CSV schreiben | erfüllt | |
| Zusatz Fehlerfall Datei fehlt | erfüllt | inkl. Entwurfsfrage None vs. Exception |
| Abnahme: nur Stdlib | erfüllt | |
| Abnahme: Encoding-Falle utf-8-sig explizit erklärt | teilweise | Text erklärt korrekt, mit der gelieferten Datei aber nicht erlebbar (U6-F06) |
| fachliche Korrektheit TN-Text | nein | Aussage zum Textvergleich falsch (U6-F07) |
| Zeitbudget | teilweise | plus 8 min Debriefing (U6-F09) |

### 3.8 Live-Demo-Drehbuch U6

| Kriterium | Status | Begründung |
|---|---|---|
| Basis db_select2.py und db_context.py | erfüllt | UseDB übernommen (inkl. commit-Schwäche, U6-F18); Datumsbereich 2020 des Repo bewusst durch `ORDER BY ... LIMIT` ersetzt |
| mysql-connector-python im venv installieren | teilweise | im Drehbuch ja; venv-Aufbau hat im Plan KT3 keinen Slot (KT3-F03) |
| Platzhalter statt f-String, SQL-Injection zeigen | erfüllt | Block 4 a-c, verifiziert |
| Ergebnisse als Python-Strukturen | erfüllt | Tupel und dicts |
| sauberes Schliessen, Kontext-Manager | erfüllt | Block 5 |
| Zugangsdaten nicht hardcodiert (config.py/.gitignore oder Umgebungsvariable) | erfüllt | config.py mit Vorlage und verständlicher Fehlermeldung; Umgebungsvariable nur erwähnt; `.gitignore` nicht mitgeliefert (U6-F24) |
| zweispaltig Code / Sprechnotiz | erfüllt | |
| Fallback SQLite | teilweise | Text und Code vorhanden, Datenbankdatei fehlt (U6-F13) |
| Schlussnotiz Brücke SQLAlchemy | erfüllt | |
| Format: lauffähige .py (MySQL und SQLite) | teilweise | SQLite nicht lauffähig ohne DB; MySQL statisch plausibel |
| Abnahme: beide Varianten lauffähig | nein | U6-F13 |
| Abnahme: Demo läuft gegen create_beispiele.sql | erfüllt (statisch) | alle Tabellen-/Spaltennamen im Demo-Code existieren; Kontrollwerte gegen SQLite-Portierung reproduziert |
| Einzelarbeit 15 min mit Auftrag | teilweise | nur im Dozentendokument, keine TN-Folie; Spaltenname-Stolperstein (U6-F16, U6-F17) |

Statische Prüfung `demo_u6_mysql.py` (Auftrag Punkt 4):

| Prüfpunkt | Befund |
|---|---|
| Treiber | `import mysql.connector`, Paket `mysql-connector-python` (wie Repo kap-18 und Drehbuch) |
| Platzhalter | durchgehend `%s` mit Tupel `(wert,)`, auch für `LIMIT` und `HAVING`; nur die absichtlich unsichere Demo-Funktion baut einen f-String |
| Credentials | keine im Code; `from config import DB_ZUGANG`, bei fehlender Datei `SystemExit` mit Anleitung; Schlüssel `password` (Repo `db_context.py` nutzt noch den Alias `passwd`) |
| Spaltennamen gegen create_beispiele.sql | `lehrveranstaltung.titel/beginn/ende`, `fach.fach_id/titel/kuerzel`, `pruefung.fach/note`: alle vorhanden. `kuerzel` ist `varchar(4)`, Testwert passt |
| Kontext-Manager | `__exit__` committet immer, auch im Fehlerfall, kein rollback (U6-F18) |
| Guard | `if __name__ == "__main__":` vorhanden |
| Unterschiede zur SQLite-Fassung | Platzhalter, Verbindungsaufbau, dict-Erzeugung, Signatur `UseDB(zugang)` vs. `UseDB(db_datei)`; MySQL liefert `datetime`/`Decimal`, SQLite Strings/float (U6-F22) |

### 3.9 Quiz U6 Module und Persistenz

| Kriterium | Status | Begründung |
|---|---|---|
| 7 Fragen: import (2), pip/venv (2), Dateien (1), DB inkl. Injection (2) | erfüllt | |
| Abnahme: eine Frage zu parametrisierten Queries statt Verkettung | erfüllt | Frage 7 mit plausiblem Distraktor |
| genau eine richtige Option | erfüllt | |
| Lösungen stimmen | erfüllt | |
| Verteilung der Lösungspositionen | nein | alle 7 Fragen haben dieselbe Lösungsposition (U6-F25) |
| Particify-Importformat | teilweise | wie Quiz U5 (KT3-F11) |
| Passung Plan (Kombination mit OOP in 15 min) | nein | KT3-F08 |

### 3.10 Selbststudium U6

| Kriterium | Status | Begründung |
|---|---|---|
| eigenes Programm, min. 3 Funktionen, lesen+schreiben, defensiv | erfüllt | A1-A4 mit Prüfweise |
| 2 Beispielideen | erfüllt | Idee 2 nahe an Repo-Lösungen (U6-F28) |
| Abgabe im Kurskanal | erfüllt | Vorlage vorhanden; Frist "vor Unit 7" unter S2610 unmöglich (KT3-F01) |
| Abnahme: in 90 min machbar | teilweise | DB-Schreiben im Unterricht nicht gezeigt (U6-F29) |
| Abnahme: bewertbare Mindestanforderungen klar | erfüllt | |

### 3.11 Handoff-Vorgaben zur Repo-Nutzung (Querschnitt)

| Vorgabe | Status | Befund |
|---|---|---|
| Adressen.csv auf ca. 20 Zeilen erweitern | teilweise | 20 Datensätze, aber ohne BOM und mit LF (U6-F06) |
| Format `;` und `utf-8-sig` (Lehrmittel-Konvention) | teilweise | Trenner und Encoding in Blatt und Lösung korrekt; Testdatei hat kein BOM |
| Zugangsdaten in config.py oder Umgebungsvariable auslagern, als Lernpunkt | erfüllt | Block 2 des Drehbuchs, `config_beispiel.py`; `.gitignore` fehlt als Datei |
| db_select2/db_context als Demo-Basis | erfüllt | |
| adressbuch0x als Szenario-Vorbild, Aufgaben neu | erfüllt | U5.2 anderes Szenario |
| Übungen nicht identisch mit Buchaufgaben | weitgehend erfüllt | Nähe in U6.2 Zusatz 1 und Selbststudium U6 Idee 2 (Abschnitt 6) |
| Kasten "Aktuelle Schreibweise" bei Legacy-APIs | n. a. | U5/U6-Code nutzt keine veralteten APIs |

---

## 4 Passung zum Unterrichtsplan KT3

### 4.1 Vormittag (U5)

| Plan-Slot | Plan (min) | Material | Bedarf laut Material (min) | Bilanz |
|---|---|---|---|---|
| 08:00-08:15 Check-in Selbststudium U4 | 15 | kein U5-Material nötig | - | ok |
| 08:15-08:35 Input/Demo Sequenztypen | 20 | kein Material in diesem Umfang (Folien Python laut Fachplan) | - | offen |
| 08:35-09:05 Übung Sequenztypen | 30 | U5.1 | 30 + 8 Debriefing = 38 | +8 in die Pause |
| 09:20-09:40 Input/Demo Dictionaries | 20 | kein Material | - | offen |
| 09:40-10:05 Übung Dictionaries | 25 | U5.2 | 25 + ca. 5 Debriefing | +5 in die Pause |
| 10:20-10:35 Quiz | 15 | Quiz U5 | 14 | ok |
| 10:35-11:10 PA-Coaching | 35 | Leitfaden Teil A/B | 35 | ok |
| 11:10-11:35 Debriefing Modelle, Beispiele zeigen | 25 | Leitfaden: 5 min, "nicht Modelle besprechen" | 5 | 20 min ohne Material, Widerspruch (U5-F18) |
| 11:35-11:45 Ausblick Selbststudium PYGR 9-13 | 10 | Selbststudium U5 | 10 | Inhalt setzt U6 später voraus (KT3-F01) |

Im Plan fehlen gegenüber Handoff-Ablauf U5: eigener Input "defensive Programmierung" (in U5.2 abgedeckt) und "Einführung Funktionen" (in den Nachmittag verschoben). LZ 3 (Stdlib-Module) steht im Plan-Überblick nicht mehr, wird nur im Quiz (2 Fragen) berührt.

### 4.2 Nachmittag (U6/U7 verdichtet)

| Plan-Slot | Plan (min) | vorhandenes Material | Bedarf laut Material (min) | Bilanz |
|---|---|---|---|---|
| 13:00-13:20 Input Funktionen, Modul-Import | 20 | keins (Folien Python); kein pip/venv-Teil im Plan | - | venv fehlt (KT3-F03) |
| 13:20-13:50 Refactoring | 30 | U6.1 | 30 + 10 = 40 | +10 |
| 13:50-14:15 Dateien/Kontext-Manager | 25 | U6.2 | 25 + 8 = 33 | +8 |
| 14:30-14:50 Demo DB-Zugriff + "10 min nachvollziehen" | 20 | Drehbuch U6 | 20 + 15 = 35, plus pip-Installation | +15 |
| 14:50-15:05 Code-Review bank2c auf Papier | 15 | fehlt | - | Lücke |
| 15:05-15:25 Input Klassen + Bug-Auflösung | 20 | fehlt (Folien Python) | - | Lücke |
| 15:40-16:10 Eigene Klasse entwerfen | 30 | fehlt | - | Lücke |
| 16:10-16:30 PP8 Best Practices | 20 | fehlt | - | Lücke |
| 16:30-16:45 Quiz OOP + Persistenz | 15 | Quiz U6 (allein 13-15 min) | 15 + OOP-Teil | muss halbiert werden (KT3-F08) |
| 16:45-17:00 Ausblick Selbststudium | 15 | Selbststudium U6 (Fristen falsch), U7 fehlt | - | Lücke |

Summe der vorhandenen U6-Materialien: 108 min Bedarf gegen 75 min im Plan, also rund 33 min Überzug vor der ersten Pause, zuzüglich 5-10 min venv/pip. Die U6-Materialien sind für eine eigene 5×45-Unit geschrieben und passen ohne Kürzung nicht in den verdichteten Nachmittag. Kürzungsvorschlag in KT3-F04.

### 4.3 Quiz U6 in Kombination mit OOP

Empfohlene Auswahl für einen 15-min-Kombiquiz: Frage 7 (Pflicht, Abnahmekriterium Injection), Frage 5 (`with`), Frage 6 (dict-Cursor); Fragen 3 und 4 nur, wenn venv an KT3 tatsächlich behandelt wird; Fragen 1 und 2 optional. Dazu 3-4 OOP-Fragen (Klasse vs. Objekt, `self`, `__init__`, kurze "Was gibt der Code aus?"-Frage mit nur behandeltem Stoff). Lösungspositionen neu mischen (U6-F25).

---

## 5 Ausführungsprotokoll (ohne Lösungsinhalte)

| Nr | Datei / Test | Aufruf | Ergebnis | Abgleich mit Blatt |
|---|---|---|---|---|
| 1 | loesung_u5_1_sequenztypen.py | `python3` ohne Eingabe (kein `input()`) | Exit 0 unter 3.11, 3.12, 3.13 | Verhalten 3a-3c und Fehlermeldung 4b wie im Blatt beschrieben. Aufgabe 5 sortiert gross/klein-sensitiv (U5-F03). Der im Blatt angekündigte "verifizierte Output im Dateikopf" existiert nicht (U5-F04) |
| 2 | loesung_u5_2_dictionaries.py | `python3` | Exit 0 unter 3.11, 3.12, 3.13 | Ausgabe Aufgabe 3 stimmt mit dem "verifizierten Output" im Blatt überein (Beträge, Zeilenzahlen, Warnung) |
| 2a | Randfall naive Lösung | Zugriff per `eintrag["preis"]` auf Datenzeile ohne Preis | `KeyError: 'preis'` | wie im Blatt |
| 2b | Randfall Gratismuster (Preis 0.00) | Zusatzzeile, Variante `is None` und `if not preis` | `is None` verarbeitet die Zeile, `if not` überspringt sie fälschlich | wie im Debriefing beschrieben |
| 2c | Randfall fehlende Menge | Zeile ohne `menge` | Kunde erscheint mit CHF 0.00, keine Warnung | widerspricht Lernziel (U5-F08) |
| 3 | spesen_monolith.py | `python3` | Exit 0 | lauffähig (Abnahmekriterium erfüllt) |
| 4 | loesung_u6_1_spesen_refactored.py | `python3 ... > b.txt`, `diff a.txt b.txt` | diff leer | Angabe "zeichengenau identisch" bestätigt |
| 4a | Aufgabe 2b | zweite Spesenliste mit einem Funktionsaufruf abgerechnet | korrekte zweite Abrechnung | Aufgabe mit Musterlösung lösbar |
| 4b | Tarifänderung 0.70 auf 0.75 | in Monolith und Musterlösung je nur die Konstante geändert | beide Fassungen rechnen nach genau einer Änderung identisch richtig | widerlegt die Problemstellung von Aufgabe 0/2a (U6-F01) |
| 5 | loesung_u6_2_csv.py mit Drive-`Adressen.csv` | `python3` | Exit 0 unter 3.11, 3.12, 3.13; `versandliste.csv` mit BOM und CRLF geschrieben; Zusatzfall "Datei fehlt" gibt Meldung statt Traceback | alle Kontrollangaben im Blatt (Lesezahl, Trefferzahl, kleinste/grösste PLZ, Gegenprobe, Ortsfilter der Zusatzaufgabe 2) stimmen |
| 5a | Code aus Aufgabe 1a mit Drive-CSV | `encoding="utf-8"` | **kein Fehler**, erstes Feld ohne BOM-Zeichen | Kernmoment der Übung tritt nicht ein (U6-F06) |
| 5b | Code aus Aufgabe 1a mit Repo-CSV (`kap-17`, mit BOM) | dito | `ValueError: 'Vorname' is not in list` | so wäre es gedacht |
| 5c | Textvergleich | `"900" < "8952"` | `False` | Blatt behauptet `True` (U6-F07) |
| 5d | Textvergleich vs. `int` bei den 20 PLZ | Filter 8000-8999 als Text und als Zahl | identische Treffer (alle PLZ 4-stellig) | "stille Falle" tritt mit diesen Daten nicht auf (U6-F08) |
| 6 | demo_u6_sqlite.py ohne `beispiele.sqlite` | frisches Temp-Verzeichnis | `sqlite3.OperationalError: no such table: lehrveranstaltung`; zusätzlich wird eine leere 0-Byte-Datei `beispiele.sqlite` angelegt | Fallback nicht lauffähig (U6-F13) |
| 7 | demo_u6_sqlite.py mit SQLite-Portierung (Kurztest, fremde Portierung aus dem Scratchpad) | Kopie neben dem Skript, danach entfernt | Exit 0, alle Blöcke laufen | Tabellengrössen im Drehbuch, Trefferzahlen Block 4a-4c, Spitzenwerte Block 5 und alle Kontrollwerte der Einzelarbeit (Aufgaben 1-3, Zusatz mit leerer Liste) reproduziert. Gleichstände in zwei Sortierungen (U6-F20) |
| 8 | demo_u6_mysql.py | nur `py_compile` | kompiliert | statische Prüfung in 3.8 |
| 9 | Repo `kap-16/bank2c.py` | Hauptprogramm; zweiter Kunde mit 3 Konten; Import als Modul | Hauptprogramm korrekt; zweiter Kunde erhält falsche und doppelte Kontonummern; beim Import ohne `kunde1` `NameError` beim zweiten Konto | Handoff-Befund bestätigt, reproduzierbar (für Lücke U7.0) |

---

## 6 Neuheit: Nähe zu Buchaufgaben und Repo-Code

| Material | Repo-Paar | Nähe | Bewertung |
|---|---|---|---|
| U5.1 Teilnehmerliste | `kap-9/namen.py` (Liste aus Eingaben) | gering | ok |
| U5.2 Aufgabe 2 (Häufigkeiten mit dict) | `kap-17/wordcount1.py`, `wordstat.py` (Worthäufigkeit) | gleiche Technik, anderes Szenario | ok |
| U5.2 Szenario | `kap-13/adressbuch01-05.py` | Handoff-Vorbild, Szenario gewechselt | ok |
| Quiz U5 (`set`) | `kap-13/Aufgabe2.py`, `lotto_mengen.py` | nur Begriff | ok |
| U6.1 Spesen | kein Buchpaar; knüpft an eigene U4.1 B (Spesen erfassen) an | Kontinuität, gewollt | ok |
| U6.2 Hauptaufgabe | `kap-17/read_csv.py` (gleiche Datei, laut Handoff gewollt) | Lesen identisch, Filtern neu | ok |
| U6.2 Schreiben | `kap-17/write_csv.py` (Schreiben mit `utf-8-sig` und `;`) | Technik bereits im Buch | Behauptung "Schreiben ist neu" abschwächen (U6-F12) |
| U6.2 Zusatzaufgabe 1 | `kap-17/copy_lines_try.py`, `kap-17/adressbuch06.py` (`FileNotFoundError` und `PermissionError` mit Meldung) | praktisch identisch | Lösung öffentlich (U6-F12) |
| Drehbuch Einzelarbeit | `kap-18/db_select1.py` (`SELECT * FROM standort`) | gering | ok |
| Selbststudium U6 Idee 2 | `kap-17/adressbuch06.py`, `kap-15/adressbuch07.py` (CSV-Adressbuch mit Erfassen, Suchen, Speichern) | hoch, bis auf SQLite-Teil gelöst | U6-F28 |
| (Lücke) Code-Review U7.0 | `kap-16/bank2d.py` enthält die Korrektur des bank2c-Bugs | Lösung im selben Repo-Ordner | bei U7.0 berücksichtigen (Abschnitt 8) |

---

## 7 Findings

Schweregrade: hoch = falsch oder blockiert Unterricht; mittel = verwirrt TN oder erzeugt Nacharbeit; tief = Kosmetik.

### 7.1 Unit 5

| ID | Grad | Datei + Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| U5-F01 | mittel | U5.1 Auftragsfolie / Debriefing | 30 min Aufgaben (3+5+10+6+6) plus 8 min Debriefing; Plan-Slot 08:35-09:05 hat 30 min, danach Pause | Aufgabe 2 als Kür, Debriefing auf 5 min, oder Debriefing nach der Pause mit dem Dict-Input verbinden |
| U5-F02 | mittel | U5.1 Aufgabe 4b und "Erwartetes Ergebnis" | Der absichtliche TypeError bricht das Skript ab, verlangt ist aber eine "lauffähige Datei, die alle fünf Aufgaben ausgibt"; kein Hinweis, die Zeile danach auszukommentieren. Musterlösung umgeht es mit try/except, das ausserhalb der Stoffgrenze liegt | Anweisung "Fehlermeldung notieren, Zeile mit `#` auskommentieren"; Musterlösung ohne try/except mit auskommentierter Zeile |
| U5-F03 | tief | loesung_u5_1, Aufgabe 5 | Aufgabe verlangt "alphabetisch sortiert", Lösung sortiert gross/klein-sensitiv, der kleingeschriebene Eintrag steht am Ende | nach Auflösung 3d gross/klein-unabhängig sortieren oder Aufgabentext anpassen |
| U5-F04 | tief | U5.1 und U5.2 Dozententeil, analog U6.1/U6.2 | "Verifizierter Output liegt im Dateikopf" bzw. "Hinweise im Dateikopf": Output fehlt, Hinweise stehen am Dateiende | Output als Kommentarblock ergänzen, "Dateiende" schreiben |
| U5-F05 | tief | U5.1 Auftragsfolie, Hilfsmittel | "Merksätze an der Wandtafel aus Unit 4": U4 war an KT2 (06.11.), Tafel ist dann gelöscht | Merksätze als Folie oder Handout |
| U5-F06 | tief | U5.1 Debriefing, Merksatz Tupel | "Ein Tupel ist eine Liste, die sich nicht mehr ändern lässt" verkürzt: Tupel kann veränderliche Elemente enthalten; typischer Einsatz fester Datensatz | Merksatz um "Datensatz fester Länge" ergänzen |
| U5-F07 | tief | U5.1 Dozententeil 3d | Rückverweis "ORDER BY und Collation, dort dasselbe Thema": Collation war nicht Stoff in U1-U3; die DB `beispiele` (utf8mb4_0900_ai_ci) sortiert gross/klein-unabhängig, also gerade anders als Python | Kontrast in einem Satz benennen |
| U5-F08 | mittel | loesung_u5_2, Aufgabe 3 | Fehlende Menge wird still durch Standardwert 0 ersetzt; Test: Zeile ohne Menge erscheint als Umsatz CHF 0.00 ohne Warnung. Widerspricht dem Merksatz der Übung ("Standardwert nur, wenn fachlich richtig") | Menge wie Preis behandeln (melden und überspringen) oder im Kommentar begründen |
| U5-F09 | tief | U5.2 "Anschluss" | ORM ab Unit 9 liefert Modell-Objekte, keine dicts; DB-Cursor liefert dicts nur mit `dictionary=True` | Formulierung präzisieren |
| U5-F10 | tief | U5.2 Aufgabe 2 | Kategorienliste ohne Bezug zu den Bestellungen aus Aufgabe 1/3; Abnahme "bauen aufeinander auf" nur konzeptionell | Zählaufgabe auf die Bestellungen beziehen (z. B. Positionen je Kunde) |
| U5-F11 | tief | Quiz U5 Auswertung / Plan-Überblick KT3 | LZ 3 (Stdlib-Module) nur mit 2 Quizfragen, in keiner U5-Übung angewendet; im Plan-Überblick KT3 fehlt LZ 3 | LZ-Abdeckung im Plan dokumentieren oder Stdlib-Mini-Aufgabe ins Selbststudium |
| U5-F12 | mittel | Quiz U5 Frage 4 und Lösungsteil | Lösungsteil erklärt zwei Optionen für vertretbar; Particify wertet nur eine; verletzt "genau eine richtige Option" | Szenario schärfen (z. B. Wert soll als dict-Schlüssel dienen) oder als ungewertete Diskussionsfrage kennzeichnen |
| U5-F13 | mittel | Quiz U5 Lösungstabelle Frage 5 | Eine Option wird damit verworfen, dass bei verschachtelten dicts die Reihenfolge verloren gehe; seit Python 3.7 bleibt die Einfügereihenfolge erhalten (U5.2 Aufgabe 1d zeigt es selbst) | Begründung auf "Umsortieren umständlich, Schlüssel nötig" ändern |
| U5-F14 | tief | Quiz U5 Besprechung Frage 8 | Live-Beispiel splittet eine Semikolon-Zeile am Komma; zeigt nicht den Fall der Frage (Komma-CSV mit Anführungszeichen) und nicht `csv.reader` | Komma-Zeile mit Quote-Feld, Vergleich `split` gegen `csv.reader` |
| U5-F15 | tief | Coaching-Leitfaden, Kriterium 3 | Heuristik "Spalte ergibt sich aus anderer Spalte" schlägt auch bei Schlüsselkandidaten an (eindeutige E-Mail bestimmt Namen, keine Verletzung) | Zusatz "... und die andere Spalte ist selbst kein eindeutiger Schlüssel" |
| U5-F16 | tief | Coaching-Leitfaden, Querverweis Schwäche 2 | "dieselbe Falle wie in Partnerübung U2.1": WP0-Material nicht in diesem Umfang; laut WP1-Übersicht (02.09.) WP0 noch nicht umgesetzt | beim WP0-Abgleich prüfen |
| U5-F17 | mittel | Coaching-Leitfaden Teil A | "Einseitig druckbar" nicht erfüllt (6 Blöcke, 21 Prüfpunkte, Ablauf, Regeln, Notizfeld, realistisch 2 Seiten); Plan verlangt "Review-Bogen (3 Prüffragen)"; 21 Punkte in 6 min Review je Modell nicht leistbar | Einseitiger Bogen mit 3 Kernfragen (Normalform, Beziehungen, zeitliche Gültigkeit) plus Ankreuzfeld PA-Umfang; Rest als Dozentenreferenz |
| U5-F18 | mittel | Coaching-Leitfaden "Nach den 35 Minuten" vs. Plan 11:10-11:35 | Leitfaden: 5 min Plenum, "nicht Modelle besprechen"; Plan: 25 min "häufigste Modell-Fehler anonymisiert, gelungene Beispiele zeigen [PRÄS]". Widerspruch, 20 min ohne Material | Entscheid treffen; entweder Material für anonymisierte Fehlergalerie (beim Sichten 3 Muster sammeln) oder Slot kürzen und Zeit an U5.1/U5.2-Debriefings geben |
| U5-F19 | mittel | Coaching-Leitfaden Ersatzmodell, Schwäche 2 | (a) Muster-DB `beispiele` speichert in `adresse` selbst plz und ort; TN kennen das als Referenz. (b) In der Schweiz ist PLZ nach Ort keine strikte funktionale Abhängigkeit (mehrere Ortschaften je PLZ), die Korrektur "Tabelle ort mit PLZ als Schlüssel" greift nicht. (c) "hängt nicht vom Primärschlüssel ab" unpräzise, korrekt: nur transitiv. (d) `firma` als Freitextwert ist keine Normalform-Verletzung | Schwäche 2 als "diskutierbar" kennzeichnen, Lösungsnotiz um (a)-(d) ergänzen, `firma` herauslösen oder als Stammdaten-Frage begründen |
| U5-F20 | tief | Coaching-Leitfaden Lösungsnotiz | Nicht erwähnte, aber gleichwertige Funde: `ort` in `durchfuehrung` als Freitext (analog Trainer), keine Eindeutigkeit für Doppelanmeldungen, E-Mail nicht eindeutig | als gültige Zusatzfunde aufnehmen |
| U5-F21 | mittel | Coaching-Leitfaden "Studierende ohne Modell" | Unklar, was die Gruppe in der Runde des fehlenden Modells tut (Einzelperson reviewt 10 min allein, die zwei anderen warten?) | In dieser Runde reviewt die ganze Gruppe das Ersatzmodell gemeinsam (dient zugleich als Kalibrierung) |
| U5-F22 | mittel | Coaching-Leitfaden Kriterium 6, typische Schwächen | PA-Umfang "mindestens 4 Tabellen", "unter 5 / über 15 Masken", "sechs Wochen" gegen Plan PP6 "3-6 Tabellen" und 5 + 2 Wochen; WP1-Übersicht "4 bis 8 Tabellen". Offizielle PA-Unterlagen fehlen | eine Quelle festlegen, nach Erhalt der PA-Vorgaben abgleichen |
| U5-F23 | mittel | Selbststudium U5, Zeitblöcke | Blockthemen passen nicht zur Kapitelstruktur (Repo als Proxy: kap-11 Strings, kap-12 Exceptions, kap-13 dict/set); Kap. 13 bekommt nach Abzug des Selbstchecks (5 × 3 min) nur ca. 10 min; Empfehlung "45 min für Kapitel 11 und 12" zielt für dict-Lücken auf die falschen Kapitel | Blöcke nach Lehrmittel neu schneiden (Kap. 13 eigener Block), Kapitelnummern gegen Lehrmittelauflage prüfen (WP1 To-do 3) |
| U5-F24 | tief | Selbststudium U5 Selbstcheck | Datensatz und Aufgaben 3/5 nahezu identisch mit U5.2 Aufgabe 3, misst eher Erinnerung als Transfer | anderes Datenset (z. B. Geräteinventar) |

### 7.2 Unit 6

| ID | Grad | Datei + Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| U6-F01 | hoch | spesen_monolith.py; U6.1 Aufgabe 0 und 2a, "Zahlen zur Kontrolle"; loesung_u6_1 Hinweis 1 | Der Kilometeransatz ist im Monolithen bereits eine Konstante. Eine Tarifänderung braucht in Original und Musterlösung genau eine Änderung (ausgeführt). Aussage im Lösungskommentar: "Jede Aenderung am Kilometeransatz muesste an drei Stellen nachgezogen werden" ist falsch; TN beantworten 0c/2a korrekt mit "eine Stelle", die Motivation der Übung fällt weg. Die echte Duplikation liegt in der Wert- und Limitenlogik | Aufgabe 0/2a auf eine Regeländerung umstellen, die die duplizierte Logik trifft (z. B. neue Limite für eine weitere Spesenart), oder den Ansatz im Monolithen an den Rechenstellen als Literal schreiben; Kontrollangaben, Hinweis 1 und diff-Test nachziehen |
| U6-F02 | mittel | U6.1 Debriefing | 10 min Debriefing zusätzlich zu 30 min; Plan 13:20-13:50 ohne Debriefing, danach direkt U6.2 | Debriefing auf 5 min (nur Frage "vierte Spesenart"), Punkt 2 in U6.2-Debriefing verschieben |
| U6-F03 | tief | U6.1 "Ausgabe vergleichen", Selbststudium U6 "Start" | Befehle nutzen `python3`; unter Windows meist `py` bzw. `python`; Demo-SQLite nutzt `python` (uneinheitlich) | beide Varianten angeben |
| U6-F04 | tief | loesung_u6_1, loesung_u6_2, U5-Lösungen | Kein `if __name__ == "__main__":`. Beim Zusatz "Fachlogik als Modul importieren" druckt die Musterlösung beim Import die ganze Abrechnung. Quiz U6 behauptet, die Musterlösungen enthielten den Guard | Guard in alle Musterlösungen |
| U6-F05 | hoch | code/Adressen.csv; U6.2 Aufgabe 1a und Dozententeil; loesung_u6_2 Hinweis 1 | Datei hat **kein BOM** (1156 B, beginnt direkt mit "Vorname"; Drive-Metadaten bestätigen die Grösse) und LF-Zeilenenden. Der Code aus 1a läuft deshalb fehlerfrei, der Kernmoment ("nie streichen") tritt nicht ein. Material behauptet "mit BOM". Repo-Original hat BOM und CRLF | Datei mit `utf-8-sig` und CRLF neu schreiben (erwartete Grösse dann 1180 B: 1156 + 3 BOM + 21 CR), 1a vor Einsatz auf Windows und macOS testen |
| U6-F06 | hoch | U6.2 Aufgabe 2a (TN-Text) | Zitat: «`"900" < "8952"` ist als Textvergleich `True`, obwohl 900 kleiner als 8952 ist». Falsch: als Text ergibt der Vergleich `False` (erstes Zeichen), numerisch wäre er `True`. Debriefing Punkt 3 fragt genau das per Handzeichen ab. Musterlösung formuliert es richtig | Satz korrigieren: als Text `False`, obwohl 900 < 8952 |
| U6-F07 | tief | U6.2 "Die stille Falle" | Mit durchwegs 4-stelligen Schweizer PLZ und Text-Grenzen liefert der Textvergleich hier dieselben Treffer wie `int` (geprüft); Testwert 900 ist keine gültige CH-PLZ | Falle realistisch machen (z. B. PLZ-Feld mit Leerzeichen, 5-stellige PLZ) oder als Denkfrage kennzeichnen |
| U6-F08 | mittel | U6.2 Debriefing | 8 min zusätzlich zu 25 min, Plan 13:50-14:15; mit U6-F02 zusammen ca. 18 min Überzug in die Pause | Aufgabe 3 im Plenum (Option steht im Blatt), Debriefing 5 min |
| U6-F09 | tief | U6.2 1d, Kontext-Manager; Quiz U6 Frage 5 | "Unter Windows gesperrt und lässt sich nicht überschreiben" zugespitzt; Kernrisiko: kein garantiertes Schliessen/Schreiben der Puffer, Sperre betrifft vor allem Löschen/Umbenennen | erwartete Antwort präzisieren |
| U6-F10 | tief | U6.2 Zusatzaufgabe 1 | "Datei in Excel geöffnet" erzeugt nur unter Windows einen PermissionError, unter macOS nicht (BYOD gemischt) | Hinweis ergänzen |
| U6-F11 | tief | U6.2 Dozententeil "Referenz im Repo", loesung_u6_2 Hinweis 9 | "Filtern, Schreiben und die defensive Behandlung sind neu": Schreiben mit `utf-8-sig`/`;` zeigt `kap-17/write_csv.py`, die Fehlerbehandlung (`FileNotFoundError`, `PermissionError`) steht fast identisch in `copy_lines_try.py` und `adressbuch06.py` | Aussage auf "Filtern und Entwurfsfrage None vs. Exception sind neu" reduzieren |
| U6-F12 | hoch | Drehbuch "Dateien" und Fallback; demo_u6_sqlite.py | `code/beispiele.sqlite` fehlt im Drive. Ohne Datei: `OperationalError: no such table: lehrveranstaltung`, zusätzlich legt `connect()` eine leere 0-Byte-Datei an, die spätere Fehlersuche verschleiert. Abnahme "beide Varianten lauffähig" nicht erfüllt; auch die WP1-Verifikationsgrundlage für U3-SQL fehlt | Portierung reproduzierbar erzeugen (Skript aus `create_beispiele.sql`), in `Unit_6/code` ablegen, Grösse dokumentieren; im Code Existenzprüfung mit klarer Meldung oder Öffnen mit `mode=ro` (URI), damit keine leere Datei entsteht |
| U6-F13 | mittel | Drehbuch Einzelarbeit Aufgabe 2 und 3 | Spalte heisst `raum.standort` (Fremdschlüssel), nicht `standort_id`; Prüfungen verweisen über `pruefung.fach`. Auftrag nennt nur den Funktionsparameter, TN schreiben erwartbar `standort_id` und erhalten "Unknown column" | Spaltennamen im Auftrag nennen oder bewusst "zuerst `DESCRIBE raum`" als Schritt einbauen |
| U6-F14 | mittel | Drehbuch Einzelarbeit | Kein TN-Handout und keine Auftragsfolie; Auftrag und Kontrollwerte stehen nur im Dozenten-Drehbuch | einseitige Auftragsfolie ohne Kontrollwerte |
| U6-F15 | mittel | demo_u6_mysql.py und demo_u6_sqlite.py, `UseDB.__exit__` | Commit auch im Fehlerfall, kein Rollback (aus Repo `db_context.py` übernommen); vermittelt ein falsches Transaktionsmuster, relevant ab Unit 9 (Session) | bei Exception `rollback()`, sonst `commit()`; ein Satz im Drehbuch Block 5 |
| U6-F16 | tief | Drehbuch Block 4c | Aufruf von `fach_suchen("DBWE")`, die Funktion wird im Live-Ablauf nie getippt (nur in der Referenzdatei) | Zeile durch `execute` mit gültigem Wert ersetzen |
| U6-F17 | tief | Drehbuch Block 3 und 5, beide Demo-Dateien | Sortierungen mit Gleichständen (gleiche Startzeit bzw. gleicher Schnitt); MySQL und SQLite können Reihenfolge verschieden liefern; Kontrollwerte Block 5 nur für die ersten zwei Zeilen eindeutig | zweiten Sortierschlüssel ergänzen |
| U6-F18 | tief | Drehbuch Kontrollwert Block 5 | Fachtitel ist in der DB falsch geschrieben ("Risikomangement"), Drehbuch schreibt ihn korrekt; TN sehen die Abweichung | Hinweis im Drehbuch oder als Datenqualitäts-Moment nutzen |
| U6-F19 | tief | Drehbuch Fallback "Was gleich bleibt: Alles" | MySQL liefert `datetime`/`Decimal`, SQLite Strings/float; Ausgaben unterscheiden sich sichtbar | Zeile in der Unterschiedstabelle ergänzen |
| U6-F20 | tief | Drehbuch Block 5 Sprechnotiz | "Die Datenbank hat einen Index, euer Python nicht" als Grund für 20 ms vs. 20 s: bei GROUP BY über die ganze Tabelle hilft ein Index kaum, Hauptgrund ist der Transfer der Rohdaten | Begründung präzisieren |
| U6-F21 | tief | Drehbuch Block 2; code-Ordner | "`.gitignore` zeigen", im Code-Ordner liegt keine Beispiel-`.gitignore` | `.gitignore` mit `config.py`, `.venv/`, `__pycache__/` mitliefern |
| U6-F22 | mittel | Quiz U6 Lösungstabelle | Alle sieben Fragen haben dieselbe Lösungsposition; Muster nach 2-3 Fragen erkennbar, Quiz verliert Aussagekraft | Optionen mischen, Lösungstabelle anpassen |
| U6-F23 | mittel | Selbststudium U6, Idee 2 | Adressverwaltung mit CSV (Erfassen, Suchen, Speichern) ist in `kap-17/adressbuch06.py` und `kap-15/adressbuch07.py` öffentlich gelöst; neu wäre nur der SQLite-Teil | Idee 2 durch neues Szenario ersetzen oder SQLite-Teil zur Pflicht machen und Suchlogik ändern |
| U6-F24 | mittel | Selbststudium U6, A2 "Datenbank" | Im Unterricht wird nur SELECT gezeigt; CREATE TABLE, INSERT und `commit()` fehlen (nur im Fallback-Text erwähnt) | Mini-Beispiel INSERT + commit als Anhang oder Empfehlung "Datei für A2, DB optional" |
| U6-F25 | tief | Selbststudium U6, Idee 1 | Verweis auf `summieren()` aus U6.1: der Name existiert nur in der Musterlösung | allgemein formulieren ("eure Summierfunktion") |
| U6-F26 | tief | code/Adressen.csv | Telefonnummern im realistischen Format mit echten Vorwahlen, könnten echten Anschlüssen gehören; Material landet ggf. im öffentlichen Repo | eindeutig fiktive Nummern verwenden |

### 7.3 KT3 übergreifend (Planpassung, Querverweise)

| ID | Grad | Datei + Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| KT3-F01 | hoch | Selbststudium U5 "Vorbereitung auf Unit 6" und Dozentenhinweise; Selbststudium U6 "Frist vor Unit 7", "Vorbereitung auf Unit 7", Dozentenhinweis "Abgaben vor Unit 7 sichten"; Leitfaden U5 "neue Frist vor Unit 6"; WP1-Übersicht "vor Unit 6: überarbeitetes CREATE-Skript" | Unter S2610 liegen U5, U6 und U7 am selben Tag (KT3). Alle Fristen und Vorbereitungen "vor Unit 6/7" (Lektüre PYGR 13-15/17-18, MySQL-Check, CREATE-Skript nachreichen, Selbstcheck-Abfrage und Übungsbesprechung zu Beginn U6, Code-Abgabe und Sichtung vor U7) sind nicht durchführbar | Fristen auf "vor KT4 (04.12.)" umstellen; Lektüre und MySQL-Check in den Selbststudiumsauftrag nach KT2 verschieben; die drei Selbststudien zu einem KT3-Auftrag mit Prioritäten zusammenführen |
| KT3-F02 | mittel | U5.2 Anschluss ("in zwei Wochen"); U6.1 Zusatz ("Modul-Input direkt nach dieser Übung"); Drehbuch ("open() heute Vormittag", "nächste Woche Klassen", "Setup-Sprechstunde vor Unit 7"); beide Demo-Docstrings ("heute Vormittag"); Quiz U6 Auswertung ("Setup-Phase am Schluss von Unit 7", "venv-Anleitung aus Selbststudium U7"); Leitfaden und Selbststudium U5 ("PA-Sprechstunde in Unit 6") | Zeitbezüge und Verweise passen nicht zum verdichteten Tag; PA-Sprechstunde, U7-Setup-Phase und Selbststudium U7 existieren nicht | alle Stellen auf KT3/KT4-Logik umschreiben (z. B. "heute Nachmittag", "gleich nach der Pause", "Setup-Sprechstunde vor KT4") |
| KT3-F03 | hoch | Plan 13:00-13:20; Drehbuch Voraussetzung "venv aktiv" und Block 1; Quiz U6 Fragen 3/4 | Der Plan enthält keinen pip/venv-Schritt (Handoff-Ablauf U6 hatte ihn). Auf macOS mit Homebrew-Python verweigert pip die globale Installation (externally-managed-environment), die MySQL-Demo blockiert dort ohne venv. LZ 3 von U6 hat keinen Slot | venv als Stopp-Marke (5-10 min) in den Input 13:00-13:20 aufnehmen oder als Vorab-Auftrag nach KT2 mit Anleitung Windows/macOS; sonst SQLite-Fallback als Standard für alle |
| KT3-F04 | hoch | Plan Nachmittag vs. U6.1, U6.2, Drehbuch | Vorhandene U6-Materialien brauchen 108 min statt 75 min (Überzug ca. 33 min plus venv). Folge: Code-Review oder Klassenübung fällt weg | Kürzungen festlegen: U6.1 Debriefing 5 min; U6.2 Aufgabe 3 im Plenum und Debriefing 5 min; Drehbuch Block 5 (Notenschnitt) streichen, Einzelarbeit auf Aufgabe 1 (5 min) reduzieren, Aufgaben 2-3 ins Selbststudium |
| KT3-F05 | hoch | Plan 14:50-17:00 | Für den U7-Teil fehlt sämtliches Material (Code-Review bank2c, Klassen-Übung, PP8, OOP-Quizteil, Selbststudium U7 inkl. Vererbung und Flask-venv) | siehe Abschnitt 8 |
| KT3-F06 | mittel | Plan 14:50-15:05 (Code-Review vor Klassen-Input) | Handoff sah U7.0 nach dem Input Properties vor (K4). `bank2c.py` nutzt Properties, doppelte Unterstriche, List Comprehension und `max()`; ohne Klassen-Grundlagen ist die Fehlersuche auf Papier in 15 min für Einsteiger kaum lösbar | Code-Review als geführte Leseaufgabe mit 3 Leitfragen (Methode markieren, "woher kommt dieser Name?") oder nach 15:25 platzieren |
| KT3-F07 | mittel | Plan 11:10-11:35 und U5.1/U5.2 | Vormittag: U5.1/U5.2 brauchen ca. 13 min mehr als geplant, das Modell-Debriefing hat 20 min ohne Material | Plan-Debriefing auf 10 min kürzen und Zeit den Übungsdebriefings geben |
| KT3-F08 | mittel | Plan 16:30-16:45; Quiz U6 | Quiz U6 füllt allein die 15 min, geplant ist ein Kombiquiz OOP + Persistenz | Auswahl gemäss 4.3; OOP-Fragen neu erstellen |
| KT3-F09 | mittel | Plan Lernziele KT3 | U6 LZ 2/3 (Module/Pakete entwickeln, Pakete installieren) ohne Slot, U7 LZ 2/3 (Vererbung, Sichtbarkeit) nur im Selbststudium; Plan führt U6 LZ 1 als K3, Handoff und U6.1 als K4 | LZ-Abdeckung im Plan ausweisen, Selbststudium so gestalten, dass LZ prüfbar sind |
| KT3-F10 | mittel | U5.1, U5.2, U6.1, U6.2 (Struktur) | TN-Teil und Dozententeil (Lösungen, Kontrollwerte, Zirkulier-Hinweise) stehen in einer Datei; kein separates Handout, obwohl der Handoff "Auftragsfolie und Handout" verlangt. U5.2 verweist TN auf die Tabelle im Dozententeil | je Übung TN-Handout (Auftragsfolie + Aufgaben) und Dozentenfassung trennen |
| KT3-F11 | tief | Quiz U5, Quiz U6 | "Particify-Importformat" nur als copy-paste-Text umgesetzt (WP1-Annahme 1), keine Importdatei | vor Einsatz Import in Particify testen, sonst Handoff-Vorgabe anpassen |
| KT3-F12 | tief | alle U5/U6-Materialien | KI-Stufen 0/1 werden verwendet, die Skala ist weder im Handoff noch im Plan definiert | Skala einmal zentral definieren (Kickoff-Folie, Kurskanal) |

Remote-Reste: keine gefunden. Geprüft durch vollständiges Lesen aller Markdown-Dateien und Textsuche in allen Codedateien (Breakout, Poll, Screen, Remote, Zoom, Teams, Miro, Kamera, geteilt). Der Kurskanal für Abgaben ist laut Handoff präsenzkonform.

Querverweise, die im Rahmen dieses Teils nicht prüfbar waren: U5.1 auf "Quiz U4 Frage 3", Drehbuch auf "Partnerübung U3.1 Aufgabe 3", U6.1 auf "Gruppenübung U3.2", Leitfaden auf "Partnerübung U2.1" und "Selbststudium U3". Die Dateien liegen ausserhalb dieses Umfangs.

---

## 8 Lücken für KT3 (U7-Block)

| Plan-Slot | benötigtes Material | vorhanden | Handoff-Spezifikation | Hinweise für die Erstellung |
|---|---|---|---|---|
| 13:00-13:20 | Input Funktionen/Module inkl. venv/pip-Stopp | nein (nur "Folien Python" laut Fachplan, nicht geprüft) | U6-Ablauf: Input Funktionen, Module/Pakete, pip/venv | venv-Anleitung Windows und macOS (KT3-F03) |
| 14:50-15:05 | Kurzaufgabe U7.0 Code-Review `bank2c.py` | nein | Repo-Datei unverändert, Klassendiagramm-Skizze, Fehler finden, Nachweis mit zweitem Kunden, Korrektur; Lösungsblatt, Sprechnotiz "Musterlösungen sind nicht fehlerfrei" | Bug reproduziert (Abschnitt 5, Nr. 9): Nachweis braucht einen zweiten Kunden mit mindestens zwei Konten; als Modul importiert entsteht ein `NameError`. `kap-16/bank2d.py` im selben Repo-Ordner enthält die korrigierte Zeile: TN nur `bank2c.py` geben, im Lösungsblatt erwähnen. Das Nummernschema in `add_konto()` hat eine weitere Schwäche, die sich als Zusatzfund eignet (nur im nicht öffentlichen Lösungsblatt beschreiben). Reihenfolge-Problem KT3-F06. 98 Zeilen: Ausdruck mit Zeilennummern oder gekürzte Fassung |
| 15:05-15:25 | Input Klassen/Objekte + Auflösung des Bugs | nein | im Handoff kein eigenes Material (Folien Python) | kurze Demo-Notiz für die Bug-Auflösung (Brücke zu PP8 Folie 1) |
| 15:40-16:10 | Partnerübung U7.1 Eigene Klassen entwerfen | nein | 2 Klassen, Attribute, `__init__`, Methoden, `__str__`, Testsequenz, 5 min Papierentwurf; Entwurfsentscheidung | nicht Kunde/Konto; auch Repo-Szenarien kap-16 (person, mitarbeiter, haus, computer, color, bank) und kap-19 (autos, computer, simple_person) meiden. Kurs/Teilnehmer knüpft an U5.1 und das Ersatzmodell U5 an |
| 16:10-16:30 | PP8 Best Practices und Patterns | nein | Handoff: 10-12 Folien, 25 min, 3 Diskussionsfragen; Plan: 6-8 Folien, 15-20 min, Murmelgruppen | Plan-Umfang übernehmen: Rückblick Bug, eine Verantwortung pro Klasse, `_name`-Konvention, Vererbung vs. Komposition ("Ist ein Konto eine Liste?"), Ausblick Flask-Models, Selbststudiums-Fahrplan |
| 16:30-16:45 | Quiz OOP-Begriffe + Persistenz | teilweise (Quiz U6) | Quiz U7: 7 Fragen inkl. Codefrage | Kombiquiz gemäss 4.3 |
| 16:45-17:00 und danach | Selbststudium KT3 (U5 + U6 + U7) | teilweise (U5, U6 mit falschen Fristen) | Selbststudium U7: Klassen-Übungen PYGR 16/19, PA-Klasse modellieren, venv mit Flask Schritt für Schritt (Windows/macOS), Screenshot, Setup-Sprechstunde | ein zusammengeführter Auftrag bis KT4 (04.12.) mit Prioritäten; Umfang U5 90 + U6 90 + U7 90 min + Flask-venv + Datenmodell-Überarbeitung |
| Selbststudium | Partnerübung U7.2 Vererbung und Sichtbarkeit als Selbststudiumsblatt | nein | Basisklasse mit 2 Unterklassen, `super()`, Überschreiben, Property; Stilreferenz `kap-19/inheritance1.py`, Szenario neu | laut Plan-Verdichtung ins Selbststudium; mit Musterlösung für Selbstkontrolle (nicht im öffentlichen Repo) |
| (Handoff U7) | Setup-Phase Flask-venv | im Plan ins Selbststudium verschoben | Dozent zirkuliert | Setup-Sprechstunde 07:30 vor KT4 ankündigen |

---

## 9 Vor Einsatz an KT3 zu erledigen

Priorität 1 (ohne diese Punkte ist KT3 nicht wie geplant durchführbar):

1. `Adressen.csv` mit BOM und CRLF neu schreiben, Aufgabe 1a auf Windows und macOS testen (U6-F05).
2. U6.2 Satz zum Textvergleich korrigieren (U6-F06).
3. U6.1 Problemstellung (Aufgabe 0/2a) neu fassen, Monolith und Musterlösung anpassen, diff-Test wiederholen (U6-F01).
4. `beispiele.sqlite` reproduzierbar erzeugen und in `Unit_6/code` ablegen; Existenzprüfung in `demo_u6_sqlite.py`; Fallback auf beiden Betriebssystemen testen (U6-F12).
5. `demo_u6_mysql.py` gegen MySQL 8 mit `create_beispiele.sql` testen, Kontrollwerte des Drehbuchs abgleichen (anderer Agent).
6. venv/pip-Schritt in Plan und Drehbuch verankern oder als Vorab-Auftrag nach KT2 (KT3-F03).
7. Nachmittag kürzen gemäss KT3-F04 und Kürzungen in den Dozententeilen vermerken.
8. Alle Fristen und Verweise "vor Unit 6/7" auf KT4 umstellen, Selbststudium KT3 zusammenführen (KT3-F01, KT3-F02).
9. U7-Material erstellen: Code-Review U7.0, Klassen-Übung U7.1, PP8, OOP-Quizteil, Selbststudium U7 mit U7.2 und Flask-venv-Anleitung (Abschnitt 8).
10. Frist für das Datenmodell aus Selbststudium U3 so setzen, dass vor KT3 gesichtet und Gruppen gebildet werden können (Leitfaden Teil B, Vorbereitung).

Priorität 2 (Qualität, Nacharbeit vermeiden):

11. TN-Handouts von Dozentenfassungen trennen (4 Partnerübungen, Einzelarbeit Demo) (KT3-F10, U6-F14).
12. Quiz U5 Fragen 4 und 5 überarbeiten; Quiz U6 Lösungspositionen mischen und für Kombiquiz kürzen (U5-F12, U5-F13, U6-F22, KT3-F08).
13. Review-Bogen auf eine Seite mit 3 Prüffragen; Debriefing 11:10-11:35 klären; Lösungsnotiz Ersatzmodell ergänzen, Ablauf bei fehlendem Modell festlegen (U5-F17 bis U5-F22).
14. U5.1 Hinweis zum Auskommentieren in 4b; U5.2 Musterlösung Menge (U5-F02, U5-F08).
15. `UseDB.__exit__` mit Rollback (U6-F15); Spaltennamen in der Einzelarbeit (U6-F13); `.gitignore` mitliefern (U6-F21).
16. Selbststudium U5 Zeitblöcke gegen Lehrmittelkapitel prüfen (U5-F23); Selbststudium U6 Idee 2 und DB-Schreiben (U6-F23, U6-F24).
17. Particify-Räume anlegen, Import testen (KT3-F11).

Priorität 3: übrige tief-Findings.
