# Inventar 08: Verifikation der SQL-Materialien gegen MySQL 8

Kurs DBWE.TA1A «Datenbanken und Web-Entwicklung», IFA Höhere Fachschule.
Erstellt am 29.09.2026 als Teil des Rework-Inventars. Geprüft wurden die Muster-DB «beispiele», die Repo-Dateien `SQL/kap-3.sql` bis `SQL/kap-10.sql`, das Unit-3-Material (Drive `Unit_3/code`), die Unit-6-Demo (Drive `Unit_6/code`) und die JOIN-Abfrage aus PP4.
An den Materialien wurde nichts geändert. Musterlösungen und vollständige Kontrollwerte werden hier bewusst nicht abgedruckt (Repo ist öffentlich); pro Aufgabe steht nur «stimmt» oder «weicht ab».

Schweregrade: **hoch** = falsch oder blockiert Unterricht; **mittel** = verwirrt TN oder erzeugt Nacharbeit; **tief** = Kosmetik oder Hinweis.

---

## 1 Umgebung

### 1.1 Instanzen

| Rolle | Version | Bezug | Verbindung |
|---|---|---|---|
| Hauptprüfung | **MySQL 8.0.46** (Ubuntu-Build `8.0.46-0ubuntu0.24.04.4`) | Ubuntu-Pakete `mysql-server-core-8.0` und `mysql-client-core-8.0` per `apt-get download` geholt und mit `dpkg -x` ins Scratchpad entpackt, eigenes datadir, `mysqld --initialize-insecure` | Port 3316, eigener Socket |
| Gegenprobe | **MySQL 8.4.11 Community Server (GPL)** | offizielles Docker-Image `mysql:8.4` (Oracle Linux 9), Layer ohne Docker-Daemon direkt über die Registry-API bezogen, Server über den Loader des Images gestartet | Port 3318 |
| Fallback-Test | MariaDB 10.11.14 (Ubuntu) | nur Importtest in eigener Instanz, klar **nicht MySQL** | Port 3319 |

Installationsweg und Hindernisse:

- (a) `apt-get install -y mysql-server` lieferte echtes MySQL 8.0.46, nicht MariaDB. Kurz danach hat ein parallel arbeitender Agent `mariadb-server` installiert, das die MySQL-Serverpakete verdrängt (`/usr/sbin/mysqld` zeigt seither auf `mariadbd`). Deshalb wurden die MySQL-8.0-Binaries unabhängig vom Systempaket ins Scratchpad entpackt.
- (b) dev.mysql.com, cdn.mysql.com und repo.mysql.com sind durch die Egress-Policy gesperrt (Proxy antwortet 403). Offizielles Tarball daher nicht möglich.
- (c) Docker-CLI vorhanden, Daemon nicht. Docker Hub ist erreichbar, deshalb Image-Layer direkt gezogen (8.4.11).
- MySQL 9.x wurde nicht geprüft.

### 1.2 Server-Einstellungen (Standardwerte, unverändert)

| Einstellung | MySQL 8.0.46 | MySQL 8.4.11 | MariaDB 10.11 |
|---|---|---|---|
| `sql_mode` (global) | `ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION` | identisch | `STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION` |
| ONLY_FULL_GROUP_BY aktiv? | **ja** | **ja** | **nein** |
| `character_set_server` / `collation_server` | utf8mb4 / utf8mb4_0900_ai_ci | identisch | kennt utf8mb4_0900_ai_ci nicht |
| `sql_safe_updates` (Server) | 0 (Workbench setzt pro Sitzung 1) | 0 | |
| `innodb_buffer_pool_size` | 134217728 (128 MB) | 134217728 | |
| `innodb_buffer_pool_dump_at_shutdown` / `load_at_startup` | ON / ON | ON / ON | |
| `information_schema_stats_expiry` | 86400 s | 86400 s | |
| `lower_case_table_names` | 0 (Linux; Windows-Standard 1, macOS 2) | 0 | |
| Query Cache | `have_query_cache = NO`, keine `query_cache_*`-Variablen | entfernt | |
| Auth-Plugin neuer User | caching_sha2_password | caching_sha2_password | |

Hardware: Container mit 4 vCPU (Intel Xeon 2.1 GHz), 16 GB RAM, virtuelles Laufwerk. **Das ist kein Studi-Laptop**: absolute Laufzeiten sind Anhaltspunkte, die Verhältnisse (ohne/mit Index, Schreiblast) sind aussagekräftiger.

Clients: mysql-CLI 8.0.46 bzw. 8.4.11, Python 3.11.15 im venv, mysql-connector-python 26.7.0 (aktuelle PyPI-Version, reine Python-Implementierung).

### 1.3 Methode

- Für jede SQL-Datei zerlegt ein Runner den Text in Statements (Kommentare, Strings und `/*! */` beachtet) und führt sie in **einer frischen Verbindung** nacheinander aus, wie `mysql --force` (weiter nach Fehler). Pro Statement werden Nummer (Zählung ab 1, reine Kommentare zählen nicht), Startzeile, Zeilen- oder Änderungszahl, Warnungen und Fehler protokolliert.
- Vor jeder Datei wurde «beispiele» neu aus dem Dump eingespielt, «jochen» und die Test-User gelöscht.
- Jede Datei lief zusätzlich mit `SET SESSION sql_safe_updates = 1`, um den Workbench-Standard zu simulieren. Die Workbench selbst (GUI) war nicht verfügbar.
- Drive-Dateien byte-genau geholt und gegen die erwartete Grösse geprüft: `loesung_u3_1.sql` 4849 B, `demo_u3_views.sql` 2448 B, `index_demo_setup.sql` 1935 B, `index_demo_ablauf.sql` 4851 B, `demo_u6_mysql.py` 6123 B, `config_beispiel.py` 921 B, alle stimmen. (Bei `loesung_u3_1.sql` entstand beim Übertragen ein Artefakt von 3 Byte in der ersten Kommentar-Trennlinie; korrigiert, Grösse und Inhalt danach identisch.)
- Arbeitsdateien, Logs und Zugangsdaten liegen nur im Scratchpad der Sitzung, nicht im Repo.

---

## 2 Import von `SQL/create_beispiele.sql`

### 2.1 Protokoll

| Server | Ergebnis | Dauer | Meldungen |
|---|---|---|---|
| MySQL 8.0.46 | läuft durch, 0 Fehler | 0.36 s | 15 Warnungen: 1× Code 3719 (`'utf8' is currently an alias for ... UTF8MB3`) aus `/*!50503 SET NAMES utf8 */`, 14× Code 1287 (`'utf8mb3' is deprecated`) aus dem Zurücksetzen von `character_set_client` nach jedem der 14 `CREATE TABLE` |
| MySQL 8.4.11 | läuft durch, 0 Fehler | 0.35 s | dieselben 15 Warnungen |
| MySQL 8.4.11 mit `SET NAMES utf8mb4` statt `utf8` (Testkopie) | läuft durch | | **0 Warnungen** |
| MariaDB 10.11.14 | **bricht in Zeile 1 ab** | | `ERROR 1273 (HY000) at line 1: Unknown collation: 'utf8mb4_0900_ai_ci'`; nach Ersetzen der Collation (Testkopie) läuft der Import durch |

Weitere Beobachtungen zum Dump:

- Kopf: `mysqldump 10.13 Distrib 8.0.34, for macos13 (arm64)`, Server 8.2.0, erstellt 19.01.2024. Die Zeilen 1 und 2 (`CREATE DATABASE IF NOT EXISTS beispiele ...` und `USE beispiele;`) wurden vor den eigentlichen Dump gesetzt; der Import braucht deshalb kein vorgewähltes Schema.
- Jede Tabelle hat `DROP TABLE IF EXISTS`. Ein erneuter Import setzt die Daten zurück (geprüft: nach kap-5 und kap-7 wieder Originalwerte). Views und Zusatztabellen, die TN angelegt haben (z. B. `v_standorte` aus kap-7, `vornamen`, `strasse` aus kap-4), **bleiben bestehen** und funktionieren weiter.
- Zwei Zeilen sind länger als 100'000 Zeichen (längste 405'902 Zeichen, INSERT-Blöcke).
- Umlaute werden korrekt als UTF-8 gespeichert (z. B. «Zürich 1» = `5A C3 BC 72 69 63 68 20 31`), unabhängig vom Client-Standardzeichensatz, weil der Dump selbst `SET NAMES` setzt.

### 2.2 Tabellenstatistik

| Tabelle | Zeilen (COUNT) | `table_rows` direkt nach Import (Beispiel) | `table_rows` nach Statistik-Update |
|---|---|---|---|
| adresse | 160 | 13 bis 16 | 160 |
| dozent | 14 | 14 | 14 |
| fach | 24 | 24 | 24 |
| fach_alt | 6 | 6 | 6 |
| fachplan | 31 | 31 | 31 |
| klasse | 30 | 30 | 30 |
| konto | 2 | 2 | 2 |
| lehrgang | 3 | 3 | 3 |
| lehrveranstaltung | 2310 | 2310 | 2310 |
| mitarbeiter | 9 | 9 | 9 |
| pruefung | 5421 | 0 oder 5589 | 5589 |
| raum | 25 | **0** | 25 |
| standort | 4 | **0** | 4 |
| student | 352 | **0** | 352 |

`table_rows` ist eine InnoDB-Schätzung. Direkt nach dem Import stehen die persistenten Statistiken kleiner Tabellen noch auf dem Stand von `CREATE TABLE` (0). InnoDB rechnet sie im Hintergrund nach etwa 30 bis 45 Sekunden neu. Wer `information_schema.tables` in diesem Fenster abfragt, bekommt die alten Werte **für 24 Stunden gecacht** (`information_schema_stats_expiry = 86400`), ausser nach `ANALYZE TABLE`. Siehe VER-F09.

### 2.3 Struktur-Merkmale

- 18 Fremdschlüssel-Spalten (dozent 1, fachplan 2, klasse 1, lehrveranstaltung 4, mitarbeiter 3, pruefung 3, raum 1, standort 1, student 2).
- **Spalten mit Beziehungscharakter ohne FK-Constraint:** `klasse.standort` (→ standort) und `fach.dozent` (→ dozent). Beide haben auch keinen Index. Waisen gibt es keine (0 bzw. 0). Weitere INT-Spalten ohne FK (`semester` in fach, fach_alt, fachplan, klasse; `raum.kapazitaet`) sind keine Beziehungen.
- Keine UNIQUE-Constraints ausser den Primärschlüsseln (z. B. nicht auf `student.email`, `klasse.bezeichnung`, `fach.kuerzel`).
- Keine CHECK-Constraints (z. B. `raum.kapazitaet` darf negativ werden, siehe VER-F14).
- `standort_id` hat die Werte 1, 2, 3, 9 (Lücke; AUTO_INCREMENT steht auf 100).
- Collation `utf8mb4_0900_ai_ci` ist akzent- und gross/klein-unabhängig: `WHERE ort = 'Zurich'` findet dieselben 40 Adressen wie `'Zürich'`.
- `lehrgang.beschreibung` von HFWI enthält ein unsichtbares weiches Trennzeichen (U+00AD an Position 18, zwischen «Wirtschafts» und «informatiker»). `LIKE '%Wirtschaftsinformatik%'` findet deshalb 0 Zeilen.
- `fach.titel` enthält den Tippfehler «Risikomangement» (bekannt, in der Musterlösung vermerkt).
- `lehrveranstaltung.titel` sind Kürzel mit Laufnummer (z. B. `DEUT1`, `ITAR1`), nie gleich `fach.titel`.

### 2.4 Planungsabfragen (beschreiben die DB, keine Lösungen)

| Abfrage | Anzahl |
|---|---|
| Studierende ohne Klasse (`klasse IS NULL`) | 0 |
| Klassen ohne Studierende | 0 |
| Studierende pro Klasse (Minimum / Maximum) | 3 / 17 |
| Fächer ohne Prüfung | 0 |
| Fächer ohne Lehrveranstaltung | 0 |
| Fächer ohne Fachplan-Eintrag | 0 |
| Fächer ohne Dozent (`fach.dozent IS NULL`) | 0 |
| Dozenten ohne Lehrveranstaltung | 0 |
| Dozenten ohne Fach (über `fach.dozent`) | 0 |
| Standorte ohne Raum | 0 |
| Standorte ohne Klasse | 1 (Basel 1) |
| Räume ohne Lehrveranstaltung | 15 von 25 |
| Lehrveranstaltungen ohne Dozent | 3 (alle mit Titel `ITAR1`) |
| Lehrveranstaltungen, deren Dozent vom `fach.dozent` abweicht | 6 |
| Studierende ohne Prüfung | 0 |
| Prüfungen ohne Student / ohne Note / ohne Raum | 0 / 0 / 0 |
| Prüfungsfächer, die nicht im Fachplan des Lehrgangs stehen | 0 |
| Doppelte Adressen (gleiche strasse, nr, plz, ort) | **80 Paare: jede der 160 Adressen existiert genau zweimal** |
| Adressen, die von niemandem referenziert werden | 80 |
| Adressen, die mehrere Studierende teilen | 73 |
| Doppelte Studierenden-Namen / doppelte E-Mails | je 2 Gruppen |
| Doppelte Fachtitel / Fachkürzel / Klassenbezeichnungen | 0 / 0 / 0 |
| Waisen in `klasse.standort` / `fach.dozent` (Spalten ohne FK) | 0 / 0 |
| Zeitraum Lehrveranstaltungen | 01.07.2021 bis 15.12.2026 |
| Zeitraum Prüfungen | 09.08.2021 bis 14.11.2028 |
| Prüfungen nach dem 29.09.2026, die bereits eine Note haben | 895 |
| Notenbereich | 2.8 bis 6.0, jede Zehntelnote kommt vor |

---

## 3 Repo-Dateien `SQL/kap-3.sql` bis `SQL/kap-10.sql`

Eine Datei `kap-9.sql` existiert nicht. Jede Datei lief in einer frischen Sitzung auf frisch importierter «beispiele». Ergebnisse auf MySQL 8.0.46 und 8.4.11 sind **identisch**.

### 3.1 Übersicht

| Datei | Kontext (Default-Schema) | Statements | läuft durch? | Fehler normal | Fehler Safe-Update-Modus |
|---|---|---|---|---|---|
| kap-3.sql | keines (Datei legt `jochen` an und wechselt selbst) | 31 | **nein** | 2 | 3 |
| kap-4.sql | keines | 37 | **nein** | 37 (alle 1046 No database selected) | |
| kap-4.sql | `jochen` nach kap-3 | 37 | **nein** | 20 (2 davon beabsichtigt) | |
| kap-4.sql | `beispiele` | 37 | **nein** | 6 (1 davon beabsichtigt) | 6 |
| kap-5.sql | `beispiele` | 29 | ja | 0 | 1 |
| kap-5.sql | keines | 29 | nein | 17 (1046) | |
| kap-6.sql | `beispiele` | 8 | ja | 0 | 0 |
| kap-6.sql | keines | 8 | nein | 8 (1046) | |
| kap-7.sql | `beispiele` | 14 | **nein** | 2 (1 vermutlich beabsichtigt) | 4 |
| kap-7.sql | keines | 14 | nein | 14 (1046) | |
| kap-8.sql | keines (Wegwerf-Instanz) | 14 | ja | 0 | 0 |
| kap-8.sql | zweiter Lauf | 14 | nein | 3 (1396) | |
| kap-10.sql | `beispiele` oder keines | 7 | ja | 0 | 0 |

### 3.2 Fehler im Detail

**kap-3.sql**

| Nr. | Zeile | Statement | Fehler | Bewertung |
|---|---|---|---|---|
| 29 | 138 | `UPDATE student SET email = '...' WHERE name = 'Kunz' and vorname = 'Paula'` | nur Safe-Update: 1175 `You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.` | Workbench-Standard, siehe VER-F08 |
| 30 | 142 | `DELETE FROM student WHERE student_id = 6` (ohne `;`) + folgendes `create table kunde (...)` | 1064 `You have an error in your SQL syntax ... near 'create table kunde (...' at line 5` | Fehler im Skript: Semikolon fehlt. Folge: Student 6 wird nicht gelöscht, Tabelle `kunde` nicht angelegt |
| 31 | 153 | `ALTER TABLE kunde ADD website VARCHAR(255), MODIFY name VARCHAR(255) NOT NULL );` | 1064 `... near ')' at line 5` | Fehler im Skript: überzählige `)`. Scheitert auch, wenn `kunde` existiert (geprüft) |

Zweiter Lauf zusätzlich: Nr. 1 `CREATE DATABASE jochen` → 1007 `Can't create database 'jochen'; database exists`.

**kap-4.sql** (Teil 1 bis Zeile 53 setzt `jochen` aus kap-3 voraus, ab Zeile 55 «beispiele»; kein `USE`)

Kontext `jochen` nach kap-3:

| Nr. | Zeile | Fehler | Bewertung |
|---|---|---|---|
| 4 | 29 | 1452 `Cannot add or update a child row: a foreign key constraint fails (... pruefung_ibfk_2 ...)` | beabsichtigt (ungültiges Fach 7777) |
| 5 | 36 | 1451 `Cannot delete or update a parent row: a foreign key constraint fails (... pruefung_ibfk_1 ...)` | beabsichtigt (ON DELETE RESTRICT) |
| 6 | 39 | 1062 `Duplicate entry '9' for key 'fach.PRIMARY'` | **nicht beabsichtigt**: kap-3 legt 9 Fächer an, ID 9 ist belegt. Die ON-UPDATE-CASCADE-Demo läuft nie (VER-F04) |
| 9 bis 21, 27 bis 30 | 56 bis 171 | 1146 `Table 'jochen.klasse' doesn't exist` (bzw. raum, adresse, lehrveranstaltung, dozent, mitarbeiter, fach_alt) | Kontextwechsel ohne `USE beispiele` |

Kontext `beispiele`:

| Nr. | Zeile | Fehler | Bewertung |
|---|---|---|---|
| 1 | 4 | 1050 `Table 'pruefung' already exists` | Teil 1 gehört zu `jochen` |
| 2, 4 | 18, 29 | 1054 `Unknown column 'teilnehmer' in 'field list'` | dito |
| 5 | 36 | 1451 (FK `pruefung_ibfk_2` auf student) | im Sinne der Demo |
| 6 | 39 | 1451 `Cannot delete or update a parent row ... fachplan_ibfk_1` | CASCADE-Demo scheitert auch hier |
| 8 | 45 | 1054 `Unknown column 'student.vorname' in 'field list'` | Teil 1 gehört zu `jochen` |

Inhaltlich (ohne Fehlermeldung): Nr. 19 (Zeile 116, Kommentar «LEFT JOIN findet auch Veranstaltungen ohne Dozent», Code mit `RIGHT JOIN dozent`) und Nr. 20 (Zeile 123, Kommentar «RIGHT JOIN ...», Code mit `dozent LEFT JOIN lehrveranstaltung ... JOIN klasse`) liefern je **15 Zeilen, genau wie der INNER JOIN** (Nr. 16, 18). Es gibt 18 Lehrveranstaltungen `ITAR1`, 3 davon ohne Dozent. Die richtige Richtung (`lehrveranstaltung LEFT JOIN dozent` bzw. `dozent RIGHT JOIN lehrveranstaltung`) liefert 18. Siehe VER-F01.

Nebenwirkung im Kontext «beispiele»: Nr. 22 bis 37 legen die Tabellen `vornamen`, `nachnamen`, `strasse`, `hausnr`, `ort` in «beispiele» an; sie überleben einen Re-Import.

**kap-5.sql** (Kontext `beispiele`): läuft durch. Safe-Update: Nr. 23 (Zeile 51) `UPDATE raum SET kapazitaet = kapazitaet - 5 WHERE kapazitaet < 20` → 1175. Im Normalmodus ändert Nr. 23 dauerhaft 17 Räume; danach liefert kap-6 Nr. 1 nur noch 4 statt 8 Zeilen, nach fünf Läufen stehen Kapazitäten bei -15 (VER-F14). Ohne Default-Schema laufen nur die 12 Statements ohne Tabellenbezug.

**kap-6.sql**: läuft durch. Nr. 7 und Nr. 8 («Aufgabe 1» und «Aufgabe 2», Zeilen 61 und 69) sind zeichengleich. Nr. 6 (ALL) liefert 0 Zeilen, das ist fachlich korrekt.

**kap-7.sql** (Kontext `beispiele`)

| Nr. | Zeile | Fehler | Bewertung |
|---|---|---|---|
| 9 | 42 | 1050 `Table 'v_ma_liste' already exists` | Skriptfehler: View wird in Zeile 21 und 42 zweimal angelegt |
| 11 | 51 | läuft, aber **0 Zeilen geändert**; Safe-Update: 1175 | `telefon` von «Jörg Graf» ist schon `058 211 222`, die Demo zeigt keine Änderung |
| 13 | 55 | Safe-Update: 1175 | `UPDATE v_standorte ... WHERE name = 'Basel'` |
| 14 | 57 | 1393 `Can not modify more than one base table through a join view 'beispiele.v_standorte'` | vermutlich beabsichtigt (Grenze updatebarer Views), im Skript nicht als erwarteter Fehler markiert |

**kap-8.sql**: läuft in frischer Instanz durch (User `jochen`, `paula`, Rolle `simple`). `SHOW GRANTS` bestätigt das erwartete Ergebnis inkl. REVOKE. Zweiter Lauf: Nr. 1, 10, 12 → 1396 `Operation CREATE USER failed ...` bzw. `CREATE ROLE failed`. `FLUSH PRIVILEGES` nach `GRANT` ist unnötig, erzeugt aber auf 8.0 und 8.4 keine Warnung.

**kap-10.sql**: läuft durch, auch ohne Default-Schema. Nr. 1 zeigt die veralteten `table_rows` (siehe 2.2). Nr. 5 (Zeile 39) sortiert mit `ORDER BY 'Tabelle-FK'` nach einem String-Literal, also gar nicht. Nr. 4 filtert `columns` nur nach `table_name`, nicht nach Schema.

---

## 4 Unit-3-Material

### 4.1 `loesung_u3_1.sql` gegen Kommentare und Partnerübung U3.1

Alle 9 Statements laufen auf 8.0.46 und 8.4.11 fehlerfrei, auch im Safe-Update-Modus. Vergleich mit den Kontrollwerten (Kommentare in der Datei, identisch mit dem Übungsblatt):

| Aufgabe | Zeilenzahl | Kontrollwerte (inkl. AVG-Rundung) |
|---|---|---|
| 1 Kennzahlen | stimmt | stimmt |
| 2 Klassengrössen | stimmt | stimmt (Spitze inkl. Gleichstand und Sortierung) |
| 3 Notenschnitt je Fach | stimmt | stimmt (beide genannten Spitzenwerte) |
| 4 LV pro Klasse und Jahr | stimmt | stimmt (Werte Klasse 1); die im Kommentar genannte Fehlvariante (Gruppierung nach dem vollen Datum) liefert so viele Zeilen wie die Tabelle (2310), «über 2000» stimmt; die im Kommentar erwähnte Alias-Variante läuft auf MySQL |
| 5a HAVING Klassen | stimmt | stimmt |
| 5b HAVING Fächer | stimmt | stimmt; eine Variante, die im HAVING den gerundeten Wert vergleicht, liefert dieselbe Zeilenzahl, kein Rundungs-Grenzfall |
| 6 Drei beste Klassen | stimmt | stimmt, aber Platz 2 und 3 haben gerundet denselben Schnitt; ihre Reihenfolge hängt vom Sortierausdruck ab (VER-F17) |
| Zusatz | stimmt | stimmt |

Die in der Datei verlangte Gegenprüfung der AVG-Rundung auf MySQL ist damit erledigt: MySQL rechnet AVG über DECIMAL exakt, kein Wert weicht von der SQLite-Portierung ab.

Typische TN-Fehler, auf MySQL 8.0.46 nachgestellt:

| Variante | Ergebnis |
|---|---|
| Aggregatfunktion in der WHERE-Klausel | 1111 `Invalid use of group function` (kein Syntaxfehler 1064, wie der Kommentar sagt) |
| Spalte im SELECT, die weder gruppiert noch funktional abhängig ist (z. B. ein Studierenden-Name neben der Klassen-ID) | 1055 `... not in GROUP BY clause and contains nonaggregated column 'beispiele.student.name' ... incompatible with sql_mode=only_full_group_by` |
| volle Datumsspalte im SELECT, gruppiert wird aber nur nach dem Jahr | 1055 |
| nach der Fremdschlüsselspalte gruppieren, eine Spalte der verbundenen Tabelle ausgeben (Aufgaben 3 und 6) | **kein Fehler**: MySQL 8 erkennt die funktionale Abhängigkeit über Join-Gleichheit und Primärschlüssel |
| nur nach der Bezeichnung statt nach dem Schlüssel gruppieren (Aufgabe 6) | kein Fehler, gleiches Ergebnis (Bezeichnungen sind eindeutig) |

### 4.2 `demo_u3_views.sql`

Komplett ausgeführt (13 Statements inkl. information_schema-Teil), 0 Fehler auf 8.0.46 und 8.4.11.

| Drehbuch-Minute | Statement | Ergebnis |
|---|---|---|
| 0 | Ausgangsabfrage Bern | Zeilenzahl stimmt |
| 2, 3 | `CREATE VIEW v_klassenliste`, Abfrage | stimmt (gleiche Zeilenzahl wie Minute 0) |
| 5 | INSERT `HFWI.BE.7`, Abfrage | stimmt (eine Zeile mehr) |
| 7, 8 | `v_klassengroesse`, Top 3 und `anzahl = 0` | stimmt (Spitzenklasse und leere Klasse wie im Drehbuch) |
| 10 | `DELETE FROM klasse WHERE bezeichnung = 'HFWI.BE.7'` | Normalmodus: 1 Zeile gelöscht. **Safe-Update-Modus: 1175**, Testklasse bleibt stehen (VER-F08) |
| 11 | `table_rows` aus `information_schema.tables` | liefert 16 Zeilen (14 Tabellen + 2 Views mit `NULL`). Direkt nach dem Import 0 für student, raum, standort (VER-F09) |
| 12 | `information_schema.views` | stimmt (2 Views) |
| 13 | `key_column_usage` | 18 Zeilen; **klasse.standort und fach.dozent fehlen**, weil kein FK existiert (VER-F10) |

Zweiter Lauf ohne `DROP VIEW`: Nr. 3 und 7 → 1050 `Table 'v_klassenliste' already exists`. Nach einem Safe-Update-Lauf mit stehengebliebener Testklasse legt ein weiterer Lauf eine zweite Klasse `HFWI.BE.7` an (kein UNIQUE).

Getestete Safe-Update-taugliche Alternativen fürs Aufräumen: `DELETE FROM klasse WHERE klasse_id > 30 AND bezeichnung = 'HFWI.BE.7';` und `DELETE FROM klasse WHERE bezeichnung = 'HFWI.BE.7' LIMIT 1;` werden beide mit `sql_safe_updates = 1` akzeptiert.

### 4.3 Index-Demo (`index_demo_setup.sql` + `index_demo_ablauf.sql`)

Funktional: Setup 8/8 und Ablauf 16/16 Statements fehlerfrei, auch im Safe-Update-Modus. Kontrollabfrage des Setups stimmt (100000 Zeilen, Kunden 1 bis 5000, 5000 verschiedene Kunden, 4 Aktionen). Kunde 4711 hat 20 Zeilen, `aktion = 'suche'` trifft 25'000 Zeilen. Tabellengrösse nach beiden Indexen: 4.5 MB Daten + 4.0 MB Indexe, passt also vollständig in den Buffer Pool (128 MB).

Ein **zweiter Ablauf ohne neues Setup** scheitert fünfmal mit 1061 `Duplicate key name 'idx_zugriffslog_kunde'` (Nr. 4, 7, 12, 13, 14), und Block 6a misst dann eine Tabelle, die die drei Indexe noch hat (TRUNCATE entfernt Indexe nicht).

**Laufzeiten** (Client-Wandzeit über Unix-Socket, `execute` + `fetchall`, Median; die Workbench zeigt «Duration» etwas anders gemessen an):

| Messpunkt | Angabe Kurzfolien / Skript | MySQL 8.0.46 | MySQL 8.4.11 |
|---|---|---|---|
| Setup gesamt (5 Läufe) | «ca. 5 bis 30 Sekunden» | 0.61 s (0.55 bis 0.62) | 0.54 s |
| Block 1 ohne Index (21 Läufe) | «20 bis 60 ms» | **11.4 ms** (11.2 bis 13.1) | 9.4 ms |
| Block 1, Lauf 1 / Lauf 2 direkt nach Setup | «zweiter Lauf schneller (Buffer Pool)» | 11.8 / 11.7 ms, **kein Unterschied** | 9.9 / 9.5 ms |
| nach Neustart, Standard (Buffer Pool wird geladen) | | 20.9 ms, danach 14.1 / 14.6 ms | |
| nach Neustart kalt (ohne Buffer-Pool-Load, OS-Cache geleert) | | 26.4 ms, danach 14.1 / 21.5 ms | |
| Block 3 `CREATE INDEX` (5 Läufe) | «typisch 0.3 bis 2 s» | **0.11 s** (0.10 bis 0.16) | 0.09 s |
| Block 4 mit Index (21 Läufe) | «unter 5 ms» | **0.16 ms** (0.14 bis 0.29) | 0.15 ms |
| Faktor ohne / mit Index | «Faktor anschreiben» | **ca. 70** | ca. 64 |
| Block 5 `COUNT(*) WHERE aktion = 'suche'` ohne / mit Index | «Index lohnt sich nicht» | 14.8 / **4.6 ms** (Index hilft, weil er deckt) | 12.0 / 3.9 ms |
| dieselbe Bedingung mit `SUM(dauer_ms)` ohne / mit Index | | 18.1 / **21.8 ms** (Index schadet leicht) | |
| dieselbe Bedingung mit `SELECT *` ohne / mit Index | | 195 / 195 ms | |
| Block 6a INSERT 100'000 ohne Zusatzindex (5 Läufe) | «Zeit A» | 0.49 s | 0.41 s |
| Block 6b INSERT 100'000 mit 3 Indexen (5 Läufe) | «deutlich grösser» | 1.05 s, **Faktor 2.1** | 0.94 s, Faktor 2.3 |
| Variante 1 Mio. Zeilen (nur 8.4, zur Einordnung) | | Setup 6.3 s, ohne Index 115 ms, CREATE INDEX 1.2 s, mit Index 0.32 ms | |

**EXPLAIN** (identisch auf 8.0.46 und 8.4.11):

| Block | type | possible_keys | key | rows | Extra | passt zur Folie? |
|---|---|---|---|---|---|---|
| 2 ohne Index | ALL | NULL | NULL | 100000 | Using where | ja |
| 4 mit Index | ref | idx_zugriffslog_kunde | idx_zugriffslog_kunde | 20 | Using index | ja («einstellig bis zweistellig») |
| 5 `aktion = 'suche'` (COUNT und SELECT *) | ref | idx_zugriffslog_aktion | idx_zugriffslog_aktion | 47504 (tatsächlich 25'000) | COUNT: Using index | teilweise: der Optimizer **wählt** den Index; «rows ist trotzdem riesig» stimmt, «wählt ihn gar nicht» tritt nicht ein |

Weitere Aussagen der Kurzfolien bestätigt: Query Cache existiert in 8.0 nicht mehr; `innodb_buffer_pool_size` Standard 128 MB; für jeden Fremdschlüssel gibt es einen Index (im Dump sichtbar).

Einordnung: Auf dem Container ist alles schneller als in den Folien angegeben. Auf einem Studi-Laptop mit SSD sind ähnliche Grössenordnungen zu erwarten; langsame oder volle Laptops können deutlich höher liegen. Die Verhältnisse (Faktor 60 bis 70 beim Lesen, Faktor 2 beim Schreiben) sind stabil.

---

## 5 Unit-6-Demo (`demo_u6_mysql.py`)

Ausgeführt mit mysql-connector-python 26.7.0 im venv, `config.py` nach Vorlage `config_beispiel.py` (nur im Scratchpad; eigener User mit SELECT/INSERT/UPDATE/DELETE auf «beispiele»; zusätzlich `"port"` nötig, weil die Testinstanz nicht auf 3306 läuft). Gesamtdauer 0.58 s, Exit-Code 0. Ausgabe auf 8.0.46 und 8.4.11 zeichengleich.

| Block | läuft? | Ausgabe plausibel und passend zum Drehbuch? |
|---|---|---|
| 1/2 Verbindung über `config.py` | ja | ja |
| 2 Liste von Tupeln (`LIMIT %s`) | ja | ja, 5 Tupel mit `datetime.datetime`-Werten |
| 3 Liste von Dictionaries | ja | ja; Zugriff über Spaltennamen funktioniert. Achtung: zwei Lehrveranstaltungen haben denselben frühesten `beginn`, die Reihenfolge der ersten Zeilen ist nicht garantiert |
| 4a f-String mit harmlosem Wert | ja | ja, 1 Treffer wie im Drehbuch |
| 4b f-String mit `' OR '1'='1` | ja | ja, Trefferzahl wie im Drehbuch |
| 4c Platzhalter | ja | ja, 0 Treffer, gültiger Wert wieder 1 Treffer |
| 5 Kontext-Manager + Notenschnitt je Fach | ja | ja, Spitzenwerte wie im Drehbuch; Ausgabe zeigt den Titel mit Dump-Tippfehler «Risikomangement», das Drehbuch schreibt «Risikomanagement» |

Einzelarbeit (Kontrollwerte im Drehbuch): Aufgabe 1 stimmt, Aufgabe 2 stimmt, Aufgabe 3 stimmt, Aufgabe 4 (Standort 99) liefert eine leere Menge wie beschrieben.

Notfallplan-Meldungen nachgestellt:

| Fall | tatsächliche Meldung |
|---|---|
| `config.py` fehlt | Demo-Skript fängt den ImportError ab und zeigt «config.py fehlt. Kopiert config_beispiel.py nach config.py ...»; `ModuleNotFoundError` sehen TN nur in eigenem Code |
| falsches Passwort | 1045 `Access denied for user 'u6demo'@'localhost' (using password: YES)` |
| DB fehlt, Verbindung als root | 1049 `Unknown database '...'` |
| DB fehlt, Verbindung als eingeschränkter User | 1044 `Access denied for user '...'@'localhost' to database '...'` (nicht «Unknown database») |
| kein Server auf dem Port | 2003 `Can't connect to MySQL server on 'localhost:3306' (Errno 111: Connection refused)` |

---

## 6 PP4-Test (Kurstag 1)

Folienabfrage auf «beispiele»:

```
SELECT s.name, k.bezeichnung FROM student s JOIN klasse k ON s.klasse_id = k.klasse_id;
```

Ergebnis auf MySQL 8.0.46 **und** 8.4.11:

```
ERROR 1054 (42S22): Unknown column 's.klasse_id' in 'on clause'
```

Korrekte Variante mit `s.klasse = k.klasse_id`: 352 Zeilen (INNER und LEFT JOIN gleich, da kein Student ohne Klasse). Bestätigt Finding F02 in `02_Folien_KT1_PP1-PP4.md` auf echtem MySQL.

---

## 7 Workbench- und Windows-relevante Beobachtungen

Abgeleitet aus Import und Läufen; die Workbench selbst konnte nicht gestartet werden.

1. **Safe-Update-Modus** (Workbench-Standard «Safe Updates» aktiv): 1175 bei kap-3 Nr. 29, kap-5 Nr. 23, kap-7 Nr. 11 und 13 sowie beim Aufräumen der Views-Demo. Das Drehbuch U3 rechnet damit nur «falls die Meldung kommt»; mit Standardeinstellungen kommt sie sicher.
2. **Automatisches LIMIT 1000** (Workbench «Limit Rows», Standard 1000): betroffen sind Abfragen mit mehr als 1000 Zeilen, z. B. `SELECT * FROM pruefung` (5421), kap-4 Nr. 14 (2307), kap-5 Nr. 25 (5421) und die Fehlvariante von U3.1 Aufgabe 4 (2310). In der Workbench erscheint dort «1000 row(s) returned», nicht die echte Zahl.
3. **Skriptausführung stoppt beim ersten Fehler** (Workbench-Standard «Stop Script Execution on Errors»): «Execute All» bricht kap-3 bei Nr. 30, kap-4 in «beispiele» bei Nr. 1 und kap-7 bei Nr. 9 ab. Der Rest der Datei läuft dann nicht.
4. **Kein `USE` in kap-4 bis kap-7:** Ohne vorgewähltes Default-Schema (Doppelklick auf «beispiele» im Navigator) scheitert jedes Statement mit 1046 `No database selected`.
5. **Versionskommentare im Dump:** `/*!40100 ... COLLATE utf8mb4_0900_ai_ci */` wird von jedem MySQL ab 4.1 ausgeführt und verlangt eine Collation, die es erst ab MySQL 8.0 gibt. `/*!80016 DEFAULT ENCRYPTION='N' */` wird erst ab 8.0.16 ausgeführt. Folge: Import in **MariaDB (z. B. XAMPP) oder MySQL 5.7 scheitert in Zeile 1** mit 1273 Unknown collation. Auf MariaDB fehlt zudem ONLY_FULL_GROUP_BY, der didaktisch gewollte Fehler 1055 tritt dort nicht auf.
6. **Deprecation-Warnungen beim Import:** 15 gelbe Warnungen (utf8/utf8mb3) im Output-Fenster sind harmlos, können TN aber verunsichern. Mit `SET NAMES utf8mb4` im Dump verschwinden sie (getestet).
7. **Umlaute:** Beim Import über `mysql < datei` oder die Workbench bleiben Umlaute korrekt, weil der Dump `SET NAMES` selbst setzt. Nicht geprüft: Import über Windows PowerShell 5.1 per Pipe (`Get-Content ... | mysql`), die Nicht-ASCII-Zeichen umkodieren kann; `<` gibt es in PowerShell nicht.
8. **Sehr lange Zeilen:** zwei Zeilen über 100'000 Zeichen (max. 405'902). Das Öffnen im Workbench-Editor kann träge sein; «File > Run SQL Script» umgeht den Editor (nicht in der Workbench geprüft).
9. **Gross/Kleinschreibung von Tabellennamen:** Windows (1) und macOS (2) verhalten sich anders als Linux (0). Dump und kap-Dateien verwenden durchgehend Kleinbuchstaben, deshalb kein Problem.
10. **Akzent-Unabhängigkeit** der Collation: `'Zurich' = 'Zürich'` ist wahr. Kann bei Übungen mit Umlauten überraschen, ist aber ein gutes Beispiel.
11. **Zeitmessung in der Workbench:** Sub-Millisekunden-Werte (Index-Demo mit Index, 0.16 ms) erscheinen in der Sekunden-Anzeige je nach Version als `0.000 sec`. Dann lässt sich der Faktor nicht aus der Anzeige berechnen (nicht in der Workbench geprüft).
12. **MySQL-Version bei Neuinstallationen:** MySQL 8.0 hat laut Oracle-Lifecycle im April 2026 das Supportende erreicht; neue Installationen landen auf 8.4 LTS oder 9.x. 8.4.11 verhält sich bei allen geprüften Dateien identisch zu 8.0.46.

---

## 8 Findings

| ID | Schweregrad | Datei / Statement | Befund | Vorschlag |
|---|---|---|---|---|
| VER-F01 | hoch | `SQL/kap-4.sql` Nr. 19 (Z. 115-121) und Nr. 20 (Z. 122-127), Kap. 4.4 Outer Join | Kommentare und Code passen nicht: «LEFT JOIN findet auch Veranstaltungen ohne Dozent» steht über einem `RIGHT JOIN dozent`, «RIGHT JOIN» über einem `dozent LEFT JOIN ...`. Beide liefern 15 Zeilen wie der INNER JOIN; die 3 ITAR1-Veranstaltungen ohne Dozent erscheinen nie (korrekte Richtung: 18). Das Beispiel lehrt den Unterschied INNER/OUTER falsch. | Richtung umdrehen (`lehrveranstaltung LEFT JOIN dozent` bzw. `dozent RIGHT JOIN lehrveranstaltung`) und Kommentare tauschen; Zeilenzahl 15 gegen 18 im Kommentar nennen. Da es Lehrmittel-Code ist: in eigenen Folien/Demos die korrigierte Fassung verwenden und auf den Fehler im Repo hinweisen. |
| VER-F02 | hoch | PP4 F6 (Kurstag 1), JOIN über `s.klasse_id` | Auf MySQL 8.0.46 und 8.4.11: `ERROR 1054 (42S22): Unknown column 's.klasse_id' in 'on clause'`. Korrekte Variante liefert 352 Zeilen. | Wie F02 in Inventar 02: Folie auf «beispiele»-Spaltennamen umstellen. |
| VER-F03 | mittel | `SQL/kap-4.sql` gesamt | Kein `USE`; Teil 1 (bis Z. 53) braucht `jochen` aus kap-3, Teil 2 (ab Z. 55) «beispiele». Kein Kontext läuft durch: ohne Schema 37/37 Fehler, `jochen` 20, «beispiele» 6. Im Kontext «beispiele» legt die Datei 5 Hilfstabellen dort an, die einen Re-Import überleben. | `USE jochen;` an den Anfang und `USE beispiele;` vor Kap. 4.3.4 setzen, oder Datei in zwei Teile trennen; Hilfstabellen in `jochen` anlegen. |
| VER-F04 | mittel | `SQL/kap-4.sql` Nr. 6 (Z. 39) `UPDATE fach SET fach_id = 9 WHERE fach_id = 1` | ON-UPDATE-CASCADE-Demo scheitert immer: in `jochen` 1062 Duplicate entry '9' (kap-3 legt 9 Fächer an), in «beispiele» 1451 (FK aus `fachplan`). | Freie ID verwenden (z. B. 99) und festhalten, dass das Beispiel in `jochen` läuft. |
| VER-F05 | mittel | `SQL/kap-3.sql` Z. 142 und Z. 153-156 | Semikolon nach `DELETE FROM student WHERE student_id = 6` fehlt → 1064, Student 6 bleibt, Tabelle `kunde` fehlt. `ALTER TABLE kunde ... )` hat eine überzählige Klammer → 1064 auch bei vorhandener Tabelle. | `;` ergänzen, `)` entfernen. In Folien/Demos, die sich auf kap-3 stützen, die korrigierte Fassung zeigen. |
| VER-F06 | mittel | `SQL/kap-5.sql`, `kap-6.sql`, `kap-7.sql` | Kein `USE beispiele;`: ohne vorgewähltes Schema 17/29, 8/8 bzw. 14/14 Fehler (1046). | Erste Zeile `USE beispiele;`; in der Setup-Anleitung zeigen, wie man in der Workbench das Default-Schema setzt. |
| VER-F07 | mittel | `SQL/kap-7.sql` Nr. 9 (Z. 42), Nr. 11 (Z. 51), Nr. 14 (Z. 57) | `v_ma_liste` wird zweimal angelegt (1050, bricht «Execute All» ab). Das UPDATE der Telefonnummer ändert 0 Zeilen, weil der Wert schon gespeichert ist. INSERT in die Join-View scheitert mit 1393 ohne Hinweis, ob das gewollt ist. | Doppeltes `CREATE VIEW` entfernen (oder `CREATE OR REPLACE VIEW`), eine andere Nummer verwenden, Nr. 14 als «erwarteter Fehler» kommentieren. |
| VER-F08 | mittel | Safe-Update-Modus: `demo_u3_views.sql` Nr. 10, kap-3 Nr. 29, kap-5 Nr. 23, kap-7 Nr. 11/13 | Mit Workbench-Standard kommt 1175 sicher. In der Views-Demo bleibt dann `HFWI.BE.7` stehen; ein zweiter Lauf legt die Klasse doppelt an. Drehbuch sagt nur «falls die Meldung kommt». | Aufräumen safe-mode-tauglich schreiben (`... WHERE klasse_id > 30 AND bezeichnung = 'HFWI.BE.7'` oder `... LIMIT 1`, beide getestet); im Drehbuch ankündigen, dass die Meldung kommt, und den Grund in einem Satz erklären. |
| VER-F09 | mittel | `demo_u3_views.sql` Nr. 11 / Drehbuch Min. 11; `kap-10.sql` Nr. 1 | `table_rows` zeigt kurz nach dem Import 0 für student, raum, standort, und dieser Wert bleibt 24 h im I_S-Cache. Das Drehbuch sagt «weichen leicht ab». Zusätzlich erscheinen die 2 Views mit `NULL` in der Liste. Nach aktueller Statistik weicht nur pruefung ab (5589 statt 5421, +3 %). | Vor der Demo `ANALYZE TABLE` auf die Tabellen ausführen oder `SET SESSION information_schema_stats_expiry = 0;` voranstellen; im Drehbuch den 0-Fall als möglich nennen; Filter `AND table_type = 'BASE TABLE'`. |
| VER-F10 | mittel | Drehbuch U3 Min. 13 («das ERD aus Unit 2, als Tabelle»), Schema-Kasten Partnerübung U3.1 | `key_column_usage` listet 18 FK-Spalten; `klasse.standort` und `fach.dozent` fehlen, weil im Dump kein FK existiert. Das Übungsblatt beschriftet `klasse.standort` als «(FK->standort)». TN, die ihr A3-ERD vergleichen, finden eine Differenz. | Im Blatt «standort (Beziehung ohne FK)» schreiben; im Drehbuch die Lücke als Entdeckung einplanen («Beziehung, die die DB nicht erzwingt»). Keine Waisen vorhanden, Joins funktionieren. |
| VER-F11 | mittel | `index_demo_ablauf.sql` Block 1, Kurzfolien Folie 3 und 9 | «Zweite Ausführung ist schneller (Buffer Pool)» tritt im üblichen Ablauf nicht ein: nach dem Setup liegt die Tabelle schon im Buffer Pool (11.8 / 11.7 ms). Auch nach einem Neustart lädt MySQL den Buffer Pool standardmässig wieder (20.9 → 14.1 ms). Nur ganz kalt 26.4 → 14.1 ms. | Nicht versprechen. Stattdessen Buffer-Pool-Wirkung mit `SHOW STATUS LIKE 'Innodb_buffer_pool_read%'` (Anfragen gegen Plattenlesezugriffe) zeigen, oder als «kann schneller sein» formulieren. |
| VER-F12 | mittel | `index_demo_ablauf.sql` Block 5, Kurzfolien Folie 7 | Der Optimizer **nimmt** den Index auf `aktion` (type ref, rows 47504 geschätzt, 25'000 tatsächlich). Mit `COUNT(*)` deckt der Index die Abfrage und macht sie etwa 3× schneller (14.8 → 4.6 ms). Wer misst, widerlegt die Folienaussage «Index lohnt sich nicht». | Block 5 auf `SELECT SUM(dauer_ms) ... WHERE aktion = 'suche'` umstellen (Index wird gewählt, ist aber langsamer als der Full Scan: 21.8 gegen 18.1 ms) oder `SELECT *` (kein Gewinn); Folientext von «wählt ihn unter Umständen gar nicht» auf «wählt ihn, ohne dass es hilft» anpassen. |
| VER-F13 | mittel | Partnerübung U3.1 Debriefing Aufgabe 4, `loesung_u3_1.sql` Kommentar | «105 Zeilen statt über 2000»: Die Fehlvariante liefert 2310 Zeilen, die Workbench zeigt mit Standard-LIMIT aber «1000 row(s) returned». Dasselbe bei grossen Abfragen in kap-4/kap-5. | Im Debriefing mit `SELECT COUNT(*) FROM ( ... ) x` zählen lassen oder vorher auf die Einstellung «Limit Rows» hinweisen. |
| VER-F14 | mittel | `SQL/kap-5.sql` Nr. 23 (Z. 51) | `UPDATE raum SET kapazitaet = kapazitaet - 5 WHERE kapazitaet < 20` ändert «beispiele» dauerhaft (17 Räume). Danach liefert kap-6 Nr. 1 4 statt 8 Zeilen; mehrfaches Ausführen erzeugt negative Kapazitäten (-15 nach 5 Läufen, kein CHECK). | Beispiel in `START TRANSACTION; ... ROLLBACK;` einbetten oder klar als «verändert die DB, Reset per Re-Import» markieren. |
| VER-F15 | mittel | Setup der TN (Dump, Unit 2) | Mit MariaDB (z. B. XAMPP) oder MySQL 5.7 scheitert der Import in Zeile 1 (1273 Unknown collation). Nach Collation-Ersatz läuft er, aber ohne ONLY_FULL_GROUP_BY; der Fehler 1055 aus U3.1 tritt dann nicht auf. | In der Setup-Anleitung MySQL 8.4 LTS Community ausdrücklich verlangen, XAMPP/MariaDB ausschliessen, Kontrolle mit `SELECT VERSION();` in die Setup-Checkliste aufnehmen. |
| VER-F16 | tief | Kurzfolien U3 (Folien 3, 6, 8), Kommentar `index_demo_setup.sql` | Alle gemessenen Zeiten liegen unter den Angaben: Setup 0.6 s statt «5 bis 30 s», ohne Index 11 ms statt «20 bis 60 ms», CREATE INDEX 0.11 s statt «0.3 bis 2 s». Die Workbench zeigt 0.16 ms vermutlich als `0.000 sec`, dann lässt sich kein Faktor rechnen. | Bereiche weiter fassen («unter 1 s bis 30 s»), Hinweis «eigene Zahlen notieren» beibehalten. Für sichtbarere Zeiten optional 1 Mio. Zeilen (gemessen: Setup 6.3 s, ohne Index 115 ms, mit Index 0.32 ms; Kunde 4711 hat dann 200 Zeilen) oder den Faktor aus `SHOW PROFILES` / Performance Schema ablesen. |
| VER-F17 | tief | `loesung_u3_1.sql` Aufgabe 6 | Platz 2 und 3 haben gerundet denselben Schnitt. Die Musterlösung sortiert nach dem gerundeten Wert, die Reihenfolge der beiden ist damit zufällig; wer nach dem ungerundeten Durchschnitt sortiert, bekommt sie vertauscht. Beide Lösungen sind richtig. | In der Musterlösung nach dem ungerundeten Wert sortieren und im Kommentar vermerken, dass beide Reihenfolgen gelten. |
| VER-F18 | tief | `loesung_u3_1.sql` Kommentar 5b, Partnerübung «Beim Zirkulieren» | Ein Aggregat in der WHERE-Klausel ergibt 1111 «Invalid use of group function», keinen Syntaxfehler. Fehler 1055 kommt seltener als erwartet, weil MySQL 8 funktionale Abhängigkeiten erkennt (Gruppieren nach der FK-Spalte und Ausgeben einer Spalte der verbundenen Tabelle läuft ohne Fehler). | Kommentar auf «Fehler 1111» ändern; für die Dozierenden ein sicheres 1055-Beispiel im Drive-Blatt notieren (siehe Tabelle in 4.1). |
| VER-F19 | tief | Drehbuch U6 und `demo_u6_mysql.py` | Kontrollwert «Risikomanagement» erscheint in der Ausgabe als «Risikomangement». Block 2/3 sortieren nur nach `beginn`, der früheste Zeitpunkt ist doppelt belegt, die erste Zeile kann je Rechner anders sein. Notfallplan: «Unknown database» (1049) sehen nur User mit globalen Rechten, eingeschränkte User sehen 1044. `config_beispiel.py` kennt keinen `port`. | Schreibweise im Drehbuch an die Ausgabe anpassen; `ORDER BY beginn, lehrv_id`; im Notfallplan 1044 ergänzen; optionale Zeile `"port": 3306` in die Vorlage. |
| VER-F20 | tief | `SQL/create_beispiele.sql` Kopf | 15 Deprecation-Warnungen (utf8 / utf8mb3) bei jedem Import auf 8.0 und 8.4. | `/*!50503 SET NAMES utf8 */` durch `utf8mb4` ersetzen (getestet: 0 Warnungen) oder die Warnungen in der Installationsanleitung ankündigen. |
| VER-F21 | tief | Wiederholbarkeit: kap-3 Nr. 1, kap-8 Nr. 1/10/12, `demo_u3_views.sql` Nr. 3/7, `index_demo_ablauf.sql` Nr. 4/7/12-14 | Zweite Läufe scheitern mit 1007, 1396, 1050 bzw. 1061. Für TN, die eine Übung wiederholen, sieht das wie ein eigener Fehler aus. | `IF NOT EXISTS`, `CREATE OR REPLACE VIEW`, `DROP USER IF EXISTS` voranstellen; Index-Demo: im Kopf festhalten «vor jeder Durchführung Setup neu laufen lassen». |
| VER-F22 | tief | Daten in «beispiele» | Jede Adresse existiert doppelt, 80 Adressen sind unbenutzt; je 2 doppelte Studierenden-Namen und E-Mails; 895 Prüfungen nach dem 29.09.2026 haben schon eine Note (bis 2028); weiches Trennzeichen in `lehrgang.beschreibung` (HFWI); Standort-IDs 1, 2, 3, 9. | In einem DB-Steckbrief für Dozierende festhalten; für Übungen zu Datenqualität (Duplikate, NOT EXISTS) nutzbar. |
| VER-F23 | tief | `SQL/kap-6.sql` Nr. 7/8, `SQL/kap-10.sql` Nr. 4/5 | «Aufgabe 1» und «Aufgabe 2» sind zeichengleich. `ORDER BY 'Tabelle-FK'` sortiert nach einem String-Literal (keine Sortierung). `columns`-Abfrage ohne Schema-Filter. | Bei Verwendung im Unterricht korrigierte Fassung zeigen (Backticks oder Spaltenausdruck, `AND table_schema = 'beispiele'`). |
| VER-F24 | tief | Drehbuch U3 Min. 8 | «Wer in U3.1 Aufgabe 2 nur 30 Zeilen hatte, hat auch nur die Klassen mit Studierenden gesehen»: In «beispiele» hat jede der 30 Klassen Studierende, 30 Zeilen sind also vollständig. Nur die in der Demo angelegte leere Klasse fehlt beim INNER JOIN. | Satz präzisieren: «... hätte eine leere Klasse wie HFWI.BE.7 nicht gesehen». |

---

## 9 Nicht verifiziert

- **MySQL Workbench** selbst (GUI): Safe-Update, LIMIT 1000, Stopp bei Fehlern, Anzeige der «Duration», Verhalten beim Öffnen der Datei mit 400'000-Zeichen-Zeilen sind aus den Standardeinstellungen abgeleitet und mit `sql_safe_updates = 1` simuliert, nicht in der Workbench beobachtet.
- **Windows und macOS**: keine Tests auf diesen Systemen (Installer, `lower_case_table_names` 1/2, PowerShell-Import, Pfade, Zeichensatz der Konsole).
- **MySQL 9.x** (Innovation Releases, z. B. über Homebrew) nicht geprüft; geprüft sind 8.0.46 und 8.4.11.
- **Offizielles MySQL-8.0-Tarball** (Oracle-Build) war wegen der Egress-Sperre nicht erreichbar; 8.0 wurde mit dem Ubuntu-Build geprüft, 8.4 mit dem offiziellen Oracle-Build aus dem Docker-Image.
- **Laufzeiten auf Studi-Laptops**: nur Container-Messungen; der Kaltstart-Fall wurde mit Neustart ohne Buffer-Pool-Load und geleertem OS-Cache nachgestellt.
- **`demo_u6_sqlite.py` und `beispiele.sqlite`** (Fallback der U6-Demo) lagen nicht im Auftrag und wurden nicht geprüft.
- **Folienauszüge ausser PP4 F6** (z. B. SQL auf den Folien «Folien SQL») wurden nicht gegen MySQL ausgeführt.
- Die Drehbücher wurden als Text über Drive gelesen; die Zeitmarken und die Didaktik sind nicht Teil dieser Prüfung.
