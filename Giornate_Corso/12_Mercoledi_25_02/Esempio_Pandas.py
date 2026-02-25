#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANDAS - PANORAMICA COMPLETA (unico file, esempi pratici)

Contenuti:
1) Series e DataFrame
2) Lettura/scrittura CSV (demo in memoria)
3) Selezione: colonne, loc, iloc
4) Filtri booleani
5) Nuove colonne (operazioni vettoriali)
6) Missing values (NaN): isna, fillna, dropna
7) groupby + aggregazioni
8) sort_values + value_counts
9) merge (join) tra DataFrame
10) DateTime: to_datetime, set_index, resample
"""

import pandas as pd
import numpy as np
from io import StringIO


# ==============================================================
# 1) SERIES E DATAFRAME
# ==============================================================

print("=== 1) Series e DataFrame ===")

s = pd.Series([10, 20, 30], name="punti")
print("Series:\n", s, "\n")

df = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Sara"],
    "eta":  [25, 40, 30, 22],
    "citta": ["Milano", "Roma", "Napoli", "Milano"],
    "spesa": [50.5, 120.0, 80.0, 30.0]
})

print("DataFrame:\n", df, "\n")


# ==============================================================
# 2) LETTURA/SCRITTURA CSV (IN MEMORIA)
# ==============================================================

print("=== 2) CSV in memoria (StringIO) ===")

buffer = StringIO()
df.to_csv(buffer, index=False)     # scrivo CSV in memoria
buffer.seek(0)                     # torno all'inizio del buffer
df_csv = pd.read_csv(buffer)       # leggo CSV dal buffer

print("Riletto da CSV:\n", df_csv, "\n")


# ==============================================================
# 3) SELEZIONE: COLONNE, loc, iloc
# ==============================================================

print("=== 3) Selezione dati ===")

print("Colonna 'nome':\n", df["nome"], "\n")

print("loc (riga per etichetta): df.loc[1]:\n", df.loc[1], "\n")

print("iloc (riga per posizione): df.iloc[0]:\n", df.iloc[0], "\n")

print("Sottotabella (righe 0-2, colonne 0-2):\n", df.iloc[0:3, 0:3], "\n")


# ==============================================================
# 4) FILTRI BOOLEANI
# ==============================================================

print("=== 4) Filtri booleani ===")

filtro_milano = df["citta"] == "Milano"
print("Solo Milano:\n", df[filtro_milano], "\n")

filtro_eta = df["eta"] >= 30
print("Età >= 30:\n", df[filtro_eta], "\n")

filtro_combinato = (df["citta"] == "Milano") & (df["spesa"] > 40)
print("Milano e spesa > 40:\n", df[filtro_combinato], "\n")


# ==============================================================
# 5) NUOVE COLONNE (OPERAZIONI VETTORIALI)
# ==============================================================

print("=== 5) Nuove colonne ===")

df["spesa_iva"] = df["spesa"] * 1.22  # esempio: IVA 22%
df["maggiorenne"] = df["eta"] >= 18

print(df, "\n")


# ==============================================================
# 6) MISSING VALUES (NaN)
# ==============================================================

print("=== 6) Missing values (NaN) ===")

df_nan = df.copy()
df_nan.loc[2, "spesa"] = np.nan          # imposto un NaN
print("Con NaN:\n", df_nan, "\n")

print("isna (dove sono NaN):\n", df_nan.isna(), "\n")

print("Conteggio NaN per colonna:\n", df_nan.isna().sum(), "\n")

# fillna: sostituisco NaN con la media della colonna
media_spesa = df_nan["spesa"].mean()
df_nan["spesa"] = df_nan["spesa"].fillna(media_spesa)
print("Dopo fillna con media:\n", df_nan, "\n")

# dropna: elimina righe con NaN (qui non ne restano)
df_drop = df.copy()
df_drop.loc[1, "citta"] = np.nan
print("Prima dropna:\n", df_drop, "\n")
print("Dopo dropna:\n", df_drop.dropna(), "\n")


# ==============================================================
# 7) GROUPBY + AGGREGAZIONI
# ==============================================================

print("=== 7) GroupBy e aggregazioni ===")

group = df.groupby("citta")["spesa"].agg(["count", "mean", "sum", "max"])
print(group, "\n")


# ==============================================================
# 8) SORT + VALUE_COUNTS
# ==============================================================

print("=== 8) Sort e value_counts ===")

print("Ordinato per spesa decrescente:\n", df.sort_values("spesa", ascending=False), "\n")

print("Conteggio città:\n", df["citta"].value_counts(), "\n")


# ==============================================================
# 9) MERGE (JOIN)
# ==============================================================

print("=== 9) Merge (join) ===")

df_lavori = pd.DataFrame({
    "nome": ["Anna", "Luca", "Sara"],
    "lavoro": ["Dev", "PM", "Designer"]
})

merged = pd.merge(df, df_lavori, on="nome", how="left")
print("Merge left (aggiunge lavoro quando presente):\n", merged, "\n")


# ==============================================================
# 10) DATETIME: to_datetime, set_index, resample
# ==============================================================

print("=== 10) DateTime e resample ===")

df_time = pd.DataFrame({
    "data": pd.date_range("2025-01-01", periods=10, freq="D"),
    "vendite": [5, 7, 3, 9, 2, 4, 6, 8, 1, 10]
})

df_time["data"] = pd.to_datetime(df_time["data"])
df_time = df_time.set_index("data")

print("Dati con index datetime:\n", df_time, "\n")

# resample settimanale (W) con somma
weekly = df_time.resample("W").sum()
print("Resample settimanale (somma vendite):\n", weekly, "\n")
