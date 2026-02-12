# =========================
# CLASSE BASE
# =========================
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        # "Metodo astratto" (qui lo simulo così)
        print("Errore: metodo non implementato")


# =========================
# CLASSI DERIVATE
# =========================
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print("Pagamento di", importo, "€ effettuato con CARTA DI CREDITO")


class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print("Pagamento di", importo, "€ effettuato con PAYPAL")


class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print("Pagamento di", importo, "€ effettuato con BONIFICO BANCARIO")


# =========================
# GESTORE PAGAMENTI
# =========================
class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento  # può essere qualsiasi sottoclasse

    def paga(self, importo):
        # POLIMORFISMO: chiamo sempre lo stesso metodo,
        # ma cambia l'implementazione in base all'oggetto reale
        self.metodo_pagamento.effettua_pagamento(importo)


# =========================
# TEST
# =========================
metodi = [CartaDiCredito(), PayPal(), BonificoBancario()]

for metodo in metodi:
    gestore = GestorePagamenti(metodo)
    gestore.paga(50)
