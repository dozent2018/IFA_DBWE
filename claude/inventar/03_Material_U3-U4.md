# Inventar 03: Material Unit 3 und Unit 4 (Drive, WP 1)

Kurs DBWE.TA1A «Datenbanken und Web-Entwicklung», Kurstag 2 (Fr, 06.11.2026): Vormittag Unit 3 (SQL-Abschluss, Views, DBMS-Architektur, Indexierung), Nachmittag Unit 4 (Start Python).
Geprüfte Fassung: WP-1-Materialien im Drive, Stand 10.09.2026 (erstellt 10.09.2026, seither unverändert).
Erstellt am 29.09.2026 als Teil des Rework-Inventars. Keine Änderungen an den Drive-Dateien vorgenommen.

Schweregrade: **hoch** = falsch oder blockiert Unterricht; **mittel** = verwirrt TN oder erzeugt Nacharbeit; **tief** = Kosmetik.

Hinweis öffentliches Repo: Kontrollwerte, Quiz-Lösungen und Lösungscode werden hier nicht wiedergegeben, nur beschrieben.

---

## 1 Gelesener Umfang und Ausführung

### 1.1 Quellen

| Quelle | Umfang | Methode |
|---|---|---|
| KI-Handoff v2.0 (02.09.2026), lokale Kopie | Zeilen 1 bis 110 (Rahmen, Mapping, Repo-Material, Qualitätskriterien) und 254 bis 372 (WP 1 Kontext, alle Spezifikationen Unit 3 und Unit 4) vollständig; zusätzlich gezielt Zeilen 200 bis 250 (Namen der WP-0-Materialien, Selbststudium U2) für Querverweise | Read, grep |
| WP1_Uebersicht_Units_3-5.md (Drive) | vollständig | read_file_content |
| Unterrichtsplan_DBWE_TA1A_S2610.md (Drive, 18.09.2026) | vollständig; Schwerpunkt Abschnitt 1 (Prinzipien, Methoden-Legende) und 3 (WP 2 / KT2 mit Ablauf Vormittag U3, Nachmittag U4, PP-Outlines PP5 bis PP7) | read_file_content |
| 11 Markdown-Materialien Unit 3, Unit 4, 04_Selbststudium | jede Datei vollständig (Grössen siehe 2.1) | read_file_content (Text mit Backslash-Escapes); keine Rohkopie abgelegt |
| 8 Code-Dateien Unit_3/code und Unit_4/code | byte-genau: base64 heruntergeladen, dekodiert, Grösse mit Drive-Angabe verglichen (alle 8 identisch) | download_file_content; Kopien in `scratchpad/drive/Unit_3/code/` und `scratchpad/drive/Unit_4/code/` |
| Drive-Ordner Unit_3, Unit_4 | Ordnerinhalt gelistet: nur die 9 Markdown-Dateien plus je ein code-Ordner; Suche nach PP5, PP6, PP7: keine pptx vorhanden (im Drive nur PP1 bis PP4 vom 18.09.2026) | search_files |
| SQL/create_beispiele.sql | alle 14 CREATE-TABLE-Blöcke mit Keys und Constraints gelesen; Daten maschinell in eine SQLite-Prüfdatenbank geladen (Zeilenzahlen aller 14 Tabellen = Dump) | Read, Python |
| SQL/kap-5.sql, kap-6.sql, kap-7.sql, kap-10.sql | vollständig | Read |
| Python/kap-1 bis kap-12 | Ordnerlisten vollständig; gelesen: kap-5/mittelwert.py, kap-6/beitrag.py, eintritt3c.py, kap-7/papagei.py, break_demo.py, count.py, countdown.py, kap-8/sekunden.py, timer.py, what_time.py, kap-12/div_null.py; grep über alle .py nach random, raten, rabatt, spesen, fizz, jass, staffel | Read, grep |

### 1.2 Was ausgeführt wurde

- **Python:** alle 4 Musterlösungen U4.1 mit Python 3.11.15, 3.12.3 und 3.13.12 ausgeführt, Eingaben per stdin; Zahlenraten zusätzlich mit gesetztem Zufalls-Seed (Wrapper), damit Treffer- und Verlustfälle reproduzierbar sind. Alle Codebeispiele aus Live-Coding-Drehbuch U4, Setup-Check U4 und die Code-Fragen aus Quiz U4 nachgestellt (REPL-Verhalten mit `python3 -i`). Protokoll in Abschnitt 6.
- **SQL:** keine Ausführung auf MySQL (Aufgabe eines anderen Agents). Statische Prüfung gegen das Schema; zusätzlich SQLite-Probe von `loesung_u3_1.sql` (alle 8 Abfragen, `YEAR()` durch `strftime` ersetzt) und der Blöcke 1 bis 5 von `demo_u3_views.sql`; MySQL-Rundung von `ROUND(AVG(DECIMAL))` mit Python-Decimal nachgerechnet; Datengenerierung von `index_demo_setup.sql` in Python nachgerechnet.

---

## 2 Inventar

### 2.1 Materialdateien

| Datei | Typ | Umfang | Einsatz laut Material | Einsatz laut Plan S2610 | Kurzinhalt |
|---|---|---|---|---|---|
| Unit_3/Quiz_U3_3NF-JOIN-Check.md | Quiz (Particify, Ausfall: Kartenabfrage) | 6'103 B; 6 Fragen à 4 Optionen, Lösungstabelle mit Distraktor-Analyse, Steuerungsregeln | U3 Einstieg, 10 min, Plenum | KT2 08:00-08:10 [QUIZ] | 2 Fragen 3NF (1 erkennen, 1 beheben), 2 JOIN (Typ, Syntax), 1 FK, 1 UNION vs. JOIN |
| Unit_3/Partneruebung_U3.1_GROUP-BY.md | Übungsblatt mit Auftragsfolie und Dozententeil | 7'513 B; 6 Aufgaben (Aufgabe 5 zweiteilig) + Zusatzaufgabe, Schema-Ausschnitt, Zeitgerüst, Zirkulier-Hinweise, Debriefing 10 min | U3, 30 min + 10 min Debriefing, Partner (Pair Programming, Rollenwechsel nach Aufgabe 3) | KT2 08:50-09:20 [PARTNER] | Aggregate, GROUP BY ein- und zweispaltig, HAVING, JOIN über bis zu 5 Tabellen, LIMIT auf «beispiele» |
| Unit_3/Demo-Drehbuch_U3_Views-Introspektion.md | Demo-Drehbuch (Min, SQL, Sprechnotiz) | 6'269 B; 12 Zeitschritte (0 bis 15 min), 3 Stopp-Marken, 3 typische TN-Fragen | U3, 15 min, Plenum, Mittippen freiwillig | KT2 09:35-09:50 [DEMO] | View anlegen, INSERT in Basistabelle, View auf View mit LEFT JOIN und Aggregat, information_schema (tables, views, key_column_usage) |
| Unit_3/Gruppenuebung_U3.2_Systemarchitektur.md | Fallstudie (Auftragsfolie, Teil A Handout, Teil B Debriefing) | 10'404 B; Fall «Alpsicht AG» mit 7 Qualitätsanforderungen, 3 Leitfragen, Lösungskorridore, 4 Bewertungsanker | U3, 30 min + 15 min Debriefing (Galeriegang, Klebepunkte, Synthese), Gruppen à 3, Flipchart | KT2 09:50-10:20 [GRUPPE] + Galeriegang | Webshop-Architektur aus Anforderungen ableiten, Caching-Punkte markieren, Zielkonflikte benennen |
| Unit_3/Kurzfolien_U3_Indexierung-Caching.md | Folien-Outline (Markdown) mit Sprechernotizen | 9'044 B; 10 Folien (davon 4 mit Live-Demo), 1 optionale Kontrollfrage | U3, 20 min, Plenum | KT2 10:35-10:55 **[PP 5]** + [DEMO] | Full Table Scan, B-Tree, CREATE INDEX, EXPLAIN, Selektivität, Schreibkosten, Caching-Ebenen, Merksätze |
| Unit_4/Check_U4_Setup-Check.md | Handzeichen-Abfrage + Triage-Leitfaden | 9'464 B; 4 Handzeichen-Fragen, Aufwärmaufgabe (5 REPL-Zeilen), 6 Triage-Fälle (4 Windows, 2 macOS), Schnelldiagnose, Ausweichlösung | U4 Einstieg, 10 min, Plenum, danach Triage am Platz | KT2 13:00-13:10 | Setup-Status sichtbar machen, Tandem-Regel, Fixes unter 5 min |
| Unit_4/Live-Coding-Drehbuch_U4.md | Demo-Drehbuch (Code, Sprechnotiz) | 10'873 B; 4 Blöcke à ca. 5 min, 7 Stopp-Marken, Notfallplan (5 Fälle) | U4, 20 min, Plenum, alle tippen mit | KT2 13:30-13:50 [DEMO] | REPL, Ausdruck vs. Anweisung, Typen, `is` vs. `==`, Referenz auf Liste, erste Datei mit MwSt-Rechnung und f-String |
| Unit_4/Partneruebung_U4.1_Kontrollstrukturen.md | Übungsblatt mit Auftragsfolie und Dozententeil | 9'813 B; Ctrl-C-Vorübung, 4 Aufgaben (A bis D) + mündlicher Zusatz, Zeitplan, Zirkulier-Hinweise, Debriefing 10 min | U4, 30 min + 10 min Debriefing, Partner, Rollenwechsel nach jeder Aufgabe | KT2 14:55-15:30 [PARTNER] (35 min) | Preisstaffel (if/elif), Spesen-Eingabeschleife, Zahlenraten, Jass-Zähler (FizzBuzz-Variante) |
| Unit_4/Quiz_U4_Python-Grundlagen.md | Quiz (Particify) | 7'264 B; 8 Fragen, Lösungstabelle mit Fehlkonzepten, Besprechungsdramaturgie, Auswertung | U4 Sicherung, 15 min | KT2 16:30-16:45 [QUIZ] | Code-Ausgabe, Referenzsemantik, `is`, elif-Kette, Einsatzgebiet, Stdlib-Wahl |
| 04_Selbststudium/Selbststudium_U3_Eigenes-Datenmodell.md | Selbststudiumsauftrag | 10'364 B; 2 Szenarien + eigenes, Zeitplan (6 Schritte), Selbstcheck in 3 Teilen, Abgabeformat, Dozentenhinweise | nach U3, 90 min, Einzelarbeit, Abgabe vor U5 | KT2 11:25-11:45 Ausblick | ERD + CREATE-Skript in 3NF (min. 4 Tabellen) als PA-Grundlage |
| 04_Selbststudium/Selbststudium_U4_PYGR_Kap1-5.md | Selbststudiumsauftrag | 6'611 B; 3 Schritte, 3 × 30 min, Stolperstein-Format, Selbstcheck (5 Punkte), Dozentenhinweise | nach U4, 90 min, Einzelarbeit, Post vor U5 | KT2 16:45-17:00 Ausblick | PYGR Kap. 1 bis 5 lösen, mit Repo vergleichen, 3 Stolpersteine posten |

### 2.2 Code-Dateien

| Datei | Bytes (Drive = lokal) | Zeilen | Inhalt | Zugehörig |
|---|---|---|---|---|
| Unit_3/code/loesung_u3_1.sql | 4'849 | 115 | 8 Abfragen (Aufgaben 1 bis 6 mit 5a/5b + Zusatz), Kontrollwerte als Kommentar, Hinweis «SQLite-ermittelt» | Partnerübung U3.1 |
| Unit_3/code/demo_u3_views.sql | 2'448 | 60 | 7 Blöcke: Abfrage, 2 Views, INSERT/DELETE einer Testklasse, 3 information_schema-Abfragen | Demo-Drehbuch U3 |
| Unit_3/code/index_demo_setup.sql | 1'935 | 51 | legt DB `index_demo` an, Tabelle `zugriffslog` mit 100'000 Zeilen per rekursivem CTE, leere Kopie `zugriffslog_import` | Kurzfolien U3 |
| Unit_3/code/index_demo_ablauf.sql | 4'851 | 103 | 7 Demo-Blöcke: Scan, EXPLAIN, Index, Vergleich, Selektivität, Schreiblast, Buffer Pool | Kurzfolien U3 |
| Unit_4/code/loesung_u4_1a_preisstaffel.py | 1'690 | 51 (ca. 20 Codezeilen) | Musterlösung A + Dozentenhinweise | U4.1 |
| Unit_4/code/loesung_u4_1b_spesen.py | 1'898 | 55 (ca. 20) | Musterlösung B + Hinweise | U4.1 |
| Unit_4/code/loesung_u4_1c_zahlenraten.py | 2'073 | 61 (ca. 20) | Musterlösung C + Hinweise | U4.1 |
| Unit_4/code/loesung_u4_1d_jasszaehler.py | 1'865 | 52 (ca. 11) | Musterlösung D + Hinweise | U4.1 |

### 2.3 Im Unterrichtsplan KT2 vorgesehen, aber ohne Material

| Plan-Slot | Inhalt laut Plan | Minuten | Stand |
|---|---|---|---|
| 08:10-08:30 | Besprechung Selbststudium, Fragen aus Kurskanal | 20 | kein Material nötig |
| 08:30-08:50 | Input + Demo Aggregatfunktionen, GROUP BY, HAVING (Repo `kap-5.sql` als Referenz) | 20 | kein Drehbuch |
| (nicht im Plan) | Input DBMS-Architektur (Handoff-Ablauf, LZ 3); Drehbuch U3 endet mit «Übergang zum Input DBMS-Architektur», U3.2 nennt «Folien SQL (DBMS-Architektur)» als Hilfsmittel | 0 | weder Slot noch Material |
| 10:55-11:25 | [PP 6] Einführung Praxisarbeit + Einzelarbeit Datenmodell-Idee | 30 | keine Folien; offizielle PA-Unterlagen fehlen |
| 11:25-11:45 | Kurz-Quiz + Ausblick | ca. 10 | kein Quiz (Ausblick: Selbststudium U3 vorhanden) |
| 13:10-13:30 | [PP 7] Warum Python? | 20 | keine Folien |
| 13:50-14:20 | Mini-Aufgaben Variablen und Ausdrücke (z. B. Rechnungen mit MwSt.) [PARTNER] | 30 | kein Material; auch im Handoff nicht als Material beauftragt (dort nur «Kurzaufgaben» im Ablauf) |
| 14:35-14:55 | Demo Kontrollstrukturen if/elif/else, while; erstes Skript in VS Code | 20 | kein Drehbuch |
| 15:45-16:05 | Input + Demo eingebaute Funktionen, Standardbibliothek, Ausblick list | 20 | kein Material |
| 16:05-16:30 | Kombinierte Aufgabe: kleines input()-getriebenes Programm [PARTNER] | 25 | kein Material |

Summe ohne Material: Vormittag ca. 60 min (plus fehlender DBMS-Input), Nachmittag 115 von 225 Unterrichtsminuten.

---

## 3 Konformität

### 3.1 Pflichtbestandteile laut globalen Qualitätskriterien

Legende: ja / teilw. / nein / n. a. (nicht anwendbar)

| Material | Aufgabenstellung | Zeitbudget | Sozialform | Erwartetes Ergebnis | Musterlösung / Bewertungshinweise | Projizierbare Auftragsfolie | Zirkulier-Hinweise | K-Stufe passend | Handout TN getrennt |
|---|---|---|---|---|---|---|---|---|---|
| Quiz U3 | ja | ja | ja | n. a. (Steuerungsregeln ja) | ja | n. a. (QR-Folie erwähnt, nicht erstellt) | n. a. | ja (K2/K3) | n. a. |
| Partnerübung U3.1 | ja | teilw. (Minutenplan 25 min, Richtzeiten 30 min) | ja | ja (.sql mit Zeilenzahl-Kommentaren) | ja (nur gegen SQLite geprüft) | ja | teilw. (ONLY_FULL_GROUP_BY genannt, nicht erklärt) | ja (K3) | nein (Dozententeil im selben Dokument) |
| Demo-Drehbuch U3 | ja | ja | ja | ja (Output je Schritt) | ja (Sprechnotizen) | n. a. | n. a. | teilw. (LZ 2 ist K3, TN wenden Views nicht selber an) | n. a. |
| Gruppenübung U3.2 | ja | teilw. (30 + 15 min, Plan 30) | ja | ja | ja (Korridore, Bewertungsanker) | ja | nein (kein eigener Abschnitt; Nachfragen in Teil B nutzbar) | ja (K4) | ja (Teil A / Teil B) |
| Kurzfolien U3 | n. a. | ja | ja | n. a. | ja (Sprechernotizen) | n. a. | n. a. | teilw. (LZ 5 ist K3, nur Dozentendemo) | n. a. |
| Selbststudium U3 | ja | ja | ja | ja | ja (Selbstcheck, Dozentenhinweise) | n. a. | n. a. | ja (K4) | nein (Dozentenhinweise im TN-Dokument) |
| Check U4 | ja | ja | ja | ja (Frage 4 als Kriterium) | ja (Triage) | n. a. | ja (Triage am Platz) | ja | n. a. |
| Live-Coding U4 | ja | ja | ja | ja | ja | n. a. | ja (Notfallplan) | ja (K3/K2) | n. a. |
| Partnerübung U4.1 | ja | teilw. (30 + 10 min, Plan 35) | ja | ja | ja (4 .py, ausgeführt) | ja | ja | ja (K3) | nein (Dozententeil im selben Dokument) |
| Quiz U4 | ja | ja | ja | n. a. | ja | n. a. | n. a. | ja | n. a. |
| Selbststudium U4 | ja | ja | ja | ja | teilw. (Repo-Lösungen nur für Kap. 1 und 5 vorhanden) | n. a. | n. a. | teilw. (Kap. 1 bis 5 liegen unter dem Stoffstand von U4) | nein (Dozentenhinweise im TN-Dokument) |

### 3.2 Handoff-Vorgaben je Material

**Quiz U3: 3NF- und JOIN-Check**

| Vorgabe | Status | Begründung |
|---|---|---|
| 6 MC-Fragen | erfüllt | 6 Fragen |
| 2 × 3NF-Verstoss erkennen an Mini-Tabellen | teilweise | Frage 1 erkennen; Frage 2 gibt den Verstoss vor und fragt nach der Behebung |
| 2 × JOIN-Syntax / JOIN-Typ | teilweise | Fragen 3 und 4 vorhanden, Frage 4 fachlich fehlerhaft für MySQL (U3-F01) |
| 1 × Fremdschlüssel, 1 × UNION vs. JOIN | erfüllt | Fragen 5 und 6 |
| 4 Optionen, genau eine richtig | nein | Frage 4 hat in MySQL zwei korrekte Optionen |
| Format Markdown-Tabelle + Particify-Importformat | teilweise | Tabelle bewusst durch Einzelfragen ersetzt (Annahme 1, vertretbar); kein Importformat, nur Copy-Paste-Text |
| In 10 min durchführbar | erfüllt | 6 × (45 s + 30 s) = 7.5 min |
| Distraktoren spiegeln Anfängerfehler | überwiegend | gut begründet; einzelne schwach (1 C, 6 C/D) |

**Partnerübung U3.1: GROUP BY auf «beispiele»**

| Vorgabe | Status | Begründung |
|---|---|---|
| 6 Aufgaben steigend | erfüllt | 6 + Zusatz, Schwierigkeit markiert |
| Tabellen student, klasse, lehrgang, pruefung, fach, raum, standort | teilweise | lehrgang und raum ungenutzt; lehrveranstaltung zusätzlich (fehlt im Schema-Ausschnitt) |
| COUNT/SUM/AVG | teilweise | SUM kommt nicht vor |
| GROUP BY ein- und zweispaltig, HAVING, Kombination mit JOIN | erfüllt | Aufgaben 2 bis 6 |
| Beispiele: Notenschnitt pro Klasse und Fach, Raumkapazität pro Standort, Klassen > n | teilweise | Schnitt je Fach, je Klasse, je Standort und Fach (Zusatz); Raumkapazität fehlt; Klassen ab n vorhanden |
| Nicht übereinstimmend mit DBSQL Kap. 5 | formal erfüllt, inhaltlich nah | siehe Abschnitt 7 und U3-F17 |
| Erwartete Zeilenzahl oder Kontrollwert pro Aufgabe | teilweise | nur in der Musterlösung, nicht auf dem TN-Blatt |
| Zirkulier-Hinweis ONLY_FULL_GROUP_BY mit Erklärung | teilweise | Fehler 1055 genannt, Erklärung nicht ausformuliert (U3-F09) |
| Auftragsfolie, Musterlösung als SQL gegen Dump getestet | teilweise | Folie und SQL vorhanden; Test nur gegen SQLite-Port (beispiele.sqlite fehlt im Drive); meine SQLite-Probe bestätigt die Kommentare |
| Abnahme: 1 bis 3 von allen, 5 bis 6 für Starke | erfüllt | Zeitgerüst im Dozententeil |
| Abnahme: Musterlösungen laufen auf create_beispiele.sql | statisch erfüllt | Namen, FK-Pfade, ONLY_FULL_GROUP_BY korrekt; MySQL-Lauf ausstehend |

**Demo-Drehbuch U3: Views und Schema-Introspektion**

| Vorgabe | Status | Begründung |
|---|---|---|
| Basis kap-7.sql (v_standorte, v_klassen) und kap-10.sql | teilweise | eigene Views (v_klassenliste, v_klassengroesse) statt der Lehrmittel-Views; kap-10 in reduzierter Form |
| View anlegen, abfragen | erfüllt | Minuten 2 bis 3 |
| Unterschied zu Tabelle (INSERT in Basistabelle, View aktualisiert sich) | erfüllt | Minute 5 |
| View auf Aggregation | erfüllt | Minuten 7 bis 8 |
| information_schema als Selbstbeschreibung, Brücke zu DBMS-Architektur | erfüllt im Material | Brücke zeigt auf einen Input, den der Plan nicht enthält (KT2-F03) |
| Zweispaltig SQL / Sprechnotiz, plus .sql | erfüllt | dreispaltig mit Minute; .sql vorhanden |
| Abnahme: läuft auf create_beispiele.sql | statisch erfüllt | DELETE scheitert mit Workbench-Standard «Safe Updates» (U3-F26) |
| Abnahme: jede Minute sichtbarer Output | weitgehend | Minute 10 Whiteboard statt SQL |

**Gruppenübung U3.2: Qualitätsanforderungen → Systemarchitektur**

| Vorgabe | Status | Begründung |
|---|---|---|
| KMU-Webshop, 1 Seite Handout | teilweise | Fall stimmig, Teil A aber deutlich länger als 1 Seite |
| Nutzerzahlen, Verfügbarkeit, Performance, Sicherheit, Wartbarkeit | erfüllt | Q1 bis Q7 mit Zahlen, zusätzlich Integrität und Nachvollziehbarkeit |
| Architektur ableiten (Schichten, DB-Anbindung, Caching-Punkte), Flipchart | erfüllt | Mindestbestandteile vorgegeben |
| 3 Leitfragen | erfüllt | L1 bis L3, jeweils Zielkonflikt |
| Galeriegang mit Klebepunkten «beste Begründung», Plenum | erfüllt | Teil B |
| Debriefing-Hinweise mit Lösungsvarianten | erfüllt | Korridore je Leitfrage |
| Abnahme: Anforderungen konkret genug; keine Musterlösung, klare Bewertungsanker | erfüllt | 4 Anker A bis D |
| Lernziel LZ 3 (K2 DBMS-Schichtenarchitektur) | kaum | Fall behandelt Anwendungsarchitektur, nicht die Schichten eines DBMS |

**Kurzfolien U3: Indexierung und Caching**

| Vorgabe | Status | Begründung |
|---|---|---|
| 8 bis 10 Folien | erfüllt | 10 |
| Warum Indexe, B-Tree mit Grafik-Beschreibung, CREATE INDEX, EXPLAIN, Schaden, Caching-Ebenen | erfüllt | B-Tree-Erklärung fachlich unscharf (U3-F05) |
| Live-Demo EXPLAIN vorher/nachher auf 100k-Tabelle inkl. Testdaten-Skript in DB «beispiele» (z. B. messung) | teilweise | Skript vorhanden, aber eigene DB `index_demo` mit Tabelle `zugriffslog` |
| Folien-Outline Markdown mit Sprechernotizen | erfüllt | Plan verlangt aber [PP 5] als PowerPoint (U3-F06) |
| Abnahme: lauffähig auf MySQL 8 | offen | nie ausgeführt; statisch plausibel |
| Abnahme: messbarer Laufzeitunterschied | offen | nicht gemessen (WP1 Annahme 3); Block 5 und Buffer-Pool-Aussage fraglich (U3-F03, U3-F04) |

**Selbststudium U3: Eigenes Datenmodell**

| Vorgabe | Status | Begründung |
|---|---|---|
| Eigenes oder 2 vorgegebene Szenarien | erfüllt | A Velowerkstatt, B Kursverwaltung |
| ERD (draw.io oder Foto) + CREATE in 3NF, min. 4 Tabellen | erfüllt | inkl. Qualitätsregeln für Fotos |
| Abgabe Kurskanal, Selbstcheck (3NF, FK, Namenskonventionen) | erfüllt | 3-teiliger Selbstcheck |
| Hinweis Peer-Review Unit 5, mitbringen | erfüllt | mehrfach |
| Abnahme: in 90 min machbar | erfüllt für A/B | eigenes Szenario ehrlich mit ca. 120 min ausgewiesen |
| Abnahme: PA-tauglich | erfüllt, vorbehaltlich | offizielle PA-Vorgaben fehlen |
| Fachliche Stimmigkeit | teilweise | Historisierungsanforderung fehlt in Szenario B (U3-F15) |

**Check U4: Setup-Check**

| Vorgabe | Status | Begründung |
|---|---|---|
| 4 Handzeichen-Fragen (installiert, REPL, VS Code + Extension, erste Zeile) | erfüllt | |
| Triage Windows (PATH, Store-Python, Execution Policy), macOS (python vs. python3) | erfüllt | plus VS-Code-Interpreter und pip-Fall; Lücke macOS-Systempython 3.9 (U4-F04) |
| Tandem-Regel, Dozent behebt während der Partnerübung | erfüllt im Material | Bezug auf U4.1 passt nicht zum Plan (U4-F03) |
| Abnahme: Hilfe am Platz unter 5 min pro Fall | erfüllt | Zeitangaben je Fall, Abbruchregel |

**Live-Coding-Drehbuch U4**

| Vorgabe | Status | Begründung |
|---|---|---|
| REPL öffnen, Ausdrücke vs. Anweisungen, Typen, erste Datei in VS Code | erfüllt | Blöcke 1 bis 4 |
| Variablen und Objekte mit id()-Demo | teilweise | Identität nur über `is`, kein `id()` |
| Pro Schritt: tippen, sagen, typische TN-Frage, Stopp-Marke | teilweise | TN-Fragen je Block, nicht je Schritt; Stopp-Marken vorhanden |
| Zweispaltig, 20 min, jede Minute sichtbarer Output | erfüllt | alle Ausgaben nachgeprüft (P16, P17) |

**Partnerübung U4.1: Kontrollstrukturen**

| Vorgabe | Status | Begründung |
|---|---|---|
| 4 Mini-Programme steigend, Stil kap-6/kap-7, 15 bis 35 Zeilen, input()-getrieben | teilweise | A bis C erfüllt; D ohne input() und kürzer |
| Neue Szenarien (nicht Eintritt, Sozialversicherung, Zinseszins) | erfüllt | Preisstaffel, Spesen, Zahlenraten, Jass |
| Rollenwechsel nach jeder Aufgabe | erfüllt | |
| Zirkulier-Hinweise Einrückung, = vs. ==, Endlosschleife | erfüllt | plus Tandem, Rollen |
| Auftragsfolie, Musterlösungen als Python | erfüllt | 4 Dateien, alle lauffähig |
| Abnahme: nur Stoff PYGR Kap. 1 bis 8, keine Listen/Funktionen | erfüllt | random aus Kap. 8, Snippet im Blatt |

**Quiz U4: Python-Grundlagen**

| Vorgabe | Status | Begründung |
|---|---|---|
| 8 Fragen | erfüllt | |
| 2 × Code-Ausgabe, 2 × Referenzsemantik, 2 × if/while, 1 × Einsatzgebiet, 1 × Stdlib | teilweise | 4 Code-Ausgabe-Fragen, 4 zur Referenzsemantik (Fragen 1, 3, 4, 5); Rest wie verlangt |
| Genau eine richtige Option, Lösung stimmt | erfüllt | Code-Fragen ausgeführt |
| Format Tabelle + Particify-Import | teilweise | kein Importformat |
| Abnahme: jede falsche Antwort deckt ein Fehlkonzept auf | teilweise | Fragen 7 und 8 mit Sach-Distraktoren (bei Frage 7 im Dokument selber eingeräumt) |

**Selbststudium U4: PYGR Kap. 1 bis 5**

| Vorgabe | Status | Begründung |
|---|---|---|
| Alle Übungen Kap. 1 bis 5, Vergleich mit Repo kap-1 bis kap-5 | nein (nicht durchführbar) | Repo enthält nur Python/kap-1 und kap-5 (U4-F01) |
| 3 Stolpersteine im Kurskanal | erfüllt | Format mit Beispiel |
| Zeitplan 3 × 30 min | erfüllt | |
| Abnahme: Ergebnis und Abgabekanal klar | erfüllt | Tabelle «Erwartetes Ergebnis» |

### 3.3 Lernziel-Abdeckung KT2

| LZ | Stufe | Abgedeckt durch | Bewertung |
|---|---|---|---|
| U3 LZ 1 Funktionen, Gruppierung | K3 | U3.1 | gut |
| U3 LZ 2 Views | K3 | nur Demo (Mittippen freiwillig) | K3 nicht erreicht: TN legen keine View selber an |
| U3 LZ 3 DBMS-Schichtenarchitektur | K2 | Drehbuch Minute 10 (Whiteboard-Brücke), U3.2 indirekt | schwach, Input fehlt |
| U3 LZ 4 Architektur aus Qualitätsanforderungen | K4 | U3.2, Selbststudium U3 | gut |
| U3 LZ 5 Indexierung und Caching | K3 | Kurzfolien-Demo, Caching-Punkte in U3.2 | K3 nur teilweise: keine TN-Anwendung von EXPLAIN/Index |
| U4 LZ 1 Einsatzgebiete Sprachen | K2 | Quiz U4 Frage 7 | schwach, PP7 fehlt |
| U4 LZ 2 Anweisungen, Ausdrücke, if, while | K3 | Live-Coding, U4.1, Quiz | gut |
| U4 LZ 3 Objekte/Variablen | K2 | Live-Coding Block 3, Quiz 1, 3, 4, 5 | gut |
| U4 LZ 4 eingebaute Funktionen, Stdlib | K3 | U4.1 C (random vorgegeben), Quiz 8 | schwach, Stdlib-Block fehlt |

---

## 4 Passung zum Unterrichtsplan KT2 (06.11.2026)

### 4.1 Vormittag (Unit 3)

| Plan | Methode Plan | Material | Minuten Plan / Material | Befund |
|---|---|---|---|---|
| 08:00-08:10 Check-in Quiz | [QUIZ] | Quiz U3 | 10 / 10 | passt |
| 08:10-08:30 Besprechung Selbststudium | Plenum | keins | 20 / n. a. | Reserve für fehlende Debriefings und DBMS-Input |
| 08:30-08:50 Input + Demo GROUP BY | [DEMO] | keins | 20 / 0 | Drehbuch fehlt |
| 08:50-09:20 Übung GROUP BY | [PARTNER] | U3.1 | 30 / 40 | Debriefing (10 min) ohne Slot; Views-Demo setzt die Pipeline aus diesem Debriefing voraus |
| 09:35-09:50 Views, Introspektion | [DEMO] | Drehbuch U3 | 15 / 15 | passt; Übergang zum DBMS-Input ins Leere |
| 09:50-10:20 Fallarbeit | [GRUPPE] + Galeriegang | U3.2 | 30 / 45 | 15 min zu wenig |
| 10:35-10:55 Indexierung und Caching | **[PP 5]** + [DEMO] | Kurzfolien U3 | 20 / 20 | Zeit passt; Markdown statt PowerPoint; Plan-Outline 6 bis 8 Folien, Material 10 |
| 10:55-11:25 PA-Kickoff | **[PP 6]** + Einzelarbeit | keins | 30 / 0 | fehlt |
| 11:25-11:45 Kurz-Quiz + Ausblick | [QUIZ] | Selbststudium U3 | 20 / ca. 5 | Quiz fehlt |

### 4.2 Nachmittag (Unit 4)

| Plan | Methode Plan | Material | Minuten Plan / Material | Befund |
|---|---|---|---|---|
| 13:00-13:10 Setup-Check | Plenum | Check U4 | 10 / 10 | passt; Tandem-Regel verweist auf U4.1 (erst 14:55) |
| 13:10-13:30 Warum Python? | **[PP 7]** | keins | 20 / 0 | fehlt; keine pptx im Drive |
| 13:30-13:50 Demo REPL | [DEMO] | Live-Coding U4 | 20 / 20 | passt; Block 1 wiederholt die Aufwärmaufgabe des Setup-Checks; Block 4 nimmt «erste Datei» und MwSt vorweg |
| 13:50-14:20 Mini-Aufgaben Variablen/MwSt | [PARTNER] | keins | 30 / 0 | fehlt; Drehbuch-Überleitung springt direkt zu U4.1 |
| 14:35-14:55 Demo Kontrollstrukturen | [DEMO] | keins | 20 / 0 | fehlt |
| 14:55-15:30 Übung if/while | [PARTNER] | U4.1 | 35 / 40 | 5 min zu wenig für Debriefing |
| 15:45-16:05 Stdlib | [DEMO] | keins | 20 / 0 | fehlt; random wird schon in U4.1 C gebraucht |
| 16:05-16:30 Kombinierte input()-Aufgabe | [PARTNER] | keins | 25 / 0 | fehlt |
| 16:30-16:45 Quiz | [QUIZ] | Quiz U4 | 15 / 15 | passt |
| 16:45-17:00 Ausblick | Plenum | Selbststudium U4 | 15 / 5 | passt zeitlich; Inhalt siehe U4-F01, U4-F02 |

### 4.3 PP-Status

| PP laut Plan | Soll | Ist |
|---|---|---|
| PP 5 Indexierung und Caching | PowerPoint, 6 bis 8 Folien, 15 min + Demo; Plan: «bereits vorhanden als Kurzfolien U3» | nur Markdown-Outline mit 10 Folien; keine pptx |
| PP 6 Einführung Praxisarbeit | 5 bis 6 Folien, 15 min | fehlt |
| PP 7 Warum Python? | 5 bis 6 Folien, 15 min | fehlt |

---

## 5 Fachliche Prüfung

### 5.1 SQL gegen Schema (create_beispiele.sql)

| Datei | Tabellen/Spalten | FK-Richtung | ONLY_FULL_GROUP_BY | MySQL-Spezifika | Befund |
|---|---|---|---|---|---|
| loesung_u3_1.sql | alle vorhanden (pruefung.fach/student/note, fach.fach_id/titel, student.klasse, klasse.klasse_id/bezeichnung/standort, standort.standort_id/name, lehrveranstaltung.klasse/beginn) | korrekt (pruefung → fach, pruefung → student → klasse → standort); klasse.standort ist im Dump nur logisch, ohne Constraint | konform: alle nicht aggregierten Spalten gruppiert; `YEAR(beginn)` identisch in SELECT und GROUP BY | YEAR, ROUND, LIMIT, Alias in ORDER BY: ok | SQLite-Probe reproduziert alle Zeilenzahlen und Spitzenwerte der Kommentare; MySQL-Rundung (AVG auf DECIMAL(2,1) mit Skala 5, ROUND half up) nachgerechnet: keine Abweichung zu erwarten. Keine NULL in note, student, klasse. Aufgabe 6: Gleichstand beim gerundeten Schnitt auf Rang 2/3, Reihenfolge nicht deterministisch (U3-F21) |
| demo_u3_views.sql | alle vorhanden; INSERT füllt alle NOT-NULL-Spalten von klasse; lehrgang 2 existiert (FK) | korrekt | v_klassengroesse konform | information_schema-Spalten korrekt (Ausgabe-Header in MySQL 8 in Grossbuchstaben) | Zeilenzahlen und Spitzenklasse im Drehbuch per SQLite bestätigt. key_column_usage zeigt klasse → standort und fach → dozent nicht (kein Constraint im Dump, U3-F11). DELETE per bezeichnung scheitert mit Safe Updates (U3-F26). CREATE VIEW nicht wiederholbar. table_rows in MySQL 8 zwischengespeichert (U3-F27) |
| index_demo_setup.sql | eigene DB `index_demo` | n. a. | n. a. | `INSERT ... WITH RECURSIVE ... SELECT`, `cte_max_recursion_depth`, ELT, DATE_ADD: MySQL-8-Syntax korrekt | Datenverteilung nachgerechnet: jede kunden_nr genau 20-mal (7919 und 5000 teilerfremd), jede aktion 25 %; Folienangaben stimmen |
| index_demo_ablauf.sql | ok | n. a. | n. a. | EXPLAIN, CREATE INDEX, TRUNCATE, SHOW VARIABLES: ok | Blöcke 3, 5, 6b nicht wiederholbar (Index existiert nach Probelauf, U3-F02). Block 5 ist eine Covering-Index-Abfrage, der Optimizer nimmt den Index sehr wahrscheinlich (U3-F03). Buffer-Pool-Effekt in Block 1 nicht verlässlich (U3-F04) |

### 5.2 Quiz

| Quiz / Frage | Genau eine richtig? | Markierte Lösung korrekt? | Distraktoren | Bemerkung |
|---|---|---|---|---|
| U3 / 1 | ja | ja | gut | Begründung nennt nur PLZ → Ort, nicht die Abhängigkeit der Kundenattribute von kunden_nr |
| U3 / 2 | ja | ja | gut | fragt nach Behebung statt Erkennen |
| U3 / 3 | ja | ja | gut | |
| U3 / 4 | **nein (MySQL)** | ja, aber nicht allein | Begründung zu «JOIN ohne ON» falsch für MySQL | MySQL akzeptiert JOIN ohne ON (Kreuzprodukt) und damit auch die Variante mit WHERE statt ON, die das korrekte Ergebnis liefert (U3-F01) |
| U3 / 5 | ja | ja | gut | |
| U3 / 6 | ja | ja | 2 schwache | |
| U3 gesamt | | | | Lösungsbuchstaben stark gehäuft (ein Buchstabe dominiert), Muster erratbar |
| U4 / 1, 2, 3, 6 | ja | ja (ausgeführt) | gut, je Fehlkonzept | |
| U4 / 4, 5 | ja | ja | gut | |
| U4 / 7 | ja | ja | Sachdistraktoren, kein Fehlkonzept | |
| U4 / 8 | ja | ja | ein starker Distraktor, zwei schwache | Auswertungshinweis «kommt im Selbststudium wieder» stimmt nicht (Selbststudium U4 ohne datetime) |

### 5.3 Aussagen in den Kurzfolien Indexierung/Caching

| Aussage | Bewertung |
|---|---|
| Ohne Index Full Table Scan, EXPLAIN type = ALL, key = NULL, rows ca. 100'000 | korrekt |
| B-Tree: «Gesucht wird durch Halbieren ... rund 3 Ebenen statt 100'000 Vergleiche» (Folie 4) | unscharf: 2 bis 3 Ebenen stimmen dank hoher Verzweigung (Hunderte Einträge pro Knoten); binäres Halbieren bräuchte ca. 17 Schritte. Vermischt B-Tree mit binärer Suche (U3-F05) |
| Index hilft bei =, <, >, BETWEEN, ORDER BY, LIKE 'abc%', nicht bei LIKE '%abc' | korrekt |
| PK hat automatisch Index; InnoDB legt für FK automatisch einen Index an | korrekt (falls kein passender Index existiert) |
| Nach Index: type = ref, key = Indexname, rows zweistellig | korrekt (zusätzlich «Using index») |
| Selektivität: 25'000 von 100'000 → Index lohnt nicht, Optimizer wählt ihn evtl. nicht | Prinzip korrekt, Demo-Abfrage ungeeignet: `COUNT(*)` mit Bedingung auf der Indexspalte wird vollständig aus dem Index beantwortet, der Index wird genutzt und ist schneller (U3-F03) |
| Faustregel unter 10 % Treffer | vertretbar als Faustregel |
| Index kostet bei INSERT/UPDATE/DELETE und Speicher | korrekt |
| MySQL Query Cache ab MySQL 8 entfernt | korrekt |
| innodb_buffer_pool_size Standard 128 MB, Tabelle passt hinein | korrekt |
| Zweiter Lauf schneller wegen Buffer Pool | fragwürdig für diese Demo: nach Setup liegen die Seiten bereits im Buffer Pool; MySQL 8 lädt ihn nach Neustart standardmässig wieder (buffer_pool_dump/load). Effekt oft nicht sichtbar (U3-F04) |
| Kontrollfrage: Index auf 0/1-Spalte bei 800 Zeilen lohnt nicht | korrekt |
| Plan-Outline PP5: «Grundidee Invalidierung» | fehlt (nur «wie alt dürfen Daten sein») |

### 5.4 Python

Alle vier Musterlösungen laufen und liefern die im Aufgabenblatt und in den Kommentaren genannten Ergebnisse. Details und Randfälle in Abschnitt 6. Aussagen im Live-Coding-Drehbuch (REPL-Ausgaben, `is` bei kleinen und grossen Zahlen, Unterschied REPL/Datei, Float-Darstellung der MwSt) sind in 3.11, 3.12 und 3.13 korrekt.

---

## 6 Ausführungsprotokoll

Arbeitsverzeichnis: `scratchpad/drive/Unit_4/code/`. Ergebnisse ohne Lösungsinhalte. Wo nicht anders vermerkt, identisch unter Python 3.11.15, 3.12.3 und 3.13.12.

| Nr | Befehl (sinngemäss) | Ergebnis |
|---|---|---|
| P1 | `printf '5\n' \| python3 loesung_u4_1a_preisstaffel.py`, ebenso 40, 250, 600, 0 (Testwerte des Blatts) | ok: Rabattstufe und Beträge rechnerisch korrekt; 0 liefert die verlangte Meldung und sonst nichts |
| P2 | Grenzwerte 19/20, 99/100, 499/500 sowie -3 | ok: Schwellen mit >= korrekt; negative Menge → Meldung. Nebenbefund: bei 99 Stück ist der Endpreis höher als bei 100 (Rabattsprung), guter Diskussionsanlass |
| P3 | Eingaben `zwanzig`, `40.5`, leer | Abbruch mit ValueError, laut Dozentenhinweis gewollt (Fehlerbehandlung erst Unit 5, Zusatzauftrag) |
| P4 | `printf '12.50\n8\n45.90\nende\n' \| python3 loesung_u4_1b_spesen.py` | ok: Anzahl, Total, Durchschnitt entsprechen der Angabe im Aufgabenblatt |
| P5 | `printf 'ende\n' \| python3 loesung_u4_1b_spesen.py` | ok: kein ZeroDivisionError, Meldung statt Durchschnitt |
| P6 | `printf '10\nEnde\n'` | ok: Grossschreibung wird akzeptiert |
| P7 | Eingaben `12,50`, Leerzeile, ` ende ` (mit Leerzeichen) | Abbruch mit ValueError (erwartet, aber realistische Randfälle, siehe U4-F13) |
| P8 | `printf '10\n-20\nende\n'` | läuft, negatives Total wird akzeptiert (keine Vorgabe dazu) |
| P9 | Zahlenraten mit festem Seed, sofort richtig geraten | ok: Schleife endet nach einem Versuch |
| P10 | Seed, Treffer im 6. Versuch | ok |
| P11 | Seed, 6 Fehlversuche | ok: Zahl wird verraten, keine 7. Abfrage |
| P12 | im Docstring dokumentierter Test `printf '50\n25\n37\n' \| python3 loesung_u4_1c_zahlenraten.py` | **abweichend:** bricht in den meisten Läufen mit EOFError ab (nur 3 Eingaben für bis zu 6 Versuche); Docstring nennt den interaktiven Test «deterministisch» |
| P13 | Zahlenraten mit Eingabe `abc` | ValueError (erwartet) |
| P14 | Zahlenraten mit Tipps ausserhalb 1 bis 100 | läuft, keine Bereichsprüfung (keine Vorgabe) |
| P15 | `python3 loesung_u4_1d_jasszaehler.py` | ok: 40 Zeilen, Kontrollpunkte des Blatts und Verteilung im Kommentar stimmen; Ausgabe in allen drei Versionen byte-gleich (md5) |
| P16 | Live-Coding Block 3: `a = 1000`, `b = 1000`, `a is b` via `python3 -i` und als Datei | ok: REPL und Datei verhalten sich wie im Drehbuch («Demo-Falle») beschrieben, in 3.11, 3.12, 3.13 |
| P17 | Live-Coding Blöcke 1, 2, 4 (Ausdrücke, TypeError-Text, MwSt, round, f-Strings) | ok: alle genannten Ausgaben stimmen; der f-String mit `{betrag}` zeigt den Betrag mit nur einer Nachkommastelle |
| P18 | Quiz U4, Fragen 1, 2, 3, 6 als Skript; Frage 8 (datetime-Differenz) | ok: markierte Lösungen stimmen |
| P19 | Setup-Check Aufwärmaufgabe (5 REPL-Zeilen) | ok: Auflösung im Dokument stimmt |
| S1 | Port create_beispiele.sql → SQLite (Python-Skript) | ok: 14 Tabellen, Zeilenzahlen wie Dump |
| S2 | 8 Abfragen loesung_u3_1.sql auf SQLite (YEAR → strftime) + Decimal-Nachrechnung | ok: alle Kommentarwerte reproduziert; Rundung MySQL identisch; Gleichstand Aufgabe 6 Rang 2/3 |
| S3 | Fehlvariante Aufgabe 4 (Gruppierung nach Datum statt Jahr) | ok: Aussage im Dozententeil stimmt |
| S4 | demo_u3_views.sql Blöcke 1 bis 5 auf SQLite | ok: Zeilenzahlen vor/nach INSERT und Spitzenklasse stimmen |
| S5 | Datengenerierung index_demo_setup.sql in Python | ok: Verteilung wie auf Folien 2 und 7 |
| S6 | MySQL 8 | **nicht ausgeführt** (anderer Agent); insbesondere offen: Index-Demo, Laufzeiten, EXPLAIN Block 5, Safe Updates, information_schema |

---

## 7 Neuheit: Nähe zu Buchaufgaben

| Unterrichtsmaterial | Repo-Pendant | Nähe | Bewertung |
|---|---|---|---|
| U3.1 Aufgabe 1 (Kennzahlen der Prüfungen) | SQL/kap-5.sql, Beispiele 5.2 (MIN, MAX, AVG auf pruefung.note) | gleiche Funktionen, hier kombiniert | tief, als Einstieg vertretbar |
| U3.1 Aufgabe 2 (Studierende je Klasse) | kap-5.sql Beispiel 5.3; kap-7.sql View v_klassen | gleiche Kernabfrage, nur ohne Semesterfilter | tief bis mittel |
| U3.1 Aufgabe 5a (HAVING auf Klassengrösse) | kap-5.sql Beispiel 5.4 | gleiche Gruppierung, andere HAVING-Bedingung | tief |
| U3.1 Aufgabe 6 (Notenschnitt je Klasse) | kap-5.sql, Kap. 5.7 **Aufgabe 3** (Durchschnittsnote der Klassen im Fach Deutsch) | gleicher Join-Pfad pruefung → student → klasse, gleiches Aggregat; Buchlösung öffentlich und laut Handoff im Selbststudium U2 bearbeitet | **mittel** (U3-F17); Abgrenzungstext im Blatt nennt nur die Beispiele |
| U3.1 Aufgaben 3, 4, 5b, Zusatz | kein Pendant | neu | ok |
| Demo U3 Views / Introspektion | kap-7.sql (v_klassen), kap-10.sql | bewusst, Dozentendemo laut Handoff erlaubt | ok |
| U4.1 A Preisstaffel | Python/kap-6/beitrag.py, eintritt3c.py | gleiches Muster (Schwellenkette), neues Szenario | ok |
| U4.1 B Spesen | Python/kap-7/papagei.py (while True + break bei «Ende»), kap-5/mittelwert.py | gleiches Schleifenmuster, neues Szenario mit Akkumulator | ok |
| U4.1 C Zahlenraten | kein Pendant (random nur in Lotto-Skripten und kap-8/sekunden.py) | neu | ok |
| U4.1 D Jass-Zähler | kap-6/gerade*.py (Modulo) | neu | ok |
| Quiz U4 Frage 2 | kap-7/countdown.py | ähnliche Schleife, anderer Schritt | ok (Quiz) |
| U3.2 Alpsicht AG, Selbststudium U3 Szenarien A/B | kein Pendant in SQL/kap-*.sql | neu | ok; Szenario B intern nah am Ersatzmodell des Coaching-Leitfadens U5 (U3-F30) |

---

## 8 Querverweise und roter Faden

| Verweis | In Datei | Status |
|---|---|---|
| Quiz U3 → U3.1 Aufgabe 6 (JOIN-Probleme), Selbststudium U3 (3NF-Checkliste), Coaching U5 | Quiz U3 | ok |
| Quiz U3 Frage 2 → «am Nachmittag beim Indexierungs-Input» | Quiz U3 | falsch: laut Plan Vormittag |
| U3.1 → `code/loesung_u3_1.sql`; Pipeline an Wandtafel für Views-Demo | U3.1 | ok (Debriefing hat aber keinen Slot) |
| U3.1 Zirkulier-Hinweis «Paare, die bei Aufgabe 4 hängen, haben meistens das JOIN-Problem» | U3.1 | falsch: Aufgabe 4 ist eine Ein-Tabellen-Abfrage; gemeint vermutlich Aufgabe 6 |
| Drehbuch Min 2 «Merkt euch den Satz, er kommt im Quiz» | Drehbuch U3 | tot: kein Quiz mit Views-Frage; Kurz-Quiz 11:25 ohne Material |
| Drehbuch Min 8 → U3.1 Aufgabe 2 (fehlende leere Klassen) | Drehbuch U3 | irreführend (U3-F12) |
| Drehbuch → Partnerübung U2.2, Safe-Update-Hinweis Unit 1 | Drehbuch U3 | Namen stimmen mit Handoff WP 0; Existenz der WP-0-Materialien hier nicht geprüft |
| Drehbuch → «Übergang zum Input DBMS-Architektur» | Drehbuch U3 | tot im Plan (KT2-F03) |
| U3.2 → «Folien SQL (DBMS-Architektur)» | U3.2 | externer Foliensatz, nicht geprüft |
| U3.2 → «Brücke zum ACID-Stoff aus Unit 1/2» | U3.2 | im Handoff WP 0 kein ACID/Transaktions-Material, im Plan nur Stichwort in PP2 |
| U3.2 → Kurzfolien greifen Flipcharts auf; Selbststudium U3 Historisierung | U3.2 | ok; Historisierung fehlt aber in Szenario B |
| Kurzfolien → code-Dateien, Folie 9 löst Frage aus Folie 3 auf | Kurzfolien | ok |
| WP1-Übersicht → «Tabelle messung», «alle sieben Abfragen» | WP1-Übersicht | falsch: Tabelle heisst zugriffslog (DB index_demo); es sind acht Abfragen |
| Check U4 → «erste Übung (Partnerübung U4.1)» | Check U4 | passt nicht zum Plan (erste Partnerübung 13:50) |
| Live-Coding → «Demo-Skript liegt vorab im Kurskanal» | Live-Coding | tot: kein Skript im Drive |
| Live-Coding → Check U4, U4.1, Unit 5, «DECIMAL ... Rückverweis auf Unit 3» | Live-Coding | ok; DECIMAL wird in U3-Material nicht thematisiert (nur im Selbstcheck U3) |
| U4.1 → B-Tree Unit 3, Unit 5 defensive Programmierung, Musterlösungsdateien | U4.1 | ok (Dateinamen stimmen) |
| Quiz U4 → U4.1 Aufgaben A und D, U5.1 | Quiz U4 | ok |
| Quiz U4 Auswertung → «Frage 8 kommt im Selbststudium sowieso wieder» | Quiz U4 | falsch: Selbststudium U4 (Kap. 1 bis 5) enthält kein datetime |
| Selbststudium U3 → Partnerübung U2.1, Coaching-Leitfaden U5 | Selbststudium U3 | Namen stimmen; Inhalte ausserhalb dieses Bereichs |
| Selbststudium U4 → Repo `Python/kap-1` bis `kap-5` | Selbststudium U4 | teilweise tot: kap-2, kap-3, kap-4 existieren nicht |
| Roter Faden WP1: B-Tree → Zahlenraten → set; Referenzsemantik Block 3 → Quiz 3 → U5.1; GROUP BY → dict | WP1-Übersicht | in den U3/U4-Dateien umgesetzt; B-Tree-Glied fachlich unscharf (U3-F05) |

---

## 9 Remote-Reste und Präsenz-Widersprüche

Gesucht nach Breakout, Poll, Screen-Share, Zoom, Chat, geteilt, remote.

| Fundstelle | Befund |
|---|---|
| Kurzfolien U3, «Kontrollfrage für zwischendurch»: «als Chat-Frage stellen» | Remote-Rest (U3-F24) |
| Kurzfolien U3 Folie 1: «Die Frage, die den Nachmittag zusammenhält»; Quiz U3 Frage 2: «am Nachmittag» | Tageszeit aus früherer Planung; U3 ist Vormittag |
| U4.1 Output: Kurzmeldung im Kurskanal während der Präsenzübung | kein Fehler, aber Remote-Muster; Handzeichen oder Strichliste genügt |
| Live-Coding «Mail und Chat schliessen» | ok (Beamer-Hygiene) |
| Sonst keine Treffer | Breakout, Poll, Screen-Share, Zoom kommen nicht vor |

---

## 10 Findings

### Unit 3

| ID | Schwere | Datei, Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| U3-F01 | hoch | Quiz_U3, Frage 4 und Lösungstabelle | In MySQL liefern zwei Optionen das korrekte Ergebnis: neben der ON-Variante auch «JOIN ... WHERE Bedingung», weil MySQL JOIN ohne ON als Kreuzprodukt akzeptiert. Die Begründung, JOIN ohne ON sei ein Syntaxfehler, ist für MySQL falsch und widerspricht PP4 («JOIN ohne ON → kartesisches Produkt») | Option mit WHERE durch einen echten Fehler ersetzen (z. B. falsche Join-Spalte oder LEFT JOIN mit Filter, der die Aussenzeilen entfernt); Begründung: «JOIN ohne ON: in MySQL Kreuzprodukt, in Standard-SQL Syntaxfehler» |
| U3-F02 | hoch | Kurzfolien Vorbemerkung; index_demo_setup.sql Kopf; index_demo_ablauf.sql Blöcke 3, 5, 6b | Das Material verlangt Setup plus Probelauf der Demo vor dem Unterricht. Nach dem Probelauf existieren alle Indexe: im Unterricht zeigt Block 1/2 bereits den Indexzugriff, Block 3, 5 und 6b brechen mit «Duplicate key name» ab. Kein Hinweis, das Setup danach erneut auszuführen | In Folien-Vorbemerkung und beiden Skriptköpfen: «Nach dem Probelauf index_demo_setup.sql erneut ausführen (setzt alles zurück)». Optional Reset-Block am Anfang des Ablaufs |
| U3-F03 | mittel | index_demo_ablauf.sql Block 5; Kurzfolien Folie 7 Sprechernotiz | `COUNT(*)` mit Bedingung auf der Indexspalte ist eine Covering-Index-Abfrage: MySQL nutzt den Index (type ref, «Using index») und ist damit schneller als der Scan. Die angekündigte Beobachtung «Optimizer wählt den Index nicht» tritt so kaum ein; misst der Dozent die Zeit, widerspricht die Demo der Folie | Abfrage auf eine Nicht-Index-Spalte erweitern (z. B. `SELECT AVG(dauer_ms) ... WHERE aktion = 'suche'` oder `SELECT *`), auf MySQL 8 testen und Sprechnotiz an das reale EXPLAIN anpassen |
| U3-F04 | mittel | index_demo_ablauf.sql Block 1 und 7; Kurzfolien Folien 3 und 9 | «Zweiter Lauf schneller wegen Buffer Pool» ist für diese Demo nicht verlässlich: nach dem Setup liegen die Seiten bereits im Buffer Pool, MySQL 8 lädt ihn nach Neustart standardmässig wieder. Die offene Frage an die Klasse kann ins Leere laufen | Effekt nur als Möglichkeit ansagen oder mit `SHOW STATUS LIKE 'Innodb_buffer_pool_read%'` (Disk-Reads vs. Requests) sichtbar machen |
| U3-F05 | mittel | Kurzfolien Folie 4 Sprechernotiz; U4.1 Debriefing; loesung_u4_1c Hinweis 3 | «Gesucht wird durch Halbieren ... rund 3 Ebenen» vermischt binäre Suche (bei 100'000 ca. 17 Schritte) mit dem B-Tree (hohe Verzweigung, daher 2 bis 3 Ebenen). Der Rückverweis Zahlenraten = B-Tree verfestigt das | Folie: «Jeder Knoten teilt in viele Teilbereiche, daher nur 2 bis 3 Ebenen»; Rückverweis als «gezieltes Eingrenzen statt Durchlaufen» formulieren |
| U3-F06 | mittel | Kurzfolien_U3; Plan PP 5 | Plan verlangt [PP 5] als PowerPoint und nennt sie «bereits vorhanden»; vorhanden ist nur eine Markdown-Outline, im Drive gibt es keine PP5-pptx (nur PP1 bis PP4). Grafiken (Folien 2, 4, 9) existieren nur als Beschreibung | PP5 auf der Schulvorlage wie PP1 bis PP4 erstellen, Grafiken zeichnen, Folienzahl mit Plan-Outline abgleichen |
| U3-F07 | mittel | Demo-Drehbuch U3; Kurzfolien U3 | LZ 2 (Views, K3) und LZ 5 (Indexierung, K3) werden nur vorgeführt; TN legen weder eine View an noch lesen sie selbst ein EXPLAIN | 5-min-Mini-Auftrag je Paar (eigene View zu einer U3.1-Abfrage; EXPLAIN auf eine U3.1-Abfrage lesen) oder im Selbststudium U3 ergänzen |
| U3-F08 | mittel | Partneruebung_U3.1, Aufgaben | TN-Blatt enthält keine erwartete Zeilenzahl oder Kontrollgrösse; Handoff verlangt sie pro Aufgabe. Paare können nicht selbst prüfen, der Dozent muss jede Abfrage kontrollieren | Pro Aufgabe die erwartete Zeilenzahl aufs Blatt (ohne Aggregatwerte) |
| U3-F09 | mittel | Partneruebung_U3.1, «Beim Zirkulieren achten auf», Aufgaben 3 und 6 | ONLY_FULL_GROUP_BY wird genannt, aber nicht erklärt. Zudem erkennt MySQL 8 funktionale Abhängigkeit vom Primärschlüssel: wer nur nach fach_id bzw. klasse_id gruppiert und titel bzw. bezeichnung ausgibt, bekommt keinen Fehler 1055. Die Denkfrage in Aufgabe 3 und Falle 1 in Aufgabe 6 erzeugen daher kein sichtbares Problem | 3-Satz-Erklärung plus ein Beispiel, das Fehler 1055 sicher auslöst (nicht abhängige Spalte, z. B. Studierendenname bei Gruppierung nach Klasse); Hinweis auf funktionale Abhängigkeit |
| U3-F11 | mittel | Demo-Drehbuch Minute 13; demo_u3_views.sql Block 7 | Der Dump hat für klasse.standort und fach.dozent keinen FK-Constraint. key_column_usage zeigt diese Beziehungen nicht, obwohl das ERD aus Unit 2 sie enthält und v_klassenliste selbst über klasse.standort joint. Sprechnotiz sagt «Das ist das ERD aus Unit 2, als Tabelle» | Als Lernmoment aufnehmen: «logische Beziehung ohne Constraint, die Datenbank kennt sie nicht» |
| U3-F12 | mittel | Demo-Drehbuch Minute 8 | Der Satz zu U3.1 Aufgabe 2 unterstellt, die erwartete Lösung verliere Klassen ohne Studierende. Im Dump hat jede Klasse Studierende, die Musterlösung ist vollständig; Paare mit korrekter Lösung werden verunsichert | Umformulieren: «Mit INNER JOIN wäre die neue, leere Klasse verschwunden» |
| U3-F13 | mittel | Demo-Drehbuch Minute 2; Plan 11:25 | «Merkt euch den Satz, er kommt im Quiz»: kein U3-Quiz enthält Views; das Kurz-Quiz im Plan hat kein Material | Kurz-Quiz U3 (3 bis 4 Fragen zu GROUP BY, View, Index) erstellen oder Satz streichen |
| U3-F15 | mittel | Selbststudium_U3, Selbstcheck Teil 2 «Historisierung»; Dozentenhinweise | Text behauptet, beide Szenarien enthielten eine Nachvollziehbarkeitsanforderung. Szenario B (Kursverwaltung) enthält weder Preis noch einen solchen Satz; wer B wählt, kann den Punkt nicht bearbeiten, der als «eigentlicher K4-Kern» gilt | In Szenario B eine Anforderung ergänzen (z. B. Kurspreise ändern sich, Bestätigung muss den gebuchten Preis zeigen) oder Texte korrigieren |
| U3-F16 | mittel | Selbststudium_U3, Selbstcheck vs. Dozentenhinweise | Dozentenhinweis: Historisierung ist «versteckt, nicht vorwegnehmen»; der TN-Selbstcheck nennt sie ausdrücklich samt zwei Lösungswegen. Beide Teile stehen im selben Dokument | Didaktischen Entscheid treffen (Hinweis im Selbstcheck oder bewusst weglassen) und TN- von Dozentenfassung trennen |
| U3-F17 | mittel | Partneruebung_U3.1 Aufgabe 6 und «Abgrenzung zum Lehrmittel» | Aufgabe 6 entspricht im Kern DBSQL Kap. 5.7 Aufgabe 3 (gleicher Join-Pfad, gleiches Aggregat je Klasse), deren Lösung im Repo liegt und im Selbststudium U2 bearbeitet wird. Aufgabe 2 ist nah an Beispiel 5.3 und v_klassen | Aufgabe 6 variieren (z. B. Bestehensquote Note >= 4 je Klasse mit SUM(CASE ...), deckt zugleich SUM ab) und Abgrenzungstext ergänzen |
| U3-F18 | tief | Partneruebung_U3.1, Schema-Ausschnitt und Aufgaben | SUM fehlt; lehrgang und raum ungenutzt («Raumkapazität pro Standort» aus dem Handoff fehlt); lehrveranstaltung fehlt im Schema-Ausschnitt; klasse.standort als FK dargestellt, im Dump ohne Constraint | Schema-Ausschnitt ergänzen; eine Aufgabe mit SUM(kapazitaet) je Standort |
| U3-F19 | tief | Partneruebung_U3.1, Arbeitsauftrag | Minutenplan gibt 25 min für die Aufgaben, die Richtzeiten der Aufgaben ergeben 30 min | Richtzeiten angleichen |
| U3-F20 | tief | Partneruebung_U3.1, Zirkulier-Hinweis 4 | Verweist auf «Aufgabe 4» als JOIN-Problem; Aufgabe 4 hat keinen JOIN | «Aufgabe 6» |
| U3-F21 | tief | loesung_u3_1.sql Aufgabe 6 | ORDER BY auf den gerundeten Alias; Rang 2 und 3 sind gerundet gleich, Reihenfolge in MySQL nicht garantiert und nach exaktem Schnitt umgekehrt zum Kommentar | `ORDER BY AVG(p.note) DESC` |
| U3-F22 | tief | Quiz_U3 | Frage 2 fragt nach Behebung statt Erkennen; Begründung Frage 1 nennt nicht die Abhängigkeit der Kundenattribute von kunden_nr; Lösungsbuchstaben stark gehäuft; kein Particify-Importformat | Frage 2 als Erkennungsfrage oder Handoff-Abweichung vermerken; Begründung ergänzen; Lösungspositionen mischen |
| U3-F23 | tief | Kurzfolien Folie 1 Titel; Quiz_U3 Lösung Frage 2 | Tageszeit-Reste «Nachmittag»; U3 findet am Vormittag statt | Formulierungen neutralisieren |
| U3-F24 | tief | Kurzfolien, Kontrollfrage | «als Chat-Frage stellen» (Remote-Rest) | Handzeichen oder Particify |
| U3-F25 | tief | Kurzfolien; index_demo_setup.sql; WP1-Übersicht; Plan PP5 | Demo läuft in eigener DB `index_demo`, Tabelle `zugriffslog`; Handoff wollte Testdaten in «beispiele» (z. B. messung), Plan sagt «auf beispiele», WP1-Übersicht nennt «messung» | Eigene DB beibehalten (hält «beispiele» sauber), Plan und Übersicht angleichen |
| U3-F26 | tief | Demo-Drehbuch Minute 10; demo_u3_views.sql Block 6 | Workbench «Safe Updates» ist standardmässig an; DELETE per bezeichnung (kein Schlüssel) scheitert mit Fehler 1175 sicher, nicht nur «falls». CREATE VIEW scheitert bei Wiederholung | `WHERE klasse_id = LAST_INSERT_ID()`; `CREATE OR REPLACE VIEW` |
| U3-F27 | tief | Demo-Drehbuch Minute 11 | information_schema.tables.table_rows wird in MySQL 8 zwischengespeichert (Standard 24 h); nach frischem Import sind 0 oder veraltete Werte möglich | Vorab `ANALYZE TABLE` oder `SET SESSION information_schema_stats_expiry = 0`; Sprechnotiz ergänzen |
| U3-F28 | tief | Kurzfolien Folie 6, 9 | Workbench zeigt bei der Indexabfrage oft 0.000 sec, der Faktor ist dann nicht berechenbar; Plan-Punkt «Invalidierung» fehlt | `EXPLAIN ANALYZE` für Zeiten nutzen; Invalidierung in Folie 9 ergänzen |
| U3-F29 | tief | Gruppenuebung_U3.2 | Kein Abschnitt «Beim Zirkulieren achten auf»; Handout Teil A länger als 1 Seite; «Brücke zum ACID-Stoff aus Unit 1/2» ohne Gegenstück im WP-0-Handoff | Zirkulier-Abschnitt aus den «Nachfragen» ableiten; Handout straffen; Brücke prüfen oder streichen |
| U3-F30 | tief | Selbststudium_U3 | Tabellenumfang uneinheitlich (min. 4, eigenes Szenario 4 bis 8; Plan PP6: 3 bis 6); Szenario B thematisch gleich wie das Ersatzmodell im Coaching-Leitfaden U5 (Kursverwaltung), dessen eingebaute Schwächen dann zur Lösungsvorlage werden | Spannen vereinheitlichen; Ersatzmodell U5 anderes Thema geben |

### Unit 4

| ID | Schwere | Datei, Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| U4-F01 | hoch | Selbststudium_U4, Schritt 2 und «Wenn ihr nicht weiterkommt» | Repo enthält nur `Python/kap-1` und `kap-5`; `kap-2`, `kap-3`, `kap-4` existieren nicht. Der Beispielsatz zu Kapitel 3 ist falsch, der Vergleichsschritt für drei von fünf Kapiteln nicht durchführbar. Fehler stammt aus dem Handoff | Verweis korrigieren; für Kap. 2 bis 4 eigene Kontrollhilfe (z. B. Lösungsskizzen im Kurskanal nach Frist) |
| U4-F02 | mittel | Selbststudium_U4 insgesamt; Selbstcheck | Auftrag deckt PYGR Kap. 1 bis 5 ab (laut Handoff vor U4 bereits gelesen), der Unterricht U4 behandelt Kap. 6 bis 8 (if, while, Module). Selbstcheck prüft if/elif und while, die nicht in Kap. 1 bis 5 liegen. Übungen zu Kap. 6 bis 8 werden nirgends beauftragt (Selbststudium U5 beginnt bei Kap. 9) | Auftrag auf Übungen Kap. 6 bis 8 umstellen, Kap. 1 bis 5 als optionale Repetition |
| U4-F03 | mittel | Check_U4, «Regel, die vorher laut angesagt wird»; Partneruebung_U4.1 Pair-Programming-Regeln | Tandem und Setup-Behebung sind an U4.1 gekoppelt; laut Plan startet U4.1 erst 14:55, erste Partnerübung ist 13:50. TN ohne Setup warten fast zwei Stunden | «erste Partnerübung» schreiben; Setup-Behebung während der Mini-Aufgaben 13:50 vorsehen |
| U4-F04 | mittel | Check_U4, Frage 1 und Fall 5 | macOS-Fall fehlt: `python3` ist das Apple-Python 3.9 der Command Line Tools (oder startet deren Installationsdialog). Frage 1 verlangt 3.11+, Fall 5 («python3 verwenden») hilft nicht | Fall ergänzen: Installer von python.org, danach Terminal neu, `python3 --version`, in VS Code Interpreter wählen |
| U4-F05 | tief | Check_U4, Frage 3, Frage 4, Fall 1, Fall 4, Schnelldiagnose, Vorbereitung | Aktuelle VS-Code-Versionen zeigen den Interpreter rechts in der Statusleiste und nur bei offener .py-Datei («unten links» veraltet); F5 startet den Debugger mit Konfigurationsauswahl; Windows-Einstellung heisst «App-Ausführungsaliase»; «drei Windows-Fixes» bei vier Windows-Fällen | Texte auf aktuellem VS Code/Windows prüfen und anpassen; «Run Python File» (Dreieck) statt F5 |
| U4-F06 | tief | Check_U4 Aufwärmaufgabe; Live-Coding Block 1 | Beide enthalten dieselben Ausdrücke inkl. TypeError und denselben Merksatz zur Fehlermeldung; die «Pointe» in Block 1 ist verbraucht | Aufwärmaufgabe auf andere Ausdrücke umstellen oder Block 1 kürzen |
| U4-F07 | tief | Live-Coding Block 3 | Handoff verlangt id()-Demo, gezeigt wird nur `is`; typische TN-Fragen je Block statt je Schritt | `id(a)`, `id(b)` ergänzen |
| U4-F08 | mittel | Live-Coding «Vor dem Start» und «Nacharbeiten» | «Das Demo-Skript liegt vorab im Kurskanal»: ein solches Skript existiert nicht (Unit_4/code enthält nur die U4.1-Lösungen) | Skript erstellen (alle Eingaben in Reihenfolge, REPL-Teile als Kommentar) |
| U4-F09 | tief | Live-Coding Block 4 | f-String mit `{betrag}` gibt den Betrag mit einer Nachkommastelle aus; Rückverweis «DECIMAL ... Unit 3» hat im U3-Material keinen Anker | Formatierung `:.2f` auch dort zeigen; Rückverweis auf Selbststudium U3 (Datentypen) ändern |
| U4-F10 | tief | Partneruebung_U4.1, Zeitsteuerung, Aufgabe D, Output | Hinweise widersprüchlich (Nachzügler sollen B überspringen und D machen, zugleich «D ist die Kür, A bis C reicht»); D ohne input(); Kurzmeldung im Kurskanal während Präsenz eher Remote-Muster | Zeitsteuerung vereinheitlichen; D optional mit Eingabe der Obergrenze; Handzeichen/Strichliste statt Kanal-Post |
| U4-F11 | tief | loesung_u4_1c Docstring; Plan 15:45 | «Modul random (in der Unit gezeigt)»: laut Plan kommt der Stdlib-Block erst nach U4.1; unkritisch, da Snippet im Blatt | Docstring anpassen oder Stdlib vorziehen |
| U4-F12 | tief | loesung_u4_1c Docstring und Ausgabe; loesung_u4_1a Ausgabe | Dokumentierter automatisierter Test bricht meist mit EOFError ab, «deterministisch» ist irreführend; Ausgabe «1 Versuche»; in A sind die Beschriftungen um ein Zeichen versetzt | Testhinweis mit Seed oder sechs Eingaben; Singular/Plural; Labels ausrichten |
| U4-F13 | tief | U4.1 Aufgaben A bis C (Randfälle) | Nicht-Zahlen brechen ab (gewollt); B akzeptiert negative Beträge und bricht bei Dezimalkomma ab; in A ist 99 Stück teurer als 100 (Rabattsprung) | Als Zusatz- und Debriefing-Impulse nutzen, keine Pflichtkorrektur |
| U4-F14 | tief | Quiz_U4 | Typenverteilung weicht vom Handoff ab (4 Code-Ausgabe, 4 Referenzsemantik); Fragen 7 und 8 mit Sachdistraktoren; kein Importformat; Auswertung «Frage 8 kommt im Selbststudium wieder» falsch | Verteilung als bewusste Abweichung vermerken; Auswertungssatz korrigieren (oder U4-F02 umsetzen) |

### Übergreifend KT2

| ID | Schwere | Datei, Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| KT2-F01 | hoch | Unterrichtsplan S2610, KT2 Nachmittag | 5 Plan-Blöcke ohne Material: PP7 (20 min), Mini-Aufgaben Variablen/MwSt (30), Demo Kontrollstrukturen (20), Stdlib-Demo (20), kombinierte input()-Aufgabe (25) = 115 von 225 Unterrichtsminuten. Der Handoff hat diese Materialien nicht beauftragt. LZ 1 und LZ 4 von U4 hängen daran | Materialien ergänzen (Drehbuch Kontrollstrukturen, Stdlib-Demo, 2 Aufgabenblätter, PP7) oder Plan auf vorhandenes Material zurückbauen (U4.1 früher, Mini-Aufgaben aus Live-Coding Block 4 ableiten) |
| KT2-F02 | hoch | Unterrichtsplan S2610, KT2 Vormittag | PP6 PA-Kickoff (30 min) fehlt und hängt an den fehlenden PA-Unterlagen; Selbststudium U3 baut darauf auf. Input+Demo GROUP BY (20 min) ohne Drehbuch, Kurz-Quiz ohne Material | PP6 mit Platzhaltern für PA-Vorgaben erstellen; Demo-Drehbuch GROUP BY auf Basis kap-5.sql; Kurz-Quiz U3 |
| KT2-F03 | mittel | Plan KT2 Vormittag; Drehbuch U3 Ende; U3.2 Hilfsmittel | Input DBMS-Architektur (LZ 3, K2) hat weder Slot noch Material; Plan-Überblick nennt LZ 3 nicht; Drehbuch und U3.2 setzen ihn voraus | 10 min einplanen (z. B. aus 08:10-08:30), Folien aus «Folien SQL» bestimmen oder erstellen |
| KT2-F04 | mittel | Plan vs. U3.1, U3.2, U4.1 | Debriefings ohne Slot: U3.1 10 min, U3.2 15 min, U4.1 5 min fehlen. Views-Demo braucht die Pipeline aus dem U3.1-Debriefing | Plan umbauen (08:10-08:30 kürzen, Fallarbeit 45 min) oder Debriefings straffen |
| KT2-F05 | mittel | U3.1, U4.1, Selbststudium U3, Selbststudium U4 | TN- und Dozenteninhalte im selben Dokument (Musterlösungsverweise, Fehlerbilder, «nicht vorwegnehmen»); als Handout nicht direkt verteilbar | Je TN-Handout (Auftragsfolie + Aufgaben) und Dozentenfassung erzeugen; Auftragsfolien als Folien setzen |
| KT2-F06 | mittel | WP1-Übersicht «vollständig, Code verifiziert»; alle SQL-Dateien | SQL nur gegen SQLite geprüft (beispiele.sqlite fehlt im Drive), Index-Demo nie ausgeführt, Laufzeiten nicht gemessen. Meine SQLite-Probe bestätigt Musterlösung und Drehbuch-Zahlen, ersetzt keinen MySQL-8-Lauf mit Workbench | Alle vier SQL-Dateien auf MySQL 8 in Workbench mit Standardeinstellungen durchspielen, Laufzeiten eintragen |
| KT2-F07 | tief | WP1-Übersicht | «alle sieben Abfragen» (es sind acht), «Tabelle messung» (zugriffslog), Hinweis «Unterrichtsplan noch remote formuliert» durch S2610 überholt | Übersicht nachführen |
| KT2-F08 | tief | Kopfzeilen U3.1, U3.2, U4.1, Check U4 | «KI-Stufe 0» ohne Definition der Skala (weder Handoff noch Plan) | Skala im Kursdokument definieren oder Angabe durch Klartext ersetzen |
| KT2-F09 | tief | Quiz U3, Quiz U4 | Kein Particify-Importformat, QR-Folien nicht vorhanden | Fragen vorab in Particify anlegen (ca. 15 min je Quiz), QR-Code auf Einstiegsfolie |

Anzahl: 5 hoch, 21 mittel, 25 tief (U3-F10 und U3-F14 wurden in KT2-F05 und KT2-F03 zusammengeführt, Nummern bewusst frei gelassen).

---

## 11 Vor Einsatz an KT2 (06.11.2026) zu erledigen

Priorität 1 (blockiert oder falsch):

1. Quiz U3 Frage 4 und Begründung korrigieren (U3-F01).
2. Index-Demo auf MySQL 8 durchspielen, danach Setup erneut ausführen; Hinweis in Folien und Skriptköpfe (U3-F02); Block 5 umbauen (U3-F03); eigene Laufzeiten in Sprechernotizen der Folien 3, 6, 8 eintragen; Buffer-Pool-Aussage anpassen (U3-F04).
3. Alle SQL-Dateien auf MySQL 8 mit Workbench-Standardeinstellungen laufen lassen (Kontrollwerte U3.1, DELETE mit Safe Updates, information_schema-Ausgabe) (KT2-F06, U3-F26, U3-F27).
4. Entscheid KT2 Nachmittag: fehlende Materialien erstellen (PP7, Mini-Aufgaben Variablen/MwSt, Demo-Drehbuch Kontrollstrukturen, Stdlib-Demo, kombinierte input()-Aufgabe) oder Plan kürzen (KT2-F01).
5. Entscheid KT2 Vormittag: PP6 (mit PA-Platzhaltern), Drehbuch GROUP-BY-Demo, Kurz-Quiz U3, Input DBMS-Architektur (KT2-F02, KT2-F03, U3-F13).
6. Selbststudium U4 korrigieren: Repo-Verweise, Kapitel 6 bis 8 statt 1 bis 5 (U4-F01, U4-F02).

Priorität 2 (Nacharbeit, Verwirrung vermeiden):

7. KT2-Zeitplan an Debriefings anpassen (KT2-F04).
8. PP5 als pptx auf Schulvorlage, B-Tree-Aussage korrigieren (U3-F06, U3-F05).
9. Selbststudium U3: Szenario B um Historisierung ergänzen, Widerspruch «versteckt» vs. Selbstcheck klären (U3-F15, U3-F16).
10. TN-Handouts und Dozentenfassungen trennen, Auftragsfolien als Folien setzen (KT2-F05).
11. U3.1: Zeilenzahlen aufs TN-Blatt, ONLY_FULL_GROUP_BY-Erklärung, Aufgabe 6 gegenüber Buchaufgabe variieren (U3-F08, U3-F09, U3-F17).
12. Check U4: macOS-Fall, Tandem-Regel an Plan koppeln, VS-Code-Details prüfen (U4-F04, U4-F03, U4-F05).
13. Demo-Skript Live-Coding U4 als .py ablegen (U4-F08).
14. Drehbuch U3 Minuten 2, 8, 13 anpassen; kurze Mini-Anwendung Views/EXPLAIN für TN (U3-F12, U3-F11, U3-F07).

Priorität 3 (Kosmetik, Logistik):

15. Tageszeit- und Chat-Reste, Aufgabe-4-Verweis, Quiz-Verweise, Label/Plural in Musterlösungen (U3-F20, U3-F23, U3-F24, U4-F12, U4-F14).
16. Particify-Räume für Quiz U3 und U4 anlegen, QR-Folien (KT2-F09).
17. Druck und Material: Fall-Handout U3.2 (Teil A) für alle, Flipcharts, dicke Stifte, Klebepunkte; A5-Karten mit den Windows-Fixes; Python-Installer auf USB-Stick; HDMI- und USB-C-Adapter.
18. Vorbereitungs-Post im Kurskanal vor KT2: vier Setup-Fragen aus Check U4 als Hausaufgabe, Setup-Sprechstunde 12:30 ankündigen.
