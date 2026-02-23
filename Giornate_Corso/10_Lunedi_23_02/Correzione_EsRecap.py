# ============================================
# SISTEMA GESTIONE AULA - CORREZIONE RECAP
# ============================================

import os

# =========================
# CLASSI
# =========================

class Utente:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def registra(self):
        # Salvataggio credenziali in modalità append
        with open("credenziali.txt", "a") as file:
            file.write(self.username + "," + self.password + "\n")

    @staticmethod
    def login(username, password):
        if not os.path.exists("credenziali.txt"):
            return False

        with open("credenziali.txt", "r") as file:
            for riga in file:
                user, pwd = riga.strip().split(",")
                if user == username and pwd == password:
                    return True
        return False


class Admin(Utente):
    def __init__(self):
        # Hardcoded
        super().__init__("admin", "admin123")

    def reset_studenti(self):
        # Svuota completamente il file studenti
        with open("studenti.csv", "w") as file:
            pass

        # Log intervento
        motivo = input("Inserisci motivazione reset: ")
        with open("intervento_utente.txt", "a") as log:
            log.write("RESET effettuato: " + motivo + "\n")


# =========================
# FUNZIONI STUDENTI
# =========================

def aggiungi_studente():
    nome = input("Nome studente: ")
    corso = input("Corso: ")

    with open("studenti.csv", "a") as file:
        file.write(nome + "," + corso + "\n")


def modifica_studenti():
    studenti = []

    if os.path.exists("studenti.csv"):
        with open("studenti.csv", "r") as file:
            for riga in file:
                nome, corso = riga.strip().split(",")
                studenti.append([nome, corso])

    for i, stud in enumerate(studenti):
        print(i, "-", stud[0], stud[1])

    scelta = int(input("Indice studente da modificare: "))
    nuovo_nome = input("Nuovo nome: ")
    nuovo_corso = input("Nuovo corso: ")

    studenti[scelta] = [nuovo_nome, nuovo_corso]

    # Sovrascrivo il file
    with open("studenti.csv", "w") as file:
        for stud in studenti:
            file.write(stud[0] + "," + stud[1] + "\n")


def stampa_aula():
    studenti = []

    if not os.path.exists("studenti.csv"):
        print("Nessuno studente presente.")
        return

    with open("studenti.csv", "r") as file:
        for riga in file:
            nome, corso = riga.strip().split(",")
            studenti.append([nome, corso])

    # Ordinamento per corso
    studenti.sort(key=lambda x: x[1])

    print("\n--- LISTA AULA ORDINATA PER CORSO ---")
    for stud in studenti:
        print("Nome:", stud[0], "| Corso:", stud[1])


# =========================
# MENU PRINCIPALE
# =========================

def menu():
    while True:
        print("\n1. Registrazione")
        print("2. Login")
        print("3. Login Admin")
        print("4. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            user = input("Username: ")
            pwd = input("Password: ")
            nuovo = Utente(user, pwd)
            nuovo.registra()
            print("Registrazione completata.")

        elif scelta == "2":
            user = input("Username: ")
            pwd = input("Password: ")

            if Utente.login(user, pwd):
                print("Login effettuato.")
                menu_utente()
            else:
                print("Credenziali errate.")

        elif scelta == "3":
            user = input("Username: ")
            pwd = input("Password: ")

            admin = Admin()
            if user == admin.username and pwd == admin.password:
                print("Accesso Admin.")
                admin.reset_studenti()
            else:
                print("Credenziali admin errate.")

        elif scelta == "4":
            break


def menu_utente():
    while True:
        print("\n1. Aggiungi studente")
        print("2. Modifica studente")
        print("3. Stampa aula")
        print("4. Logout")

        scelta = input("Scelta: ")

        if scelta == "1":
            aggiungi_studente()
        elif scelta == "2":
            modifica_studenti()
        elif scelta == "3":
            stampa_aula()
        elif scelta == "4":
            break


# =========================
# AVVIO PROGRAMMA
# =========================

menu()
