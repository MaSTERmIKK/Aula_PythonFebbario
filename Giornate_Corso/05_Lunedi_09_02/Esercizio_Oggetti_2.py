class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False          # ristorante chiuso di default
        self.menu = {}               # dizionario piatti: prezzo

    def descrivi_ristorante(self):
        print("Il ristorante", self.nome, "offre cucina", self.tipo_cucina)

    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante è ora aperto")

    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante è ora chiuso")

    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print("Piatto aggiunto:", piatto)

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print("Piatto rimosso:", piatto)
        else:
            print("Il piatto non è nel menu")

    def stampa_menu(self):
        print("Menu del ristorante:")
        for piatto in self.menu:
            print(piatto, "-", self.menu[piatto], "€")
