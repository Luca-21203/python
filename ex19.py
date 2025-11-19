def sumar_llista(llista):
    """
    Suma tots els valors d'una llista.
    """
    suma = 0
    for valor in llista:
        suma += valor
    return suma


def multiplicar_llista(llista):
    """
    Multiplica tots els valors d'una llista.
    """
    producte = 1
    for valor in llista:
        producte *= valor
    return producte


# Proves amb diferents exemples
print(sumar_llista([1, 2, 3, 4]))           # 10
print(sumar_llista([10, 20, 30]))           # 60
print(sumar_llista([5]))                    # 5
print(sumar_llista([0, 5, 10]))             # 15
print(sumar_llista([-1, -2, -3]))           # -6
print(sumar_llista([1.5, 2.5, 3.0]))        # 7.0

print("\n--- Multiplicació ---")
print(multiplicar_llista([1, 2, 3, 4]))     # 24
print(multiplicar_llista([2, 5, 10]))       # 100
print(multiplicar_llista([5]))              # 5
print(multiplicar_llista([0, 5, 10]))       # 0
print(multiplicar_llista([2, 3, 4]))        # 24
print(multiplicar_llista([1.5, 2, 3]))      # 9.0
