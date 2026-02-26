import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

# ===============================
# CARICAMENTO ED ESPLORAZIONE
# ===============================

df = pd.read_csv("clienti.csv")

print(df.info())
print(df.describe())
print(df["Churn"].value_counts())

# ===============================
# PULIZIA DATI
# ===============================

# Rimozione duplicati
df = df.drop_duplicates()

# Conversione colonne numeriche
cols_num = ["Eta","Durata_Abbonamento","Tariffa_Mensile",
            "Dati_Consumati","Servizio_Clienti_Contatti"]

for col in cols_num:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# Correzione anomalie semplici
df = df[df["Eta"] > 0]
df = df[df["Tariffa_Mensile"] > 0]

# ===============================
# EDA
# ===============================

# Nuova colonna
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]

# Groupby esempio
print(df.groupby("Churn")["Tariffa_Mensile"].mean())

# Correlazioni
print(df.corr(numeric_only=True))

# ===============================
# PREPARAZIONE MODELLAZIONE
# ===============================

# Conversione target
df["Churn"] = df["Churn"].map({"No":0, "Si":1})

X = df[["Eta","Durata_Abbonamento","Tariffa_Mensile",
        "Dati_Consumati","Servizio_Clienti_Contatti","Costo_per_GB"]]

y = df["Churn"]

# Normalizzazione
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ===============================
# MODELLO PREDITTIVO
# ===============================

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_prob))
