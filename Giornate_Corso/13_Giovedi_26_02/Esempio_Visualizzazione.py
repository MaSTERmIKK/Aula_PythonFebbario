#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
VISUALIZZAZIONE DATI IN PYTHON (Matplotlib + Seaborn) - GENERICO
- Matplotlib: line, scatter, bar, histogram, boxplot, heatmap base
- Seaborn: lineplot, scatterplot, histplot, boxplot, heatmap, pairplot
- Titoli, label, legenda, griglia, limiti, stile
- Salvare figure su file (savefig)

Prerequisiti:
pip install matplotlib seaborn pandas numpy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==============================================================
# 0) DATI DI ESEMPIO
# ==============================================================

np.random.seed(42)

# Time series finta
date = pd.date_range("2025-01-01", periods=60, freq="D")
trend = np.linspace(10, 25, len(date))
noise = np.random.normal(0, 1.2, len(date))
valori = trend + noise

# DataFrame "vendite" finto
df = pd.DataFrame({
    "data": date,
    "valore": valori,
    "categoria": np.random.choice(["Tech", "Food", "Casa"], size=len(date)),
    "negozio": np.random.choice(["Genova", "Milano", "Roma"], size=len(date)),
    "qta": np.random.randint(1, 8, size=len(date)),
    "prezzo": np.round(np.random.uniform(5, 120, size=len(date)), 2)
})
df["totale"] = df["qta"] * df["prezzo"]

print(df.head())


# ==============================================================
# 1) MATPLOTLIB: LINE PLOT (serie temporale)
# ==============================================================

plt.figure()
plt.plot(df["data"], df["valore"], marker="o", linewidth=1)
plt.title("Matplotlib - Line plot (time series)")
plt.xlabel("Data")
plt.ylabel("Valore")
plt.grid(True)
plt.tight_layout()
plt.show()


# ==============================================================
# 2) MATPLOTLIB: SCATTER (relazione tra due variabili)
# ==============================================================

plt.figure()
plt.scatter(df["prezzo"], df["qta"])
plt.title("Matplotlib - Scatter prezzo vs quantità")
plt.xlabel("Prezzo")
plt.ylabel("Quantità")
plt.grid(True)
plt.tight_layout()
plt.show()


# ==============================================================
# 3) MATPLOTLIB: BAR PLOT (aggregazione)
# ==============================================================

# Somma totale per categoria (pandas per aggregare)
by_cat = df.groupby("categoria")["totale"].sum().sort_values(ascending=False)

plt.figure()
plt.bar(by_cat.index, by_cat.values)
plt.title("Matplotlib - Bar plot (totale per categoria)")
plt.xlabel("Categoria")
plt.ylabel("Totale")
plt.tight_layout()
plt.show()


# ==============================================================
# 4) MATPLOTLIB: HISTOGRAM (distribuzione)
# ==============================================================

plt.figure()
plt.hist(df["prezzo"], bins=10)
plt.title("Matplotlib - Istogramma prezzi")
plt.xlabel("Prezzo")
plt.ylabel("Frequenza")
plt.tight_layout()
plt.show()


# ==============================================================
# 5) MATPLOTLIB: BOXPLOT (distribuzione per gruppi)
# ==============================================================

# Prepariamo i dati: lista di liste, una per categoria
cats = ["Tech", "Food", "Casa"]
data_box = [df.loc[df["categoria"] == c, "totale"].values for c in cats]

plt.figure()
plt.boxplot(data_box, labels=cats)
plt.title("Matplotlib - Boxplot totale per categoria")
plt.xlabel("Categoria")
plt.ylabel("Totale")
plt.tight_layout()
plt.show()


# ==============================================================
# 6) MATPLOTLIB: HEATMAP SEMPLICE (matrice di correlazione)
# ==============================================================

corr = df[["valore", "qta", "prezzo", "totale"]].corr()

plt.figure()
plt.imshow(corr.values)
plt.title("Matplotlib - Heatmap correlazioni (base)")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.index)), corr.index)

# Scrivo i valori nella matrice (facoltativo)
for i in range(corr.shape[0]):
    for j in range(corr.shape[1]):
        plt.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center")

plt.tight_layout()
plt.show()


# ==============================================================
# 7) SEABORN: STILE GENERICO
# ==============================================================

sns.set_theme(style="whitegrid")  # tema globale seaborn


# ==============================================================
# 8) SEABORN: LINEPLOT (con grouping)
# ==============================================================

plt.figure()
sns.lineplot(data=df, x="data", y="valore", hue="negozio")
plt.title("Seaborn - Lineplot valore nel tempo per negozio")
plt.xlabel("Data")
plt.ylabel("Valore")
plt.tight_layout()
plt.show()


# ==============================================================
# 9) SEABORN: SCATTERPLOT (con categoria/negozio)
# ==============================================================

plt.figure()
sns.scatterplot(data=df, x="prezzo", y="totale", hue="categoria", style="negozio")
plt.title("Seaborn - Scatter prezzo vs totale (hue categoria, style negozio)")
plt.tight_layout()
plt.show()


# ==============================================================
# 10) SEABORN: HISTPLOT / KDE (distribuzione)
# ==============================================================

plt.figure()
sns.histplot(data=df, x="prezzo", bins=12, kde=True)
plt.title("Seaborn - Distribuzione prezzi (hist + kde)")
plt.tight_layout()
plt.show()


# ==============================================================
# 11) SEABORN: BOXPLOT (per gruppi)
# ==============================================================

plt.figure()
sns.boxplot(data=df, x="categoria", y="totale")
plt.title("Seaborn - Boxplot totale per categoria")
plt.tight_layout()
plt.show()


# ==============================================================
# 12) SEABORN: HEATMAP (correlazioni)
# ==============================================================

plt.figure()
sns.heatmap(corr, annot=True, fmt=".2f")
plt.title("Seaborn - Heatmap correlazioni")
plt.tight_layout()
plt.show()


# ==============================================================
# 13) SEABORN: PAIRPLOT (esplorazione rapida)
# ==============================================================

# Attenzione: pairplot apre più grafici e può essere "pesante"
sns.pairplot(df[["valore", "qta", "prezzo", "totale", "categoria"]], hue="categoria")
plt.show()


# ==============================================================
# 14) SALVARE UNA FIGURA SU FILE
# ==============================================================

plt.figure()
sns.lineplot(data=df, x="data", y="totale")
plt.title("Salvataggio su file - Totale nel tempo")
plt.tight_layout()

# Salva la figura (PNG)
plt.savefig("grafico_totale.png", dpi=150)
plt.show()

print("\nCreato file: grafico_totale.png")
