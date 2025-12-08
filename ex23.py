def crear_repetits(n, c):
    resultat = ""
    for _ in range(n):
        resultat += c
    return resultat


# Demanar les dades a l'usuari
numero = int(input("Introdueix un número enter: "))
caracter = input("Introdueix un caràcter: ")

# Mostrar el resultat
print(crear_repetits(numero, caracter))
