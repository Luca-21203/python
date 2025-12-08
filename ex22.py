def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False


# Demanar la primera llista
llista1 = []
print("Introdueix els elements de la primera llista. Escriu 'fi' per acabar:")
while True:
    x = input("Element: ")
    if x == "fi":
        break
    llista1.append(x)

# Demanar la segona llista
llista2 = []
print("Introdueix els elements de la segona llista. Escriu 'fi' per acabar:")
while True:
    y = input("Element: ")
    if y == "fi":
        break
    llista2.append(y)

# Mostrar resultat
print(superposicio(llista1, llista2))
