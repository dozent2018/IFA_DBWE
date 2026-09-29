# Inventar 01: Planung, Drive-Struktur, Soll-Ist-Matrix

**Kurs:** DBWE.TA1A, IFA Höhere Fachschule, Präsenzunterricht, Periode S2610
**Stand:** 29.09.2026 (Inventar, keine Änderungen an Quelldateien)
**Bereich:** Planungsdokumente, Google-Drive-Ablage, Abgleich Handoff gegen Unterrichtsplan

**Begriffe in diesem Dokument**

| Kürzel | Bedeutung |
|---|---|
| HO | KI-Handoff v2.0 vom 02.09.2026 (`01_Planung/KI-Handoff_DBWE.TA1A.md`) |
| HO-WP0 bis HO-WP6 | Work Packages des Handoffs, gegliedert nach Units (HO-WP0 = U1-U2, HO-WP1 = U3-U5, HO-WP2 = U6-U7, HO-WP3 = U8-U9, HO-WP4 = U10-U11, HO-WP5 = U12-U13, HO-WP6 = U14-U16) |
| UP | Unterrichtsplan S2610, Stand 18.09.2026 (`18.09.2026/Unterrichtsplan_DBWE_TA1A_S2610.md`) |
| KT1 bis KT6 | Kurstage gemäss UP (im UP selbst "WP 1" bis "WP 6" genannt): KT1 Fr 23.10.2026, KT2 Fr 06.11.2026, KT3 Fr 20.11.2026, KT4 Fr 04.12.2026, KT5 Fr 18.12.2026, KT6 Fr 22.01.2027 |
| VM / NM | Vormittag 08:00-12:00 / Nachmittag 13:00-17:00 eines Kurstags |
| SST | Selbststudiumsauftrag |
| PA | Praxisarbeit (Prüfungsleistung) |
| Projektinhaber / Co-Autor | Owner-Rollen der Drive-Dateien (keine Personennamen) |

Um Verwechslungen zu vermeiden, verwendet dieses Dokument nie "WP" allein, sondern immer "HO-WP" (Handoff) oder "KT" (Kurstag).

---

## 1. Gelesener Umfang

| Datei | Ort | Umfang | Vollständig gelesen | Bemerkung |
|---|---|---|---|---|
| KI-Handoff v2.0, Markdown | lokal `scratchpad/handoff_md.md` (Kopie von Drive `01_Planung/KI-Handoff_DBWE.TA1A.md`) | 988 Zeilen | ja | Alle HO-WP0 bis HO-WP6 inkl. Kontextblöcke, 80 Materialspezifikationen, "Challenge / Prüfung", "Offene Punkte". Lokale Kopie ist nach Entfernen der Markdown-Escapes bytegleich mit der Drive-Datei (110'535 Bytes). |
| KI-Handoff, Google-Doc-Fassung | lokal `scratchpad/handoff_gdoc.md`, zusätzlich Drive-Abruf mit Kommentaren | 775 Zeilen | ja | Abruf mit `includeComments=true` liefert identischen Text, **keine Kommentare**. Wortweiser Vergleich mit der Markdown-Fassung siehe Abschnitt 4.2. |
| Unterrichtsplan S2610 | Drive `18.09.2026/Unterrichtsplan_DBWE_TA1A_S2610.md` | 35'149 Bytes, 8 Kapitel | ja | Alle 6 Kurstage mit Ablauftabellen, PP1-PP15-Outlines, Querschnitts-Checkliste. |
| WP1-Übersicht Units 3-5 | Drive `WP1_Uebersicht_Units_3-5.md` | 14'896 Bytes | ja | Inkl. Code-Artefakte, Annahmen, gelöschte Dateien, Fristen. |
| WP2-Übersicht Units 6-7 | Drive `WP2_Uebersicht_Units_6-7.md` | 8'233 Bytes | ja | Nicht zugewiesen, aber für den Ist-Status von U6/U7 nötig und deshalb vollständig gelesen. |
| Drive-Metadaten | Wurzelordner "IFA-DB&SE" rekursiv | 13 Ordner, 47 Dateien | ja | Alle Ordner mit `parentId`-Abfrage und Paginierung bis leer abgefragt; Kontrollsuchen nach fehlenden Dateien (Titel "remote-archiv", "beispiele", "Unterrichtsplan", "U7", "bank2c", "DBWE", Volltext "DBWE.TA1A"). Rohliste mit Drive-IDs: `scratchpad/drive/drive_tree.tsv` (nicht im Repo). |
| Repo-Struktur | `/home/user/IFA_DBWE` (SQL, Python, Flask, microblog) | Verzeichnislisten | ja (nur Struktur) | Nur geprüft, ob im Handoff referenzierte Repo-Pfade existieren. |
| PP1-PP4 (.pptx) | Drive `18.09.2026/` | 4 Dateien | nein | Nur Metadaten (Existenz, Grösse, Datum). Inhalt gehört nicht zu diesem Inventarteil. |
| Materialien in `02_Materialien` und `04_Selbststudium` | Drive | 38 Dateien | nein | Nur Metadaten. Inhaltsprüfung gehört zu den materialbezogenen Inventarteilen. |

---

## 2. Drive-Struktur

### 2.1 Baum komplett

Wurzel: Ordner "IFA-DB&SE" in "Meine Ablage" des Projektinhabers. Zeiten in UTC (Schweizer Ortszeit = UTC + 2 h). Grössen in Bytes. Bei Google-Docs ist die Grösse die von Drive gemeldete Speichergrösse.

| Pfad | Typ | Grösse | Erstellt | Geändert | Owner-Rolle |
|---|---|---|---|---|---|
| `IFA-DB&SE/` | Ordner | | 10.09. 11:45 | 10.09. 11:48 | Projektinhaber |
| `01_Planung/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `01_Planung/KI-Handoff_DBWE.TA1A.md` | Markdown | 110'535 | 10.09. 12:52 | 10.09. 12:52 | Projektinhaber |
| `01_Planung/KI-Handoff_DBWE.TA1A.md` (gleicher Titel) | Google Doc | 45'629 | 18.09. 07:29 | 18.09. 07:29 | Co-Autor |
| `02_Materialien/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `02_Materialien/Unit_3_SQL_Funktionen_Views_DBMS/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/Quiz_U3_3NF-JOIN-Check.md` | Markdown | 6'103 | 10.09. 11:53 | 10.09. 11:53 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/Demo-Drehbuch_U3_Views-Introspektion.md` | Markdown | 6'269 | 10.09. 11:54 | 10.09. 11:54 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/Gruppenuebung_U3.2_Systemarchitektur.md` | Markdown | 10'404 | 10.09. 12:23 | 10.09. 12:23 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/Kurzfolien_U3_Indexierung-Caching.md` | Markdown | 9'044 | 10.09. 12:24 | 10.09. 12:24 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/Partneruebung_U3.1_GROUP-BY.md` | Markdown | 7'513 | 10.09. 12:24 | 10.09. 12:24 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/code/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/code/demo_u3_views.sql` | SQL | 2'448 | 10.09. 12:25 | 10.09. 12:25 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/code/index_demo_ablauf.sql` | SQL | 4'851 | 10.09. 12:25 | 10.09. 12:25 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/code/index_demo_setup.sql` | SQL | 1'935 | 10.09. 12:25 | 10.09. 12:25 | Projektinhaber |
| `.../Unit_3_SQL_Funktionen_Views_DBMS/code/loesung_u3_1.sql` | SQL | 4'849 | 10.09. 12:25 | 10.09. 12:25 | Projektinhaber |
| `02_Materialien/Unit_4_Start_Python/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_4_Start_Python/Check_U4_Setup-Check.md` | Markdown | 9'464 | 10.09. 12:27 | 10.09. 12:27 | Projektinhaber |
| `.../Unit_4_Start_Python/Live-Coding-Drehbuch_U4.md` | Markdown | 10'873 | 10.09. 12:27 | 10.09. 12:27 | Projektinhaber |
| `.../Unit_4_Start_Python/Partneruebung_U4.1_Kontrollstrukturen.md` | Markdown | 9'813 | 10.09. 12:28 | 10.09. 12:28 | Projektinhaber |
| `.../Unit_4_Start_Python/Quiz_U4_Python-Grundlagen.md` | Markdown | 7'264 | 10.09. 12:29 | 10.09. 12:29 | Projektinhaber |
| `.../Unit_4_Start_Python/code/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_4_Start_Python/code/loesung_u4_1a_preisstaffel.py` | Python | 1'690 | 10.09. 12:29 | 10.09. 12:29 | Projektinhaber |
| `.../Unit_4_Start_Python/code/loesung_u4_1b_spesen.py` | Python | 1'898 | 10.09. 12:29 | 10.09. 12:29 | Projektinhaber |
| `.../Unit_4_Start_Python/code/loesung_u4_1c_zahlenraten.py` | Python | 2'073 | 10.09. 12:29 | 10.09. 12:29 | Projektinhaber |
| `.../Unit_4_Start_Python/code/loesung_u4_1d_jasszaehler.py` | Python | 1'865 | 10.09. 12:29 | 10.09. 12:29 | Projektinhaber |
| `02_Materialien/Unit_5_Datenstrukturen_Python/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/Coaching-Leitfaden_U5_Review-Datenmodelle.md` | Markdown | 16'518 | 10.09. 12:31 | 10.09. 12:31 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/Partneruebung_U5.1_Sequenztypen.md` | Markdown | 8'717 | 10.09. 12:31 | 10.09. 12:31 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/Partneruebung_U5.2_Dictionaries.md` | Markdown | 9'444 | 10.09. 12:32 | 10.09. 12:32 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/Quiz_U5_Datenstrukturen.md` | Markdown | 8'142 | 10.09. 12:33 | 10.09. 12:33 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/code/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/code/loesung_u5_1_sequenztypen.py` | Python | 4'982 | 10.09. 12:33 | 10.09. 12:33 | Projektinhaber |
| `.../Unit_5_Datenstrukturen_Python/code/loesung_u5_2_dictionaries.py` | Python | 5'561 | 10.09. 12:33 | 10.09. 12:33 | Projektinhaber |
| `02_Materialien/Unit_6_Funktionen_Module_Persistenz/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/Live-Demo-Drehbuch_U6_Datenbankzugriff.md` | Markdown | 16'931 | 10.09. 12:35 | 10.09. 12:35 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/Partneruebung_U6.1_Funktionen-entwerfen.md` | Markdown | 10'232 | 10.09. 12:36 | 10.09. 12:36 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/Partneruebung_U6.2_Dateien-Kontextmanager.md` | Markdown | 11'280 | 10.09. 12:36 | 10.09. 12:36 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/Quiz_U6_Module-Persistenz.md` | Markdown | 9'268 | 10.09. 12:37 | 10.09. 12:37 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/Adressen.csv` | CSV | 1'156 | 10.09. 12:37 | 10.09. 12:37 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/config_beispiel.py` | Python | 921 | 10.09. 12:37 | 10.09. 12:37 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/demo_u6_mysql.py` | Python | 6'123 | 10.09. 12:38 | 10.09. 12:38 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/demo_u6_sqlite.py` | Python | 6'176 | 10.09. 12:38 | 10.09. 12:38 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/loesung_u6_1_spesen_refactored.py` | Python | 7'093 | 10.09. 12:38 | 10.09. 12:38 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/loesung_u6_2_csv.py` | Python | 8'492 | 10.09. 12:39 | 10.09. 12:39 | Projektinhaber |
| `.../Unit_6_Funktionen_Module_Persistenz/code/spesen_monolith.py` | Python | 3'709 | 10.09. 12:39 | 10.09. 12:39 | Projektinhaber |
| `04_Selbststudium/` | Ordner | | 10.09. 11:49 | 10.09. 11:49 | Projektinhaber |
| `04_Selbststudium/Selbststudium_U3_Eigenes-Datenmodell.md` | Markdown | 10'364 | 10.09. 12:43 | 10.09. 12:43 | Projektinhaber |
| `04_Selbststudium/Selbststudium_U4_PYGR_Kap1-5.md` | Markdown | 6'611 | 10.09. 12:43 | 10.09. 12:43 | Projektinhaber |
| `04_Selbststudium/Selbststudium_U5_PYGR_Kap9-13.md` | Markdown | 6'755 | 10.09. 12:44 | 10.09. 12:44 | Projektinhaber |
| `04_Selbststudium/Selbststudium_U6_Programm-mit-Persistenz.md` | Markdown | 10'101 | 10.09. 12:44 | 10.09. 12:44 | Projektinhaber |
| `18.09.2026/` | Ordner | | 18.09. 09:15 | 18.09. 09:15 | Co-Autor |
| `18.09.2026/Unterrichtsplan_DBWE_TA1A_S2610.md` | Markdown | 35'149 | 18.09. 09:16 | 18.09. 09:12 (lokal vor Upload) | Co-Autor |
| `18.09.2026/PP1_U1_Kickoff_Kursueberblick.pptx` | PowerPoint | 362'696 | 18.09. 16:39 | 18.09. 16:39 | Co-Autor |
| `18.09.2026/PP2_U1_Grundbegriffe_Relationales-Modell.pptx` | PowerPoint | 271'367 | 18.09. 16:39 | 18.09. 16:39 | Co-Autor |
| `18.09.2026/PP3_U2_Anomalien_Normalisierung.pptx` | PowerPoint | 405'881 | 18.09. 16:39 | 18.09. 16:39 | Co-Autor |
| `18.09.2026/PP4_U2_Schluessel_ERD_JOIN.pptx` | PowerPoint | 373'809 | 18.09. 16:39 | 18.09. 16:39 | Co-Autor |
| `WP1_Uebersicht_Units_3-5.md` | Markdown | 14'896 | 10.09. 11:51 | 10.09. 11:51 | Projektinhaber |
| `WP2_Uebersicht_Units_6-7.md` | Markdown | 8'233 | 10.09. 11:52 | 10.09. 11:52 | Projektinhaber |

Summe: 13 Ordner (inkl. Wurzel), 47 Dateien, rund 1.9 MB. Alle Materialdateien sind Uploads vom 10.09.2026 (Stand der Inhalte laut WP1-/WP2-Übersicht: 02.09.2026). Seit dem 18.09.2026 gab es keine Änderung mehr im Drive.

### 2.2 Auffälligkeiten der Struktur

1. **Nummernlücke 03_:** Es gibt `01_Planung`, `02_Materialien`, `04_Selbststudium`, aber kein `03_...`. Vermutlich war ein Ordner für Prüfung/Praxisarbeit vorgesehen (Annahme); die PA-Unterlagen fehlen ohnehin (siehe Abschnitt 5).
2. **Datumsordner ausserhalb des Schemas:** `18.09.2026/` enthält den Unterrichtsplan (gehört nach `01_Planung`) und PP1-PP4 (gehören zu den Materialien von U1/U2 bzw. KT1).
3. **Übersichten im Wurzelordner:** `WP1_Uebersicht_Units_3-5.md` und `WP2_Uebersicht_Units_6-7.md` liegen im Wurzelordner statt in `01_Planung`.
4. **Doppelter Titel:** In `01_Planung` liegen zwei Dateien namens `KI-Handoff_DBWE.TA1A.md` (eine echte Markdown-Datei, ein Google Doc). Welche massgebend ist, ist nicht gekennzeichnet; das Google Doc ist verlustbehaftet konvertiert (Abschnitt 4.2).
5. **Unit-Ordner nur für U3-U6:** Es fehlen `Unit_1`, `Unit_2`, `Unit_7` bis `Unit_16`. Die Ordnerlogik folgt den 16 Fachplan-Units, der UP dagegen 6 Kurstagen. Materialien, die im UP pro Halbtag gebündelt sind (z. B. KT3-NM = U6/U7), müssten auf zwei Unit-Ordner verteilt werden.
6. **v1-Reste:** Keine Dateien mit "Breakout", "Poll" oder "schema_handel" gefunden; die in WP1/WP2-Übersicht dokumentierten Löschungen sind vollständig.

### 2.3 In Dokumenten referenziert, im Drive aber nicht vorhanden

| Referenzierte Datei | Referenziert in | Befund |
|---|---|---|
| `01_Planung/KI-Handoff_DBWE.TA1A_v1-remote-archiv.md` | HO Kopfzeile (lokale Kopie Z. 4); WP1-Übersicht Kopf "Ersetzt" | fehlt |
| `01_Planung/Unterrichtsplan_DBWE.TA1A.docx` (Remote-Fassung) | HO Kopfzeile und "Offene Punkte"; WP1-Übersicht "Was noch offen ist" | fehlt; faktisch ersetzt durch `Unterrichtsplan_DBWE_TA1A_S2610.md`, aber nirgends so vermerkt |
| `02_Materialien/Unit_6_.../code/beispiele.sqlite` | WP1-Übersicht "Verifikationsmethode" und Annahme 2; WP2-Übersicht "Code-Artefakte" und "Repo-Einbindung" | fehlt; SQLite-Fallback der Demo U6 und Nachprüfung der Kontrollwerte U3.1 dadurch nicht möglich |
| `02_Materialien/Unit_7_.../` mit `Kurzaufgabe_U7.0_Code-Review-bank2c.md`, `Partneruebung_U7.1_Eigene-Klassen.md`, `Partneruebung_U7.2_Vererbung-Sichtbarkeit.md`, `Kurzfolien_U7_Best-Practices-Patterns.md`, `Quiz_U7_OOP-Begriffe.md` | WP2-Übersicht Tabelle "Unit 7" | ganzer Ordner fehlt |
| `Unit_7/code/bank2c.py`, `bank2c_korrigiert.py`, `loesung_u7_1_kurs.py`, `u7_2_ausgangscode.py`, `loesung_u7_2.py`, `patterns_beispiele.py` | WP2-Übersicht "Code-Artefakte" | fehlen |
| `04_Selbststudium/Selbststudium_U7_Klassen-Uebungen.md` | WP2-Übersicht Tabelle "Unit 7" | fehlt |
| Foliensätze "Folien SQL", "Folien Python", "Folien Flask" | HO "Bereits vorhandene Materialien" ("laut Fachplan vorhanden, vom Dozenten bereitzustellen"); WP1-Übersicht "Foliensätze" | nicht im Drive; Verhältnis zu PP1-PP15 ungeklärt |
| PA-Aufgabenstellung und Bewertungsraster | HO "Challenge / Prüfung"; UP 1.5 und Checkliste; WP1/WP2-Übersicht | nicht im Drive ("zentral bereitgestellt", lag nie vor) |
| Repo `Python/kap-2`, `kap-3`, `kap-4` | HO SST U4 ("Vergleich mit Musterlösungen Repo `Python/kap-1` bis `kap-5`") | im Repo nicht vorhanden (vorhanden: kap-1, kap-5 bis kap-19) |
| Repo `microblog/` | Repo-Wurzel | leeres Verzeichnis: Gitlink ohne `.gitmodules`, Inhalt nicht auflösbar |

---

## 3. Soll-Ist-Matrix

### 3.1 Legende

- **KT (UP):** Kurstag und Zeitfenster laut Ablauftabelle im UP; "nach KTx" = Selbststudium im Intervall danach.
- **Im UP vorgesehen?** ja = im Ablauf enthalten (ggf. mit Anpassung); verdichtet = gekürzt oder mit anderem Material zusammengelegt; verschoben = ins Selbststudium oder an einen anderen Zeitpunkt verlegt; entfällt = im UP ersatzlos oder durch eine andere Form ersetzt. Begründung jeweils aus dem UP.
- **Ist-Status Drive:** vorhanden = Datei existiert (Inhalt in diesem Teil nicht geprüft); fehlt = keine Datei.

### 3.2 Handoff-Materialien (80 Spezifikationen)

**HO-WP0: U1-U2, alle an KT1 (23.10.2026)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 1 | U1 | Vorbereitungs-Mail + Installationsanleitung | Mail-Vorlage + Anleitung | ca. 60 min Einzelarbeit, vor U1 | vor KT1, Versand bis Fr 16.10.2026 | ja (UP 1.5 und Checkliste) | fehlt |
| 2 | U1 | Setup-Sprechstunde U1: Triage-Leitfaden | Leitfaden Dozierende | 30 min vor U1 | KT1 07:30-08:00 | ja (HO-Türschild "ab 17:30" passt nicht, UP 07:30) | fehlt |
| 3 | U1 | Kickoff-Folien U1: Kursüberblick und Lernweg | Foliensatz (Outline md) | 20 min Plenum | KT1 08:00-08:25 (PP1, inkl. Vorstellungsrunde) | ja, als PP1 (6 Kurstage statt "16 Units in 3 Teilen") | vorhanden als `18.09.2026/PP1_U1_Kickoff_Kursueberblick.pptx` (pptx statt md-Outline, falscher Ordner) |
| 4 | U1 | Check U1: Setup- und Vorwissens-Check | Handzeichen + Particify | 10 min Plenum | KT1 08:25-08:35 | ja | fehlt |
| 5 | U1 | Gruppenübung U1.1: Relationales Modell, passt es? | Fallarbeit | 25 min, Gruppen à 3 | KT1 08:55-09:20 | ja (+ Galeriegang) | fehlt |
| 6 | U1 | Live-Demo-Drehbuch U1: Workbench und SQL-Grundoperationen | Demo-Drehbuch + .sql | 25 min Plenum | KT1 09:35-10:00 | ja | fehlt |
| 7 | U1 | Partnerübung U1.2: SQL-Grundoperationen | Übungsblatt | 30 min Partner | KT1 10:00-10:30 und 10:45-11:15 | ja, erweitert auf 60 min inkl. Besprechung | fehlt |
| 8 | U1 | Quiz U1: Begriffe und Grundoperationen | Quiz | 15 min Plenum | KT1 11:15-11:30 | ja | fehlt |
| 9 | U1 | SST U1: Übungen DBSQL Kap. 3, Kap. 4 lesen | SST | 225 min | nach KT1 | verdichtet: zwischen U1 und U2 liegt nur die Mittagspause; mit SST U2 zusammenlegen | fehlt |
| 10 | U2 | Quiz U2: Check-in SQL-Grundoperationen | Quiz | 10 min Plenum | KT1 13:00-13:10 | ja, Zweck geändert ("vom Vormittag" statt Selbststudiumskontrolle) | fehlt |
| 11 | U2 | Partnerübung U2.1: Normalisieren bis 3NF | Übungsblatt | 30 min Partner | KT1 13:30-14:00 | ja | fehlt |
| 12 | U2 | Partnerübung U2.2: ERD aus «beispiele» | Übungsblatt | 25 min Partner, A3 | KT1 14:35-15:00 | ja | fehlt |
| 13 | U2 | Partnerübung U2.3: JOIN und UNION auf «beispiele» | Übungsblatt | 30 min Partner | KT1 15:20-15:50 (+ Besprechung 16:05-16:30) | ja | fehlt |
| 14 | U2 | Quiz U2: Schlüssel, JOIN und UNION | Quiz | 15 min Plenum | KT1 16:30-16:45 | ja | fehlt |
| 15 | U2 | Zusatzauftrag U2: Eigenes Mini-Datenmodell | Differenzierung | 20-30 min flexibel | KT1 16:45 (Ausblick) | ja | fehlt |
| 16 | U2 | SST U2: Übungen Kap. 4-5, Kap. 6-7 lesen | SST | 225 min | nach KT1 | ja (zusammen mit SST U1: 450 min in 2 Wochen) | fehlt |

**HO-WP1: U3-U4 an KT2 (06.11.2026), U5 an KT3-VM (20.11.2026)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 17 | U3 | Quiz U3: 3NF- & JOIN-Check | Quiz | 10 min Plenum | KT2 08:00-08:10 | ja | vorhanden: `Unit_3_.../Quiz_U3_3NF-JOIN-Check.md` |
| 18 | U3 | Partnerübung U3.1: GROUP BY auf «beispiele» | Übungsblatt | 30 min Partner | KT2 08:50-09:20 | ja (UP ergänzt Demo GROUP BY 08:30-08:50) | vorhanden: `Partneruebung_U3.1_GROUP-BY.md` + `code/loesung_u3_1.sql` |
| 19 | U3 | Demo-Drehbuch U3: Views und Schema-Introspektion | Demo-Drehbuch + .sql | 15 min Plenum | KT2 09:35-09:50 | ja | vorhanden: `Demo-Drehbuch_U3_Views-Introspektion.md` + `code/demo_u3_views.sql` |
| 20 | U3 | Gruppenübung U3.2: Qualitätsanforderungen zur Systemarchitektur | Fallstudie | 30 min, Gruppen à 3 | KT2 09:50-10:20 | ja | vorhanden: `Gruppenuebung_U3.2_Systemarchitektur.md` |
| 21 | U3 | Kurzfolien U3: Indexierung und Caching | Foliensatz (Outline md) | 20 min Plenum | KT2 10:35-10:55 (PP5) | ja, als PP5 (UP-Outline 6-8 Folien, 15 min + Demo) | vorhanden als md-Outline `Kurzfolien_U3_Indexierung-Caching.md` + `code/index_demo_setup.sql`, `index_demo_ablauf.sql`; PP5 als pptx fehlt |
| 22 | U3 | SST U3: Eigenes Datenmodell ableiten | SST | 90 min | nach KT2 | ja (Abgabe vor KT3) | vorhanden: `04_Selbststudium/Selbststudium_U3_Eigenes-Datenmodell.md` |
| 23 | U4 | Check U4: Setup-Check Python & VS Code | Handzeichen + Triage | 10 min Plenum | KT2 13:00-13:10 | ja (Sprechstunde "30 min vor Unit 4" fällt in die Mittagspause) | vorhanden: `Unit_4_Start_Python/Check_U4_Setup-Check.md` |
| 24 | U4 | Live-Coding-Drehbuch U4 | Demo-Drehbuch | 20 min Plenum | KT2 13:30-13:50 | ja (UP ergänzt zwei weitere Demos) | vorhanden: `Live-Coding-Drehbuch_U4.md` |
| 25 | U4 | Partnerübung U4.1: Kontrollstrukturen if/while | Übungsblatt | 30 min Partner | KT2 14:55-15:30 (35 min) | ja | vorhanden: `Partneruebung_U4.1_Kontrollstrukturen.md` + 4 Lösungsdateien in `code/` |
| 26 | U4 | Quiz U4: Python-Grundlagen | Quiz | 15 min Plenum | KT2 16:30-16:45 | ja | vorhanden: `Quiz_U4_Python-Grundlagen.md` |
| 27 | U4 | SST U4: Übungen PYGR Kap. 1-5 | SST | 90 min | nach KT2 | ja | vorhanden: `04_Selbststudium/Selbststudium_U4_PYGR_Kap1-5.md` |
| 28 | U5 | Partnerübung U5.1: Sequenztypen | Übungsblatt | 30 min Partner | KT3 08:35-09:05 | ja | vorhanden: `Unit_5_.../Partneruebung_U5.1_Sequenztypen.md` + `code/loesung_u5_1_sequenztypen.py` |
| 29 | U5 | Partnerübung U5.2: Dictionaries | Übungsblatt | 25 min Partner | KT3 09:40-10:05 | ja | vorhanden: `Partneruebung_U5.2_Dictionaries.md` + `code/loesung_u5_2_dictionaries.py` |
| 30 | U5 | Quiz U5: Datenstrukturen auswählen | Quiz | 15 min Plenum | KT3 10:20-10:35 | ja | vorhanden: `Quiz_U5_Datenstrukturen.md` |
| 31 | U5 | Coaching-Leitfaden U5: Review Datenmodelle | Leitfaden + Review-Bogen | 35 min, Gruppen à 3 | KT3 10:35-11:10 (+ Debriefing 11:10-11:35) | ja (UP: "Review-Bogen (3 Prüffragen)") | vorhanden: `Coaching-Leitfaden_U5_Review-Datenmodelle.md` |
| 32 | U5 | SST U5: Übungen PYGR Kap. 9-13 | SST | 90 min | nach KT3 | verschoben: "Vorbereitung auf Unit 6" ist zwischen VM und NM nicht möglich; mit SST U6/U7 bündeln | vorhanden: `04_Selbststudium/Selbststudium_U5_PYGR_Kap9-13.md` |

**HO-WP2: U6-U7, beide an KT3-NM (20.11.2026, verdichtet)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 33 | U6 | Partnerübung U6.1: Funktionen entwerfen | Übungsblatt (Refactoring) | 30 min Partner | KT3 13:20-13:50 | ja | vorhanden: `Unit_6_.../Partneruebung_U6.1_Funktionen-entwerfen.md` + `code/spesen_monolith.py`, `loesung_u6_1_spesen_refactored.py` |
| 34 | U6 | Partnerübung U6.2: Dateien und Kontext-Manager | Übungsblatt | 25 min Partner | KT3 13:50-14:15 | ja | vorhanden: `Partneruebung_U6.2_Dateien-Kontextmanager.md` + `code/Adressen.csv`, `loesung_u6_2_csv.py` |
| 35 | U6 | Live-Demo-Drehbuch U6: Datenbankzugriff aus Python | Demo-Drehbuch + .py | 20 min Demo + 15 min Einzelarbeit | KT3 14:30-14:50 | verdichtet: "danach 10 min selbst nachvollziehen" ohne eigenes Zeitfenster | vorhanden: `Live-Demo-Drehbuch_U6_Datenbankzugriff.md` + `code/demo_u6_mysql.py`, `demo_u6_sqlite.py`, `config_beispiel.py`; `beispiele.sqlite` fehlt |
| 36 | U6 | Quiz U6: Module & Persistenz | Quiz | 15 min Plenum | KT3 16:30-16:45 | verdichtet: UP "Quiz OOP-Begriffe und Persistenz" (U6 + U7 in 15 min) | vorhanden: `Quiz_U6_Module-Persistenz.md`; kombiniertes Quiz fehlt |
| 37 | U6 | SST U6: Beispielprogramm mit Persistenz | SST | 90 min | nach KT3 | ja | vorhanden: `04_Selbststudium/Selbststudium_U6_Programm-mit-Persistenz.md` |
| 38 | U7 | Kurzaufgabe U7.0: Code-Review bank2c.py | Analyseaufgabe | 15 min Partner | KT3 14:50-15:05 | ja, aber vor den Klassen-Input vorgezogen ("Einstieg in OOP über Analyse") | fehlt (laut WP2-Übersicht vorhanden, Ordner `Unit_7` existiert nicht) |
| 39 | U7 | Partnerübung U7.1: Eigene Klassen entwerfen | Übungsblatt | 30 min Partner | KT3 15:40-16:10 | ja | fehlt |
| 40 | U7 | Partnerübung U7.2: Vererbung & Sichtbarkeit | Übungsblatt | 25 min Partner | nach KT3 | ins Selbststudium verschoben (UP 4 "Verdichtungshinweis") | fehlt |
| 41 | U7 | Kurzfolien U7: Best Practices und Patterns | Foliensatz (Outline md) | 25 min Plenum, 10-12 Folien | KT3 16:10-16:30 (PP8) | verdichtet: PP8 6-8 Folien, 15-20 min, anderer Zuschnitt | fehlt (weder md noch pptx) |
| 42 | U7 | Quiz U7: OOP-Begriffe | Quiz | 15 min Plenum | KT3 16:30-16:45 | verdichtet (mit Quiz U6 kombiniert) | fehlt |
| 43 | U7 | SST U7: Klassen-Übungen abschliessen | SST | 90 min | nach KT3 | ja, erweitert (Vererbung aus U7.2, venv mit Flask) | fehlt |

**HO-WP3: U8-U9 an KT4 (04.12.2026)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 44 | U8 | Partnerübung U8.1: HTTP-Requests analysieren | Übungsblatt + Analyse-Bogen | 25 min Partner | KT4 08:20-08:40 nur als Demo | entfällt als Übung: DevTools werden vorgeführt, der Übungsslot 08:40-09:05 geht an HTML-Basics | fehlt |
| 45 | U8 | Partnerübung U8.2: Erste Flask-App & Templates | Übungsblatt | 35 min Partner | KT4 09:40-10:15 und 10:50-11:25 | ja, auf zwei Übungen à 35 min aufgeteilt | fehlt |
| 46 | U8 | Quiz U8: HTTP & HTML | Quiz | 10 min Plenum | KT4 11:25-11:45 | ja, Inhalt "HTTP/Flask" | fehlt |
| 47 | U8 | SST U8: microblog-Tutorial Kap. 3 | SST | 90 min | nach KT4 | verschoben: UP-Check-in U9 um 13:00 fragt bereits "Stand Tutorial?" | fehlt |
| 48 | U9 | Partnerübung U9.1: Formulare mit WTForms | Übungsblatt | 30 min Partner | KT4 13:35-14:10 (35 min) | ja | fehlt |
| 49 | U9 | Partnerübung U9.2: ORM-Mapping mit SQLAlchemy | Übungsblatt | 30 min Partner | KT4 14:50-15:30 (40 min) | ja, erweitert (Anzeige im Template) | fehlt |
| 50 | U9 | Quiz U9: Request-Lebenszyklus | Quiz + Sortier-Kärtchen | 15 min Plenum | KT4 16:35-16:50 | verdichtet/umgewidmet: UP "Quiz Forms/ORM"; der Request-Muster-Input fehlt im UP | fehlt |
| 51 | U9 | SST U9: microblog vervollständigen | SST | 90 min | nach KT4 | ja, erweitert (FLASK Kap. 6-8, PA-App-Entwurf) | fehlt |

**HO-WP4: U10-U11 an KT5-VM (18.12.2026, verdichtet)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 52 | U10 | Partnerübung U10.1: Login & Sessions mit flask-login | Übungsblatt + Starter-Code | 30 min Partner | KT5 08:35-09:15 (40 min) | ja ("Starter-Code wird gestellt") | fehlt |
| 53 | U10 | Übungsauftrag U10.2: Gravatar einbinden | Übungsblatt | 20 min Einzel | KT5 09:50-10:10 nur als Demo | verdichtet: nur Demo, keine TN-Übung | fehlt |
| 54 | U10 | Transferauftrag U10: Entwurf eigene App | Transferauftrag PA | 30 min Start im Unterricht + SST | Ausgabe KT4 16:50 | verschoben: Ausgabe am KT4, Bearbeitung nur im Selbststudium | fehlt |
| 55 | U10 | Quiz U10: Security-Grundbegriffe | Quiz | 10 min Plenum | (kein Slot) | entfällt: Check-in KT5 fragt nur Tutorial-Stand ab | fehlt |
| 56 | U10 | SST U10: microblog bis Kap. 8 | SST | 90 min | vor KT5 | verdichtet: UP setzt "FLASK Kap. 6-13 über zwei Selbststudiumsblöcke" voraus | fehlt |
| 57 | U11 | Debug-Challenge U11: Fehler finden | präpariertes Projekt | 30 min Partner | KT5 09:50-10:10 nur als Demo | entfällt als Übung (Debug/Logging nur Demo) | fehlt |
| 58 | U11 | Partnerübung U11.1: Unit-Tests schreiben | Übungsblatt + Starter | 30 min Partner | KT5 10:45-11:15 | ja, reduziert (2 statt 4 Tests, "Vorlage gestellt") | fehlt |
| 59 | U11 | Peer-Review U11: Entwürfe Praxisarbeit | Bogen + Ablauf | 30 min, Gruppen à 3 | KT5 11:15-11:45 als COACH | entfällt: ersetzt durch Security-Checkliste und Kurzberatung pro Tisch | fehlt |
| 60 | U11 | SST U11: microblog Kap. 10, eigene App starten | SST | 90 min | nach KT5 | verdichtet in den 5-Wochen-Fahrplan | fehlt |

**HO-WP5: U12-U13 an KT5-NM (18.12.2026, verdichtet)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 61 | U12 | Git-Kata U12: Versionierung im Team | angeleitete Kata | 30 min, Gruppen à 3 | KT5 13:20-13:50 | entfällt: ersetzt durch "Eigene App unter Git, erster Push" | fehlt |
| 62 | U12 | Partnerübung U12.1: Frontend-Facelift | Übungsblatt | 30 min Partner | KT5 13:50-14:10 nur als Demo | entfällt als Übung | fehlt |
| 63 | U12 | Quiz U12: Git-Grundbegriffe | Quiz | 10 min Plenum | (kein Slot) | entfällt | fehlt |
| 64 | U12 | SST U12: Implementierungsplan Praxisarbeit | SST + Plan-Vorlage | 90 min | KT5 16:00-16:30 | in den Unterricht vorgezogen (COACH + Peer-Check) | fehlt |
| 65 | U13 | Entscheidungsmatrix U13: Deployment-Varianten | Fallarbeit + A3-Matrix | 30 min, Gruppen à 3 | KT5 14:25-14:45 nur PP13 | entfällt: nur Input, K4-Beurteilung wird nicht geübt | fehlt |
| 66 | U13 | Live-Demo-Drehbuch U13: Deployment mit HTTPS | Demo-Drehbuch + Konfigurationen | 25 min Demo + 20 min Nachvollziehen | KT5 14:45-15:15 und 15:30-16:00 | ja | fehlt |
| 67 | U13 | Quiz U13: Deployment & HTTPS | Quiz | 10 min Plenum | (kein Slot) | entfällt | fehlt |
| 68 | U13 | SST U13: Deployment auf ifalabs.org | SST | 90 min | nach KT5 | verdichtet in den 5-Wochen-Fahrplan | fehlt |

**HO-WP6: U14-U15 an KT6-VM, U16 an KT6-NM (22.01.2027)**

| Nr | Unit | Material (HO-Titel) | Typ | Min. / Sozialform (HO) | KT (UP) | Im UP vorgesehen? | Ist-Status Drive |
|---|---|---|---|---|---|---|---|
| 69 | U14 | Partnerübung U14.1: REST-API entwerfen | Design-Übung, A3 | 30 min Partner | (kein Slot) | entfällt (keine Design-Übung im UP) | fehlt |
| 70 | U14 | Partnerübung U14.2: GET-Routen implementieren | Übungsblatt + Starter | 30 min Partner | KT6 08:55-09:30 (35 min) | ja, umgestellt auf die eigene App (kein Starter aus `Flask/kap-14`) | fehlt |
| 71 | U14 | SST U14: API für eigene App planen | SST | 90 min | vor KT6 | verschoben in die 5-Wochen-Phase (U14 und U15 am selben Vormittag) | fehlt |
| 72 | U15 | Partnerübung U15.1: POST/PUT-Routen | Übungsblatt + Starter | 30 min Partner | KT6 10:05-10:35 | verdichtet: mit U15.2 zu "1 schreibender Endpunkt + Auth" | fehlt |
| 73 | U15 | Partnerübung U15.2: HTTP-Authentisierung | Übungsblatt | 25 min Partner | KT6 10:05-10:35 | verdichtet (siehe Nr. 72) | fehlt |
| 74 | U15 | Auftrag U15: Architekturdokumentation | Transferauftrag PA | 20 min Einführung | KT6 13:00 (PP15) | verschoben: keine Ausgabe vor KT6, Präsentation am selben Tag | fehlt |
| 75 | U15 | SST U15: API entwerfen und implementieren | SST | 135 min | nach KT6 (PA-Phase) | verschoben in die PA-Phase | fehlt |
| 76 | U16 | Kurzfolien U16: Architekturdoku mit UML | Foliensatz (Outline md) | 20 min Plenum | KT6 13:00-13:20 (PP15) | ja, als PP15 (erweitert um PA-Doku-Anforderungen und Fahrplan) | fehlt |
| 77 | U16 | Übung U16.1: System-Entwurf mit UML | Übungsblatt | 30 min Einzel + 20 min Peer | KT6 13:20-14:10 | ja | fehlt |
| 78 | U16 | Handout U16: Beispiel Architekturdokumentation | Handout | 45 min Lektüre | vor KT6 | im UP nicht erwähnt (Annahme: weiterhin nötig als Qualitätsmassstab) | fehlt |
| 79 | U14-U16 | Peer-Feedback-Raster PA | Raster + Moderationsanleitung | in 4 min ausfüllbar | KT6 10:50-11:45 und 14:25-16:25 | ja (UP-Checkliste: drucken) | fehlt |
| 80 | U16 | SST U16: Praxisarbeit fertigstellen | SST Abschluss | 135 min + 30 Lektionen PA | KT6 16:25-16:45 + 2 Wochen | ja | fehlt |

### 3.3 Zusätzliche Materialien, die der UP verlangt und der Handoff nicht spezifiziert

Grundlage: jede UP-Zeile mit [PP], [DEMO] (laut Legende mit "Stopp-Marken", also Drehbuch nötig), neuer Übung oder neuem Dokument ohne passende ####-Spezifikation im HO.

| Nr | KT | Zeitfenster (UP) | Material | Herkunft im UP | Ist-Status Drive |
|---|---|---|---|---|---|
| Z01 | KT1 | 08:35-08:55 | PP2 Datenbank-Grundbegriffe und relationales Modell | PP-Outline KT1 | vorhanden: `18.09.2026/PP2_U1_Grundbegriffe_Relationales-Modell.pptx` |
| Z02 | KT1 | 13:10-13:30 | PP3 Anomalien und Normalisierung | PP-Outline KT1 | vorhanden: `18.09.2026/PP3_U2_Anomalien_Normalisierung.pptx` |
| Z03 | KT1 | 14:00-14:20, 15:00-15:20 | PP4 PK/FK, ERD und JOIN | PP-Outline KT1 | vorhanden: `18.09.2026/PP4_U2_Schluessel_ERD_JOIN.pptx` |
| Z04 | KT1 | 14:00-14:20, 15:00-15:20 | Demo-Drehbuch "beispiele einrichten + JOIN/UNION" inkl. TN-Kurzanleitung Import `create_beispiele.sql` | Ablauf NM [DEMO] | fehlt |
| Z05 | KT2 | 08:30-08:50 | Demo-Drehbuch Aggregatfunktionen, GROUP BY, HAVING (Referenz `kap-5.sql`) | Ablauf VM [DEMO] | fehlt |
| Z06 | KT2 | 10:35-10:55 | PP5 als Foliensatz (aus Kurzfolien U3) | PP-Outline KT2 ("bereits vorhanden als Kurzfolien U3") | fehlt (nur md-Outline) |
| Z07 | KT2 | 10:55-11:25 | PP6 Einführung Praxisarbeit | PP-Outline KT2 | fehlt |
| Z08 | KT2 | 11:25-11:45 | Kurz-Quiz Sicherung U3 | Ablauf VM [QUIZ] | fehlt |
| Z09 | vor KT2 | | TN-Anleitung Python 3 + VS Code installieren (Aufforderung im Kurskanal) | WP1-Übersicht "Abhängigkeiten", UP-Setup-Check 13:00 | fehlt (Triage-Teil für Dozierende steckt in Check U4) |
| Z10 | KT2 | 13:10-13:30 | PP7 Warum Python? | PP-Outline KT2 | fehlt |
| Z11 | KT2 | 13:50-14:20 | Partnerübung Variablen und Ausdrücke (z. B. MwSt.) | Ablauf NM [PARTNER] | fehlt |
| Z12 | KT2 | 14:35-14:55, 15:45-16:05 | Demo-Drehbuch U4 Teil 2 (Kontrollstrukturen, eingebaute Funktionen, Stdlib) | Ablauf NM [DEMO] | fehlt |
| Z13 | KT2 | 16:05-16:30 | Partnerübung kombinierte Aufgabe (input()-Programm) | Ablauf NM [PARTNER] | fehlt |
| Z14 | KT3 | 08:15-08:35, 09:20-09:40 | Demo-Drehbuch U5 (Sequenztypen, Dictionaries) | Ablauf VM [DEMO] | fehlt |
| Z15 | KT3 | 13:00-13:20, 15:05-15:25 | Demo-Drehbuch U6/U7 (Funktionen und Modul-Import; Klassen, Konstruktor, self, Auflösung bank2c-Bug) | Ablauf NM [DEMO] | fehlt |
| Z16 | KT3 | 16:30-16:45 | Kombiniertes Quiz "OOP-Begriffe und Persistenz" | Ablauf NM [QUIZ] | fehlt |
| Z17 | KT3 | 14:30-14:50 | `beispiele.sqlite` (SQLite-Fallback für Demo U6) | WP1/WP2-Übersicht | fehlt |
| Z18 | KT4 | 07:30-08:00 | Setup-Sprechstunde: Triage venv/Flask | Ablauf VM | fehlt |
| Z19 | KT4 | 08:00-08:20 | PP9 Technologiestack Web und HTTP | PP-Outline KT4 | fehlt |
| Z20 | KT4 | 08:20-08:40 | Demo-Drehbuch DevTools + microblog-Zielbild (lab1.ifalabs.org) | Ablauf VM [DEMO] | fehlt |
| Z21 | KT4 | 08:40-09:05 | Partnerübung HTML-Basics (HTML5, semantisch) | Ablauf VM [PARTNER]; HO verlangt Neuerstellung nur im Repo-Abschnitt, ohne ####-Spezifikation | fehlt |
| Z22 | KT4 | 09:20-09:40 | PP10 Serverseitige Frameworks und Flask | PP-Outline KT4 | fehlt |
| Z23 | KT4 | 09:20-09:40, 10:30-10:50 | Demo-Drehbuch Flask minimal, Routing, Jinja2 | Ablauf VM [DEMO] | fehlt |
| Z24 | KT4 | 13:15-13:35, 14:25-14:50 | Demo-Drehbuch WTForms und ORM | Ablauf NM [DEMO] | fehlt |
| Z25 | KT4 | 14:25-14:50, 16:15-16:35 | PP11 ORM und Persistenz-Schicht | PP-Outline KT4 | fehlt |
| Z26 | KT5 | 08:15-08:35 | PP12 Web-Security-Grundlagen | PP-Outline KT5 | fehlt |
| Z27 | KT5 | 09:30-09:50 | Gruppenübung Mini-Threat-Analyse (3 Angriffsszenarien, A3) | Ablauf VM [GRUPPE] | fehlt |
| Z28 | KT5 | 09:50-10:10 | Demo-Drehbuch Gravatar, Debug-Modus, Logging | Ablauf VM [DEMO] | fehlt |
| Z29 | KT5 | 10:25-10:45 | Demo-Drehbuch Unit-Tests (inkl. Testvorlage für die Übung) | Ablauf VM [DEMO] | fehlt |
| Z30 | KT5 | 11:15-11:45 | Security-Checkliste für die PA (Handout) | PP12 Folie 8, Ablauf VM [COACH] | fehlt |
| Z31 | KT5 | 13:00-13:20 | Demo-Drehbuch Git-Essentials | Ablauf NM [DEMO] | fehlt |
| Z32 | KT5 | 13:20-13:50 | Übung "Eigene App unter Git, erster Push" | Ablauf NM [PARTNER] | fehlt |
| Z33 | KT5 | 13:50-14:10 | Demo-Drehbuch Bootstrap-Facelift | Ablauf NM [DEMO] | fehlt |
| Z34 | KT5 | 14:25-14:45 | PP13 Deployment-Varianten | PP-Outline KT5 | fehlt |
| Z35 | KT5 | 15:30-16:00 | Deployment-Checkliste (Walkthrough ohne eigene VM) | Ablauf NM [PARTNER] | fehlt |
| Z36 | KT5 | 16:45-17:00 | Selbststudiums-Fahrplan 5 Wochen (bündelt SST U10 bis U14) | Ablauf NM, Verdichtungshinweis | fehlt |
| Z37 | KT6 | 08:15-08:35 | PP14 REST-APIs | PP-Outline KT6 | fehlt |
| Z38 | KT6 | 08:35-08:55, 09:45-10:05 | Demo-Drehbuch API (GET, POST/PUT, Token-Auth) | Ablauf VM [DEMO] | fehlt |

Nicht als Material gezählt, aber im UP vorausgesetzt: Particify-Räume je Halbtag, Check-in-Abfragen (Kartenabfrage, "Stand nach 5 Wochen"), Kursabschluss-Feedback, Präsentationsreihenfolge (Aushang).

### 3.4 Summen pro Kurstag

"Soll nach UP" = HO-Materialien, die laut UP weiterhin gebraucht werden (ja, verdichtet, verschoben) plus UP-Zusatzmaterialien. Entfallene HO-Materialien sind nicht im Soll.

| KT | Datum | HO-Spezifikationen | davon entfällt | HO noch benötigt | davon vorhanden | UP-Zusatz | davon vorhanden | **Soll nach UP** | **vorhanden** | **fehlt** |
|---|---|---|---|---|---|---|---|---|---|---|
| KT1 | Fr 23.10.2026 | 16 | 0 | 16 | 1 | 4 | 3 | **20** | **4** | **16** |
| KT2 | Fr 06.11.2026 | 11 | 0 | 11 | 11 | 9 | 0 | **20** | **11** | **9** |
| KT3 | Fr 20.11.2026 | 16 | 0 | 16 | 10 | 4 | 0 | **20** | **10** | **10** |
| KT4 | Fr 04.12.2026 | 8 | 1 | 7 | 0 | 8 | 0 | **15** | **0** | **15** |
| KT5 | Fr 18.12.2026 | 17 | 8 | 9 | 0 | 11 | 0 | **20** | **0** | **20** |
| KT6 | Fr 22.01.2027 | 12 | 1 | 11 | 0 | 2 | 0 | **13** | **0** | **13** |
| **Total** | | **80** | **10** | **70** | **22** | **38** | **3** | **108** | **25** | **83** |

Lesart: Für den nächsten Kurstag (KT1, in 24 Tagen) liegen nur die vier Foliensätze PP1-PP4 vor. KT2 ist bis auf die UP-Ergänzungen vollständig. Ab KT4 existiert noch kein einziges Material.

---

## 4. Konflikte und Widersprüche

### 4.1 Handoff, Unterrichtsplan, WP1-/WP2-Übersicht

| ID | Thema | Handoff v2.0 | Unterrichtsplan S2610 | WP1-/WP2-Übersicht | Folge |
|---|---|---|---|---|---|
| K-01 | WP-Nummerierung | "WP 0" bis "WP 6" = Unit-Gruppen | "WP 1" bis "WP 6" = Kurstage; TN-sichtbare Verweise in Folien: PP1 Folie 4 "Details ab WP 2", PP9 Folie 6 "Sessions in WP 5", PP12 Folie 7 "Rückgriff auf WP 3!" | "WP 1" = U3-U5 (verteilt auf UP-WP2 und UP-WP3), "WP 2" = U6-U7 | Gleiche Bezeichnung, andere Bedeutung. "WP 3" heisst im HO Flask (U8-U9), im UP Python-OOP (U5-U7). |
| K-02 | Tagesaufbau und Präsenzzeit | 16 Units à 5 × 45 min = 3'600 min; "Was unverändert bleibt: Unit-Struktur (5×45 min)" | 1.2: "2 Unit-Slots à 5 Lektionen" in 08:00-12:00 und 13:00-17:00. Ablauftabellen: VM 08:00-11:45 mit 2 × 15 min Pause = 195 min netto, NM 13:00-17:00 mit 2 × 15 min Pause = 210 min netto; 405 min pro KT, 2'430 min total | U3-U5 je "5×45" geplant | 5 × 45 min (225) plus Pausen passen nicht in 240 min. Real sind es rund 4.3 bzw. 4.7 Lektionen pro Halbtag, 32.5 % weniger Präsenzzeit als der Handoff annimmt. Die Vormittage enden überall 11:45 (15 min ungeplant). |
| K-03 | Verdichtung 16 Units auf 12 Slots | nicht vorgesehen | 1.2: "Verdichtung liegt in der zweiten Kurshälfte (Units 9-16)". Tatsächlich verdichtet: U6/U7 (KT3), U10/U11 und U12/U13 (KT5), U14/U15 (KT6). U9 ist nicht verdichtet. | "WP 2 und WP 3 laufen parallel" (Units einzeln) | UP-Text falsch; 10 HO-Materialien entfallen, 16 werden verdichtet oder verschoben (Abschnitt 3.2). |
| K-04 | Selbststudiumsumfang | Pflicht "gleicher Umfang wie Unterricht", spezifiziert aber 225 min für U1/U2, 90 min für U3-U14, 135 min für U15/U16: Summe 1'800 min (50 % des Unterrichts) | 1.3: "Selbststudium = gleicher Umfang wie Unterricht" (405-450 min pro KT); zusätzlich verschoben: U7.2, FLASK Kap. 6-13, API-Planung, Implementierung | SST U3, U4, U5 je 90 min | Budget pro KT unklar; KT1 hätte laut HO 450 min, KT2 nur 180 min. |
| K-05 | Selbststudium zwischen Units am selben Tag | SST U1 → "Vorbereitung Unit 2"; Quiz U2 "deckt auf, wer das Selbststudium nicht gemacht hat"; U6 beginnt mit "Übungsbesprechung dict" (aus SST U5); U9 ist "Flipped Classroom" (FLASK Kap. 4-5 vorbereitet); SST U14 → Implementierung in U15 | U1/U2, U3/U4, U5/U6-7, U8/U9, U10-11/U12-13, U14-15/U16 jeweils am selben Tag; nur die Mittagspause liegt dazwischen | "vor Unit 6: überarbeitetes CREATE-Skript nachgereicht" (U5 und U6 am selben Tag); "Setup-Sprechstunde 30 min vor Unitbeginn" für U4 | Sechs HO-Übergänge sind nicht umsetzbar; Quiz- und Check-in-Zwecke laufen ins Leere. |
| K-06 | Beginn Flipped Classroom | U1-Kontext: "Theorie ist ab Unit 2 jeweils vorbereitet"; U9 als "Flipped Classroom" markiert | 1.3: "Flipped Classroom ab WP 4" (KT4); zugleich KT1 11:30 "Erinnerung: Theorie ab jetzt vorbereitet"; KT5 setzt "FLASK Kap. 6-13 über zwei Selbststudiumsblöcke" voraus, die KT4-Ausblick-Zeile weist aber nur "FLASK Kap. 6-8" zu | keine Aussage | Drei verschiedene Startpunkte; zwischen KT4 und KT5 gibt es nur einen Selbststudiumsblock, Kap. 9-13 werden nirgends zugewiesen. |
| K-07 | Sozialformen | Mapping: Partnerübung "beide Laptops, ein gemeinsamer Bildschirm"; Materialien: "Pair Programming an einem Laptop" | Legende [PARTNER]: "ein Laptop, Pair Programming"; ab KT5 "[PARTNER] (jeder am eigenen Projekt, Nachbar hilft)"; KT6 Kernmethoden "[PARTNER] Diagramm in draw.io", Ablauf 13:20 "Einzelarbeit" | "ein Laptop, Driver/Navigator" | Uneinheitlich; ab KT5 ist [PARTNER] faktisch Einzelarbeit mit Nachbarhilfe. Ersetzungen: U8.1 Partner → Demo, U10.2 Einzel → Demo, Debug-Challenge Partner → Demo, Git-Kata Gruppe → Einzel/Partner, U12.1 Partner → Demo, Entscheidungsmatrix Gruppe → Input, U14.1 Partner → entfällt. |
| K-08 | Reihenfolge | U7.0 "nach Input Properties"; "Einführung Funktionen" am Ende von U5; Transferauftrag Entwurf eigene App in U10; Implementierungsplan als SST U12; Auftrag Architekturdoku in U15, Präsentation in U16; Request-Muster am Whiteboard in U9 | U7.0 um 14:50 vor dem Klassen-Input (15:05) als "Einstieg in OOP über Analyse"; Funktionen erst KT3-NM; App-Entwurf als Ausblick KT4; Implementierungsplan im Unterricht KT5; Architekturdoku-Anforderungen erst PP15 am KT6 13:00; Request-Muster ohne Slot | WP2: U7.0 "Analyse (neu in v2)" | K4-Analyse von Klassencode vor jeder Klassen-Einführung; PA-Doku-Anforderungen kommen erst nach der 5-Wochen-Implementierungsphase. |
| K-09 | Lernziele und K-Stufen | U3: 5 LZ, U4: 4, U5: 3, U6: 4 (LZ1 K4), U7: 3, U10: 4, U11: 4, U12: 4, U13: 4, U14: 4, U15: 4 | UP-Lernzielzeilen: U3 ohne LZ3 (K2 DBMS-Schichtenarchitektur); U4 ohne LZ4 (Stdlib); U5 ohne LZ3 (Stdlib-Module); U6 LZ1 als K3 statt K4, ohne LZ2/LZ3 (Module/Pakete entwickeln, pip/venv); U7 ohne LZ3 (Sichtbarkeit), LZ2 (Vererbung) nur im Selbststudium; U10/U11 nur 3 von 8 LZ; U12/U13 nur 4 von 8 (ohne E-Mail-Integration, Linux-Server einrichten, Updates mit Git, Transfer K5); U14/U15 nur 3 von 8 (ohne Integrierbarkeit K4, API-Arten K4) | U3-U5 wie HO | Fachplan-LZ ohne Unterrichtsgelegenheit; mehrere K4-Ziele nur noch als Input (z. B. Deployment-Varianten beurteilen ohne Entscheidungsmatrix). |
| K-10 | Zeiten einzelner Materialien | U1.2 30 min, U4.1 30, U8.2 35, U9.1 30, U9.2 30, U10.1 30, Demo U6 20 + 15, Kurzfolien U3 20 min (8-10 Folien), Kurzfolien U7 25 min, Präsentationen U14 35 + 35, U15 25, U16 2 × 45 min | U1.2 60 min, U4.1 35, U8.2 2 × 35, U9.1 35, U9.2 40, U10.1 40, Demo U6 20 + "10" ohne Slot, PP5 "15 min + Demo, 6-8 Folien" bei 20-min-Slot, PP8 15-20 min, Zwischenpräsentationen 55 min, Schlusspräsentationen 45 + 60 min | U3.1-U5.2 wie HO | HO-Minutenwerte ("die Minutenwerte bleiben", Offene Punkte) gelten nicht mehr. |
| K-11 | PA-Umfang | Zusatzauftrag U2 "3 Tabellen"; SST U3 "min. 4 Tabellen"; Transferauftrag U10 "min. 3-4 Tabellen, realistisch in ~6 Wochen" | PP6 Folie 4 "3-6 Tabellen, realistisch klein"; 5 Wochen + 2 Wochen | WP1: "4 bis 8 Tabellen, CRUD, Login, ca. 6 Wochen" | Fünf verschiedene Umfangsangaben ohne offizielle PA-Vorgabe. |
| K-12 | Setup-Sprechstunden | U1: Türschild "Setup-Hilfe ab 17:30"; vor U8 laut SST U7 und U8 | 1.5 "jeweils 30 min vor Unterrichtsbeginn"; Ablauf nur KT1 und KT4 um 07:30 | WP1: "30 min vor Unitbeginn" für U4 (fällt auf 12:30); WP2: "vor Unit 7 und Unit 8" (U7 beginnt nicht separat) | Zeiten und Termine widersprüchlich, Abend-Uhrzeit aus einer anderen Kursform. |
| K-13 | Fachbezeichnung | "Datenbanken und Web-Entwicklung" | Titelzeile "Datenbanken und Web-Entwicklung", Feld "Fach:" dagegen "IT-Architektur, Datenbank und Web-Entwicklung" | "Datenbanken und Web-Entwicklung" | Offizielle Bezeichnung laut Fachplan V_I-1.0 unklar (Repo-README: "Datenbanken und Webentwicklung"). |
| K-14 | Verweise auf Dokumente | Bezug "Unterrichtsplan_DBWE.TA1A.docx (Units 3-16; ... noch remote formuliert)"; Offene Punkte: "Ablaufraster ... angleichen; die Minutenwerte bleiben"; v1-Archiv referenziert | S2610 ersetzt die docx-Fassung, verweist aber nicht auf den HO und nennt keine Version | WP1: "Unterrichtsplan ... muss noch nachgezogen werden" | Veraltete Bezüge in allen drei Dokumenten; referenzierte Dateien fehlen im Drive (2.3). |
| K-15 | Existenz von Materialien | "Zwei Materialien neu" (U7.0, Setup-Sprechstunde) | KT2: "Für Unit 3 existieren bereits fertige Materialien" (stimmt); KT3: "Für Units 5-7 existieren bereits fertige Materialien" (für U7 falsch) | WP2 listet 6 U7-Materialien + 6 Code-Dateien, WP1/WP2 `beispiele.sqlite` | Planung beruht für KT3-NM auf nicht vorhandenen Dateien. |
| K-16 | Foliensätze und Format | "Folien SQL/Python/Flask" vorhanden (Fachplan); nur Ergänzungen als "Folien-Outline in Markdown" | PP1-PP15 als "PowerPoint-Input" [PP], eigene Outlines; PP1-PP4 als pptx vorhanden | "Grundfoliensätze ... nicht angetastet" | Unklar, ob die Fachplan-Foliensätze noch genutzt werden; Zielformat md oder pptx nicht festgelegt. |
| K-17 | Quizinhalte | Quiz U8 "HTTP & HTML"; Quiz U9 "Request-Lebenszyklus" mit Sortier-Kärtchen; Quiz U10, U12, U13 | Quiz U8 "HTTP/Flask"; Quiz U9 "Forms/ORM"; keine Sicherungsquiz an KT5 | keine Aussage | Handoff-Spezifikation für U8/U9 passt nicht zum UP-Inhalt. |
| K-18 | Repo-Test Flask | "vor Unit 8" durchlaufen | Checkliste "vor WP 4" (= KT4, 04.12.) | keine Aussage | Gleicher Termin, aber zu spät: Starter-Codes für HO-WP3 bis HO-WP6 werden aus dem Repo abgeleitet und müssen vorher getestet sein. |
| K-19 | VMs ifalabs.org | "Klären, ob die VMs ... (Units 13-16) pro TN bereitstehen" | Checkliste "(WP 5-6) pro TN klären"; Live-Deployment und Nachvollziehen bereits KT5 | keine Aussage | Termin ist KT5 (18.12.), Klärung offen. |
| K-20 | Starter-Code-Strategie API | U14.2/U15.1/U15.2 mit Starter-Code aus `Flask/kap-14`, Endstand identisch mit Repo | "2 GET-Endpunkte für die eigene App", "1 schreibenden Endpunkt + Auth ergänzen" (eigenes Projekt) | keine Aussage | HO-Spezifikation und UP-Übungsform schliessen sich aus. |
| K-21 | Kickoff-Umfang | Kickoff 20 min + separate Vorstellungsrunde (1 min pro TN) | 08:00-08:25 PP1 (8-10 Folien) inkl. Vorstellungsrunde; PP1 Folie 3 "6 Kurstage" statt HO "16 Units in 3 Teilen" | keine Aussage | Bei mehr als etwa 5 TN nicht in 25 min machbar. |

### 4.2 Handoff: Markdown-Datei gegen Google-Doc-Fassung

Methode: beide Fassungen von Markdown-Syntax, Escapes und Leerzeichen bereinigt und Wort für Wort verglichen (je 12'282 Wörter).

**Ergebnis:** Inhaltlich identisch, keine redaktionellen Änderungen, keine Kommentare. Die Google-Doc-Fassung (Co-Autor, 18.09.2026) ist eine verlustbehaftete Konvertierung mit fünf sinnverändernden Stellen:

| Stelle (lokale Kopie `handoff_gdoc.md`) | Markdown-Original | Google Doc | Wirkung |
|---|---|---|---|
| Z. 399, Partnerübung U7.1 | Dunder-Methoden `__init__`, `__str__` | fett gesetztes "init", "str" | Methodennamen falsch |
| Z. 438, HO-WP3 Kontext (Repo) | `app/__init__.py` | "app/**init**.py" | falscher Dateiname für alle Flask-Materialien |
| Z. 460, Partnerübung U8.2 | `app/__init__.py` | "app/**init**.py" | wie oben |
| Z. 669, HO-WP6 Kontext (Repo) | `/api/users/<id>`, PUT `/api/users/<id>` | "/api/users/" | Platzhalter `<id>` verschwunden; zusätzlich sichtbare Escape-Zeichen (Backslash-Backticks, `\*\*Endstand\*\*`) |
| Z. 692, Partnerübung U14.2 | `/users/<id>/posts` | "/users//posts" | Route unbrauchbar |

Weitere Unterschiede sind reine Formatierung (Tabellen mit leerer Kopfzeile, Aufzählungszeichen). Wer HO-WP2, HO-WP3 oder HO-WP6 aus dem Google Doc an eine KI weitergibt, erhält falsche Pfade und Routen.

---

## 5. Offene Punkte, Annahmen, externe Abhängigkeiten

### 5.1 Konsolidierte Liste

| Nr | Punkt | Art | Betrifft | Frist | Zuständig |
|---|---|---|---|---|---|
| O-01 | PA-Aufgabenstellung und Bewertungsraster (zentral bereitgestellt) | extern | PP6 (KT2), Transferauftrag (Ausgabe KT4), Implementierungsplan (KT5), Auftrag Architekturdoku, PP15, Peer-Feedback-Raster, SST U16 | anfordern sofort; spätestens 30.10.2026 (Produktion PP6 für KT2); hart 04.12.2026 (App-Entwurf) | Dozent bei Lehrgangsleitung |
| O-02 | Verbindliche Arbeitsannahme PA-Umfang bis zum Eintreffen von O-01 (eine Formulierung für alle Materialien) | Annahme | alle PA-Bausteine | 09.10.2026 | Dozent |
| O-03 | Lehrmittelzugang TN (DBSQL, PYGR, FLASK als PDF/Ebook), Kapitelnummern der Auflage prüfen (WP1 "vor dem Einsatz", Punkt 3) | extern | Vorbereitungs-Mail (Lektüre DBSQL Kap. 1-2), alle SST | 16.10.2026 | Schule / Dozent |
| O-04 | Foliensätze "Folien SQL/Python/Flask" (Fachplan): beschaffen oder bewusst durch PP1-PP15 ersetzen; Zielformat pptx festlegen | offen | PP5-PP15 | 09.10.2026 | Dozent |
| O-05 | Kurskanal: Teams oder Moodle entscheiden, einrichten, TN einschreiben | extern | Vorbereitungs-Mail, alle SST-Abgaben | 16.10.2026 | Schule / Dozent |
| O-06 | Klassengrösse und TN-Liste | extern | Präsentationskapazität KT6, Gruppenbildung, Druckmengen | 16.10.2026 | Schule |
| O-07 | Particify: Account, Räume (Vorschlag: je Halbtag statt je Unit, also 12), QR-Code auf erste Folie | offen | alle Quiz | KT1-Räume bis 20.10.2026, danach jeweils Dienstag vor dem KT | Dozent |
| O-08 | Raumcheck: Beamer HDMI/USB-C, Flipchart, Tischgruppen, Steckdosen BYOD, Gäste-WLAN (Particify, GitHub, ifalabs.org, Gravatar, PyPI, MySQL-Download) | extern | alle KT | 16.10.2026 | Dozent / Hausdienst |
| O-09 | Schul-WLAN: Proxy- oder Zertifikatsprobleme bei `pip install` und DevTools-Analyse | extern | KT3 (pip/venv), KT4 | 13.11.2026 | Dozent / IT |
| O-10 | VMs auf ifalabs.org pro TN, SSH-Zugang, Zertifikate (Let's Encrypt oder vorkonfiguriert) | extern | Demo U13 und Nachvollziehen (KT5), SST U13, PA-Deployment | Klärung bis 30.10.2026; betriebsbereit bis 11.12.2026 | Dozent / ifalabs |
| O-11 | Demo-Instanz lab1.ifalabs.org erreichbar | extern | KT4 (Zielbild, DevTools-Demo) | 27.11.2026 | Dozent / ifalabs |
| O-12 | Repo-Test mit Python 3.12, Flask 3.x, Flask-SQLAlchemy 3.x (`Flask/kap-2`, `kap-3`, `kap-13`, `kap-14`, `kap-15`) | offen | alle Starter-Codes KT4-KT6 | laut HO/UP 04.12.2026; empfohlen 13.11.2026 | Dozent |
| O-13 | MySQL-8-Gegenprobe: `index_demo_*.sql`, `loesung_u3_1.sql` (WP1 Annahmen 2, 3); `demo_u6_mysql.py` (WP2 Offene Punkte) | offen | KT2, KT3 | 30.10.2026 bzw. 13.11.2026 | Dozent |
| O-14 | `beispiele.sqlite` wiederherstellen oder neu portieren | offen | Demo U6 Fallback | 13.11.2026 | Dozent |
| O-15 | Unit-7-Materialien und `Selbststudium_U7` auffinden oder neu erstellen | offen | KT3-NM | 13.11.2026 | Dozent |
| O-16 | TN-Vorleistungen Git: Git installiert, GitHub-Account (HO SST U11) | TN | KT5-NM | Aufforderung im SST nach KT4; Kontrolle 11.12.2026 | TN |
| O-17 | Repo-Hinweise für TN: `microblog/` im Repo leer (Gitlink), für FLASK Kap. 4-12 und Python Kap. 2-4 kein Repo-Code | offen | SST mit "Vergleich mit Repo" | vor KT2 (Python) bzw. KT4 (Flask) | Dozent |
| O-18 | Betreuung in der 5-Wochen-Phase (19.12.2026 bis 21.01.2027, inkl. Weihnachten/Neujahr): Antwortzeiten, Abwesenheiten, Zwischencheck | offen | PA | Ankündigung KT5 | Dozent |
| O-19 | PA-Abgabetermin: Annahme Fr 05.02.2027 (2 Wochen nach KT6) | Annahme | SST U16, Fahrplan | mit O-01 bestätigen | Schule |
| O-20 | Annahme: Die 10 laut UP entfallenen HO-Materialien werden nicht erstellt | Annahme | Produktionsplanung | 09.10.2026 bestätigen | Dozent |
| O-21 | Annahme: Handout U16 (Beispiel-Architekturdoku) wird trotz fehlender UP-Erwähnung gebraucht und spätestens an KT5 abgegeben | Annahme | PA-Doku | 18.12.2026 | Dozent |
| O-22 | Fachplan-LZ, die im UP ohne Unterrichtsgelegenheit sind (K-09): Abdeckung im Selbststudium zulässig? | offen | Lernzielabdeckung | 16.10.2026 | Dozent mit Lehrgangsleitung |
| O-23 | Master-Dokument festlegen: UP S2610 führend, HO auf v2.1 nachführen (Kurstage, Selbststudium, entfallene Materialien, Bezüge) | offen | alle weiteren KI-Aufträge | 09.10.2026 | Dozent |

### 5.2 Zeitleiste ab heute bis PA-Abgabe

| Datum | Meilenstein |
|---|---|
| Di 29.09.2026 | Inventar erstellt. Bis KT1 bleiben 24 Tage. |
| Fr 02.10.2026 | Entscheid Master-Dokument und Begriffe (KT1-KT6), Drive-Struktur bereinigen, Google-Doc-Handoff kennzeichnen |
| Fr 09.10.2026 | PA-Unterlagen angefordert, Arbeitsannahme PA-Umfang, Foliensatz-Frage, Handoff v2.1 (Selbststudium pro KT, entfallene Materialien) |
| Fr 16.10.2026 | **Vorbereitungs-Mail + Installationsanleitung versendet** (1 Woche vor KT1), Kurskanal live, Lehrmittelzugang, Raumcheck, Klassengrösse bekannt |
| Di 20.10.2026 | Alle KT1-Materialien fertig, Particify KT1, Demo-Skript im Kurskanal, A3/Flipchart bereit |
| **Fr 23.10.2026** | **KT1** (U1 + U2) |
| Fr 30.10.2026 | Spätestdatum PA-Unterlagen; VM-Klärung; MySQL-Gegenprobe U3; Python-Installationsaufforderung an TN |
| Di 03.11.2026 | KT2-Zusatzmaterialien (PP5-PP7, Demos, Übungen) fertig |
| **Fr 06.11.2026** | **KT2** (U3 + U4), PA-Kickoff mit PP6 |
| Fr 13.11.2026 | Unit-7-Materialien und `beispiele.sqlite` vorhanden; Repo-Test Flask abgeschlossen; `demo_u6_mysql.py` geprüft |
| So 15.11.2026 | Abgabe Datenmodell der TN (SST U3) als Grundlage für das Review in KT3 (Vorschlag) |
| Di 17.11.2026 | KT3-Material komplett, Review-Bogen gedruckt, Review-Gruppen gebildet |
| **Fr 20.11.2026** | **KT3** (U5 + U6/U7) |
| Fr 27.11.2026 | TN-Nachweis venv mit Flask (Screenshot); lab1.ifalabs.org geprüft; HO-WP3-Materialien fertig |
| **Fr 04.12.2026** | **KT4** (U8 + U9), Ausgabe App-Entwurf |
| Fr 11.12.2026 | VMs betriebsbereit; GitHub-Accounts der TN; App-Entwurf der TN abgegeben (Vorschlag: So 13.12.); HO-WP4/HO-WP5-Materialien fertig; Auftrag Architekturdoku und Handout U16 bereit |
| **Fr 18.12.2026** | **KT5** (U10/U11 + U12/U13), Implementierungsplan, Start 5-Wochen-Phase |
| 19.12.2026 bis 21.01.2027 | Implementierung PA im Selbststudium; Zwischencheck im Kurskanal (Vorschlag: Fr 08.01.2027) |
| Fr 15.01.2027 | HO-WP6-Materialien fertig, Peer-Feedback-Raster gedruckt, Präsentationsreihenfolge ausgehängt |
| **Fr 22.01.2027** | **KT6** (U14/U15 + U16), Schlusspräsentationen |
| **Fr 05.02.2027** | **PA-Abgabe** (Annahme: 2 Wochen nach KT6) |

---

## 6. Findings

| ID | Schweregrad | Datei + Stelle | Befund | Vorschlag |
|---|---|---|---|---|
| P-01 | hoch | Drive `02_Materialien/`; `WP2_Uebersicht_Units_6-7.md` Abschnitt "Unit 7" und "Code-Artefakte"; UP 4 "Verdichtungshinweis" | Ordner `Unit_7_...` fehlt komplett (5 Materialien, 6 Code-Dateien) sowie `04_Selbststudium/Selbststudium_U7_Klassen-Uebungen.md`. UP behauptet "Für Units 5-7 existieren bereits fertige Materialien" und setzt am KT3 U7.0, U7.1, PP8 und das OOP-Quiz ein. | Ursprungsablage der HO-WP2-Erstellung (lokale Arbeitskopie) suchen und hochladen; sonst bis 13.11.2026 neu erstellen. WP2-Übersicht und UP-Satz korrigieren. |
| P-02 | hoch | WP1-Übersicht "Verifikationsmethode", Annahme 2; WP2-Übersicht "Code-Artefakte"; Drive `Unit_6_.../code/` | `beispiele.sqlite` fehlt. Der SQLite-Fallback der Demo U6 (`demo_u6_sqlite.py`) läuft ohne diese Datei nicht, die dokumentierte Verifikation der Kontrollwerte U3.1 ist nicht reproduzierbar. | Portierung aus `SQL/create_beispiele.sql` neu erzeugen, zusammen mit dem Konvertierungsskript in `Unit_6_.../code/` ablegen. |
| P-03 | hoch | Soll-Ist-Matrix 3.4; HO-WP0 (lokale Kopie Z. 120-246) | Für KT1 (23.10.2026, in 24 Tagen) fehlen 16 von 20 Materialien, vorhanden sind nur PP1-PP4. Die Vorbereitungs-Mail muss spätestens am 16.10.2026 verschickt sein. | HO-WP0 sofort priorisieren: Vorbereitungs-Mail + Installationsanleitung, Triage-Leitfaden, Demo-Drehbuch U1 + Import-Anleitung «beispiele», dann Übungen und Quiz. |
| P-04 | hoch | UP 1.2 "Terminplan und WP-Zuordnung" gegen alle Ablauftabellen; HO "Was unverändert bleibt" (Z. 30) | "2 Unit-Slots à 5 Lektionen" passt nicht in 4-h-Blöcke mit Pausen. Netto sind es 195 min (VM) bzw. 210 min (NM), total 2'430 statt 3'600 min laut HO. Vormittage enden 11:45. Der HO-Satz "Unit-Struktur (5×45 min) ... bleibt" ist damit falsch. | Im UP die effektive Netto-Zeit pro Halbtag ausweisen; im HO v2.1 den Abschnitt "Was unverändert bleibt" streichen und alle Minutenbudgets auf Halbtage à 195/210 min umstellen. |
| P-05 | hoch | HO SST U1 (Z. 184-190), Quiz U2 (Z. 198), U6-Ablauf (Z. 443), U9 "Flipped" (Z. 568), SST U14; UP KT1 bis KT6; WP1 "Abhängigkeiten" ("vor Unit 6") | Selbststudium und Vorbereitungen zwischen zwei Units desselben Kurstags sind unmöglich; betroffen sind 6 Übergänge. Quiz U2 soll aufdecken, "wer das Selbststudium nicht gemacht hat", U9 setzt vorbereitete FLASK Kap. 4-5 voraus. | Pro KT genau einen SST nach dem Kurstag mit Vorbereitungsteil für den nächsten KT. Flipped-Lektüre für U9 in den SST nach KT3 legen. Quiz U2 als Aktivierung umwidmen. WP1-Frist "vor Unit 6" auf "vor KT4" ändern. |
| P-06 | hoch | HO "Challenge / Prüfung"; UP 1.5, PP6, Checkliste; WP1 "Was noch offen ist"; HO Z. 236, 329, 691; UP PP6 Folie 4 | PA-Aufgabenstellung und Bewertungsraster fehlen, obwohl der PA-Kickoff bereits am KT2 (06.11.) stattfindet. Die Umfangsvorgaben widersprechen sich fünffach (3, 3-4, min. 4, 3-6, 4-8 Tabellen; "~6 Wochen" gegen 5 + 2 Wochen). | Offizielle Unterlagen bis 30.10.2026 einfordern. Bis dahin eine Arbeitsannahme festlegen und in allen Materialien gleich formulieren. Ordner `03_Praxisarbeit` anlegen. |
| P-07 | hoch | HO "Offene Punkte" (Z. 987); UP Checkliste; UP KT5 14:45-16:00 | VMs auf ifalabs.org pro TN sind ungeklärt; der UP plant Live-Deployment und Nachvollziehen auf der eigenen VM bereits am KT5 (18.12.). Ohne VMs fallen Übung, SST U13 und das PA-Deployment weg. | Bis 30.10.2026 mit dem Betreiber klären, Bereitstellung bis 11.12.2026. Checklisten-Walkthrough (UP-Fallback) als eigenes Material ausarbeiten. |
| P-08 | mittel | UP 1.2 Tabelle, PP1 Folie 4, PP9 Folie 6, PP12 Folie 7; HO "WP-Übersicht"; WP1/WP2-Übersicht Titel | "WP" bezeichnet im UP Kurstage, im HO Unit-Gruppen. Folien für TN verweisen auf "WP 2/3/5"; "WP 3" ist je nach Dokument Python-OOP oder Flask. | Einheitlich "KT1-KT6" (mit Datum) für Kurstage, Units für Inhalte, "HO-WP" nur in internen Dokumenten. TN-Folien nur mit Kurstag und Datum. |
| P-09 | mittel | UP KT3-NM 14:50-15:05; HO Kurzaufgabe U7.0 (Z. 491) | Der Code-Review `bank2c.py` (K4, Fehler bei `self`) steht vor dem Klassen-Input. TN sollen einen `self`-Fehler finden, bevor `self` eingeführt ist. | U7.0 nach "Klassen und Objekte" (15:25) oder vor das Quiz legen; alternativ als Vorhersage-Aufgabe mit Auflösung in der Demo umformulieren. |
| P-10 | mittel | UP Lernzielzeilen KT2 bis KT6; HO Unit-Kontexte | Fachplan-LZ fehlen im UP oder werden abgestuft (u. a. U3-LZ3 DBMS-Schichtenarchitektur, U6-LZ1 K4 → K3, U6-LZ2/3 Module/pip/venv, U12-LZ2 E-Mail-Integration, U13-LZ2/4, U14-LZ1/2 K4). Die K4-Beurteilung von Deployment-Varianten findet nur noch als Input statt. | LZ-Abdeckungsmatrix Fachplan zu KT erstellen; ins Selbststudium verschobene LZ mit prüfbarem Auftrag belegen; Zulässigkeit mit Lehrgangsleitung klären. |
| P-11 | mittel | HO U1-Kontext ("Selbststudium im gleichen Umfang ... Pflicht") gegen SST-Minuten (225/90/135); UP 1.3 | Der HO fordert gleichen Umfang wie Unterricht, spezifiziert aber nur 50 %. Der UP übernimmt "gleicher Umfang" und verschiebt zusätzlich Stoff ins Selbststudium. | Selbststudiumsbudget pro KT festlegen (z. B. 405 min) und alle SST danach dimensionieren; im Kickoff genau diese Zahl kommunizieren. |
| P-12 | mittel | UP KT6 10:50-11:45 und 14:25-16:25; HO Peer-Feedback-Raster | Schlusspräsentationen: Block 1 (45 min) und Block 2 (60 min) bei 8 + 4 min je TN ergeben 3 + 5 = höchstens 8 TN, mit 1 min Beamer-Wechsel nur 3 + 4 = 7 TN. Zwischenpräsentationen: 55 min bei 4 min/TN (plus Wechsel) ergeben 11 bis 13 TN. Klassengrösse unbekannt. | Klassengrösse bis 16.10. klären; ab 9 TN Parallelräume, Galerie-Format oder kürzere Slots planen. |
| P-13 | mittel | UP KT6 13:00 PP15 Folie 9; HO Auftrag U15 (Z. 918-924) | Die Anforderungen an die Architekturdokumentation werden am KT6 vorgestellt, am selben Tag wie die Schlusspräsentationen und nach der 5-Wochen-Phase. | Auftrag Architekturdoku und Handout U16 spätestens am KT5 (18.12.) ausgeben; PP15 Folien 9-10 an KT5 verschieben. |
| P-14 | mittel | HO Setup-Sprechstunde U1 (Z. 132, "ab 17:30"); UP 1.5 und Ablauf KT1/KT4; WP1 "vor Unit 4"; WP2 "vor Unit 7 und Unit 8" | Setup-Sprechstunden: Uhrzeit aus einer Abendkursform, Termine widersprüchlich (UP "jeweils", Tabellen nur KT1 und KT4; WP1 fällt in die Mittagspause). | Sprechstunden KT1 (MySQL), KT2 (Python), KT4 (Flask), KT5 (Git/SSH) jeweils 07:30-08:00 festlegen; Türschild-Zeit auf 07:30 korrigieren. |
| P-15 | mittel | UP Kopfzeile "Fach:"; HO Kopf; Repo README | Drei Fachbezeichnungen ("IT-Architektur, Datenbank und Web-Entwicklung", "Datenbanken und Web-Entwicklung", "Datenbanken und Webentwicklung"). | Mit Fachplan V_I-1.0 abgleichen und eine Schreibweise auf Folien, Mail und PA-Unterlagen verwenden. |
| P-16 | mittel | Drive `01_Planung/KI-Handoff_DBWE.TA1A.md` (Google Doc); `handoff_gdoc.md` Z. 399, 438, 460, 669, 692 | Zweite Datei mit gleichem Titel, verlustbehaftet konvertiert: "app/**init**.py" statt `app/__init__.py`, "/users//posts" statt `/users/<id>/posts`, sichtbare Escapes im HO-WP6-Kontext. Keine Kommentare, keine inhaltlichen Abweichungen. | Markdown-Datei als Master kennzeichnen; Google Doc umbenennen (z. B. "Leseansicht, nicht für KI-Aufträge") oder löschen. |
| P-17 | mittel | Drive-Wurzel, `18.09.2026/`, `02_Materialien/` | Datumsordner mit Unterrichtsplan und PP1-PP4; Übersichten im Wurzelordner; Nummernlücke `03_`; Unit-Ordner nur für U3-U6, während der UP nach Kurstagen plant. | Struktur `01_Planung`, `02_Materialien/KT1_...` bis `KT6_...` (Units als Unterordner), `03_Praxisarbeit`, `04_Selbststudium`; Dateien verschieben (Drive-Links bleiben erhalten). |
| P-18 | mittel | HO Kopf (Z. 4) und "Offene Punkte" (Z. 984); WP1-Übersicht Kopf und "Was noch offen ist" | Verweise auf `Unterrichtsplan_DBWE.TA1A.docx` (Remote) und `KI-Handoff_..._v1-remote-archiv.md`, beide nicht im Drive; "die Minutenwerte bleiben" ist durch S2610 überholt; WP1 "Unterrichtsplan muss noch nachgezogen werden" ebenso. | HO v2.1 mit Bezug auf S2610; v1-Archiv ablegen oder Verweise entfernen; Übersichten nachführen. |
| P-19 | mittel | HO SST U4 (Z. 369) | Vergleich mit "Repo `Python/kap-1` bis `kap-5`" verlangt; im Repo fehlen `kap-2`, `kap-3`, `kap-4`. | Verweis auf vorhandene Ordner (kap-1, kap-5) einschränken und im SST vermerken, dass es für Kap. 2-4 keine Repo-Lösungen gibt. Materialteil prüfen, ob `Selbststudium_U4_PYGR_Kap1-5.md` den Verweis übernommen hat. |
| P-20 | mittel | UP KT4-NM 16:50 (Ausblick) gegen UP KT5 "Verdichtungshinweis" | KT4 weist nur FLASK Kap. 6-8 zu, KT5 setzt Kap. 6-13 "über zwei Selbststudiumsblöcke" voraus; zwischen KT4 und KT5 gibt es nur einen Block. Kap. 9-13 (Tests, Git, Deployment) werden nirgends beauftragt. | SST nach KT4 auf Kap. 6-13 mit Priorisierung erweitern oder KT5 auf Kap. 6-8 plus Demo-Stoff zurücknehmen. |
| P-21 | mittel | UP KT5 13:20-13:50 und 11:15-11:45; HO SST U11 (Z. 739), Peer-Review U11 (Z. 727) | KT5 setzt eine "eigene App" voraus (Git-Übung, Security-Checkliste), beauftragt ist bis dahin nur der App-Entwurf. Das Gate "spätestens hier müssen alle TN einen PA-Entwurf vorlegen" samt Peer-Review entfällt ersatzlos. | SST nach KT4 um "Projektgerüst eigene App (Struktur wie `Flask/kap-2`/`kap-3`, venv, 1 Model)" ergänzen; Abgabe App-Entwurf bis 13.12. als Gate; 10 min Peer-Check im KT5-VM. |
| P-22 | mittel | UP KT1 08:00-08:25; HO Kickoff-Folien (Z. 140) | PP1 (8-10 Folien) und Vorstellungsrunde mit 1 min pro TN in 25 min. | Vorstellungsrunde an die Tischgruppen auslagern oder in die Fallarbeit integrieren; PP1 auf 15 min begrenzen. |
| P-23 | mittel | UP KT1 14:00-14:20 | Input PP4 (PK/FK, ERD) und Import von `create_beispiele.sql` bei allen TN in 20 min, ohne Anleitung. | Import als Teil der Vorbereitungs-Mail (Verifikationsschritt) oder der Setup-Sprechstunde; Kurzanleitung mit Kontrollabfrage erstellen (Z04). |
| P-24 | mittel | UP KT1 11:15 und 13:00; UP KT2 08:00 | Quiz U1 und Check-in-Quiz U2 prüfen im Abstand von 105 min denselben Stoff; KT1-Schlussquiz und KT2-Eingangsquiz prüfen beide 3NF/JOIN. | Check-in U2 durch 5-min-Aktivierung ersetzen (Zeitgewinn für P-23); Quiz U3 als Abrufübung nach 2 Wochen beibehalten. |
| P-25 | mittel | HO "Bereits vorhandene Materialien"; UP 1.4 [PP]; Drive `18.09.2026/` | "Folien SQL/Python/Flask" laut HO vorhanden, im Drive nicht auffindbar. Der UP plant PP1-PP15 als eigene PowerPoints, der HO verlangt Folien als Markdown-Outline. PP5 existiert nur als md. | Entscheiden, ob PP1-PP15 die Fachplan-Foliensätze ersetzen; Zielformat pptx festlegen; PP5 aus `Kurzfolien_U3_Indexierung-Caching.md` bauen. |
| P-26 | mittel | UP 1.2 "Kalender-Chance", KT5 16:30-17:00 | Die 5-Wochen-Phase fällt über Weihnachten/Neujahr, ohne Betreuungsplan und ohne Zwischenstand. | Betreuungsfenster und Antwortzeit ankündigen; Zwischenstand im Kurskanal (z. B. 08.01.2027) als Pflichtabgabe. |
| P-27 | mittel | HO Partnerübungen U14.2, U15.1, U15.2 (Z. 886-916); UP KT6-VM | Der HO spezifiziert Starter-Code aus `Flask/kap-14` mit Konvergenz zum Repo-Endstand, der UP lässt die Endpunkte in der eigenen App bauen. | Variante festlegen. Empfehlung: Demo am Repo-Stand, Übung an der eigenen App, HO-Spezifikation entsprechend kürzen. |
| P-28 | tief | HO "WP-Übersicht" (Z. 36-37) | HO-WP0 und HO-WP1 sind mit je 15 Materialien angegeben, tatsächlich sind es je 16 (Summe 80 statt 78). | Tabelle korrigieren. |
| P-29 | tief | UP 1.2 ("Units 9-16"), UP 7 Kernmethoden U16 ("[PARTNER]") gegen Ablauf ("Einzelarbeit"); UP 1.4 gegen HO-Mapping | Verdichtung betrifft auch U6/U7 und nicht U9; Sozialform U16-Übung doppelt definiert; [PARTNER] "ein Laptop" gegen HO "beide Laptops". | UP-Texte korrigieren; eine Definition für [PARTNER] und eine eigene Kennzeichnung für "Einzelarbeit mit Nachbarhilfe". |
| P-30 | tief | UP PP5-Outline "6-8 Folien, 15 min + Demo" gegen Slot 20 min und HO Kurzfolien U3 "8-10 Folien, 20 min" | Umfangsangaben passen nicht zusammen. | Angaben an das vorhandene Material angleichen. |
| P-31 | tief | WP1-Übersicht Abschnitt "Materialien" | "Kopfzeile mit Sozialform und KI-Stufe" (gemeint vermutlich K-Stufe). | Begriff korrigieren; im Materialteil prüfen, ob die Kopfzeilen der Übungsblätter denselben Fehler tragen. |
| P-32 | tief | Repo `microblog/` (Gitlink ohne `.gitmodules`); Repo `Flask/` (nur kap-1, 2, 3, 13, 14, 15) | Der microblog-Code ist im Repo nicht auflösbar; für FLASK Kap. 4-12 gibt es keinen Repo-Code zum Vergleichen. | In SST U8-U11 keinen "Vergleich mit Repo" für diese Kapitel versprechen; auf die Demo lab1.ifalabs.org verweisen. |
