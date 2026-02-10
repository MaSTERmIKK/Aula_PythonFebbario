# ==========================
# ESERCIZIO: Gestore di Pacchi
# Soluzione facile e ripetibile
# ==========================

class Pacco:
    def __init__(self, codice, peso):
        self.codice = codice
        self.peso = peso
        self.stato = "in magazzino"  # stato iniziale

    def mostra_info(self):
        print(f"Codice: {self.codice} | Peso: {self.peso} kg | Stato: {self.stato}")

    def cambia_stato(self, nuovo_stato):
        self.stato = nuovo_stato


class Magazzino:
    def __init__(self):
        self.pacchi = []  # lista di oggetti Pacco

    def aggiungi_pacco(self, pacco):
        self.pacchi.append(pacco)

    def cerca_per_codice(self, codice):
        # cerca e ritorna l'oggetto Pacco (oppure None se non esiste)
        for p in self.pacchi:
            if p.codice == codice:
                return p
        return None

    def mostra_per_stato(self, stato):
        print(f"\n--- Pacchi con stato: {stato} ---")
        trovato = False
        for p in self.pacchi:
            if p.stato == stato:
                p.mostra_info()
                trovato = True
        if not trovato:
            print("Nessun pacco trovato.")

    def peso_totale_non_consegnati(self):
        totale = 0
        for p in self.pacchi:
            if p.stato != "consegnato":
                totale += p.peso
        return totale


class GestorePacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino

    def metti_in_consegna(self, codice):
        pacco = self.magazzino.cerca_per_codice(codice)
        if pacco is None:
            print(f"Pacco {codice} non trovato.")
        else:
            if pacco.stato == "in magazzino":
                pacco.cambia_stato("in consegna")
                print(f"Pacco {codice} ora è IN CONSEGNA.")
            else:
                print(f"Pacco {codice} non è in magazzino (stato attuale: {pacco.stato}).")

    def consegna(self, codice):
        pacco = self.magazzino.cerca_per_codice(codice)
        if pacco is None:
            print(f"Pacco {codice} non trovato.")
        else:
            if pacco.stato == "in consegna":
                pacco.cambia_stato("consegnato")
                print(f"Pacco {codice} ora è CONSEGNATO.")
            else:
                print(f"Pacco {codice} non è in consegna (stato attuale: {pacco.stato}).")

    def stampa_peso_non_consegnati(self):
        peso = self.magazzino.peso_totale_non_consegnati()
        print(f"\nPeso totale pacchi NON consegnati: {peso} kg")


# ==========================
# MAIN (parte principale)
# ==========================
def main():
    magazzino = Magazzino()
    gestore = GestorePacchi(magazzino)

    # 1) Creo 5 pacchi
    p1 = Pacco("P001", 2.5)
    p2 = Pacco("P002", 1.0)
    p3 = Pacco("P003", 4.2)
    p4 = Pacco("P004", 3.3)
    p5 = Pacco("P005", 0.8)

    # 2) Li aggiungo al magazzino
    magazzino.aggiungi_pacco(p1)
    magazzino.aggiungi_pacco(p2)
    magazzino.aggiungi_pacco(p3)
    magazzino.aggiungi_pacco(p4)
    magazzino.aggiungi_pacco(p5)

    # 3) Avvio una consegna e ne completo una
    gestore.metti_in_consegna("P002")
    gestore.metti_in_consegna("P003")
    gestore.consegna("P003")

    # 4) Stampo elenchi e peso totale
    magazzino.mostra_per_stato("in magazzino")
    magazzino.mostra_per_stato("in consegna")
    magazzino.mostra_per_stato("consegnato")
    gestore.stampa_peso_non_consegnati()


# Avvio programma
main()
