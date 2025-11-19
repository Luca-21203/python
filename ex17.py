# Definim la funció
def longitud(obj):
    """
    Calcula la longitud d'una llista o d'una cadena.
    
    Args:
    obj (list o str): Llista o cadena de la qual volem la longitud.
    
    Returns:
    int: Longitud de l'objecte.
    """
    return len(obj)  # Utilitzem la funció integrada len()

# Proves amb diferents exemples
# Exemple 1: llista
llista_ex = [1, 2, 3, 4, 5]
print("Longitud de la llista:", longitud(llista_ex))

# Exemple 2: cadena
cadena_ex = "Hola món"
print("Longitud de la cadena:", longitud(cadena_ex))

# Exemple 3: llista buida
print("Longitud de la llista buida:", longitud([]))

# Exemple 4: cadena buida
print("Longitud de la cadena buida:", longitud(""))
