#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANDAS - GESTIONE DEL TEMPO / TIME SERIES (panoramica completa, un unico file)

Contenuti:
1) Creazione DateTimeIndex (date_range) + Serie temporale
2) Parsing e conversioni: to_datetime, dayfirst, errori
3) Attributi .dt (year, month, weekday, ecc.)
4) Set index su datetime + sorting
5) Slicing temporale avanzato (string slicing, between_time, at_time)
6) Resample (D, W, M, Q) con aggregazioni
7) Rolling windows (media mobile) + min_periods
8) Shift / Diff / Pct_change (lag e variazioni)
9) Timezone: localize/convert
10) PeriodIndex e conversioni
11) Asfreq (riempimento frequenza) + fillna/interpolate
"""

import pandas as pd
import numpy as np

pd.set_option("display.width", 140)
pd.set_option("display.max_columns", 50)
np.set_printoptions(precision=3, suppress=True)


# ==============================================================
# 1) CREAZIONE TIME SERIES (DateTimeIndex)
# ==============================================================

print("=== 1) Creazione time series ===")

idx = pd.date_range("2025-01-01", periods=48, freq="H")  # 48 ore
ts = pd.Series(np.random.randn(len(idx)), index=idx, name="valore")

print("ts.head():\n", ts.head(), "\n")
print("Index type:", type(ts.index), "\n")


# ==============================================================
# 2) PARSING / CONVERSIONI con to_datetime
# ==============================================================

print("=== 2) Parsing con to_datetime ===")

raw_dates = pd.Series(["01/02/2025", "15/02/2025", "31/02/2025", "01/03/2025"])  # una data è invalida
parsed = pd.to_datetime(raw_dates, dayfirst=True, errors="coerce")  # errors='coerce' -> invalide diventano NaT

print("Raw:\n", raw_dates)
print("Parsed:\n", parsed, "\n")


# ==============================================================
# 3) ACCESSORI dt: estrazione parti del tempo
# ==============================================================

print("=== 3) .dt: year/month/day/weekday ===")

df_dates = pd.DataFrame({"data": parsed})
df_dates["anno"] = df_dates["data"].dt.year
df_dates["mese"] = df_dates["data"].dt.month
df_dates["giorno"] = df_dates["data"].dt.day
df_dates["weekday"] = df_dates["data"].dt.day_name()  # nome giorno
print(df_dates, "\n")


# ==============================================================
# 4) SET INDEX su datetime + sort_index
# ==============================================================

print("=== 4) set_index + sort_index ===")

df_ts = ts.reset_index()
df_ts.columns = ["data", "valore"]
df_ts = df_ts.set_index("data").sort_index()
print(df_ts.head(), "\n")


# ==============================================================
# 5) SLICING TEMPORALE AVANZATO
# ==============================================================

print("=== 5) Slicing temporale ===")

# String slicing: funziona con DateTimeIndex ordinato
print("Dal 2025-01-01 05:00 al 2025-01-01 10:00:\n", df_ts.loc["2025-01-01 05:00":"2025-01-01 10:00"], "\n")

# between_time: filtra per fascia oraria (utile su dati giornalieri o multi-giorno)
multi_idx = pd.date_range("2025-01-01", periods=24*7, freq="H")  # 7 giorni
multi_ts = pd.Series(np.random.randn(len(multi_idx)), index=multi_idx, name="x")
print("between_time 09:00-17:00 (prime righe):\n", multi_ts.between_time("09:00", "17:00").head(), "\n")

# at_time: prende un orario preciso di ogni giorno (es. solo le 12:00)
print("at_time 12:00 (prime righe):\n", multi_ts.at_time("12:00").head(), "\n")


# ==============================================================
# 6) RESAMPLE (cambio granularità)
# ==============================================================

print("=== 6) Resample ===")

# Resample giornaliero: media
daily_mean = multi_ts.resample("D").mean()
print("Media giornaliera:\n", daily_mean, "\n")

# Resample settimanale: somma
weekly_sum = multi_ts.resample("W").sum()
print("Somma settimanale:\n", weekly_sum, "\n")

# Resample mensile su esempio più lungo
long_idx = pd.date_range("2024-01-01", periods=365, freq="D")
long_ts = pd.Series(np.random.randn(len(long_idx)), index=long_idx, name="y")
monthly = long_ts.resample("M").agg(["mean", "sum", "max"]).round(3)
print("Resample mensile (mean/sum/max):\n", monthly.head(), "\n")


# ==============================================================
# 7) ROLLING WINDOW (media mobile)
# ==============================================================

print("=== 7) Rolling (media mobile) ===")

roll7 = long_ts.rolling(window=7).mean()
roll7_min = long_ts.rolling(window=7, min_periods=3).mean()  # inizia prima

print("Rolling 7 giorni (head):\n", roll7.head(10), "\n")
print("Rolling 7 giorni min_periods=3 (head):\n", roll7_min.head(10), "\n")


# ==============================================================
# 8) SHIFT / DIFF / PCT_CHANGE
# ==============================================================

print("=== 8) shift / diff / pct_change ===")

s = daily_mean  # serie giornaliera
s_prev = s.shift(1)               # valore giorno precedente
s_diff = s.diff(1)                # differenza con giorno precedente
s_pct = s.pct_change(1) * 100      # variazione percentuale

out = pd.DataFrame({
    "oggi": s,
    "ieri": s_prev,
    "diff": s_diff,
    "var_%": s_pct
}).round(3)

print(out.head(10), "\n")


# ==============================================================
# 9) TIMEZONE: localize e convert
# ==============================================================

print("=== 9) Timezone ===")

tz_idx = pd.date_range("2025-01-01", periods=3, freq="H")  # naive (senza timezone)
tz_series = pd.Series([100, 120, 90], index=tz_idx, name="val")

# localize: assegna timezone (non cambia l'orario "visualizzato", cambia l'interpretazione)
rome = tz_series.tz_localize("Europe/Rome")

# convert: converte in un'altra timezone mantenendo l'istante assoluto
utc = rome.tz_convert("UTC")

print("Naive:\n", tz_series)
print("Localized Europe/Rome:\n", rome)
print("Converted to UTC:\n", utc, "\n")


# ==============================================================
# 10) PERIODINDEX: mesi, trimestri, ecc.
# ==============================================================

print("=== 10) PeriodIndex ===")

df_period = pd.DataFrame({"data": long_ts.index, "y": long_ts.values})
df_period["mese"] = df_period["data"].dt.to_period("M")
by_month = df_period.groupby("mese")["y"].mean().round(3)

print("Media per mese (PeriodIndex):\n", by_month.head(), "\n")


# ==============================================================
# 11) ASFREQ (frequenza fissa) + fill/interpolate
# ==============================================================

print("=== 11) asfreq + fill/interpolate ===")

# Creo una serie con buchi (solo giorni dispari)
gap_idx = pd.date_range("2025-01-01", periods=10, freq="2D")
gap_ts = pd.Series(np.random.randn(len(gap_idx)), index=gap_idx, name="z")

# asfreq('D') espande a giornaliero e inserisce NaN nei giorni mancanti
daily_gap = gap_ts.asfreq("D")
print("Serie con buchi (asfreq D):\n", daily_gap.head(10), "\n")

# fillna: forward-fill (propaga ultimo valore)
ffill = daily_gap.fillna(method="ffill")
print("Forward fill:\n", ffill.head(10), "\n")

# interpolate: interpolazione lineare
interp = daily_gap.interpolate(method="time")
print("Interpolazione time:\n", interp.head(10), "\n")


print("=== FINE DEMO TIME SERIES ===")
