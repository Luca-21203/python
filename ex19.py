# Funció per sumar tots els elements d'una llista
def sumar_llista(llista):
    suma = 0
    for num in llista:
        suma += num
    return suma

# Funció per multiplicar tots els elements d'una llista
def multiplicar_llista(llista):
    if not llista:  # Comprovem si la llista està buida
        return 0
    producte = 1
    for num in llista:
        producte *= num
    return producte

# Proves
llistes_prova = [
    [1, 2, 3, 4],
    [5, 6, 7],
    [10],
    [],
    [2, 3, 0, 4]
]

for llista in llistes_prova:
    print(f"Llista: {llista}")
    print(f"Sumar: {sumar_llista(llista)}")
    print(f"Multiplicar: {multiplicar_llista(llista)}\n")

