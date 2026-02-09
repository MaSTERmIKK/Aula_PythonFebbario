import random

# =========================
# CLASSE UTENTE (CLIENTE)
# =========================
class Utente:
    def __init__(self, nome):
        self.nome = nome
        # budget autogenerato (es. tra 10 e 100 euro)
        self.budget = random.randint(10, 100)
        # lista degli acquisti effettuati (nomi articoli)
        self.acquisti = []

    def mostra_budget(self):
        print(self.nome, "ha un budget di", self.budget, "€")

    def compra(self, negozio, nome_articolo, quantita):
        # prova ad acquistare dal negozio
        successo = negozio.vendi(self, nome_articolo, quantita)
        if successo:
            # se l'acquisto va a buon fine, memorizzo l'acquisto
            self.acquisti.append((nome_articolo, quantita))


# =========================
# CLASSE NEGOZIO
# =========================
class Negozio:
    def __init__(self, nome):
        self.nome = nome

        # inventario: dizionario
        # chiave = nome articolo
        # valore = dizionario con prezzo e quantità
        self.inventario = {}

        # traccia vendite e guadagni
        self.vendite = []       # lista di tuple (cliente, articolo, qta, totale)
        self.guadagno_totale = 0

    # ---- INVENTARIO ----
    def aggiungi_articolo(self, nome_articolo, prezzo, quantita):
        self.inventario[nome_articolo] = {"prezzo": prezzo, "quantita": quantita}
        print("Aggiunto:", nome_articolo, "- prezzo:", prezzo, "€ - qta:", quantita)

    def aggiorna_articolo(self, nome_articolo, nuovo_prezzo=None, nuova_quantita=None):
        if nome_articolo in self.inventario:
            if nuovo_prezzo is not None:
                self.inventario[nome_articolo]["prezzo"] = nuovo_prezzo
            if nuova_quantita is not None:
                self.inventario[nome_articolo]["quantita"] = nuova_quantita
            print("Articolo aggiornato:", nome_articolo, self.inventario[nome_articolo])
        else:
            print("Articolo non trovato:", nome_articolo)

    def rimuovi_articolo(self, nome_articolo):
        if nome_articolo in self.inventario:
            del self.inventario[nome_articolo]
            print("Rimosso articolo:", nome_articolo)
        else:
            print("Articolo non trovato:", nome_articolo)

    def mostra_inventario(self):
        print("\n--- INVENTARIO DI", self.nome, "---")
        if len(self.inventario) == 0:
            print("Inventario vuoto")
        else:
            for articolo in self.inventario:
                prezzo = self.inventario[articolo]["prezzo"]
                qta = self.inventario[articolo]["quantita"]
                print("-", articolo, "|", prezzo, "€ | qta:", qta)
        print("---------------------------\n")

    # ---- ACQUISTO ----
    def vendi(self, utente, nome_articolo, quantita):
        # controllo esistenza articolo
        if nome_articolo not in self.inventario:
            print("ERRORE:", nome_articolo, "non esiste in inventario")
            return False

        prezzo = self.inventario[nome_articolo]["prezzo"]
        disponibile = self.inventario[nome_articolo]["quantita"]
        costo_totale = prezzo * quantita

        # controllo quantità disponibile
        if quantita <= 0:
            print("ERRORE: quantità non valida")
            return False

        if disponibile < quantita:
            print("ERRORE: quantità non disponibile. Disponibile:", disponibile)
            return False

        # controllo budget utente
        if utente.budget < costo_totale:
            print("ERRORE:", utente.nome, "non ha abbastanza budget. Costo:", costo_totale, "€")
            return False

        # se tutto ok: aggiorno inventario, budget, vendite, guadagni
        self.inventario[nome_articolo]["quantita"] = disponibile - quantita
        utente.budget = utente.budget - costo_totale

        self.vendite.append((utente.nome, nome_articolo, quantita, costo_totale))
        self.guadagno_totale = self.guadagno_totale + costo_totale

        print("OK:", utente.nome, "ha comprato", quantita, nome_articolo, "per", costo_totale, "€")
        return True

    # ---- REPORT ADMIN ----
    def report_vendite(self):
        print("\n=== REPORT VENDITE ===")
        if len(self.vendite) == 0:
            print("Nessuna vendita registrata")
        else:
            for v in self.vendite:
                cliente, articolo, qta, totale = v
                print("-", cliente, "ha comprato", qta, articolo, "| Totale:", totale, "€")
        print("Guadagno totale:", self.guadagno_totale, "€")
        print("======================\n")


# =========================
# TEST (SIMULAZIONE)
# =========================
negozio = Negozio("TechShop")

# inventario iniziale
negozio.aggiungi_articolo("Mouse", 15, 10)
negozio.aggiungi_articolo("Tastiera", 25, 5)
negozio.aggiungi_articolo("Cuffie", 30, 3)

negozio.mostra_inventario()

# creazione utenti (budget random)
u1 = Utente("Marco")
u2 = Utente("Sara")

u1.mostra_budget()
u2.mostra_budget()

# acquisti
u1.compra(negozio, "Mouse", 2)
u2.compra(negozio, "Cuffie", 1)
u2.compra(negozio, "Tastiera", 2)  # potrebbe fallire se budget basso

# inventario dopo vendite
negozio.mostra_inventario()

# report admin
negozio.report_vendite()

# storico acquisti utenti
print("Acquisti di", u1.nome, ":", u1.acquisti)
print("Acquisti di", u2.nome, ":", u2.acquisti)
