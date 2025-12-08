def index_paraula(llista, paraula):
    for i in range(len(llista)):
        if llista[i] == paraula:
            return i
    return -1


# Demanar la llista ordenada a l'usuari
llista = []
print("Introdueix paraules ordenades. Escriu 'fi' per acabar:")

while True:
    p = input("Paraula: ")

    if p == "fi":
        break

    llista.append(p)


# Demanar la paraula a cercar
buscar = input("Introdueix la paraula a cercar: ")

# Mostrar el resultat
print(index_paraula(llista, buscar))
