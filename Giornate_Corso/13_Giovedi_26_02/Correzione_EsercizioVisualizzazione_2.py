import pandas as pd

# Esempio DataFrame (se già esiste df puoi saltare questa parte)
df = pd.DataFrame({
    "altezza": [160, 170, 180, 175, 165],
    "peso": [55, 70, 80, 75, 60],
    "eta": [25, 30, 35, 28, 22]
})

# Copia per mantenere originale
df_mod = df.copy()

# Funzione Min-Max
def min_max(col):
    return (col - col.min()) / (col.max() - col.min())

# Applicazione solo a altezza e peso
df_mod["altezza"] = min_max(df_mod["altezza"])
df_mod["peso"] = min_max(df_mod["peso"])

# Stampa confronto
print("DataFrame originale:")
print(df)

print("\nDataFrame normalizzato:")
print(df_mod)
