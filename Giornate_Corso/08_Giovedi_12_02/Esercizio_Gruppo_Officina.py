# =====================================================
# GESTIONALE OFFICINA ELETTRODOMESTICI
# =====================================================


# =====================================================
# 1. CLASSE BASE: Elettrodomestico
# =====================================================

class Elettrodomestico:
    def __init__(self, marca, modello, anno_acquisto, guasto):
        self.__marca = marca
        self.__modello = modello
        self.set_anno_acquisto(anno_acquisto)
        self.__guasto = guasto

    # -------- GETTER --------
    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def get_guasto(self):
        return self.__guasto

    # -------- SETTER --------
    def set_anno_acquisto(self, anno):
        if anno <= 2025:
            self.__anno_acquisto = anno
        else:
            self.__anno_acquisto = 2025

    # -------- METODI --------
    def descrizione(self):
        return f"{self.__marca} {self.__modello} ({self.__anno_acquisto}) - Guasto: {self.__guasto}"

    def stima_costo_base(self):
        return 50


# =====================================================
# 2. CLASSI DERIVATE
# =====================================================

class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri = giri

    def stima_costo_base(self):
        costo = 60
        if self.capacita_kg > 8:
            costo += 20
        return costo


class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self):
        costo = 70
        if self.litri > 300:
            costo += 25
        if self.ha_freezer:
            costo += 15
        return costo


class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        self.ventilato = ventilato

    def stima_costo_base(self):
        costo = 55
        if self.tipo_alimentazione == "gas":
            costo += 15
        if self.ventilato:
            costo += 10
        return costo


# =====================================================
# 3. CLASSE TicketRiparazione
# =====================================================

class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "aperto"
        self.__note = []

    # GETTER
    def get_id(self):
        return self.__id_ticket

    def get_stato(self):
        return self.__stato

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    # SETTER
    def set_stato(self, nuovo_stato):
        self.__stato = nuovo_stato

    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    # METODO VARIADICO
    def calcola_preventivo(self, *voci_extra):
        totale = self.__elettrodomestico.stima_costo_base()
        for voce in voci_extra:
            totale += voce
        return totale


# =====================================================
# 4. CLASSE Officina
# =====================================================

class Officina:
    def __init__(self, nome):
        self.nome = nome
        self.tickets = []

    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)

    def chiudi_ticket(self, id_ticket):
        for t in self.tickets:
            if t.get_id() == id_ticket:
                t.set_stato("chiuso")

    def stampa_ticket_aperti(self):
        print("\n--- Ticket Aperti ---")
        for t in self.tickets:
            if t.get_stato() == "aperto":
                tipo = type(t.get_elettrodomestico()).__name__
                print(f"ID: {t.get_id()} | Tipo: {tipo} | Stato: {t.get_stato()}")

    def totale_preventivi(self):
        totale = 0
        for t in self.tickets:
            totale += t.calcola_preventivo()
        return totale

    def statistiche_per_tipo(self):
        lavatrici = 0
        frigoriferi = 0
        forni = 0

        for t in self.tickets:
            elettro = t.get_elettrodomestico()

            if isinstance(elettro, Lavatrice):
                lavatrici += 1
            elif isinstance(elettro, Frigorifero):
                frigoriferi += 1
            elif isinstance(elettro, Forno):
                forni += 1

        print("\n--- STATISTICHE ---")
        print("Lavatrici:", lavatrici)
        print("Frigoriferi:", frigoriferi)
        print("Forni:", forni)


# =====================================================
# 5. TEST PRINCIPALE
# =====================================================

if __name__ == "__main__":

    officina = Officina("RiparaTech")

    # Creazione elettrodomestici
    lav = Lavatrice("Bosch", "X100", 2020, "Non centrifuga", 9, 1200)
    frigo = Frigorifero("Samsung", "Cool300", 2018, "Non raffredda", 350, True)
    forno = Forno("Whirlpool", "HeatPro", 2019, "Non si accende", "gas", True)

    # Creazione ticket
    t1 = TicketRiparazione(1, lav)
    t2 = TicketRiparazione(2, frigo)
    t3 = TicketRiparazione(3, forno)

    officina.aggiungi_ticket(t1)
    officina.aggiungi_ticket(t2)
    officina.aggiungi_ticket(t3)

    # Stampa ticket aperti
    officina.stampa_ticket_aperti()

    # Preventivi (uso metodo variadico)
    print("\nPreventivo Ticket 1:", t1.calcola_preventivo(20, 15))
    print("Preventivo Ticket 2:", t2.calcola_preventivo(30))
    print("Preventivo Ticket 3:", t3.calcola_preventivo())

    # Statistiche per tipo
    officina.statistiche_per_tipo()

    # Totale generale
    print("\nTotale preventivi:", officina.totale_preventivi())
