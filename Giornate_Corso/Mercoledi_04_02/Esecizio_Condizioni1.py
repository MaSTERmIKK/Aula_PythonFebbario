# es 1

accesso = input("Hai il badge? (si/no): ")

if accesso == "si":
    ruolo = input("Sei admin o utente? ")

    if ruolo == "admin":
        stato = input("Account attivo? (si/no): ")

        if stato == "si":
            print("Accesso consentito")
        else:
            print("Account bloccato")
    else:
        print("Accesso limitato")
else:
    print("Accesso negato")


# es 3

utenti = []
id_utente = 1

nome = input("Inserisci nome: ")

if nome not in utenti:
    password = input("Inserisci password: ")
    utenti.append(nome)
    print("Account creato")
    print("ID utente:", id_utente)
    id_utente = id_utente + 1
else:
    print("Account già presente")
    print("Fine programma")



# es 2

dati = ["mirko", "Paulo"]

print("1 - Aggiungi")
print("2 - Rimuovi")
print("3 - Elimina tutto")

scelta = input("Scegli un'opzione: ")

if scelta == "1":
    valore = input("Inserisci valore: ")
    dati.append(valore)
    print(dati)

elif scelta == "2":
    valore = input("Valore da rimuovere: ")
    if valore in dati:
        dati.remove(valore)
    print(dati)

elif scelta == "3":
    dati.clear()
    print("Lista svuotata")

else:
    print("Scelta non valida")

