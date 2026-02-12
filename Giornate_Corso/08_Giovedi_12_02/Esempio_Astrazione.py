#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SULL'ASTRAZIONE IN PYTHON
- Classe astratta base (ABC)
- Metodi astratti
- Metodo concreto nella classe astratta
- Polimorfismo tramite astrazione
- Interfaccia astratta
- Template Method Pattern
"""

from abc import ABC, abstractmethod


# ==============================================================
# 1. CLASSE ASTRATTA SEMPLICE
# ==============================================================

class Animale(ABC):
    """
    Classe astratta.
    Non può essere istanziata direttamente.
    """

    @abstractmethod
    def verso(self):
        """Ogni animale deve implementare il proprio verso."""
        pass

    def descrizione(self):
        """Metodo concreto disponibile per tutte le sottoclassi."""
        return "Sono un animale."


class Cane(Animale):
    def verso(self):
        return "Bau!"


class Gatto(Animale):
    def verso(self):
        return "Miao!"


print("=== ESEMPIO 1: Classe Astratta Animale ===")
animali = [Cane(), Gatto()]
for a in animali:
    print(a.descrizione(), "Verso:", a.verso())
print()


# ==============================================================
# 2. INTERFACCIA ASTRATTA (SOLO METODI ASTRATTI)
# ==============================================================

class Forma(ABC):
    """
    Interfaccia astratta per forme geometriche.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)


class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14 * self.raggio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raggio


print("=== ESEMPIO 2: Interfaccia Forma ===")
forme = [Rettangolo(4, 5), Cerchio(3)]
for f in forme:
    print("Area:", f.area(), "| Perimetro:", f.perimetro())
print()


# ==============================================================
# 3. TEMPLATE METHOD PATTERN (ASTRAZIONE + LOGICA FISSA)
# ==============================================================

class Processo(ABC):
    """
    Definisce una struttura fissa di algoritmo.
    Alcune parti sono astratte.
    """

    def esegui(self):
        print("Inizio processo")
        self.step1()
        self.step2()
        print("Fine processo")

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass


class ProcessoPagamento(Processo):
    def step1(self):
        print("Verifica fondi")

    def step2(self):
        print("Addebito carta")


class ProcessoRegistrazione(Processo):
    def step1(self):
        print("Validazione dati")

    def step2(self):
        print("Creazione account")


print("=== ESEMPIO 3: Template Method ===")
p1 = ProcessoPagamento()
p2 = ProcessoRegistrazione()

p1.esegui()
print()
p2.esegui()
print()


# ==============================================================
# 4. ASTRATTA CON PROPRIETÀ ASTRATTA
# ==============================================================

class Veicolo(ABC):

    @property
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def muovi(self):
        pass


class Auto(Veicolo):
    @property
    def tipo(self):
        return "Auto"

    def muovi(self):
        return "L'auto si muove su strada"


class Barca(Veicolo):
    @property
    def tipo(self):
        return "Barca"

    def muovi(self):
        return "La barca naviga in acqua"


print("=== ESEMPIO 4: Proprietà Astratta ===")
mezzi = [Auto(), Barca()]
for m in mezzi:
    print(m.tipo, "->", m.muovi())
print()


# ==============================================================
# 5. ASTRATTA + POLIMORFISMO FUNZIONALE
# ==============================================================

def esegui_azione(oggetto_astratto):
    """
    Funzione che accetta qualunque oggetto che implementi muovi().
    """
    print("Azione:", oggetto_astratto.muovi())


print("=== ESEMPIO 5: Polimorfismo tramite astrazione ===")
esegui_azione(Auto())
esegui_azione(Barca())
