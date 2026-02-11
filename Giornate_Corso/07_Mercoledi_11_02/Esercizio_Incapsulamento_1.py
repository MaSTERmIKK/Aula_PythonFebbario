class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        # attributi "privati" (name mangling)
        self.__titolare = ""
        self.__saldo = 0.0

        # uso i setter per validare subito
        self.set_titolare(titolare)

        # saldo iniziale valido (solo se >= 0)
        if saldo_iniziale >= 0:
            self.__saldo = float(saldo_iniziale)

    # --------- GETTER / SETTER ---------
    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nuovo_titolare):
        if type(nuovo_titolare) == str and nuovo_titolare.strip() != "":
            self.__titolare = nuovo_titolare
        else:
            print("Errore: titolare non valido")

    def visualizza_saldo(self):
        # getter del saldo (solo lettura)
        return self.__saldo

    # --------- METODI OPERATIVI ---------
    def deposita(self, importo):
        if importo > 0:
            self.__saldo = self.__saldo + importo
            print("Deposito OK. Nuovo saldo:", self.__saldo)
        else:
            print("Errore: importo non valido")

    def preleva(self, importo):
        if importo <= 0:
            print("Errore: importo non valido")
        elif importo > self.__saldo:
            print("Errore: fondi insufficienti")
        else:
            self.__saldo = self.__saldo - importo
            print("Prelievo OK. Nuovo saldo:", self.__saldo)


# ---------------- TEST ----------------
conto = ContoBancario("Mirko", 50)

print("Titolare:", conto.get_titolare())
print("Saldo:", conto.visualizza_saldo())

conto.deposita(20)
conto.preleva(30)
conto.preleva(999)     # fondi insufficienti
conto.deposita(-5)     # importo non valido

# Tentativo di "accesso diretto" (non consigliato e non immediato)
# print(conto.__saldo)  # darebbe errore
