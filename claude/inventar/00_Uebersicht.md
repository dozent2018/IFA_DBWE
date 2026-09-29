# Inventar DBWE.TA1A: Übersicht

Stand 29.09.2026. Erstellt mit 8 parallelen Subagents; jede Datei im Google Drive (Rework-Ordner) und im Repo wurde vollständig gelesen, Python-Code ausgeführt, Flask mit aktuellen Versionen getestet, SQL gegen MySQL 8.0.46 und 8.4.11 ausgeführt (08).

Begriffe: **KT1-KT6** = die 6 Kurstage laut Unterrichtsplan S2610 (UP). **HO-WP0-6** = Work Packages im KI-Handoff v2.0 (nach Units). Die beiden Nummerierungen sind nicht deckungsgleich.

## Dateien

| Datei | Inhalt |
|---|---|
| [01_Planung_Soll-Ist.md](01_Planung_Soll-Ist.md) | Drive-Baum, Soll-Ist-Matrix aller Materialien (Handoff + UP), Konflikte der Planungsdokumente, Zeitleiste bis PA-Abgabe |
| [02_Folien_KT1_PP1-PP4.md](02_Folien_KT1_PP1-PP4.md) | Foliensätze KT1: Inventar pro Folie, Abgleich Outline, fachliche Prüfung, Passung zu «beispiele» |
| [03_Material_U3-U4.md](03_Material_U3-U4.md) | Material KT2 (U3, U4): Konformität, Ausführungsprotokoll, Lücken im Tagesablauf |
| [04_Material_U5-U6.md](04_Material_U5-U6.md) | Material KT3 (U5, U6): Konformität, Ausführungsprotokoll, Lücken U7 |
| [05_Repo_SQL_Python_kap1-12.md](05_Repo_SQL_Python_kap1-12.md) | Schema «beispiele» mit ERD und Datenstatistik, SQL-Kapiteldateien, Python kap-1 bis 12, verbrauchte Szenarien |
| [06_Repo_Python_kap13-19.md](06_Repo_Python_kap13-19.md) | Python kap-13 bis 19, bank2c-Analyse, Datendateien, Bereinigungsliste |
| [07_Repo_Flask_Struktur.md](07_Repo_Flask_Struktur.md) | Flask-Kapitel, Legacy-APIs, Smoke-Test Flask 3.1, Deployment-Config, microblog-Gitlink |
| [08_Verifikation_MySQL.md](08_Verifikation_MySQL.md) | Import «beispiele», Repo-SQL und Unit-3-Material gegen MySQL 8, Index-Messung, Demo U6 |

Das Repo ist öffentlich. Die Inventardateien enthalten deshalb keine Musterlösungen, Quiz-Lösungen, Kontrollwerte, Credentials oder Personendaten.

## Kernaussagen

1. **KT1 (23.10.2026) ist der Engpass.** Von 20 benötigten Materialien existieren 4 (PP1-PP4), und diese haben selbst 7 schwere Fehler. Die Vorbereitungs-Mail mit Installationsanleitung muss bis 16.10.2026 raus.
2. **Gesamtstand: 25 von 108 Materialien vorhanden.** KT2 und KT3 sind teilweise gedeckt (U3-U6), KT4-KT6 haben noch nichts. Der Ordner Unit_7 fehlt, obwohl der UP "Units 5-7 fertig" angibt.
3. **Die Planungsgrundlage widerspricht sich.** Der UP verdichtet 16 Units auf 12 Halbtage mit netto 2'430 statt 3'600 Minuten; der Handoff rechnet weiter mit 5×45 min pro Unit und mit Selbststudium zwischen Units, die jetzt am selben Tag liegen.
4. **Der Code des vorhandenen Materials läuft, die Texte darum enthalten Fehler.** Python-Musterlösungen U4-U6, die Kontrollwerte U3.1 und die Demo U6 sind jetzt auch auf MySQL 8 bestätigt. Mehrere Übungsblätter und Folien machen aber Aussagen, die beim Ausführen nicht eintreten (BOM-Falle U6.2, Textvergleich, Refactoring-Prämisse U6.1, Index-Demo U3).
5. **Die Muster-DB «beispiele» trägt einige geplante Übungen nicht.** Es gibt keine Studierenden ohne Klasse, keine Klassen ohne Studierende, kein Fach ohne Prüfung; LEFT-JOIN-Aufgaben aus Handoff und PP4 zeigen keinen Unterschied. Zwei Beziehungen haben keinen FK.
6. **Der Repo-Code ist als Referenz nur bedingt brauchbar.** Syntaxfehler in kap-3.sql, falsch rechnende Anfängerskripte, kap-18-Demos ohne Treffer, Flask kap-15 unter Werkzeug 3 nicht importierbar, kap-14 unvollständig.
7. **Offene externe Abhängigkeiten blockieren ab KT2:** PA-Aufgabenstellung und Raster (PA-Kickoff am KT2), Lehrmittel-Verteilung (Leseauftrag vor KT1), VMs auf ifalabs.org (Deployment am KT5), Klassengrösse (Präsentationsslots KT6).

## Soll-Ist pro Kurstag

Quelle: 01, Abschnitt 3.4.

| KT | Datum | Units | Soll | vorhanden | fehlt |
|---|---|---|---|---|---|
| KT1 | Fr 23.10.2026 | U1 + U2 | 20 | 4 | 16 |
| KT2 | Fr 06.11.2026 | U3 + U4 | 20 | 11 | 9 |
| KT3 | Fr 20.11.2026 | U5 + U6/7 | 20 | 10 | 10 |
| KT4 | Fr 04.12.2026 | U8 + U9 | 15 | 0 | 15 |
| KT5 | Fr 18.12.2026 | U10/11 + U12/13 | 20 | 0 | 20 |
| KT6 | Fr 22.01.2027 | U14/15 + U16 | 13 | 0 | 13 |
| **Total** | | | **108** | **25** | **83** |

## Schwere Findings nach Thema

### A. KT1-Material (Folien)
- PP4: Syntaxfehler im CREATE TABLE (fehlendes Komma, MySQL-Fehler 1064); JOIN-Beispiel mit `klasse_id`/`id`, in «beispiele» heissen die Spalten `klasse`/`student_id` (02 F01, F02).
- PP4 und Handoff U2.3: LEFT-JOIN-Szenario existiert in «beispiele» nicht (02 F03). Brauchbare Alternative: `lehrveranstaltung` LEFT JOIN `dozent` (05 SQL-F03).
- PP3: setzt Selbststudium Kap. 4-5 voraus, das es am selben Tag nicht geben kann (02 F04).
- PP1: PA-Details als verbindlich dargestellt; Lehrmittel "im Unterricht verteilt" widerspricht dem Leseauftrag vor KT1; "8 Lektionen" statt 10 (02 F05-F07).

### B. Planung
- Netto-Unterrichtszeit 32.5 % unter Handoff-Annahme; 6 Selbststudiums-Übergänge zwischen Units desselben Tages nicht umsetzbar (01 P-04, P-05).
- PA-Unterlagen fehlen, PA-Umfang in den Dokumenten fünffach widersprüchlich (01 P-06).
- VMs ifalabs.org ungeklärt, Live-Deployment am KT5 geplant (01 P-07).
- Unit_7-Ordner und `beispiele.sqlite` fehlen im Drive (01 P-01, P-02).

### C. Vorhandenes Material KT2/KT3
- Quiz U3 Frage 4: zwei richtige Optionen unter MySQL (03 U3-F01).
- Index-Demo U3 bricht nach dem vorgeschriebenen Probelauf (03 U3-F02).
- Selbststudium U4 verweist auf nicht existierende Repo-Ordner (03 U4-F01).
- KT2: 115 von 225 Minuten am Nachmittag ohne Material, PP6 (PA-Kickoff) fehlt (03 KT2-F01, F02).
- U6.1: Refactoring-Prämisse falsch; U6.2: Drive-CSV ohne BOM (Kernmoment fällt aus) und falsche Aussage zum Textvergleich (04 U6-F01, F05, F06).
- Demo U6 SQLite-Fallback läuft nicht ohne `beispiele.sqlite` (04 U6-F12).
- KT3: Fristen "vor Unit 6/7" unmöglich, kein venv-Schritt (macOS blockiert pip), U6-Material 33 min zu lang, U7 komplett ohne Material (04 KT3-F01, F03-F05).

### D. Repo-Code
- `create_beispiele.sql`: Collation `utf8mb4_0900_ai_ci` verhindert Import in MariaDB/XAMPP (05 SQL-F01).
- `kap-3.sql` (Basis Demo U1): zwei Syntaxfehler (05 SQL-F02).
- Anfängerskripte: 11 Dateien kompilieren nicht oder rechnen falsch, z. B. `beitrag.py`, `eintritt2/3` (05 PY-F01 bis F03).
- `kap-18` (Basis Demo U6): Abfragezeitraum 2020 liefert 0 Zeilen; Credentials hardcodiert (06 PY2-F02).
- `bank2c.py`: Bug bestätigt; `bank2d.py` zeigt die Korrektur öffentlich, Auftrag U7.0 muss Begründung statt Fix verlangen (06 PY2-F03).
- Flask: kap-15 ImportError unter Werkzeug 3 (`url_parse`); kap-14 unvollständig, Vollstand in Commit 877e509; `password_hash` String(128) zu kurz für scrypt (162 Zeichen); Handoff-Pläne U14.2 und U15.1 funktionieren so nicht (07 FL-F01, F02, F04, F06, F07).

### E. Öffentliches Repo und Datenschutz
- Private Kalenderexporte (`kap-17/IFA-TimeOverlap.csv`, `daten.csv`) und eine Studierenden-Abgabe mit Namen (`kap-16/bank2_patrick.py`, `color.py`): **im aktuellen Stand gelöscht** (Commit 7c1676b, Entscheid Projektinhaber). In der Git-Historie und im Upstream-Repo weiterhin vorhanden.
- `kap-8.sql` enthält Klartext-Passwörter (05 SQL-F04).
- Musterlösungen für neue Übungen dürfen nicht in dieses Repo (CLAUDE.md). Ablageort ist noch zu entscheiden.

## MySQL-8-Verifikation

Quelle: 08. Geprüft auf MySQL 8.0.46 (Ubuntu-Build) und 8.4.11 (offizielles Oracle-Build), Ergebnisse identisch.

- **Import «beispiele»:** läuft auf beiden Versionen fehlerfrei (15 Deprecation-Warnungen wegen `SET NAMES utf8`). MariaDB/XAMPP und MySQL 5.7 scheitern in Zeile 1 an der Collation. Empfehlung für die Installationsanleitung: MySQL 8.4 LTS, Kontrolle mit `SELECT VERSION();` (VER-F15).
- **Unit 3:** Alle Kontrollwerte von `loesung_u3_1.sql` stimmen auf MySQL (die bisherige SQLite-Prüfung ist damit bestätigt). Views-Demo läuft; im Safe-Update-Modus der Workbench bleibt beim Aufräumen eine Testklasse stehen, `table_rows` zeigt nach dem Import 0 (VER-F08, F09).
- **Index-Demo:** Funktioniert nur mit frischem Setup (VER-F21). Gemessen: ohne Index 11 ms, mit Index 0.16 ms (Faktor ca. 70), Schreiben mit 3 Indexen Faktor 2. Zwei Folienaussagen treffen nicht ein: der zweite Lauf ist nicht schneller (Buffer Pool schon gefüllt), und in Block 5 wählt der Optimizer den Index und wird damit schneller (VER-F11, F12).
- **Demo U6 (`demo_u6_mysql.py`):** läuft vollständig, alle Kontrollwerte des Drehbuchs stimmen; kleine Abweichungen bei Schreibweise und Fehlermeldungen (VER-F19).
- **Repo-SQL:** kap-5, kap-6, kap-8, kap-10 laufen (mit Default-Schema); kap-3, kap-4, kap-7 nicht. kap-4 zeigt OUTER JOIN falsch (VER-F01), kap-5 verändert «beispiele» dauerhaft (VER-F14).
- **PP4:** Die Folienabfrage endet mit `ERROR 1054 Unknown column 's.klasse_id'` (VER-F02).
- **Nicht geprüft:** Workbench-GUI selbst, Windows und macOS, MySQL 9.x.

## Entscheide, die anstehen

1. Master-Dokument und Begriffe: UP S2610 als Taktgeber, Handoff auf v2.1 nachführen (Kurstage, Netto-Minuten, Selbststudium pro KT).
2. Ablage der Musterlösungen und Kontrollwerte: Drive oder privates Repo.
3. Arbeitsannahme PA-Umfang, bis die offiziellen Unterlagen vorliegen (einheitlich in PP1, PP6, Selbststudium U3, Coaching U5).
4. Foliensätze: Ersetzen PP1-PP15 die Fachplan-Folien? Zielformat pptx?
5. Ziel-DBMS: nur MySQL 8, oder zusätzlich eine MariaDB-taugliche Kopie von «beispiele»?
6. Umgang mit fehlenden LEFT-JOIN-Fällen: Übungen auf `lehrveranstaltung`/`dozent` umstellen oder «beispiele» mit einem Zusatzskript ergänzen.

## Empfohlene Reihenfolge

1. **bis 09.10.:** Vorbereitungs-Mail + Installationsanleitung (inkl. Import «beispiele» mit Kontrollzahl), Setup-Triage; PA-Unterlagen, Lehrmittelzugang, Kurskanal, VMs, Klassengrösse anfragen.
2. **bis 16.10.:** PP1-PP4 korrigieren; Demo-Drehbuch U1 (korrigierte kap-3-Basis), Übungen U1.1, U1.2, U2.1-U2.3 mit gegen MySQL 8 getesteten Lösungen, Quiz U1/U2, Selbststudium nach KT1. Mail versenden.
3. **bis 03.11.:** KT2-Lücken (PP5-PP7, Demos, Übungen U4), Korrekturen U3/U4 aus 03.
4. **bis 17.11.:** KT3: Korrekturen U5/U6 aus 04, U7-Block neu, `beispiele.sqlite` erzeugen.
5. **danach:** KT4 (Flask-Basis aus 07 rekonstruieren), KT5, KT6.
