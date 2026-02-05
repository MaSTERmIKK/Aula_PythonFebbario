# es 1 

ripeti = "si"

while ripeti == "si":
    scelta = input("Vuoi inserire un numero o una stringa? (numero/stringa): ")

    if scelta == "numero":
        valore = int(input("Inserisci un numero: "))

        if valore % 2 == 0:
            print("Il numero è pari")
        else:
            print("Il numero è dispari")

    elif scelta == "stringa":
        testo = input("Inserisci una stringa: ")

        pari = 0
        dispari = 0

        for i in range(len(testo)):
            if i % 2 == 0:
                pari = pari + 1
            else:
                dispari = dispari + 1

        print("Lettere in posizione pari:", pari)
        print("Lettere in posizione dispari:", dispari)

    else:
        print("Scelta non valida")
        continue

    ripeti = input("Vuoi ripetere? (si/no): ")

# es 2

ripeti = "si"

while ripeti == "si":
    inizio = int(input("Inserisci inizio intervallo: "))
    fine = int(input("Inserisci fine intervallo: "))

    primi = []
    non_primi = []

    for numero in range(inizio, fine + 1):
        if numero < 2:
            non_primi.append(numero)
            continue

        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break   # esce dal ciclo interno

        if primo:
            primi.append(numero)
        else:
            non_primi.append(numero)

    print("Numeri primi:", primi)
    print("Numeri non primi:", non_primi)

    ripeti = input("Vuoi ripetere? (si/no): ")


# es 3 numeri 

ripeti = "si"

while ripeti == "si":
    a = int(input("Inserisci primo numero: "))
    b = int(input("Inserisci secondo numero: "))

    fattori_comuni = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            fattori_comuni.append(i)

    if len(fattori_comuni) == 1:
        print("I numeri sono coprimi")
    else:
        print("Fattori comuni:", fattori_comuni)

    ripeti = input("Vuoi ripetere? (si/no): ")


# es 3 stringhe 

ripeti = "si"

while ripeti == "si":
    s1 = input("Inserisci prima stringa: ")
    s2 = input("Inserisci seconda stringa: ")

    complementari = True

    for lettera in s1:
        if lettera not in s2:
            complementari = False
            break

    if complementari:
        print("Le stringhe sono complementari")
    else:
        print("Le stringhe NON sono complementari")

    ripeti = input("Vuoi ripetere? (si/no): ")

