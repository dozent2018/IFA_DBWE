# 07 Repo: Flask/, microblog, Root-Dateien

Inventar fuer den Rework DBWE.TA1A. Stand der Pruefung: 29.09.2026. Gepruefter Repo-Stand: `main` = `9cf489a` (21.01.2024), Arbeitsbranch `claude/youthful-thompson-0r4o22`.
Smoke-Tests liefen ausschliesslich in Kopien im Scratchpad (`.../scratchpad/flask_run/`), im Repo wurde ausser dieser Datei nichts angelegt oder geaendert.

Inhalt:

1. Gelesener Umfang
2. Root, Git-Historie, Branches, microblog
3. Inventar Flask pro Kapitel
4. Legacy-API-Liste mit aktueller Schreibweise
5. Smoke-Test-Protokoll (Flask 3.x)
6. Deployment-Config-Review (kap-13)
7. Abgleich mit dem KI-Handoff v2.0
8. Findings

---

## 1. Gelesener Umfang

Alle zugewiesenen Dateien wurden vollstaendig gelesen.

| Bereich | Dateien | Zeilen | Status |
|---|---|---|---|
| Root | `README.md`, `.gitignore`, `.gitignore 2` | 11 / 7 / 6 | vollstaendig gelesen |
| Root (neu im Fork, nicht Lehrmittel) | `CLAUDE.md`, `.github/workflows/claude.yml` (Commit `1ea756c` vom 29.09.2026, waehrend der Pruefung hinzugekommen) | 15 / 56 | gesichtet, nicht Teil dieses Inventars |
| microblog | Gitlink (Mode 160000), kein Inhalt im Repo | 0 | Commit-Ziel ueber Upstream geprueft |
| Flask/kap-1 | 6 HTML-Dateien | 267 | vollstaendig gelesen, mit html5lib geparst |
| Flask/kap-2 | 3 Python-Dateien | 28 | vollstaendig gelesen, getestet |
| Flask/kap-3 | 3 Python-Dateien, 7 Templates | 141 | vollstaendig gelesen, getestet |
| Flask/kap-13 | `config.py`, `microblog.conf`, `microblog.nginx` | 79 | vollstaendig gelesen, Review |
| Flask/kap-14 | `app/__init__.py`, `api.py`, `errors.py`, `models.py` | 377 | vollstaendig gelesen, getestet |
| Flask/kap-15 | 5 Python-Dateien, 9 Templates | 377 | vollstaendig gelesen, getestet |
| Summe Flask/ | 40 Dateien | 1269 | alle gelesen |
| Zusaetzlich (Git-Historie) | Commit `877e509`, Pfad `Flask/kap-14/kap-15/app/`: `routes.py`, `forms.py`, `email.py` und 13 Templates (per `git archive` ins Scratchpad) | 909 inkl. der 4 mit kap-14 identischen Dateien | vollstaendig gelesen, getestet |
| Handoff v2.0 | Zeilen 40-100 und 543-976 | | gelesen und abgeglichen |

Zeilen pro Datei stehen in den Tabellen in Abschnitt 3.

---

## 2. Root, Git-Historie, Branches, microblog

### 2.1 README.md

- 11 Zeilen, Englisch, drei Abschnitte (SQL, Python, Flask = "1st/2nd/3rd part of the course").
- Fehlt: Zuordnung `kap-N` zu den Kapiteln des Lehrmittels FLASK, Setup-Hinweise (venv, Pakete, Python-Version), Hinweis auf den Ordner `microblog`, Lizenz.
- Im Repo gibt es keine `LICENSE`. Der Code in kap-14/kap-15 ist erkennbar vom microblog-Tutorial abgeleitet, das unter MIT-Lizenz (Copyright Miguel Grinberg) steht; ein Attributionshinweis fehlt (siehe FL-F24).

### 2.2 .gitignore und ".gitignore 2"

| Datei | Inhalt | Wirkung |
|---|---|---|
| `.gitignore` | 4 auskommentierte Pfade (`#**/Flask/kap-2/myenv` usw.), aktiv: `**__pycache__`, `**myenv`, `**tutorial` | wirksam fuer `__pycache__`, Ordner namens `myenv` und `tutorial` (mit `git check-ignore` geprueft) |
| `.gitignore 2` | identisch bis auf die fehlende Zeile `**tutorial` | wirkungslos, Git liest nur Dateien namens `.gitignore`. Typisches macOS-Finder-Duplikat ("Datei 2"), eingecheckt mit Commit `6b343ce` (11.07.2022). Im selben Muster existiert `Python/kap-17/file_name 2` (ausserhalb dieses Bereichs). |

Mit `git check-ignore --no-index` geprueft und **nicht** ignoriert: `venv/`, `.venv/`, `.env`, `*.db` (z. B. `app.db`), `instance/`, `logs/`. Fuer ein oeffentliches Repo und fuer die Vorbildwirkung in U12 (Quiz-Frage zu `.gitignore`) ist das zu duenn (FL-F17). Aktuell sind keine `.pyc`, `.env`, `.db` oder venv-Dateien getrackt; frueher eingecheckte `__pycache__`-Dateien wurden 2022 entfernt (Commits `869ea9a`, `4fdf321`).

### 2.3 Git-Historie

| Kennzahl | Wert |
|---|---|
| Commits auf `main` | 56 (davon 2 Merge-Commits) |
| Zeitraum | 20.01.2022 bis 21.01.2024 |
| Verteilung | 2022: 52, 2023: 3, 2024: 1 |
| Autoren | ausschliesslich Lehrmittelautor (3 Identitaeten: zwei Git-Namen, ein GitHub-Webkonto) |
| Upstream | im Handoff genannt: github.com/dozent2018/IFA_DBWE; lokales `origin` ist der oeffentliche Fork |
| Zusaetzlich im Fork | 1 Commit vom 29.09.2026 auf dem Arbeitsbranch (CLAUDE.md, GitHub-Action), nicht Lehrmittelstand |

Historie pro Flask-Kapitel (Branch `main`):

| Ordner | erster Commit | letzter Commit | Commits |
|---|---|---|---|
| Flask/kap-1 | 27.02.2022 | 28.02.2022 | 4 |
| Flask/kap-2 | 28.02.2022 | 04.05.2022 | 7 |
| Flask/kap-3 | 07.03.2022 | 21.01.2024 | 6 |
| Flask/kap-13 | 11.07.2022 | 11.07.2022 | 1 |
| Flask/kap-14 | 04.05.2022 | 04.05.2022 | 2 |
| Flask/kap-15 | 04.05.2022 | 11.07.2022 | 3 |

Wichtig: Der Flask-Code stammt aus **2022** (Werkzeug-2.x-Aera). Der einzige Flask-Commit von 2024 aendert in `Flask/kap-3/app/routes.py` nur, welche `return`-Zeile aktiv ist. Die Handoff-Aussage "Repo-Code stammt von Anfang 2024" (Handoff Z. 85, 555, 654, 859) ist fuer Flask zu korrigieren (FL-F25).

Auffaellige Historie (relevant fuer fehlende Dateien, siehe 3.8): Commit `877e509` (04.05.2022, "Kapitel 13-15") legte unter `Flask/kap-14/kap-15/app/` eine **vollstaendige** microblog-App an (routes.py 196 Zeilen, forms.py, email.py, Bootstrap-Templates, Passwort-Reset-Mails). `2510ab3` verschob sie nach `Flask/kap-15/app/`, `4fdf321` loeschte sie am selben Tag, `2b760a4` (11.07.2022) legte `Flask/kap-15/app/` mit einem frueheren, kleineren Stand neu an. `api.py`, `errors.py`, `models.py`, `__init__.py` des historischen Vollstands sind byte-identisch mit dem heutigen `Flask/kap-14/app/`.

### 2.4 Branches

| Branch | Stand |
|---|---|
| `main` (lokal) = `origin/main` | `9cf489a`, 21.01.2024 |
| `claude/youthful-thompson-0r4o22` (lokal, aktuell) und `origin/...` | `main` + 1 Commit vom 29.09.2026 |

Keine weiteren Branches, keine Tags.

### 2.5 microblog (Gitlink ohne .gitmodules)

Befund:

- `microblog` ist ein Gitlink (Mode 160000) auf Commit `68368ea5c5e4b674e7661ef06891c1fb813588c8`, hinzugefuegt mit Commit `9cf489a` ("Changes January 2024", 21.01.2024) als einzige Aenderung ausserhalb von SQL/Python/kap-3.
- Es gibt keine `.gitmodules` und keinen Eintrag in `.git/config`. `git submodule status` bricht ab ("no submodule mapping found in .gitmodules for path 'microblog'").
- Der Commit-Hash existiert nicht im IFA_DBWE-Repo selbst.

Worauf zeigt der Gitlink? Per `git fetch` des einzelnen Commits aus dem oeffentlichen Repo von Miguel Grinberg (github.com/miguelgrinberg/microblog, lesend im Scratchpad) verifiziert:

- `68368ea` = "Chapter 4: Database (v0.4)", Autor Miguel Grinberg, Autorendatum 11.09.2017, Committerdatum 10.07.2021.
- Inhalt: microblog auf Stand Tutorial-Kapitel 4 (config.py mit Fallback-SECRET_KEY und SQLite-Fallback, Models User/Post im `db.Column`-Stil, `migrations/` mit 2 Revisionen, `.flaskenv`, MIT-LICENSE).
- Der Commit ist in keinem aktuellen Branch mehr erreichbar (`main` und `2023` geprueft). Grinberg hat seine Historie mehrfach umgeschrieben; Tag `v0.4` zeigt heute auf `d86cf37` (neu signiert Dezember 2023). `68368ea` war der Stand von `v0.4` zwischen Juli 2021 und November 2023 und ist derzeit nur noch per SHA abrufbar (GitHub kann unerreichbare Objekte jederzeit aufraeumen).

Interpretation (Annahme): Der Lehrmittelautor hatte einen lokalen Klon von microblog auf Tag `v0.4` im Arbeitsverzeichnis und hat ihn mit `git add .` versehentlich als eingebettetes Repo eingecheckt.

Konsequenzen:

- `git clone`, GitHub-ZIP-Download und `git submodule update --init` liefern einen **leeren** Ordner `microblog/` (lokal bestaetigt); auf GitHub erscheint ein nicht anklickbares Submodul-Symbol.
- Studierende koennten den Ordner fuer die Referenz-App halten; der referenzierte Stand (Kapitel 4, 2017) passt ohnehin nicht zum Kursstand (Units 8-15).
- Kein Datenverlust fuer den Kurs: Der Inhalt ist nicht Teil des Lehrmittel-Codes und wird im Handoff nicht verwendet.

Empfehlung: Gitlink entfernen (`git rm --cached microblog`, nur mit Auftrag) und im README auf das Grinberg-Repo mit konkretem Tag verlinken, oder, falls ein Referenzstand gewuenscht ist, als echtes Submodul mit `.gitmodules` und stabilem Tag einbinden. Entscheid durch Kursverantwortung (FL-F03).

---

## 3. Inventar Flask pro Kapitel

Legende Legacy: **Bruch** = Fehler mit Flask 3.1/Werkzeug 3.1, **Warnung** = Deprecation-/Legacy-Warnung im Test, **still** = veraltet, aber ohne Warnung lauffaehig.

### 3.1 kap-1 (statisches HTML)

| Datei | Zeilen | Zweck | Veraltetes Markup und Fehler (Datei:Zeile) | html5lib-Parsefehler |
|---|---|---|---|---|
| index.html | 33 | Startseite, Ueberschriften, Absatz, Links | `<center>` falsch verschachtelt (in `h1`/`p` geoeffnet, erst nach `<hr>` geschlossen) :8-10; Entities ohne Semikolon (`&lth2&gt`) :11-18; `<html>` ohne `lang` :2; `meta http-equiv` statt `meta charset` :4 | 16 |
| listen.html | 33 | ul/ol | `<center>` :8-10; Entities ohne `;` :12-24; `<b>` statt `<strong>` :12, :22; `<br><br>` als Abstand :31 | 18 |
| textformate.html | 23 | Textauszeichnungen | kein `h1`, kein `</html>` (endet :24); `<br><br>` :22; Tippfehler "verschieden" :8 | 0 |
| tabellen.html | 49 | einfache Tabelle | `<center>` :8-10; Entities ohne `;`; Tabelle ohne `thead`/`caption`/`scope` :21-42; `&nbsp;&nbsp;&nbsp;` als Abstand :47 | 18 |
| tabellen-css.html | 52 | Tabelle mit internem CSS | `<center>` :18-20; **CSS-Fehler** `align: left` (keine CSS-Eigenschaft, gemeint `text-align`) :12, der Text :25-26 verspricht aber Linksausrichtung | 6 |
| style-css.html | 77 | CSS inline/intern | `<center>` :37-39; Tippfehler "tyle fuer Parafen" :74; Inline-Styles (didaktisch gewollt) :62-73 | 16 |

Gesamtbild: Alle 6 Dateien haben `<!DOCTYPE html>`, "fehlender Doctype" trifft also nicht zu. Es fehlen durchgehend `lang`, `meta charset` (Kurzform), `viewport` und semantische Elemente (`header`, `nav`, `main`, `footer`). `<font>` und Layout-Tabellen kommen **nicht** vor. Summe: 74 Parsefehler (html5lib, nicht strikt). Fachbeispiele nennen alte IFA-Faecher/Lehrgaenge (SYEN, LUBG, ITBM, HFSNT, HFWI).

Handoff-Aussage "Bewusst nicht verwenden: veraltetes Markup (`<center>`, fehlende Struktur)" (Z. 81, 555): **bestaetigt**, mit Praezisierung: nicht der Doctype fehlt, sondern Semantik, `lang`, korrekte Verschachtelung und Entity-Syntax. Option: kap-1 als K4-Analyseuebung "Validieren und modernisieren" (W3C-Validator) einsetzen statt ganz zu verwerfen.

### 3.2 kap-2 (erste Flask-App, ohne Templates)

| Datei | Zeilen | Zweck | Abhaengigkeiten | Legacy | Security | Bemerkungen |
|---|---|---|---|---|---|---|
| hello_flask.py | 2 (davon 1 Kommentar) | Einstiegsmodul, `from app import app` | Flask | keine | keine | keine Newline am Dateiende |
| app/\_\_init\_\_.py | 5 | App-Objekt ohne Factory, Import der Routen am Ende | Flask | keine | kein SECRET_KEY (hier nicht noetig) | Muster "zirkulaerer Import am Dateiende" wie Lehrmittel |
| app/routes.py | 22 | Routen `/`, `/index`, `/user/<name>`, `/useragent`, `/appname` | Flask (`request`, `current_app`) | keine | **Reflected XSS**: URL-Parameter :10 und User-Agent :16 werden unescaped per `str.format` in HTML eingesetzt (im Test bestaetigt) | Imports mitten in der Datei :12, :18; Einrueckung 2 statt 4 Leerzeichen :10 |

Fehlend fuer Lauffaehigkeit: nichts ausser `pip install flask`. Kein `requirements.txt`, kein `.flaskenv`.

### 3.3 kap-3 (Jinja2-Templates)

| Datei | Zeilen | Zweck | Befunde (Datei:Zeile) |
|---|---|---|---|
| hello_flask.py | 2 | Einstiegsmodul | Kommentar nennt `kap-2/hello_flask.py` :1 (Kopierfehler) |
| app/\_\_init\_\_.py | 5 | wie kap-2 | keine |
| app/routes.py | 36 | 4 Testrouten: `/`+`/index` (hello_user), `/looptest`, `/macrotest`, `/inheritance` | fester Vorname als Beispielwert :9, :17, :27; Varianten mit `hello_if.html` nur auskommentiert :11-12 (keine aktive Route) |
| templates/base.html | 15 | Basis-Template mit Bloecken `head`, `title`, `body` | HTML-Kommentar vor `<!doctype>` :1 (landet in jeder abgeleiteten Seite); kein `lang` :3 |
| templates/hello_derived.html | 12 | Vererbung, `super()` | leerer `<style>`-Block :6-7 |
| templates/hello_for.html | 19 | Schleife | `<p>` statt `</p>` :14; kein charset |
| templates/hello_if.html | 19 | Bedingung | nicht ueber Route erreichbar; kein charset |
| templates/hello_macro.html | 16 | Makro-Import | Kommentar nennt `hello_macros.html` :1; `{% import %}` vor `<head>` :4; kein charset |
| templates/hello_user.html | 12 | Variable im Template | **`</h1` ohne `>`** :9 (verschluckt `</body>`, 3 Parsefehler) |
| templates/macros.html | 6 | Makro `render_line` | keine |

Abhaengigkeiten: nur Flask/Jinja2. Keine Legacy-APIs, keine Security-Themen (Jinja2-Autoescaping aktiv). Empfehlung: Struktur 1:1 uebernehmen (Handoff), Inhalt bereinigen; Datei-Kommentare als Jinja-Kommentare `{# ... #}` schreiben.

### 3.4 kap-13 (Deployment-Konfiguration)

| Datei | Zeilen | Zweck | Abhaengigkeiten | Security |
|---|---|---|---|---|
| config.py | 21 | Server-config mit `.env` via python-dotenv | python-dotenv, `os` | keine Secrets im Code; SECRET_KEY und DATABASE_URL ohne Fallback :12-13; Platzhalter-Adresse fuer ADMINS vorhanden :20 |
| microblog.conf | 10 | Supervisor-Programm fuer Gunicorn (4 Worker, autostart/autorestart) | supervisor, gunicorn | laeuft als unprivilegierter User :5 |
| microblog.nginx | 48 | Nginx: Port 80 mit `/.well-known` und 301-Redirect, Port 443 mit Let's-Encrypt-Pfaden, `proxy_pass` auf Gunicorn, `/static` direkt | nginx, certbot | TLS nur mit Nginx-Defaults, kein HSTS, kein `X-Forwarded-Proto` |

Detailreview in Abschnitt 6.

### 3.5 kap-14 (REST-API, Endstand Units 14-15)

| Datei | Zeilen | Zweck | Abhaengigkeiten | Legacy (Datei:Zeile) | Security |
|---|---|---|---|---|---|
| app/\_\_init\_\_.py | 49 | App ohne Factory; SQLAlchemy, Migrate, LoginManager, Mail, Bootstrap; Mail- und Datei-Logging im Nicht-Debug-Modus | flask, flask_sqlalchemy, flask_migrate, flask_login, **flask_mail**, **flask_bootstrap**, `config` | Flask-Bootstrap 3.3.7.1 (Bootstrap 3, jQuery 1.12) :9, :19 (still) | Log-Datei relativ zum Arbeitsverzeichnis :37-39; importiert `routes` :49, das **fehlt** |
| app/api.py | 117 | GET users, user, followers, followed, posts; POST users; PUT user; POST/DELETE tokens; Auth-Callbacks | flask, flask_httpauth | `User.query.get_or_404` :16, :29, :36, :43, :72 (Warnung); `query.filter_by().first()` :53, :55, :75, :78, :104 (still) | Token-Auth auf allen Endpunkten, auch `POST /api/users` :48 (Registrierung per API nur mit bestehendem Token); PUT-Besitzpruefung via `token_auth.current_user()` :70; `abort(403)` liefert HTML :71; `request.get_json()` ohne JSON-Content-Type liefert 415 HTML :50, :73; doppelter Import :4/:7 |
| app/errors.py | 34 | 404/500 mit Content-Negotiation, `error_response()`, `bad_request()` | flask, werkzeug.http | keine | Negotiation liefert bei `Accept: */*` (curl-Default) HTML statt JSON :7-8, :18-19; kein Handler fuer 403/405/415 |
| app/models.py | 177 | followers-Tabelle, User (Passwort, Avatar, follow, followed_posts, Reset-JWT, to_dict/from_dict, Collections, Token), Post | werkzeug.security, flask_login, **PyJWT** :6, hashlib, base64, os | `db.Column`-Stil ohne `Mapped` (alle Spalten); `backref` + `lazy='dynamic'` :25, :32; `Query.get` :81, :150 (Warnung); `datetime.utcnow` :27, :132, :140, :144, :156 (Warnung); `Post.query.join().union()` :63-67, `query.all()` :124, :174 (still) | Hash-Spalte `String(128)` :24 zu kurz fuer scrypt (162 Zeichen); Token im Klartext in DB, `base64` aus `os.urandom` (nicht URL-sicher) :135; nacktes `except:` :79; MD5 fuer Gravatar :46; Post-Link falsch :165 |

Fehlend fuer Lauffaehigkeit: `app/routes.py`, `app/forms.py`, `app/email.py`, `app/templates/` (inkl. `bootstrap/`-basierter Templates und `email/`), `config.py`, `microblog.py`, `migrations/`, `requirements.txt`, `.env`-Vorlage. Import scheitert unveraendert mit `ModuleNotFoundError: flask_mail`, nach Installation mit `ImportError` (zirkulaerer Import wegen fehlendem `routes`). Alle fehlenden App-Dateien sind in Commit `877e509` vorhanden (3.8).

### 3.6 kap-15 (Login, Profil, Avatar, Fehlerseiten)

| Datei | Zeilen | Zweck | Abhaengigkeiten | Legacy (Datei:Zeile) | Security / Bugs |
|---|---|---|---|---|---|
| app/\_\_init\_\_.py | 14 | App, SQLAlchemy, Migrate, LoginManager (`login_view='login'`) | flask, flask_sqlalchemy, flask_migrate, flask_login, `config` | keine | importiert `routes, models`, aber **nicht `errors`** :14, eigene 404/500-Seiten sind inaktiv |
| app/errors.py | 15 | 404/500-Handler mit Rollback | flask | keine | wird nie registriert (siehe oben) |
| app/forms.py | 38 | LoginForm, RegistrationForm (Custom-Validatoren), EditProfileForm | flask_wtf, wtforms, **email_validator** (fuer `Email()`) | `User.query.filter_by().first()` :25, :30 (still) | EditProfileForm ohne Eindeutigkeitspruefung :35-38; keine Laengenvalidatoren passend zu `String(64/120)` |
| app/models.py | 44 | User (UserMixin, set/check_password, avatar), Post | werkzeug.security, flask_login, hashlib | `db.Column`-Stil; `backref`/`lazy='dynamic'` :13; `datetime.utcnow` :15, :40 (Warnung); `Query.get` :34 (Warnung) | Hash-Spalte `String(128)` :12; MD5-Gravatar :27 |
| app/routes.py | 98 | before_request (last_seen), index (Platzhalterposts), login, logout, register, user, edit_profile | flask, flask_login, **werkzeug.urls** | **`from werkzeug.urls import url_parse` :4, :46 (Bruch: ImportError)**; `datetime.utcnow` :13 (Warnung); `first_or_404` :76, `filter_by().first()` :40 (still) | CSRF via Flask-WTF aktiv; `next`-Pruefung :45-47 wirksam; Logout per GET :52; Profil-Duplikat fuehrt zu IntegrityError/500 :89-91; englische Platzhalterposts mit fiktiven Namen :21-30 |
| templates/base.html | 33 | Navigation, Flash-Messages, Block `content` | Jinja2, flask_login (`current_user`) | keine | kein charset/lang/viewport; `url_for('login')` :15, `url_for('logout')` :18 (relevant fuer Starter U10.1) |
| templates/index.html | 8 | Begruessung und Posts | | | |
| templates/_post.html | 6 | Post mit Avatar | | `valign` (obsolet) :2 | Tabellenlayout; `img` ohne `alt` :3 |
| templates/user.html | 21 | Profil mit Avatar 128px, about_me, last_seen | | `valign` :5 | Tabellenlayout; `img` ohne `alt` :6; `last_seen` roh formatiert :10 |
| templates/edit_profile.html | 23 | Formular | Flask-WTF | | `form.hidden_tag()` (CSRF) vorhanden |
| templates/login.html | 25 | Formular mit `novalidate` | | | |
| templates/register.html | 37 | Formular | | | |
| templates/404.html | 7 | Fehlerseite | | | HTML-Kommentar vor `extends` :1 |
| templates/500.html | 8 | Fehlerseite | | | wie 404 |

Inhaltlicher Stand: entspricht etwa microblog-Tutorial Kapitel 5 bis 7 (Login, Profil, Avatare, Fehlerseiten ohne Logging), also **frueher** als kap-14. Die Ordnernummer entspricht nicht der Tutorial-Reihenfolge; die Zuordnung zu den Kapiteln des Lehrmittels FLASK ist im Repo nicht dokumentiert (Annahme: mit Inhaltsverzeichnis FLASK verifizieren).

Fehlend fuer Lauffaehigkeit: `config.py`, `microblog.py` (Einstiegsmodul), `migrations/`, `requirements.txt`, `.env`/`.flaskenv`, Registrierung von `errors`. Mit Flask 3 zusaetzlich zwingend: Fix von `url_parse`.

### 3.7 Lauffaehigkeit im Ueberblick

| Kapitel | Unveraendert lauffaehig (Flask 3.1)? | Minimal noetig |
|---|---|---|
| kap-2 | ja | `pip install flask` |
| kap-3 | ja | `pip install flask` |
| kap-13 | nicht eigenstaendig (Konfigurationsdateien) | App, `.env`, gunicorn, nginx, supervisor, certbot |
| kap-14 | **nein** (fehlende Pakete, fehlende `routes.py`) | Pakete flask-mail, flask-bootstrap, pyjwt, flask-httpauth; `routes.py`/`forms.py`/Templates (kap-15 oder Historie); `config.py` mit DB-URI; `microblog.py`; `url_parse`-Fix |
| kap-15 | **nein** (`config.py` fehlt, danach ImportError `url_parse`) | `config.py` mit DB-URI und SECRET_KEY; `microblog.py`; `url_parse`-Fix; empfohlen: `errors` importieren |

### 3.8 Historischer Vollstand (Commit 877e509)

| Datei (historisch) | Zeilen | Bedeutung |
|---|---|---|
| routes.py | 196 | index mit PostForm und Pagination, explore, login/logout/register, Passwort-Reset, user mit Pagination, edit_profile (mit Eindeutigkeitspruefung), follow/unfollow per POST mit EmptyForm |
| forms.py | 69 | zusaetzlich ResetPassword-Formulare, EditProfileForm mit `original_username`, EmptyForm, PostForm |
| email.py | 27 | Flask-Mail, Versand im Thread |
| templates/ (13 Dateien) | 240 | Flask-Bootstrap-Basis (`bootstrap/base.html`, `wtf.quick_form`), Pager, Mail-Templates |

Legacy im historischen Stand: `url_parse` :4 (Bruch), `paginate(page, per_page, False)` mit Positionsargumenten :31-32, :46-47, :131-132 (**Bruch**: TypeError mit Flask-SQLAlchemy 3.x), `super(EditProfileForm, self)` (still). Nach zwei Minimal-Patches voll lauffaehig (Abschnitt 5.5). Dieser Stand ist die beste Quelle, um kap-14 zu einer lauffaehigen Referenz zu ergaenzen.

---

## 4. Legacy-API-Liste mit aktueller Schreibweise

Fundstellen im aktuellen Repo, ergaenzt um den historischen Stand (H = Commit 877e509). Wirkung gemessen mit Python 3.12.3, Flask 3.1.3, Werkzeug 3.1.9, Flask-SQLAlchemy 3.1.1, SQLAlchemy 2.1.1.

| Nr | Legacy-Schreibweise | Fundstellen | Wirkung im Test | Aktuelle Schreibweise |
|---|---|---|---|---|
| L1 | `from werkzeug.urls import url_parse` | kap-15 routes.py:4, :46; H routes.py:4 | **ImportError** (Bruch) | `from urllib.parse import urlsplit`, dann `urlsplit(next_page).netloc` |
| L2 | `query.paginate(page, per_page, False)` | nur H routes.py:31-32, :46-47, :131-132 | **TypeError** (Bruch) | `db.paginate(query, page=page, per_page=n, error_out=False)` oder Keyword-Argumente |
| L3 | `User.query.get(id)` | kap-14 models.py:81, :150; kap-15 models.py:34 | LegacyAPIWarning | `db.session.get(User, id)` |
| L4 | `User.query.get_or_404(id)` | kap-14 api.py:16, :29, :36, :43, :72 | LegacyAPIWarning (intern `Query.get`) | `db.get_or_404(User, id)` |
| L5 | `query.filter_by(...).first()` | kap-14 api.py:53, :55, :75, :78, :104, models.py:143; kap-15 forms.py:25, :30, routes.py:40 | still | `db.session.scalar(sa.select(User).where(User.username == name))` |
| L6 | `query.filter_by(...).first_or_404()` | kap-15 routes.py:76 | still | `db.first_or_404(sa.select(User).where(User.username == name))` |
| L7 | `Model.query.all()`, `Post.query.join(...).union(...)` | kap-14 models.py:124, :174, :63-67 | still | `db.session.scalars(sa.select(User)).all()`; `sa.select(Post).join(...).where(...)` |
| L8 | `db.Column(...)` ohne Typannotation | alle Models kap-14/kap-15 | still | `id: so.Mapped[int] = so.mapped_column(primary_key=True)` |
| L9 | `db.relationship(..., backref=..., lazy='dynamic')` mit `.count()`/`.filter()` | kap-14 models.py:25, :32, :59-60, :89-91; kap-15 models.py:13 | still | `so.WriteOnlyMapped[...]` mit `back_populates=`; Zaehlen per `sa.select(sa.func.count())` |
| L10 | `datetime.utcnow` (als Default und im Code) | kap-14 models.py:27, :132, :140, :144, :156; kap-15 models.py:15, :40, routes.py:13 | DeprecationWarning (Python 3.12) | `datetime.now(timezone.utc)`, als Default `lambda: datetime.now(timezone.utc)`. **Achtung:** SQLite liefert naive Werte zurueck; Vergleich aware/naive in models.py:133, :144 wirft TypeError (getestet). Kasten muss `.replace(tzinfo=timezone.utc)` beim Lesen zeigen. |
| L11 | `password_hash = db.Column(db.String(128))` | kap-14 models.py:24; kap-15 models.py:12 | still in SQLite; in MySQL-Strict-Mode Fehler (Hash 162 Zeichen, gemessen) | `String(256)` |
| L12 | Flask-Bootstrap 3.3.7.1 (`flask_bootstrap.Bootstrap`) | kap-14 \_\_init\_\_.py:9, :19; H templates | lauffaehig, laedt Bootstrap 3.3.7 und jQuery 1.12.4 | Bootstrap-Flask (`Bootstrap5`) oder Bootstrap 5.3 per CDN |
| L13 | `request.get_json() or {}` | kap-14 api.py:50, :73 | ohne JSON-Content-Type 415 (HTML) statt 400 (JSON) | `request.get_json(silent=True) or {}` oder 415 als JSON behandeln |
| L14 | `python -m smtpd` (Mail-Debugserver im Tutorial) | nicht im Repo, relevant fuer U12-Demo | Modul in Python 3.12 entfernt (getestet) | `aiosmtpd` (`python -m aiosmtpd -n -c aiosmtpd.handlers.Debugging`) |
| L15 | `'...'.format()`, `super(Klasse, self)` | durchgehend | still | f-Strings, `super()` (Stil) |

Nicht gefunden (geprueft per grep): `before_first_request`, `flask_script`, `jinja2.Markup`, `from flask import escape`, `flask.json.JSONEncoder`, `app.json_encoder`, `Query.paginate` im aktuellen Stand (nur Historie).

Hinweis zum Handoff (Z. 85): Die dort genannten drei Kaesten (`db.session.get()`, `datetime.now(timezone.utc)`, `Mapped[]`) decken die zwei **Brueche** (L1, L2) und die Falle bei L10/L11 nicht ab (FL-F01, FL-F02, FL-F19).

---

## 5. Smoke-Test-Protokoll (Flask 3.x)

### 5.1 Umgebung

- Ort: `.../scratchpad/flask_run/`, eigenes venv, Python 3.12.3 (`/usr/bin/python3.12 -m venv venv`), pip 26.2.1. Netz: PyPI erreichbar, `/root/.ccr/README.md` gelesen; Hosts `lab1.ifalabs.org` und `lab70.ifalabs.org` durch Egress-Policy gesperrt (403), daher nicht geprueft.
- Dauer: ca. 10 Minuten (08:55 bis 09:05 UTC), innerhalb der Time-Box.
- Installierte Versionen (`pip freeze` in `versions_freeze.txt` im Scratchpad):

| Paket | Version | Paket | Version |
|---|---|---|---|
| Flask | 3.1.3 | Flask-Login | 0.6.3 |
| Werkzeug | 3.1.9 | Flask-WTF | 1.3.0 |
| Jinja2 | 3.1.6 | WTForms | 3.2.2 |
| Flask-SQLAlchemy | 3.1.1 | email-validator | 2.3.0 |
| SQLAlchemy | 2.1.1 | Flask-HTTPAuth | 4.8.1 |
| Flask-Migrate | 4.1.0 | python-dotenv | 1.2.3 |
| Alembic | 1.20.0 | Flask-Mail | 0.10.0 (fuer kap-14) |
| PyJWT | 2.15.1 (fuer kap-14) | Flask-Bootstrap | 3.3.7.1 (fuer kap-14) |
| gunicorn | 26.2.0 (Deployment-Check) | html5lib | 1.1 (HTML-Pruefung) |

### 5.2 kap-2 und kap-3 (unveraendert, Flask-Testclient)

| App | Route | Status | Ergebnis |
|---|---|---|---|
| kap-2 | `/`, `/index` | 200 | Text "Hello, Flask!" |
| kap-2 | `/user/<name>` | 200 | Name wird **unescaped** eingesetzt; `<img onerror=...>` erscheint roh im HTML (XSS bestaetigt) |
| kap-2 | `/useragent` | 200 | User-Agent roh im HTML (XSS bestaetigt) |
| kap-2 | `/appname` | 200 | liefert "app" |
| kap-3 | `/`, `/index` | 200 | hello_user.html rendert (3 Parsefehler wegen `</h1`) |
| kap-3 | `/looptest` | 200 | hello_for.html rendert |
| kap-3 | `/macrotest` | 200 | Makro rendert |
| kap-3 | `/inheritance` | 200 | Vererbung mit `super()` rendert |
| kap-3 | hello_if.html (ohne Route, direkt gerendert) | ok | Zweig "stranger" rendert |
| beide | unbekannte Route | 404 | Flask-Standardseite |

Keine Warnungen. `flask routes` findet die App **auch ohne** `FLASK_APP`/`--app`, weil Flask als Fallback das Paket `app` importiert (relevant fuer den Troubleshooting-Kasten U8.2: `FLASK_APP` ist hier nicht die typische Ursache; `hello_flask.py` wird dabei gar nicht benutzt).

### 5.3 kap-15

Aufbau: Kopie von `kap-15/app` plus `kap-13/config.py` (unveraendert) plus einzeiliges `microblog.py`.

| Stufe | Ergebnis |
|---|---|
| ohne `.env` | `RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set.` (Flask-SQLAlchemy 3.x hat keinen Default mehr) |
| mit `DATABASE_URL` (SQLite) | `ImportError: cannot import name 'url_parse' from 'werkzeug.urls'` |
| Patch P1: `url_parse` durch `urlsplit` ersetzt; `.env` mit Dummy-SECRET_KEY und SQLite-URI | App importiert, `db.create_all()` legt `user`, `post` an |

Routen nach Patch P1:

| Aufruf | Status | Beobachtung |
|---|---|---|
| GET `/` anonym | 302 auf `/login?next=%2F` | `login_required` wirkt |
| GET `/register` | 200 | CSRF-Token im Formular vorhanden |
| POST `/register` ohne CSRF-Token | 200 | Formular wird nicht akzeptiert (CSRF wirkt) |
| POST `/register` gueltig | 302 auf `/login` | User angelegt; Hash-Methode `scrypt:32768:8:1`, **Laenge 162** bei Spalte `String(128)` |
| POST `/register` Duplikat | 200 | Custom-Validator-Meldung sichtbar |
| POST `/login` falsches Passwort | 302 auf `/login` | Flash-Meldung |
| POST `/login?next=/edit_profile` | 302 auf `/edit_profile` | `next` funktioniert |
| POST `/login?next=//fremde-domain` | 302 auf `/index` | Open-Redirect-Schutz wirkt; Variante mit Backslash wird von Werkzeug kodiert, kein Bypass |
| GET `/`, `/user/<name>`, `/edit_profile` eingeloggt | 200 | Gravatar-URL im HTML |
| GET `/user/<unbekannt>` | 404 | `first_or_404` wirkt |
| POST `/edit_profile` about_me | 302 | gespeichert |
| POST `/edit_profile` mit existierendem Username | **500** | `IntegrityError: UNIQUE constraint failed: user.username` |
| GET `/logout` | 302 | |
| GET unbekannte Route | 404 | **Flask-Standardseite**, eigenes `404.html` inaktiv (errors nicht importiert) |

Warnungen: `DeprecationWarning datetime.utcnow` (SQLAlchemy-Default aus models.py:15/:40 und routes.py:13), `LegacyAPIWarning Query.get()` (models.py:34).

Flask-Migrate: `flask --app microblog db init`, `db migrate`, `db upgrade` laufen fehlerfrei (Tabellen user, post, 3 Indizes erkannt). Relativer SQLite-Pfad (`sqlite:///x.db`) landet in `instance/`, nicht im Projektordner (Verhalten seit Flask-SQLAlchemy 3.0).

Gunicorn-Check (Deployment-Kette): `gunicorn -b localhost:8765 -w 2 microblog:app` auf der gepatchten Kopie startet, bindet auf 127.0.0.1, `/login` liefert 200.

### 5.4 kap-14 (Variante A: kap-14 plus routes/forms/templates aus kap-15)

| Stufe | Ergebnis |
|---|---|
| unveraendert, nur Basispakete | `ModuleNotFoundError: No module named 'flask_mail'` |
| plus flask-mail, flask-bootstrap, pyjwt | `ImportError: cannot import name 'routes' from partially initialized module 'app'` (Datei fehlt) |
| plus `routes.py` (mit Patch P1), `forms.py`, `templates/` aus kap-15, config wie 5.3 | App importiert, Tabellen `followers`, `post`, `user`; Log-Datei `logs/microblog.log` wird angelegt |

Model-Checks: `follow`, `unfollow`, `is_following`, `followed_posts` funktionieren. Token-Spalte `VARCHAR(32)`, Token hat 32 Zeichen (kann `/` und `+` enthalten).

API-Aufrufe (Testclient):

| Aufruf | Status | Content-Type | Beobachtung |
|---|---|---|---|
| GET `/api/users` ohne Token | 401 | JSON | `{"error": "Unauthorized"}` |
| POST `/api/tokens` falsches Passwort | 401 | JSON | |
| POST `/api/tokens` Basic Auth | 200 | JSON | Token; zweiter Bezug liefert denselben Token (Gueltigkeit > 60 s) |
| GET `/api/users`, `/api/users/1` | 200 | JSON | `_links` relativ, Avatar-URL absolut |
| GET `/api/users/1/followed`, `/2/followers`, `/1/posts` | 200 | JSON | Posts: `timestamp` im HTTP-Datumsformat, Links `_external` mit `http://` |
| GET `/api/users/999` mit `Accept: */*` (curl-Default) | 404 | **HTML** | 404.html statt JSON |
| GET `/api/users/999` mit `Accept: application/json` | 404 | JSON | |
| POST `/api/users` leer | 400 | JSON | Pflichtfeld-Meldung |
| POST `/api/users` Duplikat | 400 | JSON | Eindeutigkeits-Meldung |
| POST `/api/users` ohne Token | 401 | JSON | Registrierung per API nur mit Token |
| POST `/api/users` gueltig | 201 | JSON | `Location: /api/users/3` (relativ, zulaessig) |
| POST `/api/users` form-encoded bzw. ohne Content-Type | **415** | **HTML** | statt 400 JSON |
| PUT `/api/users/1` eigener User | 200 | JSON | |
| PUT `/api/users/2` fremder User | 403 | **HTML** | kein JSON-Handler fuer 403 |
| PUT `/api/users/1` Username-Duplikat | 400 | JSON | |
| DELETE `/api/tokens` | 204 | | danach GET mit altem Token 401 |

Zusatzbefunde:

- `Post.to_dict()` erzeugt falschen `url`-Link: Post 1 eines Users mit ID 2 verweist auf `/api/users/1/posts` (Post-ID wird als User-ID verwendet, models.py:165).
- Mit Header `X-Forwarded-Proto: https` bleiben `_external`-Links `http://` (kein ProxyFix; Nginx setzt den Header ohnehin nicht).

Warnungen: `DeprecationWarning datetime.utcnow` (models.py:132, :140, :144 und Defaults), `LegacyAPIWarning Query.get()` (ueber `get_or_404`).

Simulationen fuer den Handoff (je eigene Kopie):

| Simulation | Ergebnis |
|---|---|
| U14.2-Starter: `api.py` entfernt, TN-Loesung mit nur 3 GET-Endpunkten (Liste, Einzel, Posts) | GET `/api/users` und `/api/users/1`: **500**, `BuildError: Could not build url for endpoint 'get_followers'` (to_dict verlinkt followers/followed) |
| U15.1-Musterloesung "api.py ohne Auth-Decorator" | POST `/api/users` 201; PUT `/api/users/1`: **500**, `AttributeError: 'NoneType' object has no attribute 'id'` (api.py:70) |
| U11.1-Tests (Passwort, Avatar, follow/unfollow, followed_posts) mit In-Memory-SQLite, `DATABASE_URL=sqlite://` vor dem Import gesetzt | 4 Tests gruen |
| U10.1-Starter: login/logout/register-Routen und `UserMixin` entfernt | `/`, `/user/x`, `/edit_profile`: **500**, `BuildError` fuer Endpoint `login` (base.html:15, `login_view`) |
| Aware-Datetime-Kasten: `token_expiration < datetime.now(timezone.utc)` | `TypeError: can't compare offset-naive and offset-aware datetimes` |

### 5.5 kap-14 (Variante B: historischer Vollstand aus Commit 877e509)

| Stufe | Ergebnis |
|---|---|
| unveraendert (mit kap-13 config, SQLite) | ImportError `url_parse` |
| Patch P1 | Login ok; `/`, `/explore`, `/user/<name>`: **500**, `TypeError: Query.paginate() takes 1 positional argument but 4 were given` |
| Patch P2 (paginate mit Keywords) | alle Web-Routen 200 (Post erstellen, explore, Profil, follow per POST, edit_profile mit Duplikatpruefung zeigt Validierungsmeldung), Bootstrap-Templates rendern; API wie Variante A |
| Passwort-Reset ohne MAIL_SERVER | Redirect 302, Mailversand scheitert im Hintergrund-Thread (`SMTPServerDisconnected`), Request selbst stuerzt nicht ab |

Zusatzwarnung: `InsecureKeyLengthWarning` von PyJWT, weil der SECRET_KEY kuerzer als 32 Byte ist (Reset-Token per JWT). Flask-Bootstrap laedt Bootstrap 3.3.7 und jQuery 1.12.4 von cdnjs.

### 5.6 Nicht getestet

- `nginx -t`, Supervisor, certbot (nicht installiert; Paketquellen teilweise gesperrt). Review in Abschnitt 6 ist statisch.
- MySQL (kein Server). Der Laengenkonflikt der Hash-Spalte ist aus gemessener Hash-Laenge (162) und MySQL-Strict-Mode abgeleitet.
- Windows/macOS-Verhalten, Browser-Rendering.
- Erreichbarkeit der Demo `lab1.ifalabs.org` (Egress 403).

Patches im Scratchpad (nur Kopien): P1 `url_parse` zu `urlsplit` (kap-15, kap-14 Variante A/B), P2 `paginate` mit Keyword-Argumenten (nur Variante B), `microblog.py` und `.env` mit Dummy-Werten neu angelegt.

---

## 6. Deployment-Config-Review (kap-13)

### 6.1 microblog.nginx

| Zeile | Befund | Bewertung / Anpassung fuer U13-Demo |
|---|---|---|
| 1 | Zielpfad `/etc/nginx/sites-enabled/microblog` | Ubuntu-Konvention: Datei in `sites-available`, Symlink in `sites-enabled`, `default`-Site entfernen |
| 6, 25-26 | Hostname `lab70.ifalabs.org` fest | Platzhalter (z. B. `<vm-name>.ifalabs.org`), in beiden Server-Bloecken und Zertifikatspfaden |
| 8-11 | `/.well-known` mit Tabs statt Leerzeichen, Webroot `/home/student/microblog/certs` | funktional; Ordner muss existieren und fuer Nginx lesbar sein (siehe Zeile 44) |
| 19-27 | 443-Block referenziert Let's-Encrypt-Dateien | Vor dem ersten certbot-Lauf existieren diese nicht, `nginx -t` scheitert. Drehbuch zweistufig: erst nur Port-80-Block, `certbot certonly --webroot`, dann 443-Block aktivieren; alternativ `certbot --nginx` oder die im Handoff erwaehnten vorkonfigurierten Zertifikate |
| 21 | `listen 443 ssl;` | ok; optional `http2` (Nginx 1.24 auf Ubuntu 24.04: `listen 443 ssl http2;`, ab 1.25.1 `http2 on;`) |
| 22 | `server_name _;` | inkonsistent zu Zeile 6; gleichen Hostnamen setzen |
| 24-26 | keine `ssl_protocols`, `ssl_ciphers`, kein `include /etc/letsencrypt/options-ssl-nginx.conf` | TLS haengt an Distribution-Defaults (Ubuntu-OpenSSL 3 sperrt TLS < 1.2 faktisch). Fuer die Lehre explizit machen: `ssl_protocols TLSv1.2 TLSv1.3;` oder certbot-Include; HSTS-Header als Ausblick |
| 29-30 | Logs direkt in `/var/log/` | ok (Master laeuft als root); alternativ `/var/log/nginx/microblog_*.log` fuer logrotate |
| 32-39 | `proxy_pass http://localhost:8000`, Host, X-Real-IP, X-Forwarded-For | `X-Forwarded-Proto $scheme` fehlt; ohne ProxyFix in der App erzeugen `url_for(..., _external=True)` `http://`-Links (Passwort-Reset-Mail, API `Post.to_dict`) |
| 41-46 | `/static` via `alias` auf `/home/student/microblog/app/static`, `expires 30d` | ok. **Stolperstein Ubuntu 21.04+:** Home-Verzeichnisse werden mit Modus 750 angelegt, `www-data` kann `/home/student` nicht durchqueren: 403 fuer `/static` und fehlschlagende certbot-Webroot-Pruefung (nicht getestet, bekannte Default-Aenderung). Loesung: `chmod o+x /home/student` bzw. passende Rechte, oder App unter `/srv/` |

### 6.2 microblog.conf (Supervisor)

| Zeile | Befund | Anpassung |
|---|---|---|
| 1 | Kommentar nennt `/etc/supervisor/conf.d/microblog` ohne Endung | Ubuntu-Supervisor laedt nur `conf.d/*.conf`; Kommentar und Drehbuch auf `microblog.conf` korrigieren (Dateiname im Repo ist korrekt) |
| 3 | `gunicorn -b localhost:8000 -w 4 microblog:app` | lauffaehig (mit kap-15-Kopie getestet); setzt `microblog.py` und gunicorn im venv voraus, beides nicht im Repo. `127.0.0.1` statt `localhost` vermeidet IPv6-Mehrdeutigkeit; 4 Worker fuer kleine VM ggf. auf 2 reduzieren |
| 4-5 | `directory`, `user=student` | Platzhalter kennzeichnen; `directory` ist auch Basis fuer `logs/` (kap-14 \_\_init\_\_.py:37-39) |
| 6-9 | autostart, autorestart, stopasgroup, killasgroup | ok |
| fehlt | `stdout_logfile`/`stderr_logfile`, `environment=` | optional; `.env` wird ueber config.py geladen, daher nicht zwingend |

Update-Zyklus fuer die Demo: `git pull`, `pip install -r requirements.txt`, `flask db upgrade`, `sudo supervisorctl restart microblog`. Dafuer fehlt im Repo ein `requirements.txt`.

### 6.3 config.py (Server)

| Zeile | Befund | Anpassung |
|---|---|---|
| 5-8 | `load_dotenv` aus Projektordner, Import nach Code (PEP 8) | ok; `.env.example` mit Platzhaltern mitliefern |
| 12 | `SECRET_KEY` ohne Fallback | gewollt fuer Produktion, aber ohne Fehlermeldung (Sessions/CSRF scheitern erst zur Laufzeit). Fail-fast mit klarer Meldung; Wert mit `secrets.token_hex(32)` erzeugen (PyJWT warnt unter 32 Byte) |
| 13 | `DATABASE_URL` ohne Fallback | Flask-SQLAlchemy 3.x bricht beim Start ab (getestet). Fuer Unterricht SQLite-Fallback mit absolutem Pfad (`basedir`), fuer Server MySQL-URI inkl. Treiber (z. B. `mysql+pymysql://`, Paket nicht im Repo) |
| 16-17 | `MAIL_USE_TLS = ... is not None` | jeder gesetzte Wert (auch "false") aktiviert TLS; im Material erklaeren |
| 20 | ADMINS: Platzhalter-Adresse vorhanden | ok als Platzhalter |
| 21 | `POSTS_PER_PAGE = 25` | wird nur vom historischen routes.py genutzt |
| fehlt | `SESSION_COOKIE_SECURE`, `REMEMBER_COOKIE_SECURE`, `PREFERRED_URL_SCHEME` | fuer HTTPS-Deployment ergaenzen (Ausblick) |

Secrets: keine im Repo (weder in kap-13 noch kap-14/15). Keine `.env` getrackt.

### 6.4 Zusammenfassung Anpassungen fuer Demo U13

1. Hostname und Pfade als Platzhalter, `server_name` in beiden Bloecken gleich.
2. Zweistufiger Ablauf Nginx/certbot oder Nutzung vorkonfigurierter Zertifikate.
3. Rechte fuer `/home/student` bzw. Deployment unter `/srv`.
4. `X-Forwarded-Proto` in Nginx plus `ProxyFix` in der App (oder bewusst weglassen und erklaeren).
5. `ssl_protocols` explizit oder certbot-Include.
6. Supervisor-Dateiname `.conf`, `127.0.0.1`, Worker-Anzahl.
7. `requirements.txt` (mit gunicorn, python-dotenv, DB-Treiber), `.env.example`, `microblog.py` in die Demo-App.
8. Hash-Spalte `String(256)` vor dem ersten `flask db upgrade` auf MySQL.

---

## 7. Abgleich mit dem KI-Handoff v2.0

### 7.1 Aussagen zum Repo-Material (Z. 53-86)

| Handoff-Aussage (Zeile) | Befund | Bewertung |
|---|---|---|
| kap-2/kap-3 als Musterloesungs-Referenz U8.2, "mit Flask 3.x testen" (68) | laeuft unveraendert mit Flask 3.1.3; Markup-Fehler in 2 Templates, XSS in kap-2 | stimmt, Inhalt bereinigen |
| kap-13 nginx/conf: Nginx mit Let's Encrypt, Supervisor, Hostname ersetzen (69) | Beschreibung korrekt; "1:1 verwenden" scheitert am Zertifikats-Henne-Ei und ggf. an Home-Rechten | teilweise, Anpassungen 6.4 |
| kap-14 als Referenz-Endstand U14-15 mit GET/POST/PUT, JSON-Fehlern, Basic/Token-Auth, to_dict/from_dict (70) | Funktionen vorhanden und getestet; kap-14 aber nicht eigenstaendig lauffaehig; 403/404/415 teils HTML | teilweise |
| Starter U14.2 "API-Routen entfernen, Models behalten" (70) | to_dict-Links erzwingen alle 5 GET-Endpunkte (BuildError getestet) | Anpassung noetig |
| kap-15 als Starter-Basis U10.1, Gravatar U10.2, WTForms-Stilreferenz U9.1 (71) | Inhalte vorhanden; Import-Bruch `url_parse`; naive Starter-Ableitung bricht (BuildError) | teilweise |
| kap-1 bewusst nicht verwenden (81) | bestaetigt (Abschnitt 3.1) | stimmt |
| "Repo-Code stammt von Anfang 2024" (85) | Flask-Code 2022 | korrigieren |
| Legacy-Kaesten fuer `query.get`, `utcnow`, `db.Column` (85) | zusaetzlich zwei Brueche (L1, L2), Hash-Laenge (L11), aware/naive-Falle (L10), `get_or_404`/`first_or_404` | erweitern |

### 7.2 Handoff-Plaene WP3-WP6 (Z. 543-976)

| Plan | Realistisch mit vorhandenem Code? | Was fehlt / zu tun |
|---|---|---|
| U8.2 Struktur "exakt wie kap-2/kap-3", frisches venv mit `pip install flask` (584-586) | ja | Templates korrigieren; Troubleshooting FLASK_APP praezisieren (Auto-Discovery ueber Paket `app`) |
| U8 Selbststudium "Vergleich mit Repo kap-3" (600) | ja | bereinigte Referenz statt Repo-Original, sonst uebernehmen TN `</h1`-Fehler |
| U9.1 Custom-Validator im Stil `validate_username` (608) | ja | Kasten L5 |
| U9.2 SQLite, Stil User/Post, Legacy-Kasten (616-618) | ja | config mit SQLite-Fallback und absolutem Pfad; Hinweis `instance/`; Kasten L3, L5, L8 |
| U10.1 Starter aus kap-15 (Login-Teile entfernen), Musterloesung = Repo-Stand kap-15 (675-677) | **teilweise** | Starter braucht Stub-Routen oder angepasste base.html und `login_view` (sonst 500); Musterloesung braucht `url_parse`-Fix, `config.py`, `microblog.py`, `errors`-Import; "Starter lauffaehig" nur so erfuellbar |
| U10.2 Gravatar mit Referenz models.py, user.html, _post.html (683-685) | ja | Internet noetig; Datenschutz-Hinweis (MD5 der E-Mail geht an Drittanbieter; laut Gravatar-Doku inzwischen auch SHA-256 moeglich, nicht getestet); `alt`-Attribut ergaenzen |
| U11.1 Tests auf kap-14-Models mit In-Memory-SQLite (723-725) | ja (4 Tests gruen) | ohne App-Factory muss `DATABASE_URL` vor dem Import gesetzt werden; API-Teile (`to_dict`, Token) entfernen; `utcnow`-Warnungen erklaeren |
| U11 Debug-Challenge (715) | Rohmaterial vorhanden | Profil-Duplikat-500 (kap-15) und `Post.to_dict`-Link (kap-14) eignen sich als echte Fehler |
| U12 Demo Passwort-Reset per E-Mail (771) | nur mit Historie | `email.py`, Reset-Formulare und Templates nur in Commit 877e509; `smtpd` in Python 3.12 entfernt, `aiosmtpd` verwenden; SECRET_KEY >= 32 Byte |
| U12.1 flask-bootstrap (789) | technisch ja (Flask-Bootstrap 3.3.7.1 laeuft mit Flask 3.1) | Bootstrap 3/jQuery 1.12 veraltet mit bekannten Schwachstellen; Modulnamenkonflikt mit Bootstrap-Flask; Empfehlung Bootstrap-Flask 5 oder CDN |
| U12 Quiz `.gitignore` (797) | Repo ist Negativbeispiel | eigene Vorlage (venv, .env, *.db, instance/, logs/) |
| U13 Demo mit Supervisor, microblog.conf/nginx "1:1 verwenden" (821-823) | **teilweise** | siehe 6.4; "1:1" nicht haltbar, "mit gekennzeichneten Anpassungen" formulieren |
| U14.2 Starter aus kap-14 ("api.py entfernt, Token-Felder entfernt", Seed-Skript) (890-892) | **teilweise** | `routes`, `forms`, Templates fehlen (aus kap-15 oder Historie); Import `api` in \_\_init\_\_.py:49 entfernen; `to_dict`-Links an die 3 geforderten Endpunkte anpassen oder 5 GET-Endpunkte verlangen; curl-Beispiele mit `Accept: application/json` |
| U15.1 POST/PUT ohne Auth, "PUT nur fuer eigene Ressource (403)", Musterloesung "api.py ohne Auth-Decorator" (906-908) | **nein, widerspruechlich** | Besitzpruefung braucht `token_auth.current_user()`; ohne Auth 500 (getestet). 403-Pruefung nach U15.2 verschieben; curl-Beispiele mit `--json` bzw. Content-Type (sonst 415) |
| U15.2 Basic/Token-Auth nach Muster kap-14, Endstand identisch mit kap-14 (914-916) | ja, mit Vorbehalt | Endstand enthaelt Bugs (403 HTML, 404 HTML bei curl, Post-Link, Token Klartext); entscheiden, ob "identisch" oder "korrigiert mit Hinweis" |
| U14/U15 Konvergenz der Musterloesungen zum kap-14-Endstand (859, 866) | technisch ja | Konvergenz-Kette U14.2 zu U15.1 zu U15.2 bricht an U15.1 (siehe oben); Endstand zuerst lauffaehig rekonstruieren (Historie 877e509 plus P1/P2) |
| U16 Handout Deployment konsistent mit Lehrmittel (954) | ja | Gunicorn/Supervisor/Nginx-Kette ist dokumentierbar; gleiche Platzhalter wie U13 |

---

## 8. Findings

| ID | Schweregrad | Datei:Zeile | Befund | Vorschlag |
|---|---|---|---|---|
| FL-F01 | hoch | Flask/kap-15/app/routes.py:4, :46 (und Historie 877e509 routes.py:4) | `from werkzeug.urls import url_parse` existiert in Werkzeug 3.x nicht mehr; kap-15 und jede daraus abgeleitete Musterloesung (U10.1, U14/U15-Webteil) bricht mit ImportError. Handoff sieht nur Warnungs-Kaesten vor. | In allen Materialien `urllib.parse.urlsplit` verwenden; im Kasten "Aktuelle Schreibweise" als Bruch (nicht nur Warnung) kennzeichnen. |
| FL-F02 | hoch | Flask/kap-14/app/models.py:24; Flask/kap-15/app/models.py:12 | `password_hash String(128)`, Werkzeug 3.1 erzeugt scrypt-Hashes mit 162 Zeichen (gemessen). SQLite toleriert das, MySQL 8 im Strict-Mode lehnt den INSERT ab: Registrierung scheitert nach Deployment mit MySQL. | In Starter/Musterloesungen `String(256)`; im Material U10 (Hashing) und U13 (Deployment) erklaeren. |
| FL-F03 | mittel | microblog (Gitlink, Mode 160000), Commit 9cf489a | Gitlink ohne `.gitmodules` auf Grinberg-Commit 68368ea (microblog Kapitel 4, in keinem Upstream-Branch mehr erreichbar). Klon und ZIP liefern leeren Ordner, `git submodule` bricht ab. | Gitlink entfernen und README-Link auf Grinberg-Repo mit Tag setzen, oder echtes Submodul mit `.gitmodules`; nur mit Auftrag im Repo aendern. |
| FL-F04 | hoch | Flask/kap-14/app/\_\_init\_\_.py:8-9, :49 | kap-14 ist nicht lauffaehig: `routes.py`, `forms.py`, `email.py`, Templates, `config.py`, `microblog.py`, `requirements.txt` fehlen; zusaetzliche Pakete flask-mail, flask-bootstrap, PyJWT nicht dokumentiert. Vollstand liegt in Commit 877e509 (`Flask/kap-14/kap-15/app/`). | Referenz-Endstand fuer U14/U15 aus 877e509 plus Patches P1/P2 rekonstruieren (ausserhalb des oeffentlichen Repos ablegen, CLAUDE.md beachten); `requirements.txt` mit gepinnten Versionen. |
| FL-F05 | mittel | Historie 877e509 routes.py:31-32, :46-47, :131-132 | `paginate(page, per_page, False)` mit Positionsargumenten: TypeError mit Flask-SQLAlchemy 3.x (getestet). | Bei Rekonstruktion Keyword-Argumente bzw. `db.paginate()`. |
| FL-F06 | hoch | Flask/kap-14/app/api.py:70; Handoff Z. 906-908 | U15.1 verlangt "PUT nur fuer eigene Ressource (403)" mit Musterloesung "api.py ohne Auth-Decorator"; ohne Auth liefert `token_auth.current_user()` None, PUT endet mit 500 (getestet). | 403-Besitzpruefung in U15.2 verschieben; U15.1 nur Validierung, 201/Location und 400. |
| FL-F07 | hoch | Flask/kap-14/app/models.py:93-95, :165, :168; \_\_init\_\_.py:49; Handoff Z. 890 | U14.2-Starter "api.py entfernt": `to_dict()` baut Links auf `get_followers`/`get_followed`; mit den 3 geforderten GET-Endpunkten entsteht BuildError und 500 (getestet). Import von `api` muss ebenfalls weg. | Im Starter `to_dict()` auf vorhandene Endpunkte reduzieren oder 5 GET-Endpunkte fordern; `__init__`-Import anpassen; Web-Teil (routes/forms/templates) mitliefern oder bewusst weglassen. |
| FL-F08 | mittel | Flask/kap-15/app/templates/base.html:15, :18; \_\_init\_\_.py:12; Handoff Z. 675 | U10.1-Starter "routes.py ohne login/logout/register": `url_for('login')` in base.html und `login_view` erzeugen BuildError, alle Seiten 500 (getestet). | Starter mit Stub-Routen (`TODO`-Antwort) oder angepasster Navigation ausliefern; Abnahmekriterium "Starter lauffaehig" damit pruefen. |
| FL-F09 | mittel | Flask/kap-14/app/errors.py:7-8, :18-19; api.py:50, :71, :73 | API-Fehler nicht durchgaengig JSON: 404 bei `Accept: */*` (curl-Default) als HTML, 403 via `abort` als HTML, fehlender JSON-Content-Type ergibt 415 HTML (alles getestet). | Fuer `/api/`-Pfade JSON-Fehler erzwingen (Handler fuer `HTTPException`); `get_json(silent=True)`; curl-Beispiele im Material mit `-H "Accept: application/json"` und `--json`. |
| FL-F10 | mittel | Flask/kap-14/app/models.py:165, :167, :87 | `Post.to_dict()`: `url` verwendet Post-ID als User-ID (falscher Link, getestet); `timestamp` im HTTP-Datumsformat, User `last_seen` als ISO: inkonsistent; `_external` nur bei Post. | Korrigieren oder bewusst als Debug-/Review-Aufgabe (U11 oder U14) nutzen und dokumentieren. |
| FL-F11 | mittel | Flask/kap-15/app/\_\_init\_\_.py:14 | `errors` wird nicht importiert, eigene 404/500-Seiten sind inaktiv (getestet: Flask-Standardseite). | `from app import routes, models, errors` in Musterloesungen. |
| FL-F12 | mittel | Flask/kap-15/app/forms.py:35-38; routes.py:89-91 | EditProfileForm ohne Eindeutigkeitspruefung: Username-Duplikat fuehrt zu IntegrityError/500 (getestet). Historie enthaelt den Fix (`original_username`). | In Musterloesung U10 beheben oder als Fehler fuer Debug-Challenge U11 verwenden (entspricht dem Vorgehen im microblog-Tutorial). |
| FL-F13 | mittel | Flask/kap-2/app/routes.py:10, :16 | Reflected XSS: Pfadparameter und User-Agent unescaped per `str.format` ins HTML (getestet). | Im Material `markupsafe.escape()` oder Template verwenden; als Security-Lernpunkt in U8/U10 aufgreifen. |
| FL-F14 | mittel | Flask/kap-13/microblog.nginx:19-27, :22 | 443-Block setzt vorhandene Let's-Encrypt-Dateien voraus, `nginx -t` scheitert vor certbot; `server_name _` inkonsistent. | Drehbuch U13 zweistufig (HTTP, certbot, HTTPS) oder `certbot --nginx`/vorkonfigurierte Zertifikate; Hostname-Platzhalter in beiden Bloecken. |
| FL-F15 | mittel | Flask/kap-13/microblog.nginx:10, :44; microblog.conf:4 | Pfade unter `/home/student`: ab Ubuntu 21.04 Home-Modus 750, Nginx (`www-data`) erhaelt 403 fuer `/static` und `.well-known` (nicht getestet, Default-Aenderung bekannt). | Rechte im Drehbuch setzen (`chmod o+x`) oder App unter `/srv`; im Stolpersteine-Kasten auffuehren. |
| FL-F16 | mittel | Flask/kap-13/config.py:12-13 | Ohne `DATABASE_URL` bricht Flask-SQLAlchemy 3.x ab (getestet), ohne SECRET_KEY scheitern Sessions/CSRF erst zur Laufzeit; relative SQLite-Pfade landen in `instance/`; PyJWT warnt bei SECRET_KEY unter 32 Byte. | Unterrichts-config mit SQLite-Fallback (absoluter Pfad), Server-config mit Fail-fast-Meldung, `.env.example` mit Platzhaltern, Key-Erzeugung per `secrets.token_hex(32)`. |
| FL-F17 | mittel | .gitignore:5-7; ".gitignore 2" | venv (ausser `myenv`), `.env`, `*.db`, `instance/`, `logs/` werden nicht ignoriert (check-ignore); ".gitignore 2" ist ein wirkungsloses macOS-Duplikat. | Mit Auftrag bereinigen; fuer U12 eine eigene `.gitignore`-Vorlage fuer Flask-Projekte ins Material. |
| FL-F18 | mittel | Flask/kap-14/app/api.py:48; models.py:131-146 | Token-Handling: `POST /api/users` nur mit bestehendem Token (erster User muss per Web/Shell entstehen); Token im Klartext in der DB, base64 aus `os.urandom` (nicht URL-sicher); Basic Auth nur ueber HTTPS sinnvoll. | Im Material explizit einordnen (Seed-Skript fuer ersten User, `secrets.token_urlsafe`, Hash-Speicherung als Ausblick, HTTPS-Pflicht). |
| FL-F19 | mittel | Flask/kap-14/app/models.py:27, :132, :140, :144, :156; kap-15 models.py:15, :40, routes.py:13 | `datetime.utcnow` erzeugt DeprecationWarning; die im Handoff geplante "Aktuelle Schreibweise" `datetime.now(timezone.utc)` fuehrt mit SQLite zu TypeError beim Vergleich naive/aware (getestet, models.py:133, :144). | Kasten um `.replace(tzinfo=timezone.utc)` beim Lesen ergaenzen oder Legacy-Stil beibehalten und Warnung erklaeren. |
| FL-F20 | mittel | Flask/kap-14/app/\_\_init\_\_.py:9, :19; Historie templates | Flask-Bootstrap 3.3.7.1 (letztes Release 2017) laedt Bootstrap 3.3.7 und jQuery 1.12.4 (Versionen mit bekannten XSS-Schwachstellen); Modulname `flask_bootstrap` kollidiert mit Bootstrap-Flask. | U12.1 auf Bootstrap-Flask (`Bootstrap5`) oder Bootstrap 5.3 per CDN ausrichten; Lehrmittel-Weg nur als Hinweis. |
| FL-F21 | mittel | Handoff Z. 771; Historie 877e509 email.py | U12-Demo Passwort-Reset: Code nur in der Historie; der im Tutorial uebliche Mail-Debugserver `python -m smtpd` existiert in Python 3.12 nicht mehr (getestet). | Demo auf rekonstruiertem Vollstand mit `aiosmtpd` vorbereiten; SECRET_KEY >= 32 Byte. |
| FL-F22 | tief | Flask/kap-1/*.html (u. a. index.html:8-10, tabellen-css.html:12) | Veraltetes und fehlerhaftes Markup: `<center>` falsch verschachtelt (5 von 6 Dateien), Entities ohne Semikolon, kein `lang`, alte charset-Form, keine Semantik, CSS-Fehler `align: left`; 74 Parsefehler. Doctype ist vorhanden. | Handoff-Entscheid "nicht verwenden" bestaetigt; optional als K4-Uebung "validieren und modernisieren". |
| FL-F23 | tief | Flask/kap-3/app/templates/hello_user.html:9; hello_for.html:14; base.html:1; kap-3/hello_flask.py:1; hello_macro.html:1 | `</h1` ohne `>`, `<p>` statt `</p>`, HTML-Kommentare vor Doctype, falsche Dateinamen in Kommentaren, `hello_if.html` ohne aktive Route. | Bereinigte Kopie mit identischer Struktur fuer U8.2 und Selbststudium U8. |
| FL-F24 | mittel | Repo-Root (keine LICENSE); Flask/kap-14, kap-15 | Keine Lizenzdatei, kein Attributionshinweis; kap-14/kap-15 sind vom MIT-lizenzierten microblog (Copyright Miguel Grinberg) abgeleitet. Handoff plant "direkt verwenden/als Anhang mitliefern". | Nutzungsrechte beim Lehrmittelautor klaeren; in abgeleitetem Material MIT-Hinweis fuer microblog-Code mitfuehren. |
| FL-F25 | tief | Handoff Z. 85, 555, 654, 859 | "Repo-Code von 2024": Flask-Code stammt aus Februar bis Juli 2022, einziger Flask-Commit 2024 schaltet nur eine Return-Zeile in kap-3 um. | Handoff-Text korrigieren (erklaert die Werkzeug-2-Brueche). |
| FL-F26 | tief | Flask/kap-13/microblog.conf:1, :3 | Kommentar nennt Zielpfad ohne `.conf` (Supervisor laedt nur `*.conf`); `localhost` statt `127.0.0.1`; 4 Worker; keine Log-Pfade. | Kommentar und Drehbuch korrigieren; Werte als Platzhalter/Empfehlung kennzeichnen. |
| FL-F27 | tief | Flask/kap-13/microblog.nginx:24-26, :32-39 | Keine expliziten `ssl_protocols`/Cipher, kein HSTS, kein `X-Forwarded-Proto`; `_external`-Links bleiben `http://` (getestet ohne ProxyFix). | Explizite TLS-Zeilen oder certbot-Include; `X-Forwarded-Proto` plus `ProxyFix` als Erklaerpunkt in U13. |
| FL-F28 | tief | Flask/kap-15/app/templates/_post.html:2-3; user.html:5-6; base.html:1-3 | Tabellenlayout mit obsoletem `valign`, `img` ohne `alt`, kein charset/lang/viewport, englische UI. | Im U12-Facelift thematisieren; `alt` in U10.2-Musterloesung ergaenzen. |
| FL-F29 | tief | README.md:1-11 | Keine Zuordnung `kap-N` zu FLASK-Kapiteln; kap-15 enthaelt einen frueheren microblog-Stand als kap-14; keine Setup-Hinweise. | Zuordnung mit Inhaltsverzeichnis FLASK verifizieren und im Kursmaterial (nicht zwingend im Repo) dokumentieren. |
| FL-F30 | tief | Handoff Z. 49; Flask/kap-13/microblog.nginx:6 | Erreichbarkeit von `lab1.ifalabs.org` (Demo) und `lab70.ifalabs.org` hier nicht pruefbar (Egress-Policy 403). | Vor U8 (DevTools-Uebung U8.1) und U13 manuell pruefen. |
