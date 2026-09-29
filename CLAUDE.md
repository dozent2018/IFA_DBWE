# CLAUDE.md

Rework der Unterrichtsmaterialien fuer DBWE.TA1A "Datenbanken und Web-Entwicklung" (IFA Hoehere Fachschule), Start 23.10.2026.

## Repo
- `SQL/`, `Python/`, `Flask/`: Code und Musterloesungen zum Lehrmittel von Jochen Reinholdt (Stand 2024). Nur mit ausdruecklichem Auftrag aendern.
- `SQL/create_beispiele.sql`: Muster-DB «beispiele» (MySQL 8), Grundlage aller SQL-Uebungen.
- `claude/`: neues Material und Inventar (`claude/inventar/`) aus dem Rework.
- Planung (KI-Handoff, Unterrichtsplan S2610) und bestehendes Material U3-U6 liegen im Google Drive, nicht im Repo.

## Regeln
- Das Repo ist oeffentlich: keine Musterloesungen, Quiz-Loesungen, Kontrollwerte, Credentials oder Personendaten committen. Wenn ein Auftrag das verlangt, im Issue nachfragen.
- Neue Uebungen duerfen nicht mit Buchaufgaben identisch sein (deren Loesungen liegen hier im Repo).
- Sprache: Deutsch (Schweiz, kein ß). Keine Emojis, keine Gedankenstriche als Satzzeichen.
- Code pruefen, bevor er als verifiziert gilt: Python mit `python3` ausfuehren; SQL gegen MySQL 8 (auf dem GitHub-Runner: `sudo systemctl start mysql.service`, Login `root`/`root`).
