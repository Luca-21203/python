def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari.
    Un palíndrom és una paraula que s'escriu igual d'esquerra a dreta i de dreta a esquerra.
    """
    # Convertir a minúscules per fer la comparació case-insensitive
    paraula = paraula.lower()
    
    # Comparar la paraula amb la seva versió invertida
    return paraula == paraula[::-1]


# Exemples d'ús
print(es_palindrom("radar"))   # True
print(es_palindrom("ara"))     # True
print(es_palindrom("civic"))   # True
print(es_palindrom("rallar"))  # True
print(es_palindrom("tapat"))   # True
print(es_palindrom("simis"))   # True
print(es_palindrom("refer"))   # True
print(es_palindrom("casa"))    # False
print(es_palindrom("python"))  # False
