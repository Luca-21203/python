# Definim la funció
def es_vocal(caracter):
    """
    Retorna True si el caràcter és una vocal, False en cas contrari.
    Considera majúscules i minúscules.
    """
    vocals = "aeiouàèéíïòóúüAEIOUÀÈÉÍÏÒÓÚÜ"
    if caracter in vocals:
        return True
    else:
        return False

# Proves de la funció
llista_caracters = ['a', 'b', 'E', 'z', 'ó', 'u', 'X']

for c in llista_caracters:
    print(f"{c}: {es_vocal(c)}")
