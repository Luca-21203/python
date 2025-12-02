# Funció per retornar el número més gran d'una llista
def gran_llista(llista):
    """
    Retorna el número més gran d'una llista de nombres.
    """
    if not llista:  # Comprovem si la llista està buida
        return None
    max_valor = llista[0]
    for num in llista:
        if num > max_valor:
            max_valor = num
    return max_valor

# Proves
print(gran_llista([3, 4, 2, 3, 10]))  # 10
print(gran_llista([5, 5, 5, 5]))      # 5
print(gran_llista([-2, -7, -1, -9]))  # -1
print(gran_llista([]))                 # None
