# Funció per crear una cadena repetida
def crear_repetits(num, caracter):
    """
    Retorna una cadena formada pel caràcter repetit 'num' vegades.
    """
    return caracter * num

# Proves
print(crear_repetits(5, "a"))   # "aaaaa"
print(crear_repetits(3, "x"))   # "xxx"
print(crear_repetits(0, "z"))   # "" (cadena buida)
print(crear_repetits(7, "*"))   # "*******"
