# Funció per crear punts segons els valors d'una llista
def crear_punts(llista):
    """
    Per cada número de la llista, imprimeix una línia amb tants punts com el valor del número.
    """
    for num in llista:
        print("." * num)

# Proves
crear_punts([2, 3, 4])
print("---")
crear_punts([1, 5, 2])
