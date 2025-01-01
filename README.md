# Passwort-Manager

Ein einfacher und benutzerfreundlicher Passwort-Manager in Python. Mit diesem Programm kannst du deine Passwörter sicher speichern, organisieren und verwalten. Es bietet außerdem die Möglichkeit, zufällige sichere Passwörter zu generieren.

## Funktionen

1. **Passwort speichern**: Speichere neue Passwörter für verschiedene Dienste.
2. **Passwörter anzeigen**: Zeige alle gespeicherten Passwörter übersichtlich an.
3. **Passwörter sortieren**: Zeige Passwörter nach ihrer Häufigkeit an.
4. **Passwort aktualisieren**: Aktualisiere bestehende Einträge.
5. **Passwort löschen**: Entferne gespeicherte Passwörter.
6. **Zufälliges Passwort generieren**: Erstelle sichere zufällige Passwörter und kopiere sie in die Zwischenablage.

## Voraussetzungen

- Python 3.7 oder höher
- Installierte Bibliotheken:
  - `pyperclip`

### Installation von Abhängigkeiten

```bash
pip install pyperclip
```

## Verwendung

1. Lade die Datei herunter und speichere sie als `password_manager.py`.
2. Starte das Programm mit:

```bash
python password_manager.py
```

3. Folge den Menüanweisungen, um Passwörter hinzuzufügen, anzuzeigen, zu aktualisieren oder zu löschen.

## Funktionen im Detail

### Neues Passwort speichern
- Wähle die Option `1` aus dem Menü.
- Gib den Namen des Dienstes, den Benutzernamen, die E-Mail-Adresse und das Passwort ein.
- Der Eintrag wird gespeichert.

### Alle Passwörter anzeigen
- Wähle die Option `2` aus dem Menü.
- Eine Liste aller gespeicherten Einträge wird angezeigt.

### Passwörter nach Häufigkeit anzeigen
- Wähle die Option `3` aus dem Menü.
- Die Passwörter werden basierend auf ihrer Häufigkeit angezeigt.

### Passwort aktualisieren
- Wähle die Option `4` aus dem Menü.
- Gib den Namen des Dienstes ein, dessen Passwort du ändern möchtest, und folge den Anweisungen.

### Passwort löschen
- Wähle die Option `5` aus dem Menü.
- Gib den Namen des Dienstes ein, dessen Passwort gelöscht werden soll.

### Zufälliges sicheres Passwort generieren
- Wähle die Option `6` aus dem Menü.
- Gib die Details für den neuen Dienst ein.
- Ein sicheres Passwort wird erstellt, angezeigt und in die Zwischenablage kopiert.

## Speicherung

- Alle Passwörter werden lokal in einer Datei `passwords.json` gespeichert.
- Die Datei wird beim Start geladen und beim Beenden aktualisiert.

## Sicherheitshinweise

- Stelle sicher, dass die Datei `passwords.json` nur für dich zugänglich ist, da sie sensible Informationen enthält.
- Das Programm bietet keine Verschlüsselung der gespeicherten Passwörter.

## To-Do

- Verschlüsselung der Passwörter hinzufügen.
- Unterstützung für mehrere Benutzer.
- Integration mit Cloud-Speicherlösungen für Synchronisation.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.

## Autor

Dieses Projekt wurde von Alex erstellt. Feedback und Beiträge sind willkommen!
