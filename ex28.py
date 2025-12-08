def filtrar_paraules(llista, x):
    resultat = []
    for paraula in llista:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat


# Demanar la llista de paraules a l'usuari
llista = []
print("Introdueix paraules. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")

    if paraula == "fi":
        break

    llista.append(paraula)


# Demanar el número x
x = int(input("Introdueix el número de caràcters: "))


# Mostrar el resultat
print(filtrar_paraules(llista, x))
