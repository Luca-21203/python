def binari_a_enter(binari):
    decimal = 0
    potencia = 0

    for bit in binari[::-1]:
        if bit == "1":
            decimal += 2 ** potencia
        potencia += 1

    return decimal


# Demanar el número binari a l'usuari
binari = input("Introdueix un número binari: ")

# Mostrar el resultat
print(binari_a_enter(binari))
