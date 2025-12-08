def comptar_coincidencies(llista):
    comptador = 0
    for index, valor in enumerate(llista):
        if index == valor:
            comptador += 1
    return comptador


# Demanar la llista de valors numèrics a l'usuari
llista = []
print("Introdueix números enters. Escriu 'fi' per acabar:")

while True:
    valor = input("Número: ")

    if valor == "fi":
        break

    llista.append(int(valor))


# Mostrar el resultat
print(comptar_coincidencies(llista))
