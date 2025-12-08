def filtrar_per_lletra(llista, lletra):
    return list(filter(lambda paraula: paraula.lower().startswith(lletra.lower()), llista))


# Demanar la llista de paraules a l'usuari
llista = []
print("Introdueix paraules. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")

    if paraula == "fi":
        break

    llista.append(paraula)


# Demanar la lletra
lletra = input("Introdueix una lletra: ")


# Mostrar el resultat
print(filtrar_per_lletra(llista, lletra))
