def concat_llistes(llista1, llista2, connector):
    resultat = []
    for a, b in zip(llista1, llista2):
        resultat.append(a + connector + b)
    return resultat


# Demanar la primera llista
llista1 = []
print("Introdueix paraules per a la primera llista. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")
    if paraula == "fi":
        break
    llista1.append(paraula)


# Demanar la segona llista
llista2 = []
print("Introdueix paraules per a la segona llista. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")
    if paraula == "fi":
        break
    llista2.append(paraula)


# Demanar el connector
connector = input("Introdueix el connector: ")


# Mostrar el resultat
print(concat_llistes(llista1, llista2, connector))
