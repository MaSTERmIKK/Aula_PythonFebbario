#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANDAS AVANZATO (unico file copiabile)
- GroupBy (multi-chiave, agg, transform)
- Pivot / Pivot_table (anche multi-index)
- Gestione del tempo (datetime, resample, rolling, shift, tz)
- Indicizzazione avanzata (loc/iloc, MultiIndex, slice, query, mask, xs)

Esecuzione:
python pandas_avanzato.py
"""

import pandas as pd
import numpy as np

pd.set_option("display.width", 140)
pd.set_option("display.max_columns", 50)


# ==============================================================
# 0) DATASET DI ESEMPIO
# ==============================================================

# Creiamo un dataset "vendite" realistico con date, negozi, categorie, prodotto, quantità e prezzo
rng = pd.date_range("2025-01-01", periods=120, freq="D")
np.random.seed(42)

df = pd.DataFrame({
    "data": np.random.choice(rng, size=600, replace=True),
    "negozio": np.random.choice(["Genova", "Milano", "Roma"], size=600),
    "categoria": np.random.choice(["Tech", "Food", "Casa"], size=600),
    "prodotto": np.random.choice(["A", "B", "C", "D"], size=600),
    "qta": np.random.randint(1, 6, size=600),
    "prezzo": np.round(np.random.uniform(2.5, 120.0, size=600), 2)
})

# Fatturato riga per riga
df["totale"] = df["qta"] * df["prezzo"]

# Converto la colonna data in datetime (di solito è già datetime, ma lo facciamo esplicito)
df["data"] = pd.to_datetime(df["data"])

print("=== DATASET (prime 5 righe) ===")
print(df.head(), "\n")


# ==============================================================
# 1) GROUPBY: aggregazioni, multi-chiave, agg avanzate
# ==============================================================

print("=== 1) GROUPBY base: per negozio (sum/mean/max) ===")
g1 = df.groupby("negozio")["totale"].agg(["count", "sum", "mean", "max"]).round(2)
print(g1, "\n")

print("=== 1b) GROUPBY multi-chiave: negozio + categoria ===")
g2 = df.groupby(["negozio", "categoria"])["totale"].agg(["sum", "mean"]).round(2)
print(g2.head(12), "\n")

print("=== 1c) GROUPBY con più colonne e agg con nomi custom ===")
g3 = df.groupby("categoria").agg(
    righe=("totale", "count"),
    fatturato=("totale", "sum"),
    qta_tot=("qta", "sum"),
    prezzo_medio=("prezzo", "mean")
).round(2)
print(g3, "\n")


# ==============================================================
# 2) GROUPBY + transform (feature per riga) e rank
# ==============================================================

print("=== 2) GROUPBY + transform: quota sul totale del negozio ===")
df["totale_negozio"] = df.groupby("negozio")["totale"].transform("sum")
df["quota_su_negozio"] = (df["totale"] / df["totale_negozio"]).round(6)

print(df[["negozio", "categoria", "totale", "totale_negozio", "quota_su_negozio"]].head(), "\n")

print("=== 2b) Rank: classifica fatturato per negozio (riga) ===")
df["rank_in_negozio"] = df.groupby("negozio")["totale"].rank(ascending=False, method="dense")
print(df[["negozio", "totale", "rank_in_negozio"]].head(), "\n")


# ==============================================================
# 3) PIVOT e PIVOT_TABLE
# ==============================================================

print("=== 3) PIVOT: totale per data x negozio (attenzione: pivot richiede chiavi uniche) ===")

# Per pivot usiamo un dataset aggregato (chiavi uniche), altrimenti pivot esplode
daily_store = df.groupby(["data", "negozio"], as_index=False)["totale"].sum()

pivot1 = daily_store.pivot(index="data", columns="negozio", values="totale").fillna(0).round(2)
print("Pivot (prime 5 righe):\n", pivot1.head(), "\n")

print("=== 3b) PIVOT_TABLE: totale medio per negozio x categoria ===")
pivot2 = pd.pivot_table(
    df,
    index="negozio",
    columns="categoria",
    values="totale",
    aggfunc="mean",
    fill_value=0
).round(2)
print(pivot2, "\n")

print("=== 3c) PIVOT_TABLE con multi-index: negozio x categoria, colonne=prodotto ===")
pivot3 = pd.pivot_table(
    df,
    index=["negozio", "categoria"],
    columns="prodotto",
    values="totale",
    aggfunc="sum",
    fill_value=0
).round(2)
print(pivot3.head(12), "\n")


# ==============================================================
# 4) GESTIONE DEL TEMPO: set_index, resample, rolling, shift, period
# ==============================================================

print("=== 4) TIME: resample settimanale per negozio ===")

# Mettiamo la data come index per lavorare meglio con resample
ts = daily_store.set_index("data")

# Resample settimanale: somma per negozio
weekly = ts.groupby("negozio")["totale"].resample("W").sum().round(2)
print("Weekly (prime righe):\n", weekly.head(10), "\n")

print("=== 4b) TIME: rolling (media mobile 7 giorni) sul totale giornaliero di un negozio ===")
genova_daily = pivot1["Genova"]  # Serie indicizzata per data
rolling7 = genova_daily.rolling(window=7).mean().round(2)
print(pd.DataFrame({"Genova_tot": genova_daily.head(12), "Genova_roll7": rolling7.head(12)}), "\n")

print("=== 4c) TIME: shift (valore giorno precedente) e variazione % ===")
prev = genova_daily.shift(1)
pct = ((genova_daily - prev) / prev * 100).replace([np.inf, -np.inf], np.nan).round(2)
print(pd.DataFrame({"oggi": genova_daily.head(10), "ieri": prev.head(10), "var_%": pct.head(10)}), "\n")

print("=== 4d) TIME: PeriodIndex (raggruppo per mese) ===")
df["mese"] = df["data"].dt.to_period("M")
per_mese = df.groupby(["mese", "negozio"])["totale"].sum().round(2)
print(per_mese.head(12), "\n")

print("=== 4e) TIMEZONE: localizzare e convertire (demo) ===")
# Creiamo una mini serie con timezone
mini_time = pd.date_range("2025-01-01", periods=3, freq="H")
mini = pd.Series([100, 120, 90], index=mini_time, name="valore")
mini = mini.tz_localize("Europe/Rome").tz_convert("UTC")  # Rome -> UTC
print(mini, "\n")


# ==============================================================
# 5) INDICIZZAZIONE AVANZATA
# ==============================================================

print("=== 5) Indicizzazione avanzata: loc/iloc, slice su date ===")

# pivot1 ha index datetime: posso fare slicing per intervallo
subset_date = pivot1.loc["2025-02-01":"2025-02-10"]
print("Slicing date 2025-02-01..2025-02-10:\n", subset_date.head(), "\n")

print("=== 5b) query: filtra con espressione ===")
q = df.query("negozio == 'Roma' and categoria == 'Tech' and totale > 200")
print("Query (prime 5):\n", q.head(), "\n")

print("=== 5c) mask booleana complessa con isin + between ===")
mask = df["negozio"].isin(["Genova", "Milano"]) & df["prezzo"].between(20, 50) & (df["qta"] >= 3)
print(df.loc[mask, ["data", "negozio", "categoria", "prezzo", "qta", "totale"]].head(), "\n")

print("=== 5d) MultiIndex: selezione con xs (cross-section) ===")
# pivot3 ha MultiIndex su index (negozio, categoria)
# Estraggo solo "Milano" con xs:
milano_only = pivot3.xs("Milano", level="negozio")
print("Solo Milano (xs):\n", milano_only.head(), "\n")

print("=== 5e) MultiIndex: slice su due livelli ===")
# Creo un MultiIndex esplicito per demo e faccio slicing con IndexSlice
idx = pd.IndexSlice
# Seleziono (Genova..Roma) e categoria specifica, poi tutte le colonne
multi_slice = pivot3.loc[idx["Genova":"Roma", "Tech"], :]
print("Slice MultiIndex (negozio Genova..Roma, categoria Tech):\n", multi_slice.head(), "\n")

print("=== 5f) set_index multiplo e selezione con loc ===")
df_mi = df.set_index(["negozio", "categoria", "data"]).sort_index()
# Seleziono tutte le righe di Genova/Tech in un intervallo di date
sel = df_mi.loc[("Genova", "Tech", slice("2025-01-15", "2025-01-20")), ["prodotto", "qta", "prezzo", "totale"]]
print("Genova/Tech 2025-01-15..2025-01-20:\n", sel.head(), "\n")


print("=== FINE DENO ===")
