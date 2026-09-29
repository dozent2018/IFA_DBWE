# Inventar 02: Foliensätze Kurstag 1 (PP1 bis PP4)

Kurs DBWE.TA1A «Datenbanken und Web-Entwicklung», Kurstag 1 (Fr, 23.10.2026, Unit 1 + Unit 2).
Geprüfte Fassung: Foliensätze des Co-Autors vom 18.09.2026 (generiert mit PptxGenJS).
Erstellt am 29.09.2026 als Teil des Rework-Inventars. Keine Änderungen an den Foliensätzen vorgenommen.

Schweregrade: **hoch** = falsch oder blockiert Unterricht; **mittel** = verwirrt TN oder erzeugt Nacharbeit; **tief** = Kosmetik.

---

## 1 Gelesener Umfang

| Quelle | Umfang | Methode |
|---|---|---|
| PP1_U1_Kickoff_Kursueberblick.pptx | 9 von 9 Folien inkl. Sprechernotizen (100 %) | Drive-Textauszug vollständig gelesen; zusätzlich Binärdatei dekodiert und mit python-pptx 1.0.2 jede Form, Tabelle, Schriftgrösse und Notiz ausgewertet |
| PP2_U1_Grundbegriffe_Relationales-Modell.pptx | 7 von 7 Folien inkl. Notizen (100 %) | wie oben |
| PP3_U2_Anomalien_Normalisierung.pptx | 8 von 8 Folien inkl. Notizen (100 %) | wie oben |
| PP4_U2_Schluessel_ERD_JOIN.pptx | 9 von 9 Folien inkl. Notizen (100 %) | wie oben |
| Unterrichtsplan S2610 (Stand 18.09.2026) | vollständig gelesen; Schwerpunkt Abschnitte 1 (Überblick, Prinzipien, Prüfung) und 2 (WP 1: Ablauf Vormittag/Nachmittag, PP-Outlines WP 1); Abschnitte 3 bis 8 für Querbezüge (PP6, PP15, KT6, Checkliste) | Drive-Textauszug |
| KI-Handoff v2.0 (02.09.2026) | Zeilen 1 bis 254 vollständig (Rahmen, Mapping, Repo-Material, WP 0 mit allen 16 Materialspezifikationen) | lokale Markdown-Kopie |
| SQL/create_beispiele.sql | alle 14 CREATE-TABLE-Blöcke und Constraints vollständig gelesen; die INSERT-Zeilen (bis 406'000 Zeichen pro Zeile) nicht zeilenweise gelesen, sondern vollständig maschinell in eine Prüf-Datenbank geladen und abgefragt (Zeilenzahlen, NULL-Werte, Datensätze ohne Partner, Duplikate) | Read + Python/SQLite |
| SQL/kap-3.sql | vollständig (Demo-Basis U1, Namenskonventionen) | Read |
| SQL/kap-4.sql | Ausschnitt Zeilen 40 bis 160 (JOIN-, UNION-Beispiele des Lehrmittels, Konventionsvergleich) | Read |

Rohkopien der vier .pptx liegen nur im Scratchpad (`scratchpad/drive/18.09.2026/`), nicht im Repo.
Layout wurde **technisch geprüft** (python-pptx: leere Platzhalter, Notizen, Schriftgrössen, Überlauf-Heuristik, Überlappungen), aber **nicht gerendert**: Überlauf-Hinweise sind Indizien und müssen visuell bestätigt werden.

---

## 2 Inventar pro Deck

### 2.1 Zeitbudget laut Unterrichtsplan vs. Folienmenge

| Deck | Folien | Slot laut Unterrichtsplan | Outline-Soll | Einschätzung |
|---|---|---|---|---|
| PP1 Kickoff | 9 (1 Titel + 8 Inhalt) | 08:00-08:25 = 25 min **inkl.** Vorstellungsrunde (1 min/TN) | 8-10 Folien, 20 min | Zu knapp: 20 min Folien (Notiz F1) + Vorstellungsrunde (Notiz F9: 15 TN = 15 min) = ca. 35 min (siehe F08) |
| PP2 Grundbegriffe | 7 (1 + 6) | 08:35-08:55 = 20 min | 6-8 Folien, 20 min | Passt (ca. 3 min pro Inhaltsfolie) |
| PP3 Normalisierung | 8 (1 + 7) | 13:10-13:30 = 20 min | 6-8 Folien, 20 min | Knapp, weil der Stoff für die TN neu ist (kein Selbststudium zwischen U1 und U2, siehe F04) |
| PP4 Schlüssel/ERD/JOIN | 9 (1 + 8) | Teil A (F1-F4) 14:00-14:20 = 20 min **inkl.** Installation «beispiele»; F5 Auftragsfolie 14:35-15:00; Teil B (F6-F9) 15:00-15:20 = 20 min inkl. Demo | 8-10 Folien, 2 × ca. 15 min | Teil B passt; Teil A knapp, weil die DB-Installation bei allen TN im selben Slot liegt (F24) |

Alle 33 Folien haben Sprechernotizen (243 bis 471 Zeichen). Keine leeren Platzhalter (nur Foliennummern-Platzhalter, alle befüllt).

### 2.2 PP1 Kickoff: Kursüberblick und Lernweg (9 Folien)

Gedankenstriche aus Folientiteln sind hier durch Komma/Doppelpunkt ersetzt.

| Nr | Rubrik | Titel | Kerninhalt | Notizen | Fliesstext/Tabelle (pt) |
|---|---|---|---|---|---|
| 1 | PP 1 · UNIT 1 · KICKOFF | Datenbanken und Web-Entwicklung | Untertitel Lernweg, Start 23.10.2026 | ja | 13-17 |
| 2 | KURSZIEL | Am Ende steht eure eigene Webapplikation | Kacheln Daten/Logik/Web, Prüfungsform PA | ja | 13 |
| 3 | ROTER FADEN | SQL → Python → Flask → Praxisarbeit | 4 Chevrons mit Kurstagen, Box «Warum diese Reihenfolge?» | ja | 12-13.5 |
| 4 | SEMESTERÜBERBLICK | Sechs Kurstage, jeweils Freitag, 08:00 bis 17:00 | Tabelle 6 KT (VM/NM), 5-Wochen-Phase, Abgabe | ja | 12.5 |
| 5 | PRÜFUNGSFORM | Die Praxisarbeit, kurz vorgestellt | eigenes Szenario, Bausteine, Doku 3-5 S., Präsentation max. 8 min, Zeitplan, «Raster am KT2» | ja | 12.5 |
| 6 | MATERIAL | Lehrmittel und Code-Beispiele | DBSQL/PYGR/FLASK je Kurstage, GitHub-Repo, Hinweis «Übungen sind neu», Kurskanal | ja | 12-12.5 |
| 7 | ARBEITSWEISE | Selbststudium: gleicher Umfang wie der Unterricht | «1 : 1», «8 Lektionen», Wochenrhythmus, «Ab KT2 Theorie vorbereitet» | ja | 12.5-13 |
| 8 | SPIELREGELN PRÄSENZ | So arbeiten wir zusammen | Laptop zu (<10 min), Handy weg, Pünktlichkeit, Fragen, Setup-Sprechstunde | ja | 12.5 |
| 9 | JETZT SEID IHR DRAN | Vorstellungsrunde, 1 Minute pro Person | 3 Fragen, Überleitung Setup-Check | ja | 13 |

### 2.3 PP2 Datenbank-Grundbegriffe und das relationale Modell (7 Folien)

| Nr | Rubrik | Titel | Kerninhalt | Notizen | Fliesstext/Tabelle (pt) |
|---|---|---|---|---|---|
| 1 | PP 2 · UNIT 1 · INPUT | Datenbank-Grundbegriffe und das relationale Modell | Lernziele DBS/DB/DBMS, Eignung | ja | 13-17 |
| 2 | AUSGANGSLAGE | Warum überhaupt Datenbanken? | Datei-Chaos vs. Leistungen eines DBS | ja | 13 |
| 3 | BEGRIFFE | Datenbanksystem = DBMS + Datenbank | Grafik DBS-Rahmen mit DBMS und DB, Produktbeispiele | ja | 11.5-14 |
| 4 | DAS RELATIONALE MODELL | Alles ist eine Tabelle | Mini-Tabelle «student» (id, name, vorname, jahrgang), Begriffe, Schema | ja | 12.5-13 |
| 5 | MÖGLICHKEITEN | Was das relationale Modell stark macht | Konsistenz, SQL, Transaktionen, Verbreitung | ja | 12.5 |
| 6 | EINSCHRÄNKUNGEN | Wo das relationale Modell an Grenzen stösst | Sensordaten, vernetzte Daten, Merksatz | ja | 12.5-13.5 |
| 7 | AUSBLICK | SQL, eine Sprache für alles | 6 Anweisungen, Überleitung Fallarbeit und Demo | ja | 11.5-13.5 |

### 2.4 PP3 Anomalien und Normalisierung bis zur 3NF (8 Folien)

| Nr | Rubrik | Titel | Kerninhalt | Notizen | Fliesstext/Tabelle (pt) |
|---|---|---|---|---|---|
| 1 | PP 3 · UNIT 2 · INPUT | Anomalien und Normalisierung bis zur 3NF | Lernziel 3NF | ja | 13-17 |
| 2 | AUSGANGSLAGE | Eine Tabelle mit allem drin | Kursanmeldungen Weiterbildungsschule, 4 Zeilen, Redundanz markiert | ja | 12-13.5 |
| 3 | FOLGEN DER REDUNDANZ | Drei Anomalien, am selben Beispiel | Einfüge-, Änderungs-, Löschanomalie | ja | 12.5 |
| 4 | NORMALISIERUNG · SCHRITT 1 | 1. Normalform: nur atomare Werte | Verstoss/Lösung, Faustregel «Komma» | ja | 12-13 |
| 5 | NORMALISIERUNG · SCHRITT 2 | 2. Normalform: alles hängt vom ganzen Schlüssel ab | Verstoss mit (student_id, kurs_id), Zerlegung anmeldung/kurs | ja | 11-11.5 |
| 6 | NORMALISIERUNG · SCHRITT 3 | 3. Normalform: keine Abhängigkeiten über Umwege | transitive Abhängigkeit, Zerlegung kurs/dozent, Endergebnis 4 Tabellen | ja | 11-13 |
| 7 | MERKSATZ | Die 3NF in einem Satz | Merksatz, Kacheln 1NF/2NF/3NF | ja | 12 (Kacheln), 24 (Satz) |
| 8 | ÜBERLEITUNG | Und wie kommen die Tabellen wieder zusammen? | Übung, PK/FK, JOIN | ja | 13 |

### 2.5 PP4 Schlüssel, ERD und JOIN (9 Folien)

| Nr | Rubrik | Titel | Kerninhalt | Notizen | Fliesstext/Tabelle/Code (pt) |
|---|---|---|---|---|---|
| 1 | PP 4 · UNIT 2 · INPUT (ZWEITEILIG) | Schlüssel, ERD und JOIN | Teil A / Übung / Teil B | ja | 13-17 |
| 2 | TEIL A · SCHLÜSSEL | PRIMARY KEY und FOREIGN KEY in CREATE TABLE | Code kurs/anmeldung, 3 Begriffe | ja | Code 13, Text 12.5 |
| 3 | TEIL A · ERD | Beziehungen zeichnen: das ERD | dozent 1:n kurs, Lesehilfe | ja | 11.5-14 |
| 4 | TEIL A · UNSERE ÜBUNGS-DB | Die Muster-DB «beispiele»: eine Schulverwaltung | 4 Gruppen mit 13 Tabellennamen, «14 Tabellen» | ja | 12.5-13.5 |
| 5 | PARTNERÜBUNG · 25 MINUTEN | Schema lesen: ERD der Muster-DB auf Papier | Auftragsfolie U2.2 (Ziel, Sozialform, Zeit/Ergebnis, Hilfsmittel) | ja | 13 |
| 6 | TEIL B · JOIN | JOIN: verteilte Daten wieder zusammenführen | Mini-Tabellen student/klasse, Ergebnis, SQL | ja | Tabellen 11.5, Code 15 |
| 7 | TEIL B · JOIN-ARTEN | INNER JOIN oder LEFT JOIN? | Ergebnisvergleich mit Person ohne Klasse | ja | 11.5-12.5 |
| 8 | TEIL B · STOLPERSTEIN | Der Klassiker: JOIN ohne ON | kartesisches Produkt 2 × 2 | ja | Tabelle 11, Code 14 |
| 9 | TEIL B · UNION | UNION: stapeln statt verbinden | Schema JOIN vs. UNION, Kontaktliste, Überleitung Übung | ja | 11.5-13.5 |

---

## 3 Abgleich Outline (Unterrichtsplan) und Handoff-Spezifikation vs. Ist

Legende Status: **erfüllt**, **teilweise**, **fehlt**, **zusätzlich**.

### 3.1 PP1 gegen Outline «[PP 1] Kickoff» und Handoff «Kickoff-Folien U1»

| Soll | Ist | Status | Bemerkung |
|---|---|---|---|
| 1 Willkommen + Kursziel | F1, F2 | erfüllt | |
| 2 Roter Faden visuell, eine Folie, eine Grafik | F3 (4 Chevrons) | teilweise | Grafik zeigt PA als vierten Schritt nach Flask; Notiz spricht von «PA-Pfeil unten», der fehlt (F11) |
| 3 Die 6 Kurstage im Überblick | F4 | erfüllt | kleine Themenlücken KT2/KT3 (F34) |
| 4 Prüfungsform PA (kurz, Details ab WP 2) | F5 | teilweise | deutlich mehr Details als «kurz», mehrere unbestätigte Zusagen (F05) |
| 5 Lehrmittel + Repo (Buchlösungen im Repo, Übungen neu) | F6 | erfüllt | Verteilweg widersprüchlich (F06) |
| 6 Selbststudium = gleicher Umfang, Wochenrhythmus | F7 | teilweise | «8 Lektionen» falsch (F07); Beginn «Theorie vorbereitet» uneinheitlich (F09) |
| 7 Spielregeln Präsenz | F8 | erfüllt | Laptop-Regel weicht vom Unterrichtsplan ab (F10) |
| 8 Vorstellungsrunde (Name, Firma, Berührungspunkte DB/Web) | F9 | erfüllt, zusätzlich | Zusatzfrage «Was willst du mitnehmen?» verlängert die Runde (F08) |
| Handoff: «Semesterüberblick 16 Units in 3 Teilen» | F4 zeigt 6 Kurstage | bewusst abweichend | Handoff ist hier noch auf den Remote-Plan ausgerichtet; PP1 folgt korrekt dem Präsenz-Unterrichtsplan |
| Handoff: «Details folgen ab Unit 3» | F5 «am Kurstag 2» | erfüllt | KT2 Vormittag = U3 |
| Handoff Abnahme: roter Faden auf einer Folie | F3 | erfüllt mit Einschränkung | siehe F11 |
| Handoff Abnahme: Selbststudiums-Erwartung unmissverständlich | F7 | teilweise | Zahl falsch, Startzeitpunkt uneinheitlich |
| Handoff Format: Markdown-Outline mit Notizen | .pptx mit Notizen | übererfüllt | |

### 3.2 PP2 gegen Outline «[PP 2]» und Inputs für U1.1 und Demo U1

| Soll | Ist | Status | Bemerkung |
|---|---|---|---|
| 1 Warum Datenbanken? | F2 | erfüllt | Überversprechen «jede Information genau einmal» (F14) |
| 2 Begriffsklärung DBS = DBMS + DB (Grafik) | F3 | erfüllt | Hinweis «Schema = Datenbank» in MySQL fehlt (F30) |
| 3 Relationales Modell: Tabellen, Zeilen, Spalten, Schlüssel | F4 | erfüllt | Mini-Tabelle weicht von Demo und «beispiele» ab (F26) |
| 4 Stärken: Konsistenz, Abfragesprache, Transaktionen | F5 | erfüllt, zusätzlich | vierte Stärke «bewährt und verbreitet» |
| 5 Grenzen, Überleitung zur Fallarbeit | F6 | erfüllt | nimmt die Beurteilung der Fallarbeit vorweg (F13) |
| 6 SQL als Standardsprache, was heute erwartet | F7 | erfüllt | |
| Input für U1.1: Begriffe DBS/DB/DBMS für Szenario (a) | F3 | erfüllt | |
| Input für U1.1: Eignungskriterien | F5, F6 | erfüllt | aber als fertige Antworten (F13) |
| Auftragsfolie U1.1 (Ziel, Zeit, Sozialform, Output, Hilfsmittel) | nur ein Satz auf F7 | fehlt | |
| Teaser Demo U1 (6 Grundoperationen) | F7 | erfüllt | |

### 3.3 PP3 gegen Outline «[PP 3]» und Inputs für U2.1

| Soll | Ist | Status | Bemerkung |
|---|---|---|---|
| 1 Einstiegsbeispiel «böse» Tabelle | F2 | erfüllt | |
| 2 Drei Anomalien je mit konkretem Fall | F3 | erfüllt | konkrete Fälle stehen vor allem in den Notizen |
| 3 1NF: atomare Werte | F4 | erfüllt | Wiederholungsgruppen (kurs1, kurs2, ...) als zweiter typischer Verstoss fehlen (tief) |
| 4 2NF: volle funktionale Abhängigkeit | F5 | teilweise | Begriff «funktionale Abhängigkeit» und Pfeilnotation nicht eingeführt (F17) |
| 5 3NF: keine transitiven Abhängigkeiten | F6 | erfüllt | Beispielbrüche (F15) |
| 6 Faustregel | F7 | teilweise | «Jedes Attribut» statt «Jedes Nicht-Schlüssel-Attribut»; 1NF-Zuordnung widerspricht F4 (F16) |
| 7 Überleitung PK/FK | F8 | erfüllt | |
| U2.1: Anomalien benennen, 1NF→2NF→3NF | F3-F6 | erfüllt | |
| U2.1 Schritt 3: CREATE TABLE mit PK/FK in Workbench | F7/F8 «auf Papier, ohne SQL» | Widerspruch | PK/FK-Input folgt erst nach der Übung (F19) |
| U2.1: neues Szenario | Notiz F6 «genau das Modell, das die TN nachher bauen» | Widerspruch | Handoff-Szenario deckungsgleich mit PP3-Beispiel (F18) |
| Auftragsfolie U2.1 | nur ein Absatz auf F8 | fehlt | |

### 3.4 PP4 gegen Outline «[PP 4]» und Inputs für U2.2 und U2.3

| Soll | Ist | Status | Bemerkung |
|---|---|---|---|
| 1 PRIMARY KEY und FOREIGN KEY in CREATE TABLE | F2 | teilweise | Syntaxfehler (F01) |
| 2 ERD-Notation mit Kardinalitäten (Krähenfuss) | F3 | teilweise | nur «1»/«n» an einer Linie, keine Krähenfuss-Symbole, keine Min-Kardinalität, kein n:m (F20) |
| 3 Muster-DB «beispiele»: 14 Tabellen (Übersichtsgrafik) | F4 | teilweise | 13 Namen, Gruppierung teils falsch (F21); bewusster Verzicht auf Beziehungslinien ist sinnvoll (verrät die Übung nicht) |
| 4 Schnitt: Übung ERD | F5 Auftragsfolie | erfüllt, zusätzlich | Auftragsfolie war in der Outline nicht vorgesehen |
| 5 JOIN-Idee mit zwei Mini-Tabellen | F6 | teilweise | Spaltennamen passen nicht zu «beispiele» (F02) |
| 6 INNER vs. LEFT JOIN (Venn-artige Grafik + Ergebnisvergleich) | F7 | teilweise | Ergebnisvergleich vorhanden, keine Venn-Grafik (F35); Szenario auf «beispiele» nicht reproduzierbar (F03) |
| 7 JOIN ohne ON | F8 | erfüllt | Notiz-Zahlen falsch (F28) |
| 8 UNION: stapeln statt verbinden, wann was | F9 | teilweise | kein SQL, UNION ALL nur in Notiz (F23) |
| U2.2: 7 Tabellen (student, klasse, lehrgang, standort, adresse, pruefung, fach) | F5: 3 Tabellen + optional fach | Abweichung | F22 |
| U2.2: Krähenfuss, information_schema-Vorlage, 3 Lesefragen, Reverse Engineer erst danach, A3, Galeriegang | F5 | fehlt | F22 |
| U2.3: INNER JOIN 2 Tabellen | F6 | teilweise | falsche Spaltennamen (F02) |
| U2.3: JOIN über 3 Tabellen, JOIN mit WHERE | keine Folie | fehlt | F25a |
| U2.3: LEFT JOIN mit sichtbar anderem Ergebnis | F7 | teilweise | auf «beispiele» mit den Handoff-Vorschlägen nicht erfüllbar (F03) |
| U2.3: UNION zweier SELECTs | F9 | teilweise | keine Syntaxvorlage (F23) |
| U2.3: Kontrast «JOIN oder UNION?» | F9 | erfüllt | |
| Auftragsfolie U2.3 | ein Satz auf F9 | fehlt | |

---

## 4 Passung zur Muster-DB «beispiele»

### 4.1 Fakten aus create_beispiele.sql (bestätigt und erweitert)

| Nr | Befund | Status |
|---|---|---|
| B1 | FK in `student` heisst `klasse` (nicht `klasse_id`); PK heisst `student_id` (nicht `id`); `student.name` enthält den vollen Namen, es gibt keine Spalte `vorname` | bestätigt, erweitert |
| B2 | Kein Student hat `klasse` = NULL (0 von 352), obwohl die Spalte NULL erlaubt | bestätigt |
| B3 | `klasse.standort` (int NOT NULL) hat keinen FK-Constraint | bestätigt |
| B4 | Auch `fach.dozent` hat keinen FK-Constraint | neu |
| B5 | `konto` und `fach_alt` haben keinerlei Beziehung; `fach_alt` wird im Lehrmittel für das UNION-Beispiel (Kap. 4.7) genutzt; `konto` vermutlich Transaktionsbeispiel (Annahme, im Repo-SQL nicht verwendet) | neu |
| B6 | Selbstreferenz: `mitarbeiter.vorgesetzter` → `mitarbeiter.ma_id` | neu |
| B7 | Konvention: PK = `<tabelle>_id` (Ausnahmen `ma_id`, `lehrv_id`); FK-Spalte heisst wie die Zieltabelle ohne `_id` (klasse, lehrgang, standort, adresse, fach, student, raum, dozent). Die Lehrmittel-Beispiele (kap-4.sql) verknüpfen student und klasse genau über diese Konvention | neu |
| B8 | Klassen-Bezeichnungen haben das Format Lehrgang.Standort.Nummer (z. B. HFSNT.ZH.6), nicht «INF-2026a» | neu |
| B9 | Keine Datensätze ohne Partner bei: student→klasse, klasse→student (jede der 30 Klassen hat Studierende), fach→pruefung, student→pruefung, dozent→fach. Partnerlose Datensätze gibt es dagegen auf den Ebenen lehrgang/klasse, standort/klasse, raum/pruefung sowie bei lehrveranstaltung mit dozent = NULL | neu |
| B10 | n:m-Strukturen: `fachplan` (lehrgang-fach), `pruefung` (student-fach, dazu raum), `lehrveranstaltung` (klasse-fach, dazu raum, dozent) | neu |
| B11 | Einzelne Personen kommen mit identischem Namen und identischer E-Mail sowohl in `student` als auch in `dozent` vor, zudem gibt es doppelte Einträge in `student`: UNION und UNION ALL liefern für eine Kontaktliste sichtbar unterschiedliche Zeilenzahlen | neu |
| B12 | Tabellenzahl 14: adresse, dozent, fach, fach_alt, fachplan, klasse, konto, lehrgang, lehrveranstaltung, mitarbeiter, pruefung, raum, standort, student | bestätigt |

### 4.2 Folienbeispiele gegen «beispiele»

| Fundstelle | verwendete Struktur | in «beispiele»? | als Mini-Beispiel erkennbar? | Risiko |
|---|---|---|---|---|
| PP2 F4 | student(id, name, vorname, jahrgang) | nein; weicht auch von der Demo (kap-3.sql: student_id, name, vorname, email) ab | nein | tief: «beispiele» ist in U1 noch nicht installiert, aber drei verschiedene student-Tabellen am selben Tag (F26) |
| PP3 F2-F6 | Weiterbildungsschule: student, kurs, dozent, anmeldung | eigenes Szenario (kurs, anmeldung existieren nicht) | ja, durch «Kursanmeldungen einer Weiterbildungsschule» | tief: Namensgleichheit student/dozent mit «beispiele» |
| PP4 F2-F3 | kurs, anmeldung, dozent(doz_id, name, mail) | nein | nur implizit (Fortsetzung PP3) | tief |
| PP4 F4 | Tabellenübersicht | 13 von 14 Tabellen genannt | nicht relevant | mittel (F21) |
| PP4 F5 | student-klasse-lehrgang | ja, beide FK-Constraints vorhanden | nicht relevant | tief; Zusatz «fach» problematisch (F22) |
| PP4 F6 | student(id, name, klasse_id), klasse(klasse_id, bezeichnung), JOIN über `s.klasse_id` | nein: Abfrage bricht auf «beispiele» mit «Unknown column» ab | nein: gleiche Tabellennamen wie «beispiele», Unterrichtsplan sagt «anhand von beispiele», Folie 9 leitet direkt in die Übung auf «beispiele» über | **hoch** (F02) |
| PP4 F7 | Person ohne Klasse (klasse_id = NULL) | nein (B2) | nein | **hoch** (F03) |
| PP4 F8 | JOIN ohne ON | läuft in MySQL auf «beispiele» (Produkt der Zeilenzahlen student × klasse, über 10'000 Zeilen) | nicht nötig | tief (F28) |
| PP4 F9 | Kontaktliste aus student und dozent | ja (name, email in beiden, auch in mitarbeiter) | nicht nötig | mittel: UNION-Duplikate (B11, F23) |

---

## 5 Findings

| ID | Schwere | Datei + Folie | Befund | Vorschlag |
|---|---|---|---|---|
| F01 | hoch | PP4 F2 | Syntaxfehler im CREATE-TABLE-Beispiel: nach `kurs_id INT PRIMARY KEY` fehlt das Komma vor `kursname VARCHAR(50) NOT NULL`. MySQL 8 bricht mit Fehler 1064 ab. TN, die das Beispiel abtippen, scheitern am ersten FK-Beispiel. Zusätzlich hat `anmeldung.student_id` keinen FK (keine student-Tabelle im Beispiel) und die kurs-Tabelle hat auf F2 keine `doz_id`, auf F3 aber schon. | Komma ergänzen; Kommentarzeile «FK auf student analog» oder zweiten FK ergänzen; kurs-Definition zwischen F2 und F3 angleichen. Code einmal in MySQL 8 ausführen. |
| F02 | hoch | PP4 F6 (Folgewirkung F7, F8) | JOIN-Beispiel nutzt `student.id` und `student.klasse_id`; in «beispiele» heissen die Spalten `student_id` und `klasse` (B1, B7). Die Folie trägt dieselben Tabellennamen wie «beispiele», der Unterrichtsplan kündigt den Input «anhand von beispiele» an und direkt danach folgt die Übung auf «beispiele». Wer die Folienabfrage ausführt, erhält «Unknown column 's.klasse_id' in 'on clause'». Das Lehrmittel verwendet die «beispiele»-Konvention. | Mini-Tabellen auf «beispiele»-Namen umstellen (student_id, name, klasse; klasse_id, bezeichnung) und Klassenwerte im Format von B8 zeigen; Hinweiskasten «In beispiele heisst die FK-Spalte wie die Zieltabelle». Alternative: deutlich als «Mini-Beispiel, nicht auf beispiele ausführbar» kennzeichnen (schwächer). |
| F03 | hoch | PP4 F7 (und Handoff U2.3) | Das LEFT-JOIN-Szenario «Person ohne Klasse» existiert in «beispiele» nicht (B2); LEFT JOIN und INNER JOIN student-klasse liefern dort identische Ergebnisse. Die im Unterrichtsplan vorgesehene Demo «anhand von beispiele» zeigt so keinen Unterschied. Auch die Handoff-Vorschläge für U2.3 («Klassen ohne Studierende», «Fächer ohne Prüfung») liefern keine partnerlosen Zeilen (B9); das Abnahmekriterium «LEFT JOIN liefert sichtbar andere Ergebnisse» ist damit nicht erfüllbar. | Folie als Mini-Beispiel kennzeichnen und für die Demo ein Tabellenpaar mit partnerlosen Datensätzen aus B9 wählen, oder temporär einen Datensatz ohne Klasse in einer Transaktion einfügen und mit ROLLBACK zurücknehmen. Handoff U2.3 (LEFT-JOIN-Aufgabe) entsprechend anpassen. |
| F04 | hoch | PP3 F1 Notiz (Ursache: Handoff U2) | Notiz: «Die TN kennen aus dem Selbststudium DBSQL Kap. 4-5, hier wird verdichtet und gesichert». Falsch: U1 und U2 finden am selben Tag statt, dazwischen liegt nur die Mittagspause; die Vorbereitungs-Mail verlangt nur Kap. 1-2. Die Normalisierung ist für die TN neu. Dieselbe Remote-Annahme steckt im Handoff (U2-Ablauf mit «Besprechung Selbststudiums-Übungen», Check-in-Quiz «deckt auf, wer das Selbststudium nicht gemacht hat»). | Notiz korrigieren: PP3 ist Erst-Einführung. Entweder Leseauftrag Kap. 4-5 in die Vorbereitungs-Mail aufnehmen (erhöht Vorbereitungslast deutlich) oder PP3 als Erst-Input planen (ggf. +5 min zulasten der Übung). Handoff-Texte zu U2 entsprechend bereinigen. |
| F05 | hoch | PP1 F5 (auch F4, F2 Notiz) | Verbindliche PA-Aussagen, obwohl offizielle Aufgabenstellung und Bewertungsraster nicht vorliegen (Unterrichtsplan 1.5 und Checkliste): Bausteine inkl. Deployment und REST-API, Doku 3-5 Seiten, Präsentation max. 8 min, Abgabe 2 Wochen nach KT6, «Aufgabenstellung und Bewertungsraster: am Kurstag 2». Der Unterrichtsplan selbst markiert die Doku-Anforderungen (PP15) als «nach Erhalt des Rasters abgleichen». Deployment hängt zudem an der offenen VM-Frage. | Folie mit «vorläufig, verbindlich ist die offizielle Aufgabenstellung» kennzeichnen; Zahlen (Seiten, Minuten, Abgabefrist) nur als «geplant» nennen; «Raster am KT2» nur zusagen, wenn die Lieferung gesichert ist, sonst «sobald verfügbar im Kurskanal». Detailtabelle in Abschnitt 5.1. |
| F06 | hoch | PP1 F6 (Notiz vs. Folie) + Vorbereitungs-Mail | Notiz: «Die drei Skripte werden im Unterricht verteilt»; Folie: «Verteilung ... über den Kurskanal»; Unterrichtsplan 1.5 und Handoff: Leseauftrag DBSQL Kap. 1-2 **vor** KT1. Wird das Lehrmittel erst am KT1 verteilt, ist der Leseauftrag nicht erfüllbar. Zeitkritisch: Die Vorbereitungs-Mail muss spätestens am 16.10.2026 raus. Kurskanal ist zudem als «Teams/Moodle» unentschieden. | DBSQL (mindestens Kap. 1-2) mit der Vorbereitungs-Mail bereitstellen oder Leseauftrag streichen; Notiz F6 angleichen; Teams oder Moodle festlegen und auf F6/F8 konkret benennen. |
| F07 | hoch | PP1 F7 | «Pro Kurstag (8 Lektionen)» ist falsch: Laut Unterrichtsplan 1.2 hat ein Kurstag 2 Unit-Slots à 5 Lektionen = 10 Lektionen (je Halbtag ein Slot à 5 × 45 min). Die Selbststudiums-Erwartung wird damit um 20 % zu tief kommuniziert, auf der «wichtigsten Erwartungs-Folie» (Notiz). | «10 Lektionen (rund 7,5 Stunden) Selbststudium pro Kurstag» o. ä.; bei verdichteten Units (U6/7, U10/11, U12/13, U14/15) Hinweis, dass das Selbststudium dort höher ist. |
| F08 | mittel | PP1 F1 Notiz, F9 Notiz; Unterrichtsplan 08:00-08:25 | Zeitbudget: Notiz F1 plant 20 min Folien, danach Vorstellungsrunde 1 min/TN (Notiz F9: bei 15 TN 15 min). Slot 25 min. Überzug ca. 10 min, der die Fallarbeit vor der Pause verkürzt. Die Zusatzfrage «Was willst du mitnehmen?» verlängert die Runde weiter. | PP1 auf 12-13 min straffen (F4 und F6 nur zeigen, F7 ausführlich) und Vorstellungsrunde auf 30-45 s oder 2 Fragen begrenzen; alternativ Vorstellungsrunde in den Standort-Block 08:25-08:35 integrieren. |
| F09 | mittel | PP1 F7 vs. Unterrichtsplan 1.3 | «Ab Kurstag 2: Theorie ist vorbereitet. Die Unterrichtszeit gehört Fragen, Vertiefung und praktischen Übungen.» Unterrichtsplan 1.3: Flipped Classroom erst ab WP 4; KT2 und KT3 enthalten weiterhin Inputs (PP5-PP8) und Demos. Die Erwartung ist strenger als die Planung und wird am KT2 sichtbar nicht eingehalten. | Erwartung staffeln: «ab KT2 Lektüre vorbereitet, Inputs werden kürzer; ab KT4 Flipped Classroom». Unterrichtsplan 1.3 und U1-Ausblick gleich formulieren. |
| F10 | mittel | PP1 F8 vs. PP2 F1 Notiz, PP3 F1 Notiz, Unterrichtsplan 1.4 | PP1: «Laptop zu bei Folien-Inputs unter 10 Minuten». Unterrichtsplan: [PP] max. 20 min, Laptops zu; PP2/PP3 sind 20-min-Inputs mit «Laptops zu». Nach der PP1-Regel dürften die Laptops bei PP2/PP3 offen bleiben. (Die Handoff-Mapping-Tabelle nennt ebenfalls «unter 10 min».) | Eine Regel festlegen, z. B. «Laptop zu bei allen Folien-Inputs (max. 20 min)», und PP1 F8, Unterrichtsplan und Handoff angleichen. |
| F11 | mittel | PP1 F3 | Die Grafik (4 Chevrons SQL, Python, Flask, Praxisarbeit) stellt die PA als vierten Schritt nach Flask dar. Die Notiz spricht von einem «PA-Pfeil unten», der zeigt, dass die PA parallel ab KT2 läuft; diese Form existiert nicht. Die Kernbotschaft «PA läuft parallel» wird visuell widerlegt. | Drei Chevrons SQL → Python → Flask, darunter ein durchgehender PA-Balken ab KT2 (Meilensteine: Datenmodell KT2, Review KT3, App ab KT4, Implementierung nach KT5, Präsentation KT6). |
| F12 | mittel | PP1 F2 Notiz, F5; Unterrichtsplan KT6 | «Am letzten Kurstag präsentiert jede/r eine laufende App» mit max. 8 min: Die Präsentationsblöcke am KT6 umfassen 45 + 60 min = 105 min; bei 8 + 4 min pro Person reicht das für höchstens 8 Präsentationen. PP1 rechnet mit 15 TN. | Hinweis an das Inventar zum Unterrichtsplan: KT6-Zeitplan an Klassengrösse anpassen. PP1 bis dahin ohne feste Minutenzahl formulieren. |
| F13 | mittel | PP2 F6 | Die Grenzen-Folie verwendet genau die Szenarien (b) Sensordaten und (c) vernetzte Daten der unmittelbar folgenden Fallarbeit U1.1 und liefert die Bewertung gleich mit. Die K4-Beurteilung wird dadurch zur Wiedergabe der Folie. | Folie auf Kriterien abstrahieren (Schreiblast, Strukturvariabilität, Vernetzungsgrad, Konsistenzbedarf) mit anderen Beispielen, oder F6 erst im Debriefing der Fallarbeit zeigen. |
| F14 | mittel | PP2 F2 | «Jede Information genau einmal, ohne Widersprüche» wird als Leistung jedes Datenbanksystems dargestellt. Redundanzfreiheit ist Ergebnis eines guten Entwurfs; PP3 zeigt am Nachmittag eine DB-Tabelle mit Redundanz. Das erzeugt eine Fehlvorstellung, die PP3 wieder korrigieren muss. | «ermöglicht redundanzarme Speicherung, wenn gut entworfen (heute Nachmittag: Normalisierung)». |
| F15 | mittel | PP3 F2-F6 | Das «durchgehende Beispiel» hat Brüche: Werte ändern sich bei der Zerlegung (Kursname und Ort erscheinen nach der Zerlegung in Kurzform), die Spalte kursort verschwindet zwischen F5 und F6, dozent fehlt in F5, die Tabelle student wird nie gezeigt, der Übergang von Namen (F2) zu IDs (F5) ist nicht erklärt (Schlüsselwahl). Notiz F6 spricht von `dozent_id`, die Tabelle von `doz_id`. | Eine Ausgangstabelle mit allen Spalten und IDs; jede Stufe zeigt das vollständige Zwischenergebnis mit identischen Werten; kurzer «Schritt 0: Schlüssel bestimmen». Namen vereinheitlichen (siehe F26). |
| F16 | mittel | PP3 F7 | Merksatz lautet «Jedes Attribut hängt vom Schlüssel ab ...». Korrekt ist «Jedes Nicht-Schlüssel-Attribut» (F5 formuliert es richtig). Die Kachel «1NF = vom Schlüssel» widerspricht F4 (1NF = atomare Werte). | «Jedes Nicht-Schlüssel-Attribut hängt vom Schlüssel ab, vom ganzen Schlüssel und von nichts als dem Schlüssel»; Kachel 1NF: «atomare Werte, Schlüssel vorhanden». |
| F17 | mittel | PP3 F5, F6 | Der Outline-Begriff «volle funktionale Abhängigkeit» fehlt; F6 nutzt die Pfeilnotation (A → B → C) ohne Einführung. Beide Begriffe tauchen im Quiz U2 und im Lehrmittel auf. | Auf F5 eine Zeile: «A → B heisst: kenne ich A, kenne ich B (funktionale Abhängigkeit)». |
| F18 | mittel | PP3 F6 Notiz vs. F7 Notiz; Handoff U2.1 | Notiz F6: «genau das Modell, das die TN nachher in der Übung selbst bauen»; Notiz F7 und Unterrichtsplan: «neues Szenario». Das Handoff-Szenario für U2.1 (Kursverwaltung mit Teilnehmern, Kursen, Trainern) ist praktisch deckungsgleich mit dem PP3-Beispiel. Die Lösung stünde damit auf der Folie. | U2.1-Szenario deutlich anders wählen (nah an «beispiele», aber andere Entitäten und Abhängigkeiten); Notiz F6 korrigieren. |
| F19 | mittel | PP3 F7/F8 vs. Handoff U2.1, Lernziel U2-1 | PP3: Übung «auf Papier, ohne SQL». Handoff U2.1 Schritt 3: Ergebnis als CREATE TABLE mit PK/FK in der Workbench. Da PK/FK erst nach der Übung (PP4 Teil A) kommen, ist PP3 konsequent, aber das Lernziel «PRIMARY KEY / FOREIGN KEY bei CREATE TABLE einsetzen (K3)» wird am KT1 nur noch im Zusatzauftrag geübt. | Nach PP4 Teil A 10 min «3NF-Ergebnis aus U2.1 als CREATE TABLE» einplanen oder als Pflichtteil in den Selbststudiumsauftrag U2 aufnehmen; Handoff U2.1 anpassen. |
| F20 | mittel | PP4 F3 | ERD nur mit «1» und «n» an einer einfachen Linie (keine Linienenden), keine Min-Kardinalität (optional/Pflicht), keine n:m-Beziehung. Outline und Handoff U2.2 verlangen Krähenfuss; die Kontrolle per Workbench-Reverse-Engineering zeigt Symbole an den Linienenden. PP3 erzeugt mit `anmeldung` genau eine Zwischentabelle, und «beispiele» enthält drei (B10). Aussage «Der Fremdschlüssel steht immer auf der n-Seite» ohne Hinweis auf n:m. Krähenfuss wird nur in der Notiz erwähnt. | Beispiel in Krähenfuss mit Legende (Kreis = 0, Strich = 1, Gabel = viele); zweites Mini-ERD student, anmeldung, kurs als n:m-Auflösung; Satz «bei 1:n steht der FK auf der n-Seite, n:m braucht eine Zwischentabelle». |
| F21 | mittel | PP4 F4 | Die Übersicht nennt 13 Tabellen, `fach_alt` fehlt, Text sagt «14 Tabellen, über Fremdschlüssel verbunden». `konto` steht unter «Betrieb», hat aber keine Beziehung (B5); `adresse` steht unter «Personen», wird aber auch von standort genutzt. Zwei Beziehungen haben keinen FK-Constraint (B3, B4). | Gruppierung z. B.: Personen (student, dozent, mitarbeiter), Ausbildung (lehrgang, klasse, fach, fachplan), Betrieb (lehrveranstaltung, pruefung), Infrastruktur (standort, raum, adresse), Einzeltabellen ohne Beziehung (konto, fach_alt). Text: «12 Tabellen über Beziehungen verbunden (zwei dieser Beziehungen ohne FK-Constraint), 2 Einzeltabellen». |
| F22 | mittel | PP4 F5 vs. Handoff U2.2 | Auftragsfolie beschränkt auf student-klasse-lehrgang (3 statt 7 Tabellen). Es fehlen: Krähenfuss-Vorgabe, information_schema-Vorlage, 3 Lesefragen, Hinweis «Reverse Engineer erst nach dem Zeichnen», A3, Galeriegang (Folie: zwei Paare am Beamer). Der Zusatz «wer schneller ist, ergänzt die Tabelle fach» ist fachlich unpassend: fach hat keine direkte Beziehung zu den drei Tabellen, nur über n:m-Tabellen (B10), die nicht eingeführt sind. «Beide Laptops offen» weicht von der Methodenlegende [PARTNER] «ein Laptop» ab. | Umfang entscheiden (Vorschlag: 3 Pflicht + standort/adresse als Erweiterung, wobei die fehlende FK klasse.standort ein guter Diskussionspunkt ist); Zusatz «fach» nur mit Hinweis «über fachplan»; fehlende Elemente aus dem Handoff ergänzen oder Handoff anpassen. |
| F23 | mittel | PP4 F9 | UNION ohne SQL-Beispiel; «UNION entfernt Duplikate, UNION ALL behält sie» steht nur in der Notiz. Für die UNION-Aufgabe in U2.3 fehlt eine Syntaxvorlage. Auf «beispiele» liefert die Kontaktliste mit UNION sichtbar weniger Zeilen als mit UNION ALL (B11): Stolperstein und zugleich gutes Lernbeispiel. | Kurzes Code-Beispiel (zwei SELECTs mit name, email) plus Zeile UNION vs. UNION ALL auf die Folie; Hinweise: Spaltennamen kommen aus dem ersten SELECT, ORDER BY steht am Schluss. |
| F24 | mittel | PP3 F8 Notiz, PP4 F1 Notiz, PP4 F4 Notiz; Unterrichtsplan 14:00-14:20 | Reihenfolge der Installation widersprüchlich: PP3 «nach dem PK/FK-Input», PP4 F1 «vorher eingerichtet», PP4 F4 «gerade installiert». Es gibt keine Folie mit Installationsschritten (Bezugsquelle, Workbench-Schritte, `USE beispiele`, Prüfabfrage). Risiko: Nach der U1-Demo existieren `student` und `fach` auch in `dbwe_demo`, Abfragen landen im falschen Schema. Installation bei allen TN im selben 20-min-Slot wie Teil A ist knapp. | Eine Reihenfolge festlegen; Setup-Folie mit Schritten und Prüfabfrage (Zeilenzahl student); Datei vorab im Kurskanal; Import ggf. schon im Check-in um 13:00 oder in der Mittagspause mit Helfer-Tandems. |
| F25 | mittel | alle Decks | Schriftgrössen für Beamer im Schulzimmer klein: Fliesstext 12-13.5 pt, Tabellen 11-12 pt, Rubriken 11 pt, Code 13-15 pt. Absätze unter 14 pt: PP1 56, PP2 46, PP3 38, PP4 68. Besonders die Tabellen in PP3 F5/F6 und PP4 F6-F8 müssen gelesen werden, um den Inhalt zu verstehen. | Fliesstext mindestens 18 pt, Tabellen und Code mindestens 16 pt; dafür Text kürzen oder Tabellen auf weniger Spalten reduzieren. |
| F25a | mittel | PP4 Teil B | Keine Folie zeigt einen JOIN über 3 Tabellen (Kette student-klasse-lehrgang) oder JOIN mit WHERE, obwohl U2.3 genau das als Aufgaben 2 und 4 verlangt; Tabellenaliase (s, k) werden ohne Erklärung verwendet. | Eine Folie «JOIN-Kette und Filter» mit «beispiele»-Spaltennamen und einem Satz zu Aliasen ergänzen. |
| F26 | mittel | PP2 F4, PP3, PP4 F2/F3/F6; Demo kap-3.sql; «beispiele» | Uneinheitliche Namen am selben Tag: student gibt es in vier Varianten (PP2: id, name, vorname, jahrgang; Demo: student_id, name, vorname, email; PP4 F6: id, name, klasse_id; «beispiele»: student_id, name, email, klasse, adresse). dozent: doz_id/name/mail vs. dozent_id/name/email; kurs: drei Varianten. PP2-Notiz F5 verweist auf ein «Jahrgang-Feld», das in der Demo fehlt. | Eine Konvention festlegen (Empfehlung: «beispiele»-Konvention B7) und über PP2-PP4 und Demo-Drehbuch durchziehen; PP2 F4 an die Demo-Tabelle angleichen. |
| F27 | mittel | PP1 F8; Unterrichtsplan Ablauf | «Setup-Sprechstunde: jeweils 30 Minuten vor Unterrichtsbeginn im Schulzimmer» ist eine Zusage für alle sechs Kurstage; die Tagesabläufe im Unterrichtsplan sehen sie nur an KT1 und KT4 vor. Raumzugang ab 07:30 ist nicht dokumentiert. | Zusage bestätigen (Raum, Dozierendenzeit) oder auf «an KT1 und KT4, sonst nach Absprache» einschränken. |
| F28 | tief | PP4 F8 | Notiz sagt «6 statt 3 Zeilen», Folie zeigt «2 × 2 = 4 Zeilen statt 2». `JOIN` ohne ON ist MySQL-spezifisch (in Standard-SQL und z. B. PostgreSQL ein Syntaxfehler; dort entsteht das kartesische Produkt meist über die Komma-Schreibweise). Die Workbench begrenzt Ergebnisse standardmässig auf 1000 Zeilen, auf «beispiele» ist der Effekt deshalb nur mit COUNT(*) sichtbar. | Notiz angleichen; Satz «in MySQL erlaubt, in anderen DBMS Fehler»; Demo-Tipp: `SELECT COUNT(*)` statt Ergebnisraster. |
| F29 | tief | PP4 F2 | «FOREIGN KEY verweist auf den Primärschlüssel einer anderen Tabelle»: «beispiele» enthält eine Selbstreferenz (B6). Dass eine FK-Spalte NULL sein darf (optionale Beziehung), wird nicht erwähnt, obwohl F7 darauf aufbaut. | «... auf den Primärschlüssel einer (meist anderen) Tabelle»; Zeile «FK darf NULL sein = Beziehung optional». |
| F30 | tief | PP2 F3/F7 | In MySQL und in der Workbench heissen Datenbanken «Schema» (Navigator «SCHEMAS»), und ein DBMS verwaltet mehrere Datenbanken (am KT1: dbwe_demo und beispiele). Fehlt; typische Verwirrung in der ersten Demo. | Eine Zeile auf F3 oder F7: «Ein DBMS, viele Datenbanken; in MySQL: Datenbank = Schema». |
| F31 | tief | PP2 F5 | «SQL ist standardisiert: einmal gelernt, bei fast jedem DBMS anwendbar» ohne Hinweis auf Dialekte. | «... mit Dialekt-Unterschieden (z. B. AUTO_INCREMENT, LIMIT)». |
| F32 | tief | PP2 F7 Notiz | Widersprüchliche Reihenfolge in der Notiz: erst «in der Live-Demo gleich», dann «danach folgt die Gruppenübung und nach der Pause die Demo». | Notiz an Ablauf anpassen (Fallarbeit, Pause, Demo). |
| F33 | tief | PP3 F8 | «Heute Nachmittag: JOIN», PP3 läuft bereits um 13:10. | «Nach der Pause: JOIN». |
| F34 | tief | PP1 F4, F6 | F4 lässt gegenüber Unterrichtsplan 1.2 «Funktionen» (KT2 VM) und «Module» (KT3 NM) weg; KT2 ohne PA-Kickoff und Indexierung. F6: Grammatik «im Einsatz an Kurstage 1-2». | Themen angleichen; «an den Kurstagen 1-2». |
| F35 | tief | PP4 F7 | Outline verlangt «Venn-artige Grafik»; die Folie zeigt einen Ergebnisvergleich als Tabellen. Didaktisch gleichwertig oder besser (Venn-Diagramme sind für JOINs oft irreführend). | Outline im Unterrichtsplan anpassen statt Grafik ergänzen. |
| F36 | tief | alle Decks | Alle Textläufe sind mit Sprache en-US ausgezeichnet (Rechtschreibprüfung markiert den deutschen Text, Screenreader lesen englisch). Metadaten: Titel «PptxGenJS Presentation», Autor «PptxGenJS». Decks nutzen eigene PptxGenJS-Layouts (TITLE/CONTENT mit Fusszeile und Bild), nicht nachweislich eine IFA-Schulvorlage. | Sprache de-CH setzen, Metadaten-Titel pro Deck; klären, ob die IFA-Vorlage Pflicht ist. |
| F37 | tief | PP2 F3, PP3 F4, PP3 F6, PP4 F7 | Layout-Indizien (Heuristik, visuell prüfen): PP3 F4 Pfeil überlappt die linke Tabelle um ca. 0,15 in; PP3 F6 Zeile «Verstoss: ...» (6,4 in breit, 13.5 pt) und PP4 F7 Zeile «Alle Zeilen der linken Tabelle ...» (12 pt) brechen vermutlich um und laufen an die Tabelle darunter; PP2 F3 DB-Kasten ragt ca. 0,05 in über den DBS-Rahmen. | In PowerPoint sichten, Textboxen verbreitern oder kürzen. |
| F38 | tief | PP3 F2/F4 | Nachname und Vorname stehen in einer Zelle, während F4 «atomare Werte» lehrt; «beispiele» macht es ebenso (B1). Erwartbare TN-Frage «Ist das atomar?». | Notiz ergänzen: «atomar relativ zum Verwendungszweck»; gute Diskussionsfrage für das Debriefing. |
| F39 | tief | Handoff (Querbezug) | Handoff WP 0: WP-Übersicht nennt 15 Materialien, spezifiziert sind 16; Setup-Sprechstunde nennt Türschild «ab 17:30» (Remote-Rest, Präsenz: 07:30); «Folien SQL laut Fachplan vorhanden» ist mit den neuen PP2-PP4 nicht abgeglichen. | Beim Handoff-Update bereinigen; klären, ob PP2-PP4 die Fachplan-Folien ersetzen oder ergänzen. |

### 5.1 Aussagen, die verbindlich klingen, deren Grundlage aber noch offen ist

| Fundstelle | Aussage (sinngemäss) | Grundlage | Empfehlung |
|---|---|---|---|
| PP1 F4, F5 | Abgabe 2 Wochen nach dem letzten Kurstag | nur Unterrichtsplan; offizielle Aufgabenstellung fehlt | «voraussichtlich» |
| PP1 F5 | PA umfasst Datenmodell, Flask-App, Login/Security, Deployment, kleine REST-API | Kursplanung; Deployment hängt an VM-Klärung (Checkliste) | «geplant, verbindlich ist die Aufgabenstellung» |
| PP1 F5 | Architekturdoku 3-5 Seiten, Schlusspräsentation max. 8 min | Unterrichtsplan; PP15-Outline: «nach Erhalt des Rasters abgleichen» | als Richtwert kennzeichnen |
| PP1 F5 | Aufgabenstellung und Bewertungsraster am Kurstag 2 | Raster liegt nicht vor, Lieferdatum unbekannt | nur bei gesicherter Lieferung zusagen |
| PP1 F2 Notiz | jede/r präsentiert am letzten Kurstag eine laufende App | KT6-Kapazität ca. 8 Präsentationen (F12) | Zeitplan prüfen |
| PP1 F6 Notiz | Skripte werden im Unterricht verteilt | widerspricht Leseauftrag vor KT1 (F06) | Verteilung vor KT1 |
| PP1 F6, F8 | Kurskanal Teams/Moodle | Plattform nicht entschieden | festlegen |
| PP1 F7 | ab KT2 Theorie vorbereitet, Unterricht nur Fragen/Übungen | Unterrichtsplan: Flipped erst ab WP 4 (F09) | angleichen |
| PP1 F8 | Setup-Sprechstunde an jedem Kurstag | Abläufe nennen nur KT1 und KT4 (F27) | bestätigen |

---

## 6 Abdeckung der Handoff-Materialien WP 0 (U1/U2) durch die Decks

PP2, PP3 und PP4 sind im Handoff nicht als eigene Materialien beauftragt (dort gelten «Folien SQL» als vorhanden); sie liefern die Inputs, auf die sich die Übungen stützen.

| Handoff-Material | Abdeckung durch PP1-PP4 | Status |
|---|---|---|
| Vorbereitungs-Mail + Installationsanleitung | keine (PP1 F8 nennt nur die Setup-Sprechstunde) | fehlt |
| Setup-Sprechstunde U1 (Triage-Leitfaden) | keine (PP1 F8 kündigt sie an) | fehlt |
| Kickoff-Folien U1 | PP1 | weitgehend abgedeckt (Korrekturen F05-F12) |
| Check U1: Setup- und Vorwissens-Check | PP1 F9 leitet über, Vorstellungsrunde erhebt DB/Web-Erfahrung mündlich; keine Particify-Folie, keine Fragen | fehlt |
| Gruppenübung U1.1 «Relationales Modell, passt es?» | Input PP2 F3, F5, F6; Ankündigung ein Satz PP2 F7; keine Auftragsfolie, keine Szenarien, kein Debriefing | teilweise (Input) |
| Live-Demo-Drehbuch U1 | Teaser PP2 F7 (6 Anweisungen) | fehlt |
| Partnerübung U1.2 SQL-Grundoperationen | keine | fehlt |
| Quiz U1 | keine | fehlt |
| Selbststudiumsauftrag U1 | PP1 F7 nur allgemeiner Wochenrhythmus | fehlt |
| Quiz U2 Check-in | keine | fehlt |
| Partnerübung U2.1 Normalisieren bis 3NF | Input PP3; Kurzhinweis PP3 F8; Konflikte F18, F19 | teilweise (Input) |
| Partnerübung U2.2 ERD aus «beispiele» | Input PP4 F2-F4; Auftragsfolie PP4 F5 (reduzierter Umfang, F22) | teilweise (Auftragsfolie vorhanden) |
| Partnerübung U2.3 JOIN und UNION | Input PP4 F6-F9 (Mängel F02, F03, F23, F25a); ein Satz auf PP4 F9 | teilweise (Input) |
| Quiz U2 Schlüssel, JOIN, UNION | keine | fehlt |
| Zusatzauftrag U2 (eigenes Mini-Datenmodell) | keine | fehlt |
| Selbststudiumsauftrag U2 | keine | fehlt |

Fazit: 1 von 16 Handoff-Materialien ist durch die Decks weitgehend abgedeckt (Kickoff), 4 teilweise (U1.1, U2.1, U2.2, U2.3, jeweils nur Input bzw. eine Auftragsfolie), 11 fehlen vollständig.

---

## 7 Was für KT1 an Folien noch fehlt oder korrigiert werden muss

### 7.1 Vor dem Einsatz korrigieren (Pflicht)

1. PP4 F2: Komma im CREATE-TABLE-Beispiel ergänzen, kurs-Definition F2/F3 angleichen, Code in MySQL 8 testen (F01).
2. PP4 F6-F8: Spaltennamen und Beispielwerte auf «beispiele»-Konvention umstellen oder klar als Mini-Beispiel kennzeichnen (F02).
3. PP4 F7: LEFT-JOIN-Szenario für die Demo auf ein Tabellenpaar mit partnerlosen Datensätzen umstellen; Handoff U2.3 anpassen (F03).
4. PP3 F1 Notiz: Annahme «aus dem Selbststudium bekannt» streichen, Input als Erst-Einführung planen (F04).
5. PP1 F5 (und F4): PA-Angaben als vorläufig kennzeichnen, «Raster am KT2» entschärfen (F05).
6. PP1 F6: Lehrmittel-Verteilung vor KT1 klären, Notiz angleichen, Kurskanal festlegen (F06). Termin: Vorbereitungs-Mail bis 16.10.2026.
7. PP1 F7: «8 Lektionen» auf 10 korrigieren; Beginn «Theorie vorbereitet» mit Unterrichtsplan abstimmen (F07, F09).
8. PP1: Zeitbudget Kickoff plus Vorstellungsrunde auf 25 min bringen (F08).
9. PP1 F3: PA als parallelen Balken darstellen (F11); PP1 F8 Laptop-Regel vereinheitlichen (F10).
10. PP2 F6: Grenzen abstrahieren oder erst im Debriefing zeigen (F13); PP2 F2 Formulierung (F14).
11. PP3 F2-F7: Beispiel durchgehend konsistent machen, Merksatz «Nicht-Schlüssel-Attribut», funktionale Abhängigkeit einführen (F15-F17).
12. PP4 F3: Krähenfuss mit Legende, Min-Kardinalität und n:m-Beispiel (F20).
13. PP4 F4: 14 Tabellen korrekt gruppieren, Einzeltabellen und fehlende Constraints benennen (F21).
14. PP4 F9: UNION-Syntax und UNION ALL auf die Folie (F23).
15. PP4 F8 Notiz: Zeilenzahlen angleichen (F28).
16. Alle Decks: Schriftgrössen anheben (F25); Sprache de-CH (F36); Layout-Indizien sichten (F37).
17. Namenskonvention über PP2-PP4 und Demo vereinheitlichen (F26).

### 7.2 Fehlende Folien (neu erstellen)

| Nr | Zeitpunkt KT1 | Folie | Bezug |
|---|---|---|---|
| N1 | 08:25 | Particify-Folie mit QR-Code: Setup-Check (Handzeichen-Fragen) und Vorwissens-Abfrage | Handoff «Check U1», Checkliste «QR-Code auf die erste Folie» |
| N2 | 08:55 | Auftragsfolie U1.1 Fallarbeit (Ziel, 25 min, 3er-Gruppen, A3/Flipchart, 2 Argumente pro Szenario, DBS/DB/DBMS-Zuordnung in (a), Galeriegang) | Handoff U1.1 |
| N3 | 09:35 | optional: Demo-Begleitfolie (Workbench-Orientierung, Stopp-Marken, Safe-Update-Hinweis, «Skript liegt im Kurskanal») | Handoff Demo-Drehbuch U1 |
| N4 | 10:00 | Auftragsfolie U1.2 SQL-Grundoperationen (30 + 30 min, Paare, Driver/Navigator-Wechsel nach jeder zweiten Aufgabe, Startskript, Output) | Handoff U1.2 |
| N5 | 11:15 | Particify-Folie Quiz U1 | Handoff Quiz U1 |
| N6 | 11:30 | Ausblick/Selbststudiumsauftrag U1 | Handoff Selbststudium U1 (Inhalt an den Ein-Tages-Ablauf anpassen, F04) |
| N7 | 13:00 | Particify-Folie Check-in-Quiz U2 | Handoff Quiz U2 Check-in |
| N8 | 13:30 | Auftragsfolie U2.1 Normalisierung (neues Szenario, 30 min, Paare, A3, Output, Rollenwechsel) | Handoff U2.1, F18 |
| N9 | 14:00 | Setup-Folie «beispiele» installieren (Bezugsquelle, Workbench-Schritte, `USE beispiele`, Prüfabfrage) | F24 |
| N10 | 14:35 | Auftragsfolie U2.2 ergänzen: Krähenfuss-Vorgabe, Lesefragen, information_schema-Vorlage, Reverse Engineer erst danach | Handoff U2.2, F22 |
| N11 | 15:00 | Folie «JOIN-Kette über 3 Tabellen und JOIN mit WHERE» mit «beispiele»-Namen | Handoff U2.3, F25a |
| N12 | 15:20 | Auftragsfolie U2.3 JOIN/UNION (30 min, Paare, erwartete Zeilenzahlen zur Selbstkontrolle, Output) | Handoff U2.3 |
| N13 | 16:05 | Besprechungsfolie «typische Fehler» (kann PP4 F8 wiederverwenden; ergänzen: falsches Schema aktiv, LEFT JOIN mit WHERE auf die rechte Tabelle) | Unterrichtsplan 16:05 |
| N14 | 16:30 | Particify-Folie Quiz U2 | Handoff Quiz U2 |
| N15 | 16:45 | Zusatzauftrag für Schnelle (PA-Brücke) und Selbststudiumsauftrag U2, Tagesabschluss | Handoff Zusatzauftrag U2, Selbststudium U2 |

### 7.3 Entscheide, die vor der Überarbeitung nötig sind

1. Offizielle PA-Aufgabenstellung und Raster: Lieferdatum klären; bis dahin alle PA-Zahlen als vorläufig führen (F05, F12).
2. Lehrmittel-Verteilung und Leseauftrag vor KT1; Kurskanal Teams oder Moodle (F06).
3. Laptop-Regel bei Inputs (F10) und Startpunkt «Theorie vorbereitet» (F09).
4. U2.1: Szenario und SQL-Schritt (F18, F19).
5. U2.2: Umfang 3 oder 7 Tabellen, Zusatzaufgabe (F22).
6. LEFT-JOIN-Szenario für Demo und U2.3 (F03).
7. Namenskonvention für alle Mini-Beispiele (F26).
8. Schulvorlage und Verhältnis zu den Fachplan-Folien «Folien SQL» (F36, F39).
