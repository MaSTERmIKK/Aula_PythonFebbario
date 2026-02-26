import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 1️⃣ GENERAZIONE DATI
# ==========================

np.random.seed(42)

giorni = 365
date = pd.date_range(start="2024-01-01", periods=giorni)

# Rumore casuale (media 2000, std 500)
visitatori = np.random.normal(loc=2000, scale=500, size=giorni)

# Trend crescente
trend = np.linspace(0, 500, giorni)

visitatori = visitatori + trend

# ==========================
# 2️⃣ CREAZIONE DATAFRAME
# ==========================

df = pd.DataFrame({
    "Visitatori": visitatori
}, index=date)

# ==========================
# 3️⃣ ANALISI DATI
# ==========================

media_mensile = df.resample("M").mean()
std_mensile = df.resample("M").std()

print("Media mensile:")
print(media_mensile)

print("\nDeviazione standard mensile:")
print(std_mensile)

# Media mobile a 7 giorni
df["Media_Mobile_7"] = df["Visitatori"].rolling(window=7).mean()

# ==========================
# 4️⃣ VISUALIZZAZIONE
# ==========================

# Grafico giornaliero + media mobile
plt.figure()
plt.plot(df.index, df["Visitatori"])
plt.plot(df.index, df["Media_Mobile_7"])
plt.title("Visitatori Giornalieri con Media Mobile (7 giorni)")
plt.xlabel("Data")
plt.ylabel("Numero Visitatori")
plt.xticks(rotation=45)
plt.show()

# Grafico media mensile
plt.figure()
plt.plot(media_mensile.index, media_mensile["Visitatori"])
plt.title("Media Mensile Visitatori")
plt.xlabel("Mese")
plt.ylabel("Media Visitatori")
plt.xticks(rotation=45)
plt.show()
