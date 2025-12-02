# Funció per comprovar si dues llistes tenen algun element en comú
def superposicio(llista1, llista2):
    """
    Retorna True si hi ha algun element en comú entre llista1 i llista2,
    False en cas contrari.
    """
    for element in llista1:
        if element in llista2:
            return True
    return False

# Proves
llista_a = [1, 2, 3, 4]
llista_b = [5, 6, 7]
llista_c = [3, 7, 8]
llista_d = []

print(superposicio(llista_a, llista_b))  # False
print(superposicio(llista_a, llista_c))  # True (3 està en comú)
print(superposicio(llista_b, llista_c))  # True (7 està en comú)
print(superposicio(llista_a, llista_d))  # False
