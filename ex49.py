def hi_ha_duplicats(llista):
    for i in range(len(llista)):
        for j in range(i + 1, len(llista)):
            if llista[i] == llista[j]:
                return True
    return False


# Demanar la llista a l'usuari
llista = []
print("Introdueix els elements de la llista. Escriu 'fi' per acabar:")

while True:
    valor = input("Element: ")

    if valor == "fi":
        break

    llista.append(valor)


# Mostrar el resultat
print(hi_ha_duplicats(llista))
