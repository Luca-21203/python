def invertir(cadena):
    invertida = ""
    for c in cadena:
        invertida = c + invertida
    return invertida


# Demanar una cadena a l'usuari
text = input("Introdueix una cadena: ")

# Mostrar la cadena invertida
print(invertir(text))
