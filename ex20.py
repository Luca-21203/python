# Funció per invertir una cadena i retornar-la
def invertir(cadena):
    """
    Retorna la cadena invertida.
    """
    return cadena[::-1]

# Proves
cadena1 = "Soc del Ramis"
cadena_invertida1 = invertir(cadena1)
print(cadena_invertida1)  # Mostra: simaR led coS

cadena2 = "Hola món"
cadena_invertida2 = invertir(cadena2)
print(cadena_invertida2)  # Mostra: nóm aloH
