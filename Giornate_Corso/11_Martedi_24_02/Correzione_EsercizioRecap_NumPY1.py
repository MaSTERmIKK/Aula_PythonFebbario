# Importiamo la libreria NumPy
import numpy as np

# 1. Creiamo un array NumPy:
# - valori da 0 a 49
# - aggiungiamo altri 50 valori casuali tra 49 e 101

# Array da 0 a 49
array_base = np.arange(0, 50)

# 50 numeri casuali interi tra 49 e 101
array_random = np.random.randint(49, 102, 50)

# Uniamo i due array
array = np.concatenate((array_base, array_random))

# Stampiamo array, dtype e shape
print("Array iniziale:")
print(array)
print("Dtype:", array.dtype)
print("Shape:", array.shape)

print("\n" + "-"*50 + "\n")

# 2. Modifichiamo il tipo in float64
array = array.astype(np.float64)

# Verifichiamo nuovo dtype e shape
print("Array dopo conversione in float64:")
print("Dtype:", array.dtype)
print("Shape:", array.shape)

print("\n" + "-"*50 + "\n")

# 3. SLICING

# Primi 10 elementi
primi_10 = array[:10]

# Ultimi 7 elementi
ultimi_7 = array[-7:]

# Elementi dall’indice 5 all’indice 20 escluso
slice_5_20 = array[5:20]

# Ogni quarto elemento
ogni_quarto = array[::4]

print("Primi 10 elementi:", primi_10)
print("Ultimi 7 elementi:", ultimi_7)
print("Elementi da indice 5 a 20 escluso:", slice_5_20)
print("Ogni quarto elemento:", ogni_quarto)

print("\n" + "-"*50 + "\n")

# 4. Modifica tramite slicing
# Elementi dall’indice 10 a 15 escluso diventano 999
array[10:15] = 999

print("Array dopo modifica degli indici 10-15 (escluso):")
print(array)

print("\n" + "-"*50 + "\n")

# 5. FANCY INDEXING

# Elementi in posizione specifica
posizioni = array[[0, 3, 7, 12, 25, 33, 48]]

# Tutti gli elementi pari (maschera booleana)
elementi_pari = array[array % 2 == 0]

# Elementi maggiori della media
media = np.mean(array)
elementi_maggiori_media = array[array > media]

print("Elementi nelle posizioni [0,3,7,12,25,33,48]:", posizioni)
print("Elementi pari:", elementi_pari)
print("Elementi maggiori della media:", elementi_maggiori_media)

print("\n" + "-"*50 + "\n")

# 6. Stampa finale

print("Array originale finale:")
print(array)

print("\nTutti i sotto-array ottenuti:")
print("Primi 10:", primi_10)
print("Ultimi 7:", ultimi_7)
print("Slice 5-20:", slice_5_20)
print("Ogni quarto:", ogni_quarto)
print("Posizioni specifiche:", posizioni)
print("Pari:", elementi_pari)
print("Maggiori della media:", elementi_maggiori_media)
