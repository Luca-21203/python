import random

def hi_ha_duplicats(llista):
    for i in range(len(llista)):
        for j in range(i + 1, len(llista)):
            if llista[i] == llista[j]:
                return True
    return False


def llista_20_elements():
    llista = []
    for _ in range(20):
        llista.append(random.randint(1, 100))
    return llista


# Generar la llista de 20 elements
llista = llista_20_elements()

# Mostrar la llista generada
print("Llista generada:")
print(llista)

# Comprovar si hi ha duplicats
if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats")
else:
    print("No hi ha elements duplicats")
