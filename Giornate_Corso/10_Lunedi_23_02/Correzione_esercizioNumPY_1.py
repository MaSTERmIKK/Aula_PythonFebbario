# ============================================
# ESERCIZIO: NumPy Slicing e Fancy Indexing
# ============================================

import numpy as np

# 1) Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50
# Nota: randint ha upper bound esclusivo, quindi metto 51 per includere 50
arr = np.random.randint(10, 51, size=20)

# 2) Slicing: primi 10 elementi
primi_10 = arr[:10]

# 3) Slicing: ultimi 5 elementi
ultimi_5 = arr[-5:]

# 4) Slicing: elementi dall'indice 5 all'indice 15 (escluso)
da_5_a_15 = arr[5:15]

# 5) Slicing: ogni terzo elemento
ogni_terzo = arr[::3]

# 6) Modifica tramite slicing: elementi dall'indice 5 all'indice 10 (escluso) -> 99
# NB: questo modifica l'array originale
arr_modificato = arr.copy()          # copio per mostrare anche l'originale "pulito"
arr_modificato[5:10] = 99

# 7) Stampa array originale e tutti i sottoarray ottenuti
print("Array originale:")
print(arr)

print("\nPrimi 10 elementi (arr[:10]):")
print(primi_10)

print("\nUltimi 5 elementi (arr[-5:]):")
print(ultimi_5)

print("\nElementi dall'indice 5 all'indice 15 escluso (arr[5:15]):")
print(da_5_a_15)

print("\nOgni terzo elemento (arr[::3]):")
print(ogni_terzo)

print("\nArray dopo modifica (arr[5:10] = 99):")
print(arr_modificato)
