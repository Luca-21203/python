# Funció que comprova si una paraula és un palíndrom
def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari.
    La funció ignora majúscules/minúscules.
    """
    paraula = paraula.lower()  # Convertim a minúscules per comparar correctament
    return paraula == paraula[::-1]

# Proves
paraules_prova = ["radar", "ara", "civic", "rallar", "tapat", "simis", "refer", "Python", "hola"]

for p in paraules_prova:
    print(f"{p}: {es_palindrom(p)}")

