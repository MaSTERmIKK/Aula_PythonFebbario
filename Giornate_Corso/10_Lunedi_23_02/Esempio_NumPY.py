#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SU NUMPY
- Creazione array
- Shape e dtype
- Indicizzazione e slicing
- Operazioni vettoriali
- Broadcasting
- Aggregazioni
- Algebra lineare
- Random
"""

import numpy as np


# ==============================================================
# 1. CREAZIONE ARRAY
# ==============================================================

print("=== 1. Creazione Array ===")

a = np.array([1, 2, 3, 4])
print("Array 1D:", a)

b = np.array([[1, 2], [3, 4]])
print("Array 2D:\n", b)

c = np.zeros((2, 3))
print("Matrice di zeri:\n", c)

d = np.ones((3, 3))
print("Matrice di uno:\n", d)

e = np.arange(0, 10, 2)
print("Range con step 2:", e)

f = np.linspace(0, 1, 5)
print("Linspace:", f)

print()


# ==============================================================
# 2. SHAPE E DTYPE
# ==============================================================

print("=== 2. Shape e Dtype ===")
print("Shape di b:", b.shape)
print("Dimensioni di b:", b.ndim)
print("Tipo dati di b:", b.dtype)
print()


# ==============================================================
# 3. INDICIZZAZIONE E SLICING
# ==============================================================

print("=== 3. Indicizzazione ===")
x = np.arange(10)
print("Array:", x)
print("Elemento indice 3:", x[3])
print("Slice 2:7:", x[2:7])

m = np.arange(9).reshape(3, 3)
print("Matrice 3x3:\n", m)
print("Elemento riga 1 colonna 2:", m[1, 2])
print("Prima riga:", m[0])
print()


# ==============================================================
# 4. OPERAZIONI VETTORIALI (NO CICLI!)
# ==============================================================

print("=== 4. Operazioni Vettoriali ===")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("Somma:", a + b)
print("Moltiplicazione:", a * b)
print("Potenza:", a ** 2)
print("Radice:", np.sqrt(a))
print()


# ==============================================================
# 5. BROADCASTING
# ==============================================================

print("=== 5. Broadcasting ===")

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

vettore = np.array([10, 20, 30])

print("Matrice:\n", mat)
print("Vettore:", vettore)
print("Somma broadcasting:\n", mat + vettore)
print()


# ==============================================================
# 6. AGGREGAZIONI
# ==============================================================

print("=== 6. Aggregazioni ===")

m = np.arange(1, 10).reshape(3, 3)
print("Matrice:\n", m)

print("Somma totale:", m.sum())
print("Media:", m.mean())
print("Massimo:", m.max())
print("Minimo per colonna:", m.min(axis=0))
print("Somma per riga:", m.sum(axis=1))
print()


# ==============================================================
# 7. ALGEBRA LINEARE
# ==============================================================

print("=== 7. Algebra Lineare ===")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Prodotto matriciale A @ B:\n", A @ B)

print("Trasposta di A:\n", A.T)

print("Determinante di A:", np.linalg.det(A))

print("Inversa di A:\n", np.linalg.inv(A))
print()


# ==============================================================
# 8. NUMPY RANDOM
# ==============================================================

print("=== 8. Random ===")

np.random.seed(42)

print("Numeri casuali uniformi:\n", np.random.rand(2, 3))

print("Numeri casuali normali:\n", np.random.randn(3))

print("Interi casuali 0-9:\n", np.random.randint(0, 10, 5))
print()


# ==============================================================
# 9. RESHAPE E CONCATENAZIONE
# ==============================================================

print("=== 9. Reshape e Concatenazione ===")

a = np.arange(6)
print("Originale:", a)

b = a.reshape(2, 3)
print("Reshape 2x3:\n", b)

c = np.vstack([b, b])
print("Vertical stack:\n", c)

d = np.hstack([b, b])
print("Horizontal stack:\n", d)
