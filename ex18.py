def es_vocal(caracter):
    """
    Retorna True si el caràcter és una vocal, False en cas contrari.
    """
    vocals = "aeiouAEIOUàèéíòóúÀÈÉÍÒÓÚäëïöüÄËÏÖÜ"
    return caracter in vocals


# Proves amb diferents exemples
print(es_vocal('a'))    # True
print(es_vocal('e'))    # True
print(es_vocal('i'))    # True
print(es_vocal('o'))    # True
print(es_vocal('u'))    # True
print(es_vocal('A'))    # True
print(es_vocal('E'))    # True
print(es_vocal('b'))    # False
print(es_vocal('z'))    # False
print(es_vocal('x'))    # False
print(es_vocal('à'))    # True
print(es_vocal('é'))    # True
print(es_vocal('3'))    # False
print(es_vocal(' '))    # False
