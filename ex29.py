def comptar_majuscules(cadena):
    comptador = 0
    for lletra in cadena:
        if lletra.isupper():
            comptador += 1
    return comptador


# Demanar una cadena a l'usuari
text = input("Introdueix una cadena: ")

# Mostrar el resultat
print(comptar_majuscules(text))
