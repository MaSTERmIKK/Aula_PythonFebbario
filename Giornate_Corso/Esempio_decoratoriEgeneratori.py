#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DECORATORI + GENERATORI (stesso file, tutto commentato)
- Decoratori: base, con parametri, con argomenti, stacking
- Generatori: yield, yield from, generator expression
- Decoratore applicato a funzioni che consumano generatori
"""

import time

# ==============================================================
# 1) DECORATORE SEMPLICE: aggiunge log prima/dopo la chiamata
# ==============================================================

def log_call(func):
    # "wrapper" è la funzione interna che sostituisce la funzione originale
    def wrapper(*args, **kwargs):
        print(f"[LOG] Inizio: {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)  # chiamata alla funzione originale
        print(f"[LOG] Fine: {func.__name__} -> result={result}")
        return result
    return wrapper


@log_call
def somma(a, b):
    return a + b


# ==============================================================
# 2) DECORATORE PER MISURARE TEMPO DI ESECUZIONE
# ==============================================================

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] {func.__name__} ha impiegato {end - start:.6f} sec")
        return result
    return wrapper


# ==============================================================
# 3) DECORATORE CON PARAMETRI: @repeat(n)
# ==============================================================

def repeat(n):
    # repeat(n) restituisce un decoratore vero e proprio
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_result = None
            for i in range(n):
                print(f"[REPEAT] Esecuzione {i+1}/{n} di {func.__name__}")
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator


@repeat(3)
def saluta(nome):
    print("Ciao", nome)


# ==============================================================
# 4) DECORATOR STACKING: più decoratori sulla stessa funzione
#    (prima passa nel decoratore più vicino, poi negli altri)
# ==============================================================

@log_call
@timer
def somma_lenta(n):
    # finta "operazione lenta"
    totale = 0
    for i in range(n):
        totale += i
    return totale


# ==============================================================
# 5) GENERATORI: yield (producono valori uno alla volta)
# ==============================================================

def contatore_fino_a(n):
    # Generatore che produce 1,2,3,...,n
    i = 1
    while i <= n:
        yield i
        i += 1


def numeri_pari_fino_a(n):
    # Generatore che produce solo numeri pari fino a n
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def fibonacci(n):
    # Generatore Fibonacci: produce n numeri
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# ==============================================================
# 6) yield from: un generatore che "delega" a un altro
# ==============================================================

def catena_generatori():
    # Prima produce 1..3, poi 10..12
    yield from range(1, 4)
    yield from range(10, 13)


# ==============================================================
# 7) GENERATOR EXPRESSION: versione "lazy" delle comprehension
# ==============================================================

def somma_quadrati_pari(n):
    # generator expression: (x*x for x in range(...) if ...)
    gen = (x * x for x in range(n + 1) if x % 2 == 0)
    # sum consuma il generatore (una sola volta)
    return sum(gen)


# ==============================================================
# 8) DECORATORE + GENERATORE: decoriamo una funzione che consuma generatori
# ==============================================================

@log_call
def somma_da_iterabile(iterabile):
    # Somma qualunque iterabile: lista, tupla, generatore, range, ecc.
    totale = 0
    for x in iterabile:
        totale += x
    return totale


# ==============================================================
# 9) ESEMPIO IMPORTANTE: un generatore, una volta consumato, è "finito"
# ==============================================================

def esempio_generatore_consumato():
    gen = contatore_fino_a(5)
    print("Prima somma:", sum(gen))    # consuma tutto
    print("Seconda somma:", sum(gen))  # ora è vuoto -> 0


# ==============================================================
# MAIN: esegue tutti gli esempi in sequenza
# ==============================================================

def main():
    print("=== DECORATORI: base ===")
    print("somma(2, 3) =", somma(2, 3))
    print()

    print("=== DECORATORI: con parametri (@repeat) ===")
    saluta("Mirko")
    print()

    print("=== DECORATOR STACKING (timer + log_call) ===")
    print("somma_lenta(200000) =", somma_lenta(200000))
    print()

    print("=== GENERATORI: contatore_fino_a ===")
    for v in contatore_fino_a(5):
        print(v, end=" ")
    print("\n")

    print("=== GENERATORI: numeri_pari_fino_a ===")
    print(list(numeri_pari_fino_a(10)))
    print()

    print("=== GENERATORI: fibonacci ===")
    print(list(fibonacci(10)))
    print()

    print("=== yield from ===")
    print(list(catena_generatori()))
    print()

    print("=== generator expression: somma quadrati pari ===")
    print("somma_quadrati_pari(10) =", somma_quadrati_pari(10))
    print()

    print("=== Decoratore applicato a funzione che consuma generatori ===")
    gen_pari = numeri_pari_fino_a(20)
    print("Somma pari fino a 20 =", somma_da_iterabile(gen_pari))
    print()

    print("=== Generatore consumato (attenzione!) ===")
    esempio_generatore_consumato()


if __name__ == "__main__":
    main()
