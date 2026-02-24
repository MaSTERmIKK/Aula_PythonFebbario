#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NUMPY + ALGEBRA LINEARE (unico file, esempi pratici)
- Vettori: norma, prodotto scalare, angolo
- Matrici: trasposta, trace, determinante, inversa
- Sistemi lineari: solve(Ax=b) e verifica
- Decomposizioni: eigen (autovalori/autovettori) e SVD
- Minimi quadrati: lstsq
"""

import numpy as np


# ==============================================================
# 0) SETUP (stampa più leggibile)
# ==============================================================

np.set_printoptions(precision=4, suppress=True)


# ==============================================================
# 1) VETTORI: DOT, NORMA, ANGOLO
# ==============================================================

print("=== 1) Vettori: dot, norma, angolo ===")

v = np.array([2.0, 1.0, -1.0])
w = np.array([1.0, 0.0,  2.0])

dot_vw = np.dot(v, w)                 # prodotto scalare
norm_v = np.linalg.norm(v)            # norma euclidea
norm_w = np.linalg.norm(w)

# cos(theta) = (v·w)/(|v||w|)
cos_theta = dot_vw / (norm_v * norm_w)
theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # radianti, clip per sicurezza numerica

print("v =", v)
print("w =", w)
print("v·w =", dot_vw)
print("|v| =", norm_v)
print("|w| =", norm_w)
print("cos(theta) =", cos_theta)
print("theta (radianti) =", theta)
print("theta (gradi) =", np.degrees(theta))
print()


# ==============================================================
# 2) MATRICI: TRASPOSTA, TRACE, DETERMINANTE, INVERSA
# ==============================================================

print("=== 2) Matrici: T, trace, det, inv ===")

A = np.array([[3.0, 1.0],
              [2.0, 4.0]])

print("A =\n", A)
print("A^T =\n", A.T)
print("trace(A) =", np.trace(A))
print("det(A) =", np.linalg.det(A))

A_inv = np.linalg.inv(A)
print("A^-1 =\n", A_inv)

# Verifica: A * A^-1 = I
I_check = A @ A_inv
print("A @ A^-1 =\n", I_check)
print()


# ==============================================================
# 3) SISTEMI LINEARI: risolvi Ax = b
# ==============================================================

print("=== 3) Sistemi lineari: solve(Ax=b) ===")

b = np.array([9.0, 8.0])

x = np.linalg.solve(A, b)  # soluzione esatta (se A invertibile)
print("b =", b)
print("x (soluzione) =", x)

# Verifica: A @ x deve tornare b
b_check = A @ x
print("A @ x =", b_check)
print("Differenza (A@x - b) =", b_check - b)
print()


# ==============================================================
# 4) AUTOVALORI E AUTOVETTORI: eig
# ==============================================================

print("=== 4) Autovalori e autovettori (eig) ===")

eigvals, eigvecs = np.linalg.eig(A)
print("Autovalori =", eigvals)
print("Autovettori (colonne) =\n", eigvecs)

# Verifica per il primo autovalore/vettore: A v = λ v
lam0 = eigvals[0]
vec0 = eigvecs[:, 0]
left = A @ vec0
right = lam0 * vec0
print("Verifica A v0 =", left)
print("Verifica λ0 v0 =", right)
print("Differenza =", left - right)
print()


# ==============================================================
# 5) SVD: decomposizione A = U Σ V^T
# ==============================================================

print("=== 5) SVD (U, S, Vt) ===")

U, S, Vt = np.linalg.svd(A)
print("U =\n", U)
print("S (singular values) =", S)
print("Vt =\n", Vt)

# Ricostruzione: U @ diag(S) @ Vt
Sigma = np.diag(S)
A_rebuild = U @ Sigma @ Vt
print("A ricostruita =\n", A_rebuild)
print("Errore ricostruzione (A - A_rebuild) =\n", A - A_rebuild)
print()


# ==============================================================
# 6) MINIMI QUADRATI: lstsq (quando il sistema è sovradeterminato)
# ==============================================================

print("=== 6) Minimi quadrati (lstsq) ===")

# Sistema con più equazioni che incognite (3 eq, 2 incognite)
A2 = np.array([[1.0, 1.0],
               [1.0, 2.0],
               [1.0, 3.0]])

b2 = np.array([1.0, 2.0, 2.0])

# lstsq trova x che minimizza ||A2 x - b2||
x2, residui, rank, svals = np.linalg.lstsq(A2, b2, rcond=None)

print("A2 =\n", A2)
print("b2 =", b2)
print("x2 (minimi quadrati) =", x2)
print("A2 @ x2 =", A2 @ x2)
print("Residui (somma errori^2) =", residui)
print("Rank =", rank)
print("Singular values =", svals)
print()


# ==============================================================
# 7) PROIEZIONE: componente di v lungo w
# ==============================================================

print("=== 7) Proiezione di v su w ===")

# proj_w(v) = ((v·w)/(w·w)) * w
proj = (np.dot(v, w) / np.dot(w, w)) * w
print("proj_w(v) =", proj)

# componente perpendicolare: v - proj
perp = v - proj
print("v - proj_w(v) =", perp)

# verifica ortogonalità: w·perp ≈ 0
print("w·(v - proj) =", np.dot(w, perp))
print()
