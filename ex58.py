def elements_parells(llista):
    for i in range(0, len(llista), 2):
        print(llista[i])


# Demanar la llista de paraules
llista = []
print("Introdueix paraules. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")

    if paraula == "fi":
        break

    llista.append(paraula)

# Mostrar els elements en posició parell
elements_parells(llista)
