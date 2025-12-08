def llista_a_diccionari(llista):
    diccionari = {}
    for index, valor in enumerate(llista):
        diccionari[valor] = index
    return diccionari


# Demanar la llista a l'usuari
llista = []
print("Introdueix paraules. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")

    if paraula == "fi":
        break

    llista.append(paraula)


# Mostrar el resultat
print(llista_a_diccionari(llista))
