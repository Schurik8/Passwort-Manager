import json
import os
import platform
import secrets
import string
import pyperclip
import time
from collections import defaultdict

class PasswordEntry:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Passwort: {self.password}"

    def update(self, username=None, email=None, password=None):
        if username:
            self.username = username
        if email:
            self.email = email
        if password:
            self.password = password

class PasswordManager:
    FILE_NAME = "passwords.json"

    def __init__(self):
        self.password_store = self.load_passwords()

    @staticmethod
    def clear_console():
        system_name = platform.system()
        if system_name == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def pause_console():
        input("\nDrücke eine beliebige Taste, um fortzufahren...")

    def save_passwords(self):
        try:
            with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
                json.dump(
                    {service: vars(entry) for service, entry in self.password_store.items()},
                    file, ensure_ascii=False, indent=4
                )
            print("Einträge erfolgreich gespeichert!")
            time.sleep(1)
        except IOError as e:
            print(f"Fehler beim Speichern der Einträge: {e}")

    def load_passwords(self):
        if not os.path.exists(self.FILE_NAME):
            print("Keine vorhandene Datei gefunden. Eine neue wird erstellt.")
            time.sleep(1)
            return {}

        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return {service: PasswordEntry(**entry) for service, entry in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            print(f"Fehler beim Laden der Einträge: {e}")
            time.sleep(1)
            return {}

    def create_password(self):
        self.clear_console()
        print("Neues Passwort hinzufügen:")
        service = input("Gib den Namen des Dienstes ein: ").strip()
        if service in self.password_store:
            print("Ein Eintrag für diesen Dienst existiert bereits.")
            time.sleep(2)
            return

        username = input("Gib den Benutzernamen ein: ").strip()
        email = input("Gib die E-Mail-Adresse ein: ").strip()
        password = input("Gib das Passwort ein: ").strip()

        self.password_store[service] = PasswordEntry(username, email, password)
        print("Eintrag gespeichert!")
        time.sleep(2)

    def read_passwords(self):
        self.clear_console()
        if not self.password_store:
            print("Keine gespeicherten Einträge gefunden.")
            time.sleep(2)
            return

        print("Gespeicherte Einträge:")
        for service, entry in self.password_store.items():
            print(f"Dienst: {service} - {entry}")
        print(f"\nInsgesamt gespeicherte Passwörter: {len(self.password_store)}")
        self.pause_console()

    def view_sorted_by_passwords(self):
        self.clear_console()
        if not self.password_store:
            print("Keine gespeicherten Einträge vorhanden.")
            time.sleep(2)
            return

        password_groups = defaultdict(list)
        for service, entry in self.password_store.items():
            password_groups[entry.password].append(service)

        print("Gespeicherte Einträge nach Passwörtern sortiert (nach Anzahl der Vorkommen):")
        sorted_passwords = sorted(password_groups.items(), key=lambda item: len(item[1]), reverse=True)
        for password, services in sorted_passwords:
            print(f"\nPasswort: {password} - Anzahl: {len(services)}")
            for service in services:
                entry = self.password_store[service]
                print(f"  Dienst: {service}")
                print(f"    Username: {entry.username}, Email: {entry.email}")
        self.pause_console()

    def update_password(self):
        self.clear_console()
        print("Passwort aktualisieren:")
        service = input("Gib den Namen des Dienstes ein, den du aktualisieren möchtest: ").strip()
        if service not in self.password_store:
            print("Kein Eintrag für diesen Dienst gefunden.")
            time.sleep(2)
            return

        entry = self.password_store[service]
        username = input("Gib den neuen Benutzernamen ein (leer lassen, um keinen zu ändern): ").strip()
        email = input("Gib die neue E-Mail-Adresse ein (leer lassen, um keine zu ändern): ").strip()
        password = input("Gib das neue Passwort ein (leer lassen, um keines zu ändern): ").strip()

        entry.update(username=username or None, email=email or None, password=password or None)
        print("Eintrag aktualisiert!")
        time.sleep(2)

    def delete_password(self):
        self.clear_console()
        print("Passwort löschen:")
        service = input("Gib den Namen des Dienstes ein, den du löschen möchtest: ").strip()
        if service in self.password_store:
            del self.password_store[service]
            print("Eintrag gelöscht!")
        else:
            print("Kein Eintrag für diesen Dienst gefunden.")
        time.sleep(2)

    def generate_random_password(self, length=16):
        self.clear_console()
        print("Zufälliges sicheres Passwort generieren:")
        service = input("Gib den Namen des Dienstes ein: ").strip()
        if service in self.password_store:
            print("Ein Eintrag für diesen Dienst existiert bereits.")
            time.sleep(2)
            return

        username = input("Gib den Benutzernamen ein: ").strip()
        email = input("Gib die E-Mail-Adresse ein: ").strip()

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))

        pyperclip.copy(password)
        print(f"Generiertes Passwort: {password}")
        print("Das Passwort wurde in die Zwischenablage kopiert.")

        self.password_store[service] = PasswordEntry(username, email, password)
        print("Eintrag gespeichert!")
        self.pause_console()

    def main(self):
        while True:
            self.clear_console()
            print("Passwort Manager - Optionen:")
            print("1. Neues Passwort speichern")
            print("2. Alle Passwörter anzeigen")
            print("3. Passwörter nach Passwörtern sortiert anzeigen")
            print("4. Passwort aktualisieren")
            print("5. Passwort löschen")
            print("6. Zufälliges sicheres Passwort generieren")
            print("7. Beenden")
            choice = input("Bitte wähle eine Option: ").strip()

            if choice == '1':
                self.create_password()
            elif choice == '2':
                self.read_passwords()
            elif choice == '3':
                self.view_sorted_by_passwords()
            elif choice == '4':
                self.update_password()
            elif choice == '5':
                self.delete_password()
            elif choice == '6':
                self.generate_random_password()
            elif choice == '7':
                self.save_passwords()
                print("Programm beendet.")
                break
            else:
                print("Ungültige Option. Bitte eine Zahl zwischen 1 und 7 eingeben.")
                time.sleep(2)

if __name__ == "__main__":
    manager = PasswordManager()
    manager.main()
