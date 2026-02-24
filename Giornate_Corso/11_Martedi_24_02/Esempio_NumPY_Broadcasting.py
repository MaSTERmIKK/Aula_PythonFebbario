#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NUMPY - BROADCASTING COMPLETO

Contenuti:
1) Regole del broadcasting
2) Vettore + scalare
3) Matrice + vettore (riga)
4) Matrice + vettore (colonna)
5) Broadcasting tra matrici compatibili
6) Errori di broadcasting
7) Standardizzazione (caso reale data science)
8) Broadcasting 3D
"""

import numpy as np

np.set_printoptions(precision=3, suppress=True)

# ==============================================================
# 1) REGOLA DEL BROADCASTING
# ==============================================================

print("=== 1) Regola Base ===")
print("Le dimensioni si confrontano da destra verso sinistra.")
print("Compatibile se:")
print("- sono uguali")
print("- una delle due è 1")
print()


# ==============================================================
# 2) SCALARE + ARRAY
# ==============================================================

print("=== 2) Scalare + Array ===")

a = np.array([1, 2, 3])
print("Array:", a)
print("Array + 10:", a + 10)   # broadcasting automatico
print()


# ==============================================================
# 3) MATRICE + VETTORE RIGA
# ==============================================================

print("=== 3) Matrice + Vettore Riga ===")

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

v = np.array([10, 20, 30])

print("Matrice shape:", mat.shape)
print("Vettore shape:", v.shape)

print("Risultato:\n", mat + v)
print()


# ==============================================================
# 4) MATRICE + VETTORE COLONNA
# ==============================================================

print("=== 4) Matrice + Vettore Colonna ===")

v_col = np.array([[10],
                  [20]])

print("Vettore colonna shape:", v_col.shape)

print("Risultato:\n", mat + v_col)
print()


# ==============================================================
# 5) BROADCASTING TRA MATRICI
# ==============================================================

print("=== 5) Broadcasting tra matrici compatibili ===")

A = np.ones((3, 1))
B = np.array([1, 2, 3])

print("A shape:", A.shape)
print("B shape:", B.shape)

C = A + B
print("Risultato shape:", C.shape)
print(C)
print()


# ==============================================================
# 6) ERRORE DI BROADCASTING
# ==============================================================

print("=== 6) Caso incompatibile ===")

X = np.ones((2, 3))
Y = np.ones((4, 3))

print("X shape:", X.shape)
print("Y shape:", Y.shape)

try:
    Z = X + Y
except ValueError as e:
    print("Errore:", e)
print()


# ==============================================================
# 7) CASO REALE: STANDARDIZZAZIONE (DATA SCIENCE)
# ==============================================================

print("=== 7) Standardizzazione (mean per colonna) ===")

data = np.array([[10, 100],
                 [20, 200],
                 [30, 300]])

mean = data.mean(axis=0)
std = data.std(axis=0)

print("Data:\n", data)
print("Mean:", mean)
print("Std:", std)

standardized = (data - mean) / std

print("Standardized:\n", standardized)
print()


# ==============================================================
# 8) BROADCASTING 3D
# ==============================================================

print("=== 8) Broadcasting 3D ===")

tensor = np.ones((2, 3, 4))
bias = np.array([10, 20, 30, 40])

print("Tensor shape:", tensor.shape)
print("Bias shape:", bias.shape)

result = tensor + bias

print("Result shape:", result.shape)
print(result[0])  # stampa primo blocco
print()


# ==============================================================
# 9) EXPAND DIMS PER FORZARE BROADCASTING
# ==============================================================

print("=== 9) Uso di np.newaxis ===")

v = np.array([1, 2, 3])
print("v shape:", v.shape)

v_row = v[np.newaxis, :]
v_col = v[:, np.newaxis]

print("v_row shape:", v_row.shape)
print("v_col shape:", v_col.shape)

print("Matrice differenze:\n", v_col - v_row)
