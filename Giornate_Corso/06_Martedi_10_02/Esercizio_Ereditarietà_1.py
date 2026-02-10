# ==========================================================
# ESERCIZIO: Fabbrica che produce e vende prodotti (con OOP)
# Con EREDITARIETÀ: Prodotto -> Elettronica / Abbigliamento
# Usa: classi, oggetti, metodi, liste/dizionari
# ==========================================================

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        # profitto per 1 unità
        return self.prezzo_vendita - self.costo_produzione

    def descrizione(self):
        # testo base (le classi figlie possono aggiungere info)
        return f"{self.nome} (costo: {self.costo_produzione}€, prezzo: {self.prezzo_vendita}€)"


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_mesi):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia_mesi = garanzia_mesi

    def descrizione(self):
        return super().descrizione() + f" | Garanzia: {self.garanzia_mesi} mesi"


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def descrizione(self):
        return super().descrizione() + f" | Materiale: {self.materiale}"


class Fabbrica:
    def __init__(self):
        # inventario: dizionario {nome_prodotto: {"prodotto": oggetto, "quantita": numero}}
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantita"] += quantita
        else:
            self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantita": quantita}

    def vendi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto not in self.inventario:
            print("Prodotto non presente in inventario.")
            return

        disponibili = self.inventario[nome_prodotto]["quantita"]
        if quantita > disponibili:
            print(f"Quantità non disponibile. Disponibili: {disponibili}")
            return

        # vendita
        self.inventario[nome_prodotto]["quantita"] -= quantita
        prodotto = self.inventario[nome_prodotto]["prodotto"]
        profitto_totale = prodotto.calcola_profitto() * quantita

        print(f"Venduti {quantita} x {nome_prodotto}")
        print(f"Profitto realizzato: {profitto_totale}€")

    def resi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto not in self.inventario:
            print("Prodotto non presente in inventario (non posso fare il reso).")
            return
        self.inventario[nome_prodotto]["quantita"] += quantita
        print(f"Reso registrato: +{quantita} x {nome_prodotto}")

    def mostra_inventario(self):
        print("\n--- INVENTARIO ---")
        if len(self.inventario) == 0:
            print("Inventario vuoto.")
            return

        for nome in self.inventario:
            prodotto = self.inventario[nome]["prodotto"]
            qta = self.inventario[nome]["quantita"]
            print(f"{prodotto.descrizione()} | Quantità: {qta}")


# ==========================
# MAIN (parte principale)
# ==========================
def main():
    fabbrica = Fabbrica()

    # Creo prodotti (figli di Prodotto)
    telefono = Elettronica("Telefono", 200, 350, 24)
    cuffie = Elettronica("Cuffie", 20, 60, 12)
    maglietta = Abbigliamento("Maglietta", 5, 15, "Cotone")

    # Aggiungo a inventario
    fabbrica.aggiungi_prodotto(telefono, 5)
    fabbrica.aggiungi_prodotto(cuffie, 10)
    fabbrica.aggiungi_prodotto(maglietta, 20)

    fabbrica.mostra_inventario()

    # Vendite (una ok + una che fallisce)
    fabbrica.vendi_prodotto("Cuffie", 3)
    fabbrica.vendi_prodotto("Telefono", 10)  # fallisce: quantità non disponibile

    # Reso
    fabbrica.resi_prodotto("Cuffie", 1)

    fabbrica.mostra_inventario()


main()
