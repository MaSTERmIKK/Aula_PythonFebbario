# ==========================
# ESERCIZIO PANDAS - EDA BASE
# Dataset: Nome, Età, Città, Salario
# ==========================

import pandas as pd
import numpy as np

# 1) Creiamo i dati in modo casuale e li carichiamo in un DataFrame
np.random.seed(42)  # per rendere l'esempio ripetibile

nomi_possibili = ["Luca", "Marco", "Giulia", "Sara", "Anna", "Paolo", "Marta", "Davide", "Elisa", "Franco"]
citta_possibili = ["Roma", "Milano", "Torino", "Napoli", "Genova", "Bologna", "Firenze", "Palermo"]

n_righe = 20

df = pd.DataFrame({
    "Nome": np.random.choice(nomi_possibili, size=n_righe),
    "Età": np.random.randint(15, 80, size=n_righe),
    "Città": np.random.choice(citta_possibili, size=n_righe),
    "Salario": np.random.randint(1200, 4500, size=n_righe)
})

# Inseriamo volutamente alcuni valori mancanti (NaN) per l'esercizio
df.loc[np.random.choice(df.index, size=3, replace=False), "Età"] = np.nan
df.loc[np.random.choice(df.index, size=3, replace=False), "Salario"] = np.nan

# Inseriamo volutamente qualche duplicato
df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)

print("=== DataFrame generato (con NaN e duplicati) ===")
print(df)

print("\n" + "-"*60 + "\n")

# 2) Visualizzare le prime e le ultime 5 righe
print("=== Prime 5 righe ===")
print(df.head())

print("\n=== Ultime 5 righe ===")
print(df.tail())

print("\n" + "-"*60 + "\n")

# 3) Visualizzare il tipo di dato di ciascuna colonna
print("=== Tipi di dato (dtypes) ===")
print(df.dtypes)

print("\n" + "-"*60 + "\n")

# 4) Statistiche descrittive di base per colonne numeriche
# (media, mediana, deviazione standard)
print("=== Statistiche descrittive (colonne numeriche) ===")
print("Media:\n", df[["Età", "Salario"]].mean(numeric_only=True))
print("\nMediana:\n", df[["Età", "Salario"]].median(numeric_only=True))
print("\nDeviazione standard:\n", df[["Età", "Salario"]].std(numeric_only=True))

print("\n" + "-"*60 + "\n")

# 5) Identificare e rimuovere eventuali duplicati
duplicati_prima = df.duplicated().sum()
print("Duplicati trovati:", duplicati_prima)

df = df.drop_duplicates()

duplicati_dopo = df.duplicated().sum()
print("Duplicati dopo la rimozione:", duplicati_dopo)

print("\n" + "-"*60 + "\n")

# 6) Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna
# Calcoliamo le mediane (ignorando i NaN)
mediana_eta = df["Età"].median()
mediana_salario = df["Salario"].median()

# Sostituzione dei NaN
df["Età"] = df["Età"].fillna(mediana_eta)
df["Salario"] = df["Salario"].fillna(mediana_salario)

print("=== DataFrame dopo fillna con mediana ===")
print(df)

print("\n" + "-"*60 + "\n")

# 7) Aggiungere una colonna "Categoria Età"
# 0-18: Giovane, 19-65: Adulto, oltre 65: Senior
def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df["Categoria Età"] = df["Età"].apply(categoria_eta)

print("=== DataFrame con colonna 'Categoria Età' ===")
print(df)

print("\n" + "-"*60 + "\n")

# 8) Salvare il DataFrame pulito in un nuovo file CSV
nome_file_output = "dataset_pulito.csv"
df.to_csv(nome_file_output, index=False)

print(f"File salvato: {nome_file_output}")
