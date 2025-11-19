def invertir(cadena):
    """
    Retorna la cadena invertida.
    """
    return cadena[::-1]


# Proves amb diferents exemples
print(invertir("Soc del Ramis"))           # simaR led coS
print(invertir("Hola"))                    # aloH
print(invertir("Python"))                  # nohtyP
print(invertir("12345"))                   # 54321
print(invertir("A"))                       # A
print(invertir("radar"))                   # radar (palíndrom)
print(invertir("Bon dia!"))                # !aid noB
print(invertir(""))                        # (cadena buida)
