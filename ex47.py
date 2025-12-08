def eliminarcapicua(llista):
    if len(llista) <= 2:
        return []
    return llista[1:-1]


# Demanar la llista a l'usuari
llista = []
print("Introdueix els elements de la llista. Escriu 'fi' per acabar:")

while True:
    valor = input("Element: ")

    if valor == "fi":
        break

    llista.append(valor)


# Mostrar el resultat
print(eliminarcapicua(llista))
